# 第24学习周：Linux启动链与BSP：版本和资源闭环

参考日期：2027-05-31～2027-06-06（北京时间）。后续深化段。实际执行前核对[假期日历](../02_日历与中国假期.md)；正式调休或公司加班与本周冲突时整周顺延，不在假期补课。状态：未开始。

## 工作问题与门槛

板端能启动却相机/背光失效，如何分清bootloader、kernel、DTB、rootfs和服务配置？

先修：上一学习周的必过项有源码、输入与调试证据；失败项未解决先重复上一周。 本周重要性：P0：ROM→bootloader→kernel→init→服务，BSP/主线差异，Image/DTB/modules/rootfs匹配，cmdline、驱动绑定与可回退版本。

## 精确选课与官方阅读

视频主看/补看：[Bootlin Device Tree101视频与课件](https://bootlin.com/blog/device-tree-101-webinar-slides-and-videos/)只看Device Tree与Linux驱动关联主题。[Bootlin公开演讲与录像目录](https://bootlin.com/docs/)检索“Bootlin Linux boot process U-Boot device tree”，未核实独立免费录像讲次，可用官方教材替代。

文字与源码：[Linux Booting AArch64 Linux](https://docs.kernel.org/arch/arm64/booting.html)Setup the device tree、Call the kernel image。[QEMU Arm virt](https://www.qemu.org/docs/master/system/arm/virt.html)Boot options。[Bootlin内核驱动教材](https://bootlin.com/training/kernel/)启动/驱动模型教材。当前工作板的实际BSP源码与版本清单优先，不把i.MX地址写入Luckfox。

视频建议合计1～2小时，必要补看到3小时须挤掉选做，不挤编码。课程章节与手册章节分开，跨年MIT课程不要混编号。资料核验与播放/字幕限制见[课程表](../资料/01_C与系统课程章节核查.md)和[硬件架构表](../资料/02_外设架构QEMU与PCIe核查.md)。

## 每天做什么：正常周15小时

| 时间 | 具体动作与产物 |
|---|---|
| 周一 2h | 先写本周问题的预期图/表，再看指定视频、查手册。标出数据来源、控制/通知来源、对象或资源的归属。不能只抄笔记。 |
| 周二 2h | 先整理工作板只读启动日志和版本，再按Buildroot官方manual的配置/构建/QEMU章节准备锁定版qemu_aarch64_virt_defconfig环境，构建过长可后台继续但不跳门槛 |
| 周三 2h | 在独立QEMU镜像修改一个无风险cmdline或测试节点，追踪到内核日志与probe，只选一项核心变化 |
| 周四 2h | 本人写小型版本核对CLI，核架构/内核模块版本，画数据加载/启动通知/镜像资源三图并切回旧实验镜像。 |
| 周五 2h | 开始故障注入：只在副本上注入不匹配DT compatible或错误root参数，判断停在哪一层并恢复。生产板升级、烧录和服务变更不属于本周自动执行内容。 |
| 周六 5h | 2h定位/修复，2h正常与失败回归，1h闭卷解释和填写周报。没做完顺延，选做首先删减。 |
| 周日 | 休息，无看课和补债要求。 |

## 本周必过项

能把“无法启动/无法probe/服务未启动”分层定位。有一份版本清单与已试过的实验回退步骤，能解释BSP稳定点和主线资料差别。

验收同时检查：功能正确、机制解释、独立实现、故障定位、他人可复现。可查手册，不能现场复制生成答案。至少一个30～60行或等价小任务由本人从空白完成，解释每个长度、指针、状态位和失败分支。

## 要留下的文件

在实验仓库的`evidence/W24/`保存：输入与预期、源码版本/构建命令、实际结果、一次故障的现场/根因/修复前后、三张图（数据/通知/资源），以及`周报.md`。临时故障样例独立存放，不污染工作产品。周报写清哪些由本人完成、哪些来自AI，以及模拟/板端软件/波形分别过了什么。

选看与延期：P1：Buildroot重建最小rootfs。P2：为当前工作设备大规模升级内核。

未过：只保留最小复现，记录卡点并重复本周；后续日期整体顺延，不跨门槛硬赶。[上一周](第23周_MMU与cache_内存属性和屏障.md) · [下一周](第25周_RV64指令与ABI_第二种架构比较.md) · [全部周目录](../03_逐周目录.md)
