# 第21学习周：AArch64基础：指令与ABI迁移

参考日期：2027-05-10～2027-05-16（北京时间）。后续深化段。实际执行前核对[假期日历](../02_日历与中国假期.md)；正式调休或公司加班与本周冲突时整周顺延，不在假期补课。状态：未开始。

## 工作问题与门槛

把已有字节解码核心迁移到64位时，哪些长度、指针、参数和符号扩展假设会失效？

先修：上一学习周的必过项有源码、输入与调试证据；失败项未解决先重复上一周。 本周重要性：P1核心概念必过：A64执行状态、W/X寄存器、byte/halfword/word/doubleword、load/store与条件分支、AAPCS64参数和栈对齐。暂不学RTL和全指令背诵。

## 精确选课与官方阅读

视频主看/补看：[Arm官方On-demand Training](https://developer.arm.com/dev2/Training/Arm%20On-demand%20Training)精确模块《Introduction to Armv8-A Architecture》，只看程序员模型主题，页面列中文译稿但可能需订阅。免费替代检索“Arm AArch64 Instruction Set Architecture load store AAPCS64”，未核实免费视频讲次，不伪编号。

文字与源码：[Arm A-profile官方指南目录](https://www.arm.com/architecture/learn-the-architecture/a-profile)《AArch64 Instruction Set Architecture (ISA)》寄存器、load/store、分支主题。[Arm官方AAPCS64](https://github.com/ARM-software/abi-aa/blob/main/aapcs64/aapcs64.rst)Data types、Registers、Parameter passing。[QEMU Arm virt](https://www.qemu.org/docs/master/system/arm/virt.html)CPU model选择与[QEMU GDB](https://www.qemu.org/docs/master/system/gdb.html)。

视频建议合计1～2小时，必要补看到3小时须挤掉选做，不挤编码。课程章节与手册章节分开，跨年MIT课程不要混编号。资料核验与播放/字幕限制见[课程表](../资料/01_C与系统课程章节核查.md)和[硬件架构表](../资料/02_外设架构QEMU与PCIe核查.md)。

## 每天做什么：正常周15小时

| 时间 | 具体动作与产物 |
|---|---|
| 周一 2h | 先写本周问题的预期图/表，再看指定视频、查手册。标出数据来源、控制/通知来源、对象或资源的归属。不能只抄笔记。 |
| 周二 2h | 先按QEMU user-mode官方文档准备qemu-aarch64与匹配的交叉工具链/sysroot，运行W10的AArch64用户程序核类型宽度，不要求先有完整guest内核 |
| 周三 2h | 从本人写的30～60行转换/调用例程预测参数寄存器和返回值，用objdump与GDB stub逐条对照 |
| 周四 2h | 画字节→字段→返回值数据图、调用通知图、栈与buffer资源图，指出Armv7与A64至少三处差异。 |
| 周五 2h | 开始故障注入：注入指针转32位整数、把size_t用错printf格式、把有符号半字当无符号读取。危险指针截断仅在独立错误样例观察，不在生产工程运行。 |
| 周六 5h | 2h定位/修复，2h正常与失败回归，1h闭卷解释和填写周报。没做完顺延，选做首先删减。 |
| 周日 | 休息，无看课和补债要求。 |

## 本周必过项

同一输入两架构解码结果一致。能解释一次调用、两条寻址指令及符号扩展。A64作为迁移视角掌握核心，不以本周搭完64位内核为门槛。

验收同时检查：功能正确、机制解释、独立实现、故障定位、他人可复现。可查手册，不能现场复制生成答案。至少一个30～60行或等价小任务由本人从空白完成，解释每个长度、指针、状态位和失败分支。

## 要留下的文件

在实验仓库的`evidence/W21/`保存：输入与预期、源码版本/构建命令、实际结果、一次故障的现场/根因/修复前后、三张图（数据/通知/资源），以及`周报.md`。临时故障样例独立存放，不污染工作产品。周报写清哪些由本人完成、哪些来自AI，以及模拟/板端软件/波形分别过了什么。

选看与延期：P2：Neon/SVE/SME、复杂浮点ABI、微架构流水线细节。

未过：只保留最小复现，记录卡点并重复本周；后续日期整体顺延，不跨门槛硬赶。[上一周](第20周_六个月核心验收_设备诊断作品.md) · [下一周](第22周_AArch64启动_链接异常与GIC概览.md) · [全部周目录](../03_逐周目录.md)
