# 第26学习周：CSR与trap：页表和异常定位

参考日期：2027-06-21～2027-06-27（北京时间）。后续深化段。实际执行前核对[假期日历](../02_日历与中国假期.md)；正式调休或公司加班与本周冲突时整周顺延，不在假期补课。状态：未开始。

## 工作问题与门槛

RISC-V异常来了，哪几个CSR告诉你原因和返回位置？如何判断页故障而不是外设坏数据？

先修：上一学习周的必过项有源码、输入与调试证据；失败项未解决先重复上一周。 本周重要性：P0：复用W25已锁定xv6启动/GDB，沿现有UART驱动追一次外设IRQ与trap主路径。P1：M/S/U、stvec/sepc/scause/stval/sstatus/satp、ecall/sret、Sv39页表权限，时间不够仅精做一个主路径。

## 精确选课与官方阅读

视频主看/补看：[MIT6.1810 2025官方日程](https://pdos.csail.mit.edu/6.1810/2025/schedule.html)LEC6《System call entry/exit》与LEC8《Page faults》各选相关片段。官方会议补看[RISC-V International Privileged ISA](https://www.youtube.com/watch?v=fxLXvrLN5jA)，2018录像只看动机，CSR细节查现行规范。

文字与源码：[RISC-V特权规范v20260120](https://docs.riscv.org/reference/isa/v20260120/priv/priv-index.html)Machine-Level ISA的Trap Handling、Supervisor-Level ISA的Trap/Address Translation及Sv39。[MIT xv6-riscv官方源码](https://github.com/mit-pdos/xv6-riscv)kernel/trap.c、trampoline.S、vm.c与riscv.h，固定同一commit。[QEMU GDB](https://www.qemu.org/docs/master/system/gdb.html)Examining physical memory。

视频建议合计1～2小时，必要补看到3小时须挤掉选做，不挤编码。课程章节与手册章节分开，跨年MIT课程不要混编号。资料核验与播放/字幕限制见[课程表](../资料/01_C与系统课程章节核查.md)和[硬件架构表](../资料/02_外设架构QEMU与PCIe核查.md)。

## 每天做什么：正常周15小时

| 时间 | 具体动作与产物 |
|---|---|
| 周一 2h | 先写本周问题的预期图/表，再看指定视频、查手册。标出数据来源、控制/通知来源、对象或资源的归属。不能只抄笔记。 |
| 周二 2h | 在现有console→uartintr→PLIC→trap路径设置断点，输入合成字节并记录实际CSR/中断来源，禁止第二owner直接读同一UART |
| 周三 2h | 本人把W16的容量检查或溢出统计原则移入现有驱动的一处实验分支，用突发输入核对每个字节的去向，保持console功能可恢复 |
| 周四 2h | 只选UART IRQ主路径完善数据/异常通知/ring与trapframe资源三图，余时再做一次非法用户地址并核页表权限，未做则保留P1待测。 |
| 周五 2h | 开始故障注入：主路径注入突发输入超过既定容量或故意遗漏一次软件唤醒，定位设备有数据/ISR未处理/条件未唤醒哪层失败。若做页表选项，再测跨页用户buffer，不能在生产内核随意解引用用户指针。 |
| 周六 5h | 2h定位/修复，2h正常与失败回归，1h闭卷解释和填写周报。没做完顺延，选做首先删减。 |
| 周日 | 休息，无看课和补债要求。 |

## 本周必过项

一个主路径具备寄存器/MMIO、IRQ/CSR和buffer寿命的连续证据。console UART只有一个owner，独立修改与恢复均可重现。页表选项未做明确标待测，不承诺一周精通trap与完整VM。

验收同时检查：功能正确、机制解释、独立实现、故障定位、他人可复现。可查手册，不能现场复制生成答案。至少一个30～60行或等价小任务由本人从空白完成，解释每个长度、指针、状态位和失败分支。

## 要留下的文件

在实验仓库的`evidence/W26/`保存：输入与预期、源码版本/构建命令、实际结果、一次故障的现场/根因/修复前后、三张图（数据/通知/资源），以及`周报.md`。临时故障样例独立存放，不污染工作产品。周报写清哪些由本人完成、哪些来自AI，以及模拟/板端软件/波形分别过了什么。

选看与延期：P1：同一xv6上的系统调用入口/返回及一次页故障。P2：Hypervisor扩展、PMP完整配置、全套COW lab。

未过：只保留最小复现，记录卡点并重复本周；后续日期整体顺延，不跨门槛硬赶。[上一周](第25周_RV64指令与ABI_第二种架构比较.md) · [下一周](第27周_xv6锁与调度_sleep和wakeup.md) · [全部周目录](../03_逐周目录.md)
