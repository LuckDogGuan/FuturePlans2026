# 第31学习周：MMIO与IRQ：轮询INTx和MSI

参考日期：2027-07-26～2027-08-01（北京时间）。后续深化段。实际执行前核对[假期日历](../02_日历与中国假期.md)；正式调休或公司加班与本周冲突时整周顺延，不在假期补课。状态：未开始。

## 工作问题与门槛

设备计算完成后，轮询、共享中断与MSI分别怎样通知CPU，为什么确认寄存器不能省？

先修：上一学习周的必过项有源码、输入与调试证据；失败项未解决先重复上一周。 本周重要性：P0：readl/writel及宽度、寄存器副作用、bounded polling、INTx来源判定、MSI向量、完成条件与超时，EDU不假定支持MSI-X。

## 精确选课与官方阅读

视频主看/补看：[Linux Foundation LFD430官方章节目录](https://training.linuxfoundation.org/training/developing-linux-device-drivers/)《Interrupt Handling: Deferrable Functions and User Drivers》只看中断来源/上下文，结合PCI章节。免费检索“Linux Foundation PCI MSI INTx interrupt driver”，无精确免费视频讲次已核，不重复W30全部PCI课。

文字与源码：[QEMU EDU规格](https://www.qemu.org/docs/master/specs/edu.html)MMIO area spec、IRQ controller，重点0x20/0x24/0x60/0x64。[Linux MSI指南](https://docs.kernel.org/PCI/msi-howto.html)pci_alloc_irq_vectors、pci_irq_vector、free vectors。[Linux MMIO访问指南](https://docs.kernel.org/driver-api/device-io.html)Accessing the device与posted write。

视频建议合计1～2小时，必要补看到3小时须挤掉选做，不挤编码。课程章节与手册章节分开，跨年MIT课程不要混编号。资料核验与播放/字幕限制见[课程表](../资料/01_C与系统课程章节核查.md)和[硬件架构表](../资料/02_外设架构QEMU与PCIe核查.md)。

## 每天做什么：正常周15小时

| 时间 | 具体动作与产物 |
|---|---|
| 周一 2h | 先写本周问题的预期图/表，再看指定视频、查手册。标出数据来源、控制/通知来源、对象或资源的归属。不能只抄笔记。 |
| 周二 2h | 在W30驱动增加有截止时间的factorial或liveness实验，列每个寄存器的offset/width/RO-RW-WO/合法位 |
| 周三 2h | 本人实现INTx处理并判断来源和确认状态，把完成转换为可等待事件，保持设备先静默再注册 |
| 周四 2h | 切到MSI模式重复同一输入，记录IRQ计数及完成状态，画数据/中断通知/IRQ资源三图，对照轮询结果。 |
| 周五 2h | 开始故障注入：抑制一次完成通知、重复触发状态、收到非本设备INTx时返回IRQ_NONE。MSI模式仍确认EDU状态，不能只清软件标志。 |
| 周六 5h | 2h定位/修复，2h正常与失败回归，1h闭卷解释和填写周报。没做完顺延，选做首先删减。 |
| 周日 | 休息，无看课和补债要求。 |

## 本周必过项

轮询/INTx/MSI各有一次成功与一次超时记录。IRQ handler不做不允许的睡眠操作，能从计数/寄存器区分未触发、未确认、未唤醒。

验收同时检查：功能正确、机制解释、独立实现、故障定位、他人可复现。可查手册，不能现场复制生成答案。至少一个30～60行或等价小任务由本人从空白完成，解释每个长度、指针、状态位和失败分支。

## 要留下的文件

在实验仓库的`evidence/W31/`保存：输入与预期、源码版本/构建命令、实际结果、一次故障的现场/根因/修复前后、三张图（数据/通知/资源），以及`周报.md`。临时故障样例独立存放，不污染工作产品。周报写清哪些由本人完成、哪些来自AI，以及模拟/板端软件/波形分别过了什么。

选看与延期：P2：MSI-X多队列留W34能力核对，EDU不支持的功能不伪造。

未过：只保留最小复现，记录卡点并重复本周；后续日期整体顺延，不跨门槛硬赶。[上一周](第30周_PCI入门_x86EDU的probe与BAR.md) · [下一周](第32周_EDUDMA_超时取消与安全释放.md) · [全部周目录](../03_逐周目录.md)
