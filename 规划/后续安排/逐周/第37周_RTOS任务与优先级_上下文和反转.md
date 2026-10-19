# 第37学习周：RTOS任务与优先级：上下文和反转

参考日期：2027-09-06～2027-09-12（北京时间）。后续深化段。实际执行前核对[假期日历](../02_日历与中国假期.md)；正式调休或公司加班与本周冲突时整周顺延，不在假期补课。状态：未开始。

## 工作问题与门槛

如果采集与控制任务运行在RTOS，优先级、阻塞、ISR通知和互斥锁怎样协调？高优先级为何仍会被低优先级拖住？

先修：上一学习周的必过项有源码、输入与调试证据；失败项未解决先重复上一周。 本周重要性：P1必过：task状态/栈/context switch、固定优先级抢占、队列与通知、FromISR边界、mutex优先级继承及其简化限制。选择已有QEMU port，不从零移植。

## 精确选课与官方阅读

视频主看/补看：视频检索“FreeRTOS official task scheduling mutex priority inheritance”，本轮未核实免费完整官方讲次。以[FreeRTOS官方Kernel Book](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book)官方图解配合源码为主，讲者无官方来源的视频只作可选解释，不替代内核行为核查。

文字与源码：[FreeRTOS官方QEMU示例配置](https://github.com/FreeRTOS/FreeRTOS/blob/main/FreeRTOS/Demo/CORTEX_LM3S6965_GCC_QEMU/FreeRTOSConfig.h)定位已有LM3S6965 GCC QEMU demo及其main.c/Makefile，开始前按锁定commit复核。[FreeRTOS官方Kernel Book](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book)Task Management、Queue Management、ch08 Resource Management的8.3.3 Priority Inheritance。[FreeRTOS mutex说明](https://freertos.org/Real-time-embedded-RTOS-mutexes.html)Simplified priority inheritance。

视频建议合计1～2小时，必要补看到3小时须挤掉选做，不挤编码。课程章节与手册章节分开，跨年MIT课程不要混编号。资料核验与播放/字幕限制见[课程表](../资料/01_C与系统课程章节核查.md)和[硬件架构表](../资料/02_外设架构QEMU与PCIe核查.md)。

## 每天做什么：正常周15小时

| 时间 | 具体动作与产物 |
|---|---|
| 周一 2h | 先写本周问题的预期图/表，再看指定视频、查手册。标出数据来源、控制/通知来源、对象或资源的归属。不能只抄笔记。 |
| 周二 2h | 先运行官方支持的既有QEMU demo并记录port/内核配置，只保留所需示例，不改工作板固件 |
| 周三 2h | 本人写采样生产/处理两个阻塞任务与有界队列，分别记录栈归属和任务状态转换 |
| 周四 2h | 构造低/中/高三任务的一个mutex反转时序，对比binary semaphore和mutex，画数据/唤醒通知/任务栈与锁资源三图，按tick而非墙钟解释结果。 |
| 周五 2h | 开始故障注入：模拟高优先级忙等导致饥饿、队列满和低优先级持锁。ISR内不能拿mutex，优先级继承不被说成能消除全部反转或死锁。 |
| 周六 5h | 2h定位/修复，2h正常与失败回归，1h闭卷解释和填写周报。没做完顺延，选做首先删减。 |
| 周日 | 休息，无看课和补债要求。 |

## 本周必过项

能解释一次阻塞到唤醒和一次上下文切换。至少一个反转实例有预期/实际轨迹，知道QEMU port不证明硬件中断优先级或真实实时性。

验收同时检查：功能正确、机制解释、独立实现、故障定位、他人可复现。可查手册，不能现场复制生成答案。至少一个30～60行或等价小任务由本人从空白完成，解释每个长度、指针、状态位和失败分支。

## 要留下的文件

在实验仓库的`evidence/W37/`保存：输入与预期、源码版本/构建命令、实际结果、一次故障的现场/根因/修复前后、三张图（数据/通知/资源），以及`周报.md`。临时故障样例独立存放，不污染工作产品。周报写清哪些由本人完成、哪些来自AI，以及模拟/板端软件/波形分别过了什么。

选看与延期：P2：从零写RTOS、全新RISC-V port、SMP、从Linux产品迁移到RTOS。

未过：只保留最小复现，记录卡点并重复本周；后续日期整体顺延，不跨门槛硬赶。[上一周](第36周_性能与延迟_ftrace和perf证据.md) · [下一周](第38周_系统恢复_故障矩阵与回滚.md) · [全部周目录](../03_逐周目录.md)
