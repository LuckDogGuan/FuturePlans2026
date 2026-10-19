# 第28学习周：Virtio设备模型：虚拟数据路径阅读

参考日期：2027-07-05～2027-07-11（北京时间）。后续深化段。实际执行前核对[假期日历](../02_日历与中国假期.md)；正式调休或公司加班与本周冲突时整周顺延，不在假期补课。状态：未开始。

## 工作问题与门槛

QEMU里的设备请求怎样经过共享描述符与通知回到guest？模型边界与真实传感器路径有什么不同？

先修：上一学习周的必过项有源码、输入与调试证据；失败项未解决先重复上一周。 本周重要性：P1：device/driver/transport区别、feature negotiation、split virtqueue的descriptor/avail/used、notify/IRQ、buffer ownership。主做驱动阅读，不强制写QEMU设备。

## 精确选课与官方阅读

视频主看/补看：[MIT6.1810 2025官方日程](https://pdos.csail.mit.edu/6.1810/2025/schedule.html)LEC17《File systems》只取块设备调用背景，主看xv6 virtio驱动源码。视频检索“Linux Foundation virtio split virtqueue device driver”，本轮未核实精确免费视频讲次，不以搜索结果充当已看课程。

文字与源码：[OASIS Virtio1.3规范](https://docs.oasis-open.org/virtio/virtio/v1.3/virtio-v1.3.html)Basic Facilities of a Virtio Device中的Feature Bits、Virtqueues、Split Virtqueues，Device Initialization与MMIO transport。[MIT virtio_disk.c](https://github.com/mit-pdos/xv6-riscv/blob/riscv/kernel/virtio_disk.c)的init/rw/intr和kernel/virtio.h，注意xv6可能使用旧接口模式，必须对照源码而非当成完整1.3实现。

视频建议合计1～2小时，必要补看到3小时须挤掉选做，不挤编码。课程章节与手册章节分开，跨年MIT课程不要混编号。资料核验与播放/字幕限制见[课程表](../资料/01_C与系统课程章节核查.md)和[硬件架构表](../资料/02_外设架构QEMU与PCIe核查.md)。

## 每天做什么：正常周15小时

| 时间 | 具体动作与产物 |
|---|---|
| 周一 2h | 先写本周问题的预期图/表，再看指定视频、查手册。标出数据来源、控制/通知来源、对象或资源的归属。不能只抄笔记。 |
| 周二 2h | 从xv6一次只读块请求追到virtio_disk_rw，列出三个描述符的地址/长度/方向 |
| 周三 2h | 本人写一个只在普通内存运行的descriptor链检查器，拒绝越界索引和环，明确它不是设备模拟器 |
| 周四 2h | 为一次读请求记录avail提交→notify→used完成→唤醒，补数据/通知/资源三图，并解释buffer何时归还。 |
| 周五 2h | 开始故障注入：检查器注入坏next、错误WRITE标志、重复归还和长度溢出。真实队列可做少量可回退插桩，不强行改QEMU模型来覆盖所有畸形设备行为。 |
| 周六 5h | 2h定位/修复，2h正常与失败回归，1h闭卷解释和填写周报。没做完顺延，选做首先删减。 |
| 周日 | 休息，无看课和补债要求。 |

## 本周必过项

能解释虚拟设备也有地址/顺序/所有权契约。检查器有独立代码和故障案例，真实路径有读请求证据，模拟检查与guest实际完成分开标。

验收同时检查：功能正确、机制解释、独立实现、故障定位、他人可复现。可查手册，不能现场复制生成答案。至少一个30～60行或等价小任务由本人从空白完成，解释每个长度、指针、状态位和失败分支。

## 要留下的文件

在实验仓库的`evidence/W28/`保存：输入与预期、源码版本/构建命令、实际结果、一次故障的现场/根因/修复前后、三张图（数据/通知/资源），以及`周报.md`。临时故障样例独立存放，不污染工作产品。周报写清哪些由本人完成、哪些来自AI，以及模拟/板端软件/波形分别过了什么。

选看与延期：P2：自己实现完整virtio驱动、packed ring、vhost/vDPA、修改QEMU device model。

未过：只保留最小复现，记录卡点并重复本周；后续日期整体顺延，不跨门槛硬赶。[上一周](第27周_xv6锁与调度_sleep和wakeup.md) · [下一周](第29周_DMA所有权_DMAengine与总线主设备.md) · [全部周目录](../03_逐周目录.md)
