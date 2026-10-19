# 第25学习周：RV64指令与ABI：第二种架构比较

参考日期：2027-06-14～2027-06-20（北京时间）。后续深化段。实际执行前核对[假期日历](../02_日历与中国假期.md)；正式调休或公司加班与本周冲突时整周顺延，不在假期补课。状态：未开始。

## 工作问题与门槛

同一套C代码换RISC-V，如何从工具链、ISA扩展和ABI判断能不能运行？

先修：上一学习周的必过项有源码、输入与调试证据；失败项未解决先重复上一周。 本周重要性：P1必过：RV32/RV64、XLEN、整数寄存器、load/store/符号扩展、分支、-march与-mabi区别、调用约定。先通过锁定版xv6工具链/QEMU/GDB启动门槛，不从零写裸机启动。

## 精确选课与官方阅读

视频主看/补看：[MIT6.1810 2025官方日程](https://pdos.csail.mit.edu/6.1810/2025/schedule.html)LEC2《C in xv6 and examples》选RISC-V反汇编相关内容。若该年页面无独立录像，按链接年份观看并标年份，不套2020讲号。补看关键词“RISC-V International RV64I calling convention”，不要求全ISA大会录像。

文字与源码：[RISC-V非特权规范v20260120](https://docs.riscv.org/reference/isa/v20260120/unpriv/unpriv-index.html)RV32I的Programmers Model/Base Instruction Formats/Load and Store，接RV64I。[RISC-V官方psABI](https://riscv-non-isa.github.io/riscv-elf-psabi-doc/)1.1 Integer Register Convention、2.1 Integer Calling Convention、4.1 Types/Alignments。psABI网页本轮为2.0-rc0，记录阅读commit，只使用已确认的基础ABI。[QEMU RISC-V virt](https://www.qemu.org/docs/master/system/riscv/virt.html)。

视频建议合计1～2小时，必要补看到3小时须挤掉选做，不挤编码。课程章节与手册章节分开，跨年MIT课程不要混编号。资料核验与播放/字幕限制见[课程表](../资料/01_C与系统课程章节核查.md)和[硬件架构表](../资料/02_外设架构QEMU与PCIe核查.md)。

## 每天做什么：正常周15小时

| 时间 | 具体动作与产物 |
|---|---|
| 周一 2h | 先写本周问题的预期图/表，再看指定视频、查手册。标出数据来源、控制/通知来源、对象或资源的归属。不能只抄笔记。 |
| 周二 2h | 复用锁定commit的MIT xv6框架，核工具链/QEMU/GDB版本并通过make qemu与GDB断点，环境未通先停在本步 |
| 周三 2h | 本人把W16轮询/超时/ring中的纯C部分编译进xv6用户小例程，对照有符号读取及嵌套调用反汇编，记录-march/-mabi/ELF属性 |
| 周四 2h | 先沿现有console/uart驱动跟踪真实MMIO读写，再独立增加一项有界诊断或错误处理，保留原驱动唯一owner，完成数据/调用通知/栈buffer资源三图。 |
| 周五 2h | 开始故障注入：用独立构建制造ISA/ABI不匹配，保存链接或加载诊断。再对照lw/lwu的符号扩展。不得另写第二个驱动并发读写console UART，替换只在已停原owner的独占实验分支做。 |
| 周六 5h | 2h定位/修复，2h正常与失败回归，1h闭卷解释和填写周报。没做完顺延，选做首先删减。 |
| 周日 | 休息，无看课和补债要求。 |

## 本周必过项

xv6可启动且GDB断点可复现。同一纯C测试向量结果一致，能解释-march/-mabi和一次调用。真实UART路径有跟踪与一项本人修改证据，不能用W16主机模型冒充已操作MMIO。

验收同时检查：功能正确、机制解释、独立实现、故障定位、他人可复现。可查手册，不能现场复制生成答案。至少一个30～60行或等价小任务由本人从空白完成，解释每个长度、指针、状态位和失败分支。

## 要留下的文件

在实验仓库的`evidence/W25/`保存：输入与预期、源码版本/构建命令、实际结果、一次故障的现场/根因/修复前后、三张图（数据/通知/资源），以及`周报.md`。临时故障样例独立存放，不污染工作产品。周报写清哪些由本人完成、哪些来自AI，以及模拟/板端软件/波形分别过了什么。

选看与延期：P2：向量V、密码扩展、自定义指令与RTL核实现。

未过：只保留最小复现，记录卡点并重复本周；后续日期整体顺延，不跨门槛硬赶。[上一周](第24周_Linux启动链与BSP_版本和资源闭环.md) · [下一周](第26周_CSR与trap_页表和异常定位.md) · [全部周目录](../03_逐周目录.md)
