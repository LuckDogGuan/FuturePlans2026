# 第23学习周：MMU与cache：内存属性和屏障

参考日期：2027-05-24～2027-05-30（北京时间）。后续深化段。实际执行前核对[假期日历](../02_日历与中国假期.md)；正式调休或公司加班与本周冲突时整周顺延，不在假期补课。状态：未开始。

## 工作问题与门槛

CPU看见数据更新为什么不代表设备看见了？页表、cache、barrier分别解决哪一层问题？

先修：上一学习周的必过项有源码、输入与调试证据；失败项未解决先重复上一周。 本周重要性：P1必过：VA/PA、页表权限、TLB、Normal/Device属性、cache与coherency、编译器/CPU/设备顺序区别。不要靠volatile修复并发或MMIO顺序。

## 精确选课与官方阅读

视频主看/补看：[Arm官方On-demand Training](https://developer.arm.com/dev2/Training/Arm%20On-demand%20Training)按“Armv8-A memory management memory ordering barriers”检索模块内主题。免费补读[MIT6.1810 2025官方日程](https://pdos.csail.mit.edu/6.1810/2025/schedule.html)LEC5《Page tables》概念，不重复刷完整VM课程，不把MIT讲次说成Arm课。

文字与源码：[Arm A-profile官方指南目录](https://www.arm.com/architecture/learn-the-architecture/a-profile)《AArch64 Memory Management》《AArch64 Memory Attributes and Properties》《Memory Systems, Ordering, and Barriers》。[Linux MMIO访问指南](https://docs.kernel.org/driver-api/device-io.html)__iomem、Differences between I/O access functions。[Linux DMA API](https://docs.kernel.org/core-api/dma-api-howto.html)coherent memory与ordering。

视频建议合计1～2小时，必要补看到3小时须挤掉选做，不挤编码。课程章节与手册章节分开，跨年MIT课程不要混编号。资料核验与播放/字幕限制见[课程表](../资料/01_C与系统课程章节核查.md)和[硬件架构表](../资料/02_外设架构QEMU与PCIe核查.md)。

## 每天做什么：正常周15小时

| 时间 | 具体动作与产物 |
|---|---|
| 周一 2h | 先写本周问题的预期图/表，再看指定视频、查手册。标出数据来源、控制/通知来源、对象或资源的归属。不能只抄笔记。 |
| 周二 2h | 在W22 U-Boot环境阅读一项已有映射/内存属性配置，画CPU与设备看到的地址区别，不要求尚未准备的Linux guest或从零实现全部页表 |
| 周三 2h | 写一个普通内存buffer与MMIO寄存器访问的独立对照片段，列出访问器/宽度/属性/ownership变化 |
| 周四 2h | 为描述符字段→ownership→doorbell写顺序说明并查官方保证，画数据/通知/映射资源三图，QEMU无乱序只记未触发。 |
| 周五 2h | 开始故障注入：在W21 qemu-user程序中制造用户态只读页写入或无映射地址访问，收集信号与故障地址；它不证明guest内核页表已实现。屏障缺失用审查与独立模型说明，不能声称QEMU必稳定重现真机cache错误。 |
| 周六 5h | 2h定位/修复，2h正常与失败回归，1h闭卷解释和填写周报。没做完顺延，选做首先删减。 |
| 周日 | 休息，无看课和补债要求。 |

## 本周必过项

能区分cache维护、内存屏障、锁、MMIO accessor四种职责。解释一个页故障与一段设备提交顺序，未做真板一致性实验清楚标待验。

验收同时检查：功能正确、机制解释、独立实现、故障定位、他人可复现。可查手册，不能现场复制生成答案。至少一个30～60行或等价小任务由本人从空白完成，解释每个长度、指针、状态位和失败分支。

## 要留下的文件

在实验仓库的`evidence/W23/`保存：输入与预期、源码版本/构建命令、实际结果、一次故障的现场/根因/修复前后、三张图（数据/通知/资源），以及`周报.md`。临时故障样例独立存放，不污染工作产品。周报写清哪些由本人完成、哪些来自AI，以及模拟/板端软件/波形分别过了什么。

选看与延期：P2：完整页表库、TLB shootdown实现、IOMMU驱动留后续。

未过：只保留最小复现，记录卡点并重复本周；后续日期整体顺延，不跨门槛硬赶。[上一周](第22周_AArch64启动_链接异常与GIC概览.md) · [下一周](第24周_Linux启动链与BSP_版本和资源闭环.md) · [全部周目录](../03_逐周目录.md)
