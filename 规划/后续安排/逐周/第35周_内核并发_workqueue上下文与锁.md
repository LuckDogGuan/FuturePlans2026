# 第35学习周：内核并发：workqueue上下文与锁

参考日期：2027-08-23～2027-08-29（北京时间）。后续深化段。实际执行前核对[假期日历](../02_日历与中国假期.md)；正式调休或公司加班与本周冲突时整周顺延，不在假期补课。状态：未开始。

## 工作问题与门槛

中断、工作线程、用户调用和remove同时到来，怎样让采集结果只完成一次并安全退出？

先修：上一学习周的必过项有源码、输入与调试证据；失败项未解决先重复上一周。 本周重要性：P0：hard IRQ/thread/process/workqueue上下文、睡眠规则、spinlock/mutex、wait/completion、cancel/flush、引用与锁顺序。PREEMPT_RT规则单独对照。

## 精确选课与官方阅读

视频主看/补看：[Bootlin内核驱动教材](https://bootlin.com/training/kernel/)锁与睡眠/中断/工作队列教材，结合[Linux Foundation LFD430官方章节目录](https://training.linuxfoundation.org/training/developing-linux-device-drivers/)《Interrupt Handling: Deferrable Functions and User Drivers》Work Queues/Threaded Interrupt Handlers。免费检索“Bootlin workqueue locking interrupt context”，精确录像讲次未核。

文字与源码：[Linux Workqueue](https://docs.kernel.org/core-api/workqueue.html)Introduction/Why concurrency managed workqueue/queue_work/cancel_work_sync。[Linux Lock types and their rules](https://docs.kernel.org/locking/locktypes.html)Lock categories、Sleeping locks、CPU local locks、spinlock与PREEMPT_RT。[Linux generic IRQ](https://docs.kernel.org/core-api/genericirq.html)request_threaded_irq/free_irq/synchronize_irq。

视频建议合计1～2小时，必要补看到3小时须挤掉选做，不挤编码。课程章节与手册章节分开，跨年MIT课程不要混编号。资料核验与播放/字幕限制见[课程表](../资料/01_C与系统课程章节核查.md)和[硬件架构表](../资料/02_外设架构QEMU与PCIe核查.md)。

## 每天做什么：正常周15小时

| 时间 | 具体动作与产物 |
|---|---|
| 周一 2h | 先写本周问题的预期图/表，再看指定视频、查手册。标出数据来源、控制/通知来源、对象或资源的归属。不能只抄笔记。 |
| 周二 2h | 把W31或W32驱动仅一项耗时处理移入workqueue，列每个回调上下文和允许调用，先不增加新设备 |
| 周三 2h | 本人实现QUEUED/RUNNING/DONE/STOPPING及一次完成规则，短共享状态用正确锁保护，工作函数之外等待 |
| 周四 2h | 执行请求/完成/卸载交错，画数据队列/唤醒通知/锁引用资源三图，确认停止顺序不会在持锁时同步等待自己。 |
| 周五 2h | 开始故障注入：注入重复queue、取消时worker仍运行、卸载时IRQ晚到及锁顺序反转。在实验内核启可用的lockdep/DEBUG_ATOMIC_SLEEP，工具未启用就记录缺项。 |
| 周六 5h | 2h定位/修复，2h正常与失败回归，1h闭卷解释和填写周报。没做完顺延，选做首先删减。 |
| 周日 | 休息，无看课和补债要求。 |

## 本周必过项

能逐行解释每把锁保护的对象与原因。100轮有界开始/停止无已知错误，报告负载与版本，不把这个边界称长期稳定性证明。

验收同时检查：功能正确、机制解释、独立实现、故障定位、他人可复现。可查手册，不能现场复制生成答案。至少一个30～60行或等价小任务由本人从空白完成，解释每个长度、指针、状态位和失败分支。

## 要留下的文件

在实验仓库的`evidence/W35/`保存：输入与预期、源码版本/构建命令、实际结果、一次故障的现场/根因/修复前后、三张图（数据/通知/资源），以及`周报.md`。临时故障样例独立存放，不污染工作产品。周报写清哪些由本人完成、哪些来自AI，以及模拟/板端软件/波形分别过了什么。

选看与延期：P1：PREEMPT_RT下锁语义差异阅读。P2：自己实现调度器/RCU/复杂lock-free。

未过：只保留最小复现，记录卡点并重复本周；后续日期整体顺延，不跨门槛硬赶。[上一周](第34周_复位与teardown_MSIX和IOMMU边界.md) · [下一周](第36周_性能与延迟_ftrace和perf证据.md) · [全部周目录](../03_逐周目录.md)
