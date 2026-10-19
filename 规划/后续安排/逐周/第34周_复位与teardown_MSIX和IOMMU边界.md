# 第34学习周：复位与teardown：MSIX和IOMMU边界

参考日期：2027-08-16～2027-08-22（北京时间）。后续深化段。实际执行前核对[假期日历](../02_日历与中国假期.md)；正式调休或公司加班与本周冲突时整周顺延，不在假期补课。状态：未开始。

## 工作问题与门槛

设备reset、卸载或错误恢复时，哪些工作仍可能引用内存？MSI-X和IOMMU能否自动解决所有越界问题？

先修：上一学习周的必过项有源码、输入与调试证据；失败项未解决先重复上一周。 本周重要性：P0：quiesce、停止新请求、IRQ/work同步、DMA结束后回收、资源配对。P1：MSI-X capability、IOVA/IOMMU隔离、reset能力与平台依赖。

## 精确选课与官方阅读

视频主看/补看：[Linux Foundation LFD430官方章节目录](https://training.linuxfoundation.org/training/developing-linux-device-drivers/)PCI/DMA章节只补清理与约束。视频检索“Linux Foundation PCI error recovery MSI-X IOMMU”，未核实精确免费视频，不要求观看VFIO完整课程。

文字与源码：[Linux PCI Error Recovery](https://docs.kernel.org/PCI/pci-error-recovery.html)error_detected/mmio_enabled/slot_reset/resume。[Linux MSI指南](https://docs.kernel.org/PCI/msi-howto.html)MSI-X API与锁。[Linux Workqueue](https://docs.kernel.org/core-api/workqueue.html)cancel_work_sync，[Linux DMA API](https://docs.kernel.org/core-api/dma-api-howto.html)地址映射。[QEMU Arm virt](https://www.qemu.org/docs/master/system/arm/virt.html)iommu/smmuv3选项只做能力边界。

视频建议合计1～2小时，必要补看到3小时须挤掉选做，不挤编码。课程章节与手册章节分开，跨年MIT课程不要混编号。资料核验与播放/字幕限制见[课程表](../资料/01_C与系统课程章节核查.md)和[硬件架构表](../资料/02_外设架构QEMU与PCIe核查.md)。

## 每天做什么：正常周15小时

| 时间 | 具体动作与产物 |
|---|---|
| 周一 2h | 先写本周问题的预期图/表，再看指定视频、查手册。标出数据来源、控制/通知来源、对象或资源的归属。不能只抄笔记。 |
| 周二 2h | 审查W32每条cleanup路径并本人实现幂等停止状态，标出不可等待持锁区与实际同步点 |
| 周三 2h | 在现有virtio-pci设备上只读核对MSI-X capability及向量分配，与EDU支持项作表，不写新多队列驱动 |
| 周四 2h | 检查当前guest是否真有IOMMU及映射证据，画数据地址/复位通知/回收资源三图，未配置则用地址模型测试说明不冒称隔离通过。 |
| 周五 2h | 开始故障注入：注入STOPPING时重复请求、晚到完成与部分probe失败。复位API不支持或reset失败要保留失败语义，不能使用随意sleep作为DMA结束证明。 |
| 周六 5h | 2h定位/修复，2h正常与失败回归，1h闭卷解释和填写周报。没做完顺延，选做首先删减。 |
| 周日 | 休息，无看课和补债要求。 |

## 本周必过项

所有资源有唯一owner与最终释放点，停止后晚到事件不访问已释放对象。MSI-X/IOMMU分别标只读观察、模拟、实际验证状态，不以名词覆盖替代证据。

验收同时检查：功能正确、机制解释、独立实现、故障定位、他人可复现。可查手册，不能现场复制生成答案。至少一个30～60行或等价小任务由本人从空白完成，解释每个长度、指针、状态位和失败分支。

## 要留下的文件

在实验仓库的`evidence/W34/`保存：输入与预期、源码版本/构建命令、实际结果、一次故障的现场/根因/修复前后、三张图（数据/通知/资源），以及`周报.md`。临时故障样例独立存放，不污染工作产品。周报写清哪些由本人完成、哪些来自AI，以及模拟/板端软件/波形分别过了什么。

选看与延期：P2：VFIO透传、SR-IOV、ATS/PASID、真板AER与热插拔恢复。

未过：只保留最小复现，记录卡点并重复本周；后续日期整体顺延，不跨门槛硬赶。[上一周](第33周_PCIe配置_ECAM和RC_EP边界.md) · [下一周](第35周_内核并发_workqueue上下文与锁.md) · [全部周目录](../03_逐周目录.md)
