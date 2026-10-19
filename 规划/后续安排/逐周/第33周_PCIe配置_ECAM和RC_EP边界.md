# 第33学习周：PCIe配置：ECAM和RC：EP边界

参考日期：2027-08-09～2027-08-15（北京时间）。后续深化段。实际执行前核对[假期日历](../02_日历与中国假期.md)；正式调休或公司加班与本周冲突时整周顺延，不在假期补课。状态：未开始。

## 工作问题与门槛

“PCIe如何设置”究竟是枚举端点、配置RC控制器，还是把SoC设置为EP？各要哪些手册？

先修：上一学习周的必过项有源码、输入与调试证据；失败项未解决先重复上一周。 本周重要性：P1：RC/EP/root port/bridge、配置空间与BAR区别、ECAM、DT ranges/bus-range/MSI映射。软件拓扑实验必做，未采购真板不设为必修。

## 精确选课与官方阅读

视频主看/补看：[QEMU官方PCIe拓扑说明](https://github.com/qemu/qemu/blob/master/docs/pcie.txt)配套软件拓扑阅读。视频检索“Linux Foundation PCI Endpoint Framework RC EP”与“QEMU PCIvsPCIe”，本轮未核实精确公开视频讲次，不把PDF说成录像。

文字与源码：[Linux host-generic-pci.yaml](https://github.com/torvalds/linux/blob/master/Documentation/devicetree/bindings/pci/host-generic-pci.yaml)ECAM formula/reg/ranges。[QEMU官方PCIe拓扑说明](https://github.com/qemu/qemu/blob/master/docs/pcie.txt)PCI Express only hierarchy/PCI only hierarchy。[Linux Endpoint Framework](https://docs.kernel.org/PCI/endpoint/index.html)Configuring PCI Endpoint Using CONFIGFS、PCI Test User Guide。

视频建议合计1～2小时，必要补看到3小时须挤掉选做，不挤编码。课程章节与手册章节分开，跨年MIT课程不要混编号。资料核验与播放/字幕限制见[课程表](../资料/01_C与系统课程章节核查.md)和[硬件架构表](../资料/02_外设架构QEMU与PCIe核查.md)。

## 每天做什么：正常周15小时

| 时间 | 具体动作与产物 |
|---|---|
| 周一 2h | 先写本周问题的预期图/表，再看指定视频、查手册。标出数据来源、控制/通知来源、对象或资源的归属。不能只抄笔记。 |
| 周二 2h | 在现成guest读取PCI拓扑/配置，标出RC/root port/bridge/EDU的各自角色，不把传统PCI设备改称PCIe |
| 周三 2h | 本人写纯函数ECAM偏移计算器并测试bus-range起点/函数/寄存器边界，对照当前DT窗口 |
| 周四 2h | 形成目标SoC未来RC/EP调试清单，画配置访问数据/INTx-MSI通知/地址窗口资源三图，区分时钟reset-PHY与QEMU模型。 |
| 周五 2h | 开始故障注入：计算器注入bus超范围、dev>31、fn>7和寄存器越界。仅在虚拟拓扑副本模拟端点缺失，真板链路训练、眼图和PERST#没有测就标未验。 |
| 周六 5h | 2h定位/修复，2h正常与失败回归，1h闭卷解释和填写周报。没做完顺延，选做首先删减。 |
| 周日 | 休息，无看课和补债要求。 |

## 本周必过项

能解释ECAM地址如何来且不直接从用户态乱写配置空间。明确真板RC、EP与端点功能驱动的不同工作，EDU实验不被包装成完整PCIe验证。

验收同时检查：功能正确、机制解释、独立实现、故障定位、他人可复现。可查手册，不能现场复制生成答案。至少一个30～60行或等价小任务由本人从空白完成，解释每个长度、指针、状态位和失败分支。

## 要留下的文件

在实验仓库的`evidence/W33/`保存：输入与预期、源码版本/构建命令、实际结果、一次故障的现场/根因/修复前后、三张图（数据/通知/资源），以及`周报.md`。临时故障样例独立存放，不污染工作产品。周报写清哪些由本人完成、哪些来自AI，以及模拟/板端软件/波形分别过了什么。

选看与延期：P2：采购PCIe RC/EP板、PHY bring-up、LTSSM和协议分析仪，后续独立立项。

未过：只保留最小复现，记录卡点并重复本周；后续日期整体顺延，不跨门槛硬赶。[上一周](第32周_EDUDMA_超时取消与安全释放.md) · [下一周](第34周_复位与teardown_MSIX和IOMMU边界.md) · [全部周目录](../03_逐周目录.md)
