# 第22学习周：AArch64启动：链接异常与GIC概览

参考日期：2027-05-17～2027-05-23（北京时间）。后续深化段。实际执行前核对[假期日历](../02_日历与中国假期.md)；正式调休或公司加班与本周冲突时整周顺延，不在假期补课。状态：未开始。

## 工作问题与门槛

从ELF入口到C函数，栈和.bss是谁准备的？定时器或错误访存如何改变执行流？

先修：上一学习周的必过项有源码、输入与调试证据；失败项未解决先重复上一周。 本周重要性：P1：链接地址/加载地址、ENTRY/section/.bss、启动汇编、异常向量、EL与GIC职责。只做单核模板上的一次同步异常，GIC独立初始化列选做。

## 精确选课与官方阅读

视频主看/补看：[Arm官方On-demand Training](https://developer.arm.com/dev2/Training/Arm%20On-demand%20Training)模块《Introduction to Armv8-A Architecture》《Introduction to GICv3/v4 Architecture》只看异常/路由概念。免费检索“Arm AArch64 exception vector bare metal GIC overview”，没有核实可公开播放的精确讲次。

文字与源码：[Arm A-profile官方指南目录](https://www.arm.com/architecture/learn-the-architecture/a-profile)《AArch64 Exception Model》《Generic Interrupt Controller v3 and v4, Overview》。[U-Boot官方QEMU ARM](https://docs.u-boot.org/en/latest/board/emulation/qemu-arm.html)Building/Running non-secure分节及qemu_arm64_defconfig；其arch/arm/cpu/armv8/start.S与配套链接脚本。[QEMU GDB](https://www.qemu.org/docs/master/system/gdb.html)。不进入OP-TEE/TF-A secure路线，不假定运行在EL1。

视频建议合计1～2小时，必要补看到3小时须挤掉选做，不挤编码。课程章节与手册章节分开，跨年MIT课程不要混编号。资料核验与播放/字幕限制见[课程表](../资料/01_C与系统课程章节核查.md)和[硬件架构表](../资料/02_外设架构QEMU与PCIe核查.md)。

## 每天做什么：正常周15小时

| 时间 | 具体动作与产物 |
|---|---|
| 周一 2h | 先写本周问题的预期图/表，再看指定视频、查手册。标出数据来源、控制/通知来源、对象或资源的归属。不能只抄笔记。 |
| 周二 2h | 复用锁定版U-Boot官方qemu_arm64_defconfig与non-secure启动命令，先构建并停到入口，标出栈/.bss/异常表/map，不从零搭框架 |
| 周三 2h | 本人增加一段含静态零初始化数组的诊断函数，GDB跟踪已有.bss清零与调用C过程，对比SP和变量 |
| 周四 2h | 在独立实验命令中触发一次可控同步异常，观察现有向量保存的ESR/ELR/FAR及EL，不写完整异常框架，补三图，GIC仅画路由。 |
| 周五 2h | 开始故障注入：分别改坏一个链接符号或栈对齐，在独立分支观察链接错误或异常。不得假定所有异常都有有效FAR，更不能把GICv3表直接抄到A7板。 |
| 周六 5h | 2h定位/修复，2h正常与失败回归，1h闭卷解释和填写周报。没做完顺延，选做首先删减。 |
| 周日 | 休息，无看课和补债要求。 |

## 本周必过项

能从复位/加载入口解释到C的每一步。同步异常有原因和返回地址证据。GIC理论项与未做的外部IRQ实作分别标注，不冒称完整启动固件。

验收同时检查：功能正确、机制解释、独立实现、故障定位、他人可复现。可查手册，不能现场复制生成答案。至少一个30～60行或等价小任务由本人从空白完成，解释每个长度、指针、状态位和失败分支。

## 要留下的文件

在实验仓库的`evidence/W22/`保存：输入与预期、源码版本/构建命令、实际结果、一次故障的现场/根因/修复前后、三张图（数据/通知/资源），以及`周报.md`。临时故障样例独立存放，不污染工作产品。周报写清哪些由本人完成、哪些来自AI，以及模拟/板端软件/波形分别过了什么。

选看与延期：P2：自行完整实现GIC与所有异常级切换、Secure monitor、多核唤醒。

未过：只保留最小复现，记录卡点并重复本周；后续日期整体顺延，不跨门槛硬赶。[上一周](第21周_AArch64基础_指令与ABI迁移.md) · [下一周](第23周_MMU与cache_内存属性和屏障.md) · [全部周目录](../03_逐周目录.md)
