# G阶段总结：DMA与PCI/PCIe

范围W29～34，状态未开始。先修对象/地址/IRQ/资源与并发。EDU先用x86 guest，再考虑Arm迁移。

## 必交证据

CPU VA/PA/DMA地址与所有权图；mask与映射错误；PCI ID匹配、probe/BAR/MMIO；INTx/MSI路径；EDU DMA数据比对/超时/remove；PCIe BDF/配置空间/capability/root port/ECAM图；RC/EP真板能力核查表。

## 晋级检查

不能把CPU指针写给设备当DMA地址；coherent仍须遵守字段/门铃顺序；停止设备与回调后才能释放。部分probe失败可回滚，在途任务关闭不会留下UAF。EDU默认28位mask和Arm `virt`布局冲突不能靠只改驱动mask掩盖。

EDU支持的INTx/MSI与另一个真正支持MSI-X的模型分别验收。PCI/PCIe配置空间与BAR设备寄存器区分；generic ECAM不等于真SoC PHY初始化。没有RC/EP硬件时，Link、PHY、refclk/PERST#与电气项目全部记未验，不阻塞软件段。

## 总结填写

guest/模型/内核/驱动版本：待填。失败回滚与关闭时序：待填。配置空间计算与实际对照：待填。真实硬件证据或明确缺口：待填。五项软件门槛：待验。进入H前至少把一个DMA设备生命周期做完整，不以拓扑截图替代。
