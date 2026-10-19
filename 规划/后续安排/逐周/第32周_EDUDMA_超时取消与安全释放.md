# 第32学习周：EDUDMA：超时取消与安全释放

参考日期：2027-08-02～2027-08-08（北京时间）。后续深化段。实际执行前核对[假期日历](../02_日历与中国假期.md)；正式调休或公司加班与本周冲突时整周顺延，不在假期补课。状态：未开始。

## 工作问题与门槛

传输超时后能直接free吗？设备还可能写内存时如何确保回收顺序正确？

先修：上一学习周的必过项有源码、输入与调试证据；失败项未解决先重复上一周。 本周重要性：P0：协商EDU实际mask、coherent buffer、dma_addr_t、合法长度、RAM↔设备方向、完成IRQ、超时后的quiesce与释放。先只实现一种映射。

## 精确选课与官方阅读

视频主看/补看：[Linux Foundation LFD430官方章节目录](https://training.linuxfoundation.org/training/developing-linux-device-drivers/)《Direct Memory Access (DMA)》只补DMA and Interrupts/Memory Constraints。免费检索“QEMU EDU Linux DMA driver timeout teardown”，本轮没有核实高质量完整免费视频，不将随意博客当规范。

文字与源码：[QEMU EDU规格](https://www.qemu.org/docs/master/specs/edu.html)DMA controller和0x80/0x88/0x90/0x98寄存器、设备内部4096-byte buffer。[Linux DMA API](https://docs.kernel.org/core-api/dma-api-howto.html)coherent API与DMA mask。[Linux PCI驱动指南](https://docs.kernel.org/PCI/pci.html)设备停止/释放流程，实际API以锁定内核为准。

视频建议合计1～2小时，必要补看到3小时须挤掉选做，不挤编码。课程章节与手册章节分开，跨年MIT课程不要混编号。资料核验与播放/字幕限制见[课程表](../资料/01_C与系统课程章节核查.md)和[硬件架构表](../资料/02_外设架构QEMU与PCIe核查.md)。

## 每天做什么：正常周15小时

| 时间 | 具体动作与产物 |
|---|---|
| 周一 2h | 先写本周问题的预期图/表，再看指定视频、查手册。标出数据来源、控制/通知来源、对象或资源的归属。不能只抄笔记。 |
| 周二 2h | 保留x86 guest并显式协商EDU默认28位能力，分配前确认mask，打印CPU指针与DMA地址两列 |
| 周三 2h | 本人实现固定16/128/4096字节往返和独立数据校验，用超时等待完成，不把CPU指针写进DMA寄存器 |
| 周四 2h | 设计并实现停止新请求→使设备停止/确认完成→同步回调→释放的路径，画数据/完成通知/buffer资源三图并重复卸载。 |
| 周五 2h | 开始故障注入：注入超长、错误方向、完成通知丢失和等待被取消。EDU未提供可靠abort时必须先确认DMA结束再释放，无法确认就保持对象并报告，不假装“timeout后free”安全。 |
| 周六 5h | 2h定位/修复，2h正常与失败回归，1h闭卷解释和填写周报。没做完顺延，选做首先删减。 |
| 周日 | 休息，无看课和补债要求。 |

## 本周必过项

有完整字节比对、超时根因与重复bind/unbind证据。mask/长度/ownership每项有依据，不能只用一次DMA成功证明所有失败路径安全。

验收同时检查：功能正确、机制解释、独立实现、故障定位、他人可复现。可查手册，不能现场复制生成答案。至少一个30～60行或等价小任务由本人从空白完成，解释每个长度、指针、状态位和失败分支。

## 要留下的文件

在实验仓库的`evidence/W32/`保存：输入与预期、源码版本/构建命令、实际结果、一次故障的现场/根因/修复前后、三张图（数据/通知/资源），以及`周报.md`。临时故障样例独立存放，不污染工作产品。周报写清哪些由本人完成、哪些来自AI，以及模拟/板端软件/波形分别过了什么。

选看与延期：P1：第二种streaming映射单独分支。Arm virt RAM起点1GiB而EDU默认只覆盖256MiB，迁移时模型与驱动mask同时核对，不能照抄。

未过：只保留最小复现，记录卡点并重复本周；后续日期整体顺延，不跨门槛硬赶。[上一周](第31周_MMIO与IRQ_轮询INTx和MSI.md) · [下一周](第33周_PCIe配置_ECAM和RC_EP边界.md) · [全部周目录](../03_逐周目录.md)
