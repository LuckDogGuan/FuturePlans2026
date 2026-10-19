# 第29学习周：DMA所有权：DMAengine与总线主设备

参考日期：2027-07-12～2027-07-18（北京时间）。后续深化段。实际执行前核对[假期日历](../02_日历与中国假期.md)；正式调休或公司加班与本周冲突时整周顺延，不在假期补课。状态：未开始。

## 工作问题与门槛

DMA传输时谁能碰buffer，什么时候允许释放？SoC DMAengine和PCI设备自带DMA为何不是同一个接口？

先修：上一学习周的必过项有源码、输入与调试证据；失败项未解决先重复上一周。 本周重要性：P0：CPU虚拟/物理/DMA地址、mask、coherent/streaming、map/sync/unmap方向、ownership和completion、DMAengine客户端与controller区别。

## 精确选课与官方阅读

视频主看/补看：[Linux Foundation LFD430官方章节目录](https://training.linuxfoundation.org/training/developing-linux-device-drivers/)精确章节《Direct Memory Access (DMA)》目录中的DMA Masks/DMA Allocations/DMA API。课程可能付费，免费替代检索“Bootlin DMA mapping API DMAengine ownership”；无核实免费视频讲次，不加伪编号。

文字与源码：[Linux DMA API](https://docs.kernel.org/core-api/dma-api-howto.html)CPU and DMA addresses、DMA addressing capabilities、Types of DMA mappings、Using Consistent DMA mappings、Using Streaming DMA mappings。[Linux DMAengine客户端指南](https://docs.kernel.org/driver-api/dmaengine/client.html)DMA usage。旧教程dmaengine_terminate_all等接口以固定内核核查。

视频建议合计1～2小时，必要补看到3小时须挤掉选做，不挤编码。课程章节与手册章节分开，跨年MIT课程不要混编号。资料核验与播放/字幕限制见[课程表](../资料/01_C与系统课程章节核查.md)和[硬件架构表](../资料/02_外设架构QEMU与PCIe核查.md)。

## 每天做什么：正常周15小时

| 时间 | 具体动作与产物 |
|---|---|
| 周一 2h | 先写本周问题的预期图/表，再看指定视频、查手册。标出数据来源、控制/通知来源、对象或资源的归属。不能只抄笔记。 |
| 周二 2h | 为一块合成采样buffer画CPU拥有→设备拥有→完成→CPU回收状态，分别写coherent与streaming映射表 |
| 周三 2h | 本人实现普通内存ownership状态检查器，拒绝在DEVICE状态读写/释放，明确不是硬件DMA |
| 周四 2h | 沿当前BSP一个UART/SPI客户端追request/config/prepare/submit/issue/completion/terminate，拿不到可用channel只做源码证据并画数据/通知/资源三图。 |
| 周五 2h | 开始故障注入：给状态检查器注入重复complete、取消后晚到、方向错误和未完成释放。真实DMA在W32用EDU验证，本周不能把memcpy/软件模拟写成硬件通过。 |
| 周六 5h | 2h定位/修复，2h正常与失败回归，1h闭卷解释和填写周报。没做完顺延，选做首先删减。 |
| 周日 | 休息，无看课和补债要求。 |

## 本周必过项

能口述两种DMA API各在哪层。每个映射都有配对释放与owner，有至少三个失败向量，coherent不被误解为无需顺序约束。

验收同时检查：功能正确、机制解释、独立实现、故障定位、他人可复现。可查手册，不能现场复制生成答案。至少一个30～60行或等价小任务由本人从空白完成，解释每个长度、指针、状态位和失败分支。

## 要留下的文件

在实验仓库的`evidence/W29/`保存：输入与预期、源码版本/构建命令、实际结果、一次故障的现场/根因/修复前后、三张图（数据/通知/资源），以及`周报.md`。临时故障样例独立存放，不污染工作产品。周报写清哪些由本人完成、哪些来自AI，以及模拟/板端软件/波形分别过了什么。

选看与延期：P1：真板已有驱动的DMA统计。P2：从零实现SDMA控制器与cache维护汇编。

未过：只保留最小复现，记录卡点并重复本周；后续日期整体顺延，不跨门槛硬赶。[上一周](第28周_Virtio设备模型_虚拟数据路径阅读.md) · [下一周](第30周_PCI入门_x86EDU的probe与BAR.md) · [全部周目录](../03_逐周目录.md)
