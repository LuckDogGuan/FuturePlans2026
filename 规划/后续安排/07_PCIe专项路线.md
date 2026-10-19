# PCIe专项路线：怎样配置，怎样验收

对应W29～W34。此处是学习方案，命令/配置骨架尚未在本机执行。先完成C、IRQ、内存与资源生命周期门槛，再进入，不能拿入门收发函数替代整个过程。

## 先分清你在配置哪一层

| 对象 | 软件要做的事 | 不属于同一件事 |
|---|---|---|
| RC / Root Complex | 初始化SoC控制器、PHY、参考时钟/复位、地址窗口、中断/IOMMU关联，等Link up并枚举 | 不是给endpoint写一个probe就完成RC bring-up |
| EP / Endpoint | 有EP能力的控制器通过EPC/EPF框架提供功能、BAR和中断，等待RC枚举 | 不是任意开发板都有EP模式 |
| endpoint设备驱动 | ID匹配、enable、申请/映射BAR、配置DMA能力、IRQ、任务、错误恢复与remove | 不直接承担所有PHY/布线配置 |
| 配置空间/ECAM | BDF、vendor/device、capability、BAR、command、MSI、桥窗口 | 配置空间不是设备BAR寄存器空间 |

原始标准入口：[PCI-SIG Specifications](https://pcisig.com/specifications)。完整Base Specification可能有授权限制，不承诺免费拿到。实际编程主线采用[Linux PCI指南](https://docs.kernel.org/PCI/pci.html)、[Linux endpoint框架](https://docs.kernel.org/PCI/endpoint/index.html)与[QEMU PCIe拓扑说明](https://github.com/qemu/qemu/blob/master/docs/pcie.txt)。

## 路线一：QEMU先写完整PCI驱动

先用x86 PC guest的EDU，避免第一轮同时处理跨架构DMA布局。准备固定版本QEMU、guest Linux、matching kernel headers、BusyBox或最小rootfs、PCI工具与模块构建链。host架构与guest架构分别记录。

启动参数只给必要增量：在已经可启动的guest命令中增加`-device edu`；机器、磁盘、内核和console仍按已验证基础配置。进入guest用`lspci -nn`确认`1234:11e8`，再看`lspci -t`、`lspci -nnvv`与sysfs resource。未枚举到设备就先查模型和拓扑，不开始猜驱动。

EDU是**传统PCI教学设备**，不是完整PCIe endpoint。按[官方EDU规格](https://www.qemu.org/docs/master/specs/edu.html)，先做寄存器存活/计算，之后IRQ与DMA；先把偏移、访问宽度、可读写位、busy/done、ack全部做成表。低于`0x80`的访问限32位，后续规则按规格，不能任意用byte写寄存器。

| 顺序 | 实现与证据 | 故障与恢复 |
|---|---|---|
| 1 probe/enable | `pci_driver`与ID表，enable设备、检查资源类型、申请BAR、映射，逐项检查返回值 | 在第N步模拟失败，检查已经获取的资源怎样释放；devm也不能代替设备停机 |
| 2 MMIO | 用`__iomem`与对应`readl/writel`等accessor，核偏移/宽度/端序/副作用 | 非法偏移在软件接口拒绝；W1C不随意读改写；posted write按需要读合适寄存器确认 |
| 3 轮询完成 | 发起一个规格支持的操作，单调时钟限定超时，区分busy/error/done | 不就绪、超时、重复请求；不能死循环等位 |
| 4 INTx→MSI | 先清旧状态，再分配/注册IRQ，最后开设备中断；中断确认、唤醒和数据处理分工 | INTx共享时判源；MSI向量查`pci_irq_vector`；未实现的MSI-X不冒充支持 |
| 5 DMA | 先协商mask，再分配buffer；CPU地址和DMA地址分存；启动前后验证内容和所有权 | mask不支持、映射失败、长度边界、超时；设备仍DMA时不能free |
| 6 关闭/remove | 拒绝新任务→使设备停DMA/停IRQ→等待/取消在途回调→释放映射和资源 | 调用中关闭、重复bind/unbind、部分probe失败；保存每步顺序的理由 |

DMA以[DMA mapping Guide](https://docs.kernel.org/core-api/dma-api-howto.html)为准，IRQ以[MSI Driver Guide](https://docs.kernel.org/PCI/msi-howto.html)为准，MMIO以[Device I/O](https://docs.kernel.org/driver-api/device-io.html)为准。设备停止条件由设备规格决定，不能盲目按获取资源的反序就认为安全。

EDU默认DMA mask是28位，只覆盖最低256MiB。Arm `virt`的RAM布局与这个范围不匹配，迁移时必须同时核模型`dma_mask`、驱动协商与IOMMU/总线地址映射；只把驱动mask改大不是修复。此风险依据模型与地址布局推断，本轮没有运行实验。详见[硬件资料核查](资料/02_外设架构QEMU与PCIe核查.md)。

## 路线二：理解真正PCIe的配置空间和拓扑

在支持PCIe的QEMU平台选一个**确认带PCIe capability的模型**，依该版本设备帮助和拓扑文档配置root port/endpoint；不要把EDU直接挂到PCIe总线就称它升级成PCIe。通过guest输出对照root bus、root port、bridge、endpoint的BDF、BAR窗口和capability链。

ECAM练习按host window给定的起始bus计算：`(bus - bus_start) << 20 | device << 15 | function << 12 | register_offset`，再加配置窗口基址。核bus/device/function/offset范围；本式是练习地址窗口的计算，不是在用户态对物理地址随便解引用。

对照[Linux generic PCI host DT binding](https://github.com/torvalds/linux/blob/master/Documentation/devicetree/bindings/pci/host-generic-pci.yaml)，解释`reg`、`bus-range`、`ranges`、IRQ/MSI与IOMMU关联。`ranges`里总线地址与CPU地址可能不同，不能用一个普通指针混称全部地址。

配置空间学习先只读观察。使能bus mastering、调整BAR、控制reset等由内核驱动/PCI框架负责，不在已绑定设备上用`setpci`盲写来试运气。

## 路线三：有条件才做真实RC↔EP

现有i.MX6ULL不作为PCIe平台。本次不要求采购。进入真实实验前必须确认所选SoC、开发板连线、内核控制器驱动及EP模式支持，再选RC与EP两端；只有插槽没有可编程EP并不能完成双端实验。

1. **RC端**：查厂商TRM、板图、勘误与BSP，检查供电、参考时钟、PERST#、PHY、clock/reset、模式、出入站窗口、DT与link状态。具体顺序以目标平台手册为准，不能把generic ECAM当通用PHY初始化手册。
2. **EP端**：对照[configfs配置EP](https://docs.kernel.org/PCI/endpoint/pci-endpoint-cfs.html)，核`CONFIG_PCI_ENDPOINT`、实际EPC/EPF驱动，再设置function、vendor/device、BAR，绑定EPC并按支持流程启动。不是照抄某块板的控制器名。
3. **双端验证**：用[官方PCI test流程](https://docs.kernel.org/PCI/endpoint/pci-test-howto.html)验证BAR读写、copy、IRQ，再查不同长度/对齐/超时/reset。保存两端版本、拓扑、LinkSta与数据比对结果。
4. **后续**：设备具备时再做MSI-X、多队列、IOMMU、AER、FLR/热复位/电源管理。每种reset影响范围不同，必须与设备/驱动协同；不能统一叫“重启设备”。

## 验收边界

软件实验必须讲清每个buffer、每个状态位、每次通知和释放顺序。QEMU只证明该模型的软件行为；真实Link up/降速、refclk与PERST#、链路训练、带宽、电气和信号完整性需要实际硬件证据。没做的就在阶段总结写“未验”，不影响先完成软件主线。
