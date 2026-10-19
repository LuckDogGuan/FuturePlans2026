# F阶段总结：RISC-V迁移

范围W25～28，状态未开始。先修C、系统协作与架构基本阅读。固定MIT课程年份、xv6分支与QEMU版本，不混拷不同年实验。

## 必交证据

工具链/QEMU/GDB从ELF启动并停到关键函数；RV64调用约定与load/store对照；W16 UART逻辑在既有框架中的MMIO/IRQ迁移或等价独立修改；CSR/trap现场；一次页权限/页故障路径；锁与sleep/wakeup时序；一个虚拟设备数据流。

## 晋级检查

解释RV32/RV64与扩展组合、ABI的区别；不能把“都是RISC-V”当外设地址相同。说清machine/supervisor态与OpenSBI/xv6启动路径，trap和Linux signal不混。UART不能同时被自己的测试代码与原console驱动独立控制。

对同一字节序列或并发问题，比较ARM与RISC-V：语义可复用，CSR/异常入口/中断控制器/屏障/寄存器不同。虚拟设备实验不能冒称全部virtio规范已掌握。

## 总结填写

ABI/特权/地址图与命令：待填。本人修改：待填。未知故障和回归：待填。五项门槛：待验。通过后进入DMA/PCI，向量/密码/自定义扩展留选做。
