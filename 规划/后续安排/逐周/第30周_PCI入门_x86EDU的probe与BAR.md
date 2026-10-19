# 第30学习周：PCI入门：x86EDU的probe与BAR

参考日期：2027-07-19～2027-07-25（北京时间）。后续深化段。实际执行前核对[假期日历](../02_日历与中国假期.md)；正式调休或公司加班与本周冲突时整周顺延，不在假期补课。状态：未开始。

## 工作问题与门槛

从PCI枚举到可访问寄存器，设备地址是谁分配的？probe失败时哪些资源已经属于驱动？

先修：上一学习周的必过项有源码、输入与调试证据；失败项未解决先重复上一周。 本周重要性：P0：BDF/vendor/device/class、pci_driver/id_table、probe/remove、enable、BAR资源申请/映射、访问宽度。首轮固定x86 PC guest与EDU，暂不启DMA。

## 精确选课与官方阅读

视频主看/补看：[Linux Foundation LFD430官方章节目录](https://training.linuxfoundation.org/training/developing-linux-device-drivers/)章节《PCI》中的PCI Device Drivers、Accessing Configuration Space、Accessing I/O and Memory Spaces。免费检索“Linux Foundation writing PCI driver probe BAR QEMU EDU”，未核实免费视频讲次。

文字与源码：[Linux PCI驱动指南](https://docs.kernel.org/PCI/pci.html)pci_register_driver、Device Initialization Steps、Enable the PCI device、Request MMIO/IOP resources。[QEMU EDU规格](https://www.qemu.org/docs/master/specs/edu.html)PCI specs/MMIO area spec。[Linux MMIO访问指南](https://docs.kernel.org/driver-api/device-io.html)__iomem pointer tokens。[QEMU官方PCIe拓扑说明](https://github.com/qemu/qemu/blob/master/docs/pcie.txt)PCI only hierarchy仅作模型边界。

视频建议合计1～2小时，必要补看到3小时须挤掉选做，不挤编码。课程章节与手册章节分开，跨年MIT课程不要混编号。资料核验与播放/字幕限制见[课程表](../资料/01_C与系统课程章节核查.md)和[硬件架构表](../资料/02_外设架构QEMU与PCIe核查.md)。

## 每天做什么：正常周15小时

| 时间 | 具体动作与产物 |
|---|---|
| 周一 2h | 先写本周问题的预期图/表，再看指定视频、查手册。标出数据来源、控制/通知来源、对象或资源的归属。不能只抄笔记。 |
| 周二 2h | 在隔离x86 Linux guest添加EDU，记录QEMU/kernel版本和lspci/sysfs resource，保留能启动的基线 |
| 周三 2h | 本人写最小PCI模块匹配1234:11e8，enable并申请映射BAR，读取ID和liveness寄存器，逐个返回值检查 |
| 周四 2h | 实现对应remove和probe部分失败回滚，完成重复bind/unbind，画BAR数据/匹配通知/映射资源三图。 |
| 周五 2h | 开始故障注入：模拟ID不匹配、BAR申请失败与映射后人工失败出口，核资源是否回收。禁止扫描并操作宿主机任意真实PCI设备，EDU只有其规格允许的访问宽度。 |
| 周六 5h | 2h定位/修复，2h正常与失败回归，1h闭卷解释和填写周报。没做完顺延，选做首先删减。 |
| 周日 | 休息，无看课和补债要求。 |

## 本周必过项

能由BDF找到BAR并解释bus地址与host资源区别。最小驱动独立实现，失败路径可重复，尚未加入IRQ/DMA如实记录。

验收同时检查：功能正确、机制解释、独立实现、故障定位、他人可复现。可查手册，不能现场复制生成答案。至少一个30～60行或等价小任务由本人从空白完成，解释每个长度、指针、状态位和失败分支。

## 要留下的文件

在实验仓库的`evidence/W30/`保存：输入与预期、源码版本/构建命令、实际结果、一次故障的现场/根因/修复前后、三张图（数据/通知/资源），以及`周报.md`。临时故障样例独立存放，不污染工作产品。周报写清哪些由本人完成、哪些来自AI，以及模拟/板端软件/波形分别过了什么。

选看与延期：P1：managed API与手动释放方式对照后选一套。P2：字符设备完整接口/真实PCIe硬件。

未过：只保留最小复现，记录卡点并重复本周；后续日期整体顺延，不跨门槛硬赶。[上一周](第29周_DMA所有权_DMAengine与总线主设备.md) · [下一周](第31周_MMIO与IRQ_轮询INTx和MSI.md) · [全部周目录](../03_逐周目录.md)
