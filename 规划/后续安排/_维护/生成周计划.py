"""只重建本目录的生成文档；不删除文件、不访问网络、不改生产工程。

手工修改周计划前先修改这里的对应行；2027官方调休公布后更新BREAKS再运行。
"""
from datetime import date, timedelta
from pathlib import Path
import json
import sys

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[1]
START = date(2026, 10, 19)
# 个人保守休息窗口，并非国务院正式调休安排。
BREAKS = [
    ('2026-12-28', '2027-01-03', '元旦预留'),
    ('2027-01-25', '2027-02-21', '春节返乡与休息预留'),
    ('2027-03-29', '2027-04-11', '清明及调休周边预留'),
    ('2027-04-26', '2027-05-09', '劳动节及调休周边预留'),
    ('2027-06-07', '2027-06-13', '端午预留'),
    ('2027-09-13', '2027-09-19', '中秋预留'),
    ('2027-09-27', '2027-10-10', '国庆及调休周边预留'),
]

CVID = '[C01 NPTEL官方课程](https://nptel.ac.in/courses/106105171)'
CS50 = '[C02 CS50 Week4视频/字幕/讲稿](https://cs50.harvard.edu/x/2025/weeks/4/)'
N1570 = '[WG14 N1570草案](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf)'
GDB = '[GDB官方手册](https://sourceware.org/gdb/current/onlinedocs/gdb.html/)'
GCC = '[GCC Sanitizer](https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html)'
BEEJ = '[Beej作者C教材](https://beej.us/guide/bgc/html/split/)'
CSAPP = '[S01 CMU15-213官方目录/课件](https://www.cs.cmu.edu/afs/cs/academic/class/15213-f15/www/schedule.html)'
JYY = '[O01 蒋炎岩OS2024视频/讲义](https://jyywiki.cn/OS/2024/)'
MIT = '[O02 MIT6.S081 2021日程/2020录像](https://pdos.csail.mit.edu/6.S081/2021/schedule.html)'
FIREVIDEO = '[野火官方驱动视频](https://www.bilibili.com/video/BV1pf4y1974n/)'
FIRE = '[野火官方驱动教材分册目录](https://doc.embedfire.com/linux/imx6/driver/zh/latest/index.html)'
NXP = '[NXP i.MX6ULL官方手册/勘误入口](https://www.nxp.com/products/i.MX6ULL?tab=Documentation_Tab)'
BOOT = '[D01 Bootlin大纲及教材](https://bootlin.com/training/kernel/)'
DT = '[D02 Bootlin Device Tree101视频与课件](https://bootlin.com/blog/device-tree-101-webinar-slides-and-videos/)'
ARM = '[Arm A-profile官方架构指南](https://www.arm.com/architecture/learn-the-architecture/a-profile)'
ARMVIDEO = '[Arm官方Training入口](https://developer.arm.com/dev2/Training/Arm%20On-demand%20Training)'
RV = '[RISC-V官方规范固定版](https://docs.riscv.org/reference/isa/v20260120/unpriv/unpriv-index.html)'
RVP = '[RISC-V官方特权规范固定版](https://docs.riscv.org/reference/isa/v20260120/priv/priv-index.html)'
QA = '[QEMU Arm virt](https://www.qemu.org/docs/master/system/arm/virt.html)'
QR = '[QEMU RISC-V virt](https://www.qemu.org/docs/master/system/riscv/virt.html)'
QG = '[QEMU GDB](https://www.qemu.org/docs/master/system/gdb.html)'
EDU = '[QEMU EDU官方设备规格](https://www.qemu.org/docs/master/specs/edu.html)'
PCI = '[Linux PCI驱动官方指南](https://docs.kernel.org/PCI/pci.html)'
DMA = '[Linux DMA API](https://docs.kernel.org/core-api/dma-api-howto.html)'
MSI = '[Linux MSI指南](https://docs.kernel.org/PCI/msi-howto.html)'
IO = '[Linux MMIO访问](https://docs.kernel.org/driver-api/device-io.html)'

# 字段：题目，工作问题，必须掌握，视频/章节，文字/源码，三步实作，故障注入，验收，选看。
WEEKS = [
('C起步_编译类型与内存',
 '板端同一个值为什么在日志、内存和上位机里看起来不同？先建立可信的C实验环境。',
 'P0：预处理/编译/汇编/链接；变量、基本语句、函数原型；sizeof/CHAR_BIT；栈/静态存储与对象生命周期。',
 f'{CVID} L5、L6、L8、L10；已会控制流可快速测后跳过。中文补看{JYY}第8讲调试理论与实践，选一段即可。',
 f'{N1570} 5.1.1、6.2.4～6.2.6；{GDB}数据与内存检查；{BEEJ}第2～4章只补卡点。',
 '建立独立host实验目录，记录gcc/gdb版本，用-E/-S/-c保存中间产物；写type_report输出类型宽度、地址和十六进制，预测再运行；用GDB断点观察局部变量，生成一张对象/值/地址对照表。',
 '故意漏声明函数或printf格式错配，在编译阶段识别；再加入一个循环边界错误，用断点观察第一次偏离预期的位置。',
 '从空白编译一个含函数和数组的程序，解释四个构建阶段；宽度表有主机结果，ARM列先标待测，不猜；能定位而非仅删除警告。',
 'P2：编辑器美化、复杂CMake、C语言历史；不占核心实作时间。'),
('字符字节_整数与位操作',
 '把传感器原始字节变成带符号读数，同时识别文本、终止符与状态位。',
 'P0：char/unsigned char、NUL/EOF、ASCII/UTF-8字节；整数提升、截断、符号扩展、端序、移位/掩码。',
 f'{CVID} L11～13、L32～33；{CSAPP}09-03/09-08，CSAPP3e 2.1～2.3。两套选主讲，不重复全看。',
 f'{N1570}6.3.1.1、6.3.1.3、6.5.7、6.5.10～12、7.20；{BEEJ}第7、14～15章和24.1～24.2。',
 '定义合成帧字段与单位，给00/7F/80/FF写逐位预期；实现显式长度的hexdump和16位正负值解码，不用strlen处理二进制；写模拟RW/W1C寄存器，比较普通读改写与写1清位，保留位不能乱改。',
 '注入无终止符、中文多字节截断、负char参与拼接、移位量等于位宽；区分应拒绝输入和程序本身UB。',
 '随机给8个字节，能逐字节解释偏移/值/字段/端序和符号；掩码仅修改目标位；边界向量含最小/最大值和缺失数据，无效不伪装0°。',
 'P1：浮点误差简看CSAPP2.4；P2：复杂CRC推导，先明确协议参数。'),
('一级指针_对象与访问范围',
 'SDK交给你一个buffer指针时，地址、内容和可访问长度分别是什么？',
 'P0：&/*、T*、const、指针步长、数组末尾后一位、对象范围；指针不是数据所有权。',
 f'{CVID}L58～59（按主题提前看）；或{CS50}Pointers/Strings/Pointer Arithmetic，Shorts2。',
 f'{N1570}6.3.2.3、6.5.3.2、6.5.6；{BEEJ}第5章、第11章；{GDB}Memory。',
 '画buf/p/&p/*p对象图，在unsigned char和uint16_t数组上预测p+1；实现带len/cap的只读span遍历，列出允许的索引区间；GDB用x/16bx和x/8hx对照同一对象，解释显示单位与实际类型。',
 '独立错误样例里传NULL、末尾后一位解引用、返回局部变量地址；用ASan/UBSan和GDB分别取证，错误代码不混入正确库。',
 '不用背地址数值，能解释步长、范围和const约束；能从崩溃指令找到哪块对象被越界，给出正确接口长度。',
 'P2：任意整数转地址玩技巧；MMIO留到有资源映射依据再做。'),
('二级指针_数组与输出参数',
 '函数为什么能返回新buffer给调用者？二维数组、指针数组和T**到底怎样布局？',
 'P0：按值传参；T**；T(*)[N]与T*[N]；数组退化；输出参数失败契约与char**argv。',
 f'{CVID}L26～30、L34、L39～40、L47选缺口；{MIT}LEC2 C and gdb作指针补课。目录未明确二级指针专讲，不能把L59当覆盖证明。',
 f'{N1570}6.7.6.1～2、6.3.2.1、6.5.2.1；{BEEJ}6.6、18.1.2、23.1；{CS50}Swapping小节。',
 '用栈上固定存储实现选择输出对象的T**接口，先排除malloc干扰；写三种二维布局并打印每级指针及字段地址，禁止强转掩盖类型错配；写有长度的指针游标解析函数，成功才推进游标，失败保持原状态。',
 '故意把二维连续数组当T**传入，先看编译诊断与内存图；另测输出参数为NULL、剩余长度0/1和失败后游标错误推进。',
 '闭卷画三种布局并解释一行声明；能修改调用者指针，能解释只改局部T*为何无效；失败接口行为有测试。',
 'P2：复杂声明谜题；只保留驱动回调/数组真实会用的声明。'),
('结构体联合体_位域与布局',
 '上位机和32位板端直接发送同一个struct，为什么可能字段错位？',
 'P0：struct/union/enum/typedef、嵌套结构、padding、offsetof、_Alignof、位域实现限制、wire format。',
 f'{CVID}L55～57、L60；{CSAPP}09-24，CSAPP3e3.8～3.9；{CS50}Shorts3 Custom Types作备选。',
 f'{N1570}6.7.2.1、6.2.6.1、7.19；{BEEJ}第8章、20.5/20.6/20.8/20.9；[Arm AAPCS32](https://github.com/ARM-software/abi-aa/blob/main/aapcs32/aapcs32.rst)5.3.4/8.1.6/8.1.7。',
 '设计含uint8_t/uint32_t/指针的诊断记录，预测再量字段偏移和总大小；做tagged union表示不同事件，并检查tag再访问payload；将同一标志位写成位域版和显式掩码版，导出字节比较，再实现独立序列化格式。',
 '注入错误tag、裸struct网络传输和memcmp比较含padding对象；展示为何偶尔相等/能跑不能作为可移植保证。',
 '解释union共享存储与struct分别存储；每个线上字段有偏移、宽度和端序；位域不作为跨编译器协议保证；主机与ARM布局差异后续实测。',
 'P1：flexible array member，至少解释sizeof不含尾部数据；P2：C++类继承布局。'),
('动态内存_生命周期与所有权',
 '异步采集回调晚到，谁负责释放buffer？多个失败出口怎样避免泄漏和重复free？',
 'P0：malloc/calloc/realloc/free、乘法溢出、owner/borrowed、浅拷贝、单一清理路径、错误码。',
 f'{CVID}L61；或{CS50}Copying/malloc/Overflow及Shorts4 Dynamic Memory。',
 f'{N1570}7.22.3、7.24；{GCC}ASan/UBSan；{BEEJ}第12章。',
 '把W04接口改成分配输出，写清out参数失败值与释放责任；为记录对象加入create/destroy，逐个分配点可控失败，realloc用临时指针；实现单线程单槽handoff，成功转移后原调用者不能再释放，队列算法留W09。',
 '注入第1/第2次分配失败、重复释放、释放后回调、长度乘法溢出；给每个案例保留最小复现与修复前后日志。',
 '失败路径和成功路径都无已知泄漏/UAF；能口述每个对象在哪个事件转移所有权；工具未报告不等于所有路径已证明安全。',
 'P2：自写malloc/内存池优化；先不取代系统allocator。'),
('对齐别名_半字与SIGBUS调试',
 '协议偏移1读32位，在PC成功但换平台出错，该怎样判断语言错误、CPU异常和Linux信号？',
 'P0：对齐、访问宽度、effective type/aliasing、memcpy、packed边界；SIGBUS/SIGSEGV与CPU fault区别。',
 f'{CSAPP}09-24/09-29，CSAPP3e3.8～3.10；{JYY}第8讲；没有“ARM未对齐必崩”的背诵结论。',
 f'{N1570}6.2.8、6.3.2.3、6.5；[Linux非对齐访问](https://docs.kernel.org/core-api/unaligned-memory-access.html)；[mmap](https://man7.org/linux/man-pages/man2/mmap.2.html)；{GDB}。',
 '对同一合成payload写危险强转版与字节拼接/memcpy版，错误版单独运行；用UBSan alignment和反汇编定位byte/halfword/word读取；在独立临时文件实验中mmap后截短文件，访问越界页，收集SIGBUS现场并标明它是映射错误实验。',
 '给出未对齐指针、越界长度与截短文件三种故障，用GDB的$_siginfo记录实际信号、si_code/PC/地址，不提前编写信号handler；不要求任意架构必产生SIGBUS。',
 '能解释对象对齐与硬件支持是两回事；有bt、寄存器、故障指令和对象范围；正确解码路径跨偏移0～7都符合预期。',
 'P1：ARMv7同案例实测；若板端工具缺失，保留待测，不能用主机结果填上。'),
('链接ABI_调用栈与反汇编',
 '程序能编译却链接失败，或函数返回后坏栈，怎样从ELF和指令找到原因？',
 'P0：.h/.c、static/extern、符号、section、重定位；参数/返回值/栈帧；调试优化对照。',
 f'{CVID}L41；{CSAPP}09-22过程调用3.7、10-13链接第7章；中文可检索“小彭 现代CMake target_link_libraries”，非必修。',
 f'{N1570}6.2.2、6.7.6.3、6.10；{GDB}Registers/Backtrace；[Arm ABI官方仓库](https://github.com/ARM-software/abi-aa)。',
 '把解码器拆核心库和CLI，制造并修复重复定义/未定义符号；用readelf/nm/objdump跟踪一个函数从符号到调用指令；同一函数用主机与ARMv7工具链编译，画参数/局部变量/返回地址位置，固定优化等级。',
 '注入跨文件原型不一致和错误函数指针签名，先解释为何强转压警告危险；保留优化构建与调试构建的差异。',
 '能独立修复一个链接问题并解释符号来自哪；不是照背x86寄存器到ARM；能依据ABI解释一次调用和返回。',
 'P2：复杂链接脚本/动态加载器；裸机链接脚本在W22补。'),
('环形缓冲_回调与状态机',
 '字节到得快、处理得慢，如何既不越界也不无限占内存？',
 'P0：固定容量ring、head/tail、满空约定、函数指针、void*上下文、回调寿命、状态机；先单线程。',
 f'{CVID}L35～40函数参数补缺；[CS50 Week5](https://cs50.harvard.edu/x/2025/weeks/5/)数据结构，链表只借对象关联思路。',
 f'{N1570}6.7.6.3、6.5.6；{BEEJ}23.7函数指针；先读W06所有权记录再写接口。',
 '实现容量8的ring并画每一步head/tail，明确丢弃/拒绝策略；给解析器加状态与回调context，显式传长度和状态；将模拟按键/采样/超时事件重放进状态机，输出转移原因与事件序号。',
 '连续绕环3轮、空读、满写、回调重入、错误长度、CRC错和部分帧；并发先不加，避免把算法错误与线程错误混为一谈。',
 '所有边界都有预期向量；解释为什么数组/队列适合当前任务；回调触发时对象仍有效；无静默覆盖关键事件。',
 'P1：链表插入删除一次；P2：无锁ring，先不实现。'),
('C阶段实战_陌生故障与验收',
 '离开AI答案，能否接管一个真实风格的C核心模块并独立定位坏数据？',
 'P0：前九周知识组合；接口契约、失败语义、诊断记录；不增加新语言主题。',
 f'不新增大课。按卡点回看{CVID}L58～61或{CS50}Week4；{JYY}第8讲只复盘方法。',
 f'{N1570}按问题查条款；{GDB}和{GCC}；本计划06清单逐项核验。',
 '从空白完成小型字节记录解析器，含分配输出、tagged事件和长度校验；让他人或AI只提供三种未知坏输入/故障位置，不先看修复；自己保存复现、最小化、断点、根因与修复，再把同一核心交叉编译到ARMv7执行。',
 '未知故障至少覆盖长度/生命周期/符号或布局三类；未拿到合适板端工具时明确ARM执行待验，不以“编译成功”代替。',
 '闭卷30～60行核心+逐行解释；3个未知故障各有证据链；正常与失败向量回归；C阶段总结五项关键维度全部过关才进入驱动实作。',
 'P2：刷语言冷门题；不以背题和代码行数打分。'),
('GPIO与引脚复用_从程序到电平',
 '按键/背光enable不响应时，怎样区分应用、GPIO、pinmux、供电和接线？',
 'P0：原理图网络、IOMUXC/pad、输入输出、上下拉、电平、clock；Linux GPIO用户接口与驱动边界。',
 f'{FIREVIDEO}检索“pinctrl gpio led”；文档定位框架第1章《pinctrl子系统和gpio子系统-led实验》，视频P号未核。',
 f'{FIRE}框架第1章；{NXP}IOMUXC/CCM/GPIO；[Linux GPIO用户API](https://docs.kernel.org/userspace-api/gpio/index.html)。',
 '确认板型号/引脚/电平/共地并绘一条完整路径，不占用系统关键脚；先查uname-r/CONFIG_GPIO_CDEV/libgpiod版本，再用匹配工具控制实验脚，旧4.19对照v1接口，不为课程升级内核；沿设备树和驱动查到寄存器职责，测输入/输出波形与软件状态分别存证。',
 '在独立实验配置中模拟line被占用/方向不符/权限问题；不对在线生产板随意改pinmux；硬件断线只在安全实验连接做。',
 '能解释应用调用到引脚的各层；有引脚依据和真实电平证据；若只有API返回则硬件项标未过；能按最小配置恢复。',
 'P2：遍历整片GPIO所有位；只精读本次通路，其他列索引。'),
('PWM与时钟_背光输出闭环',
 '亮度设置保存了但屏幕未变，软件占空比、实际波形和光学效果分别怎样验证？',
 'P0：时钟源/分频/周期/占空比/极性/enable；纳秒与频率；0%/100%边界；安全默认输出。',
 f'{FIREVIDEO}检索“PWM子系统 pwm波形”；文档框架第6章《PWM子系统–pwm波形输出实验》。',
 f'{FIRE}框架第6章；{NXP}RM Chapter38 PWM及CCM；[Linux PWM框架](https://docs.kernel.org/driver-api/pwm.html)。',
 '从手册画clock→divider→counter→pad→负载路径，计算目标参数；写独立CLI设定周期/占空比/极性，非法duty>period拒绝；测0/25/50/100%和disable，记录示波器周期及实际背光观察。',
 '注入错误单位、反极性、禁用状态和应用写入失败；区分寄存器读回、PWM脚波形、负载发光三个结果。',
 '预测与实测误差有合理说明；失败可定位层次；退出/恢复状态明确，不自动改工作设备原有保存设置。',
 'P1：时钟树测量；P2：电源模拟电路设计不作为本周主项。'),
('驱动模型与设备树_资源从哪里来',
 '硬件地址、中断和时钟怎样从DT进入probe，再成为用户可以调用的设备？',
 'P0：module、platform_device/driver、compatible、资源、probe/remove、错误回滚；用户态和内核态分工。',
 f'{DT}设备描述/驱动匹配主题；{FIREVIDEO}检索“设备模型 平台设备驱动 Linux设备树”。',
 f'{FIRE}基础第6～8章；{BOOT}Half day2/3；[Devicetree官方规范](https://www.devicetree.org/specifications/)。',
 '先制作可回退的实验镜像/DTB与模块构建环境并记录kernel版本；写不驱动生产外设的最小platform模块和匹配节点，打印资源来源；逐项申请资源并用统一失败路径释放，完成load/unload与compatible不匹配对照。',
 '错compatible、缺资源、probe中途失败；只改实验DT配置，验证旧配置可重新启动。',
 '画DT→设备→匹配→probe→用户接口的链；能解释reg/ranges/interrupts/clock/pinctrl谁解析；模块构建匹配运行内核。',
 'P2：写新设备树编译器；旧4.19教程API必须与本机版本对照。'),
('I2C传感器_原始数据与有效性',
 '从采集芯片到带符号角度/加速度数据，每个字节何时有效、读失败如何上报？',
 'P0：7位地址与寄存器地址、START/repeated START、ACK/NACK、批量读、量程/符号/比例、时间戳。',
 f'{FIREVIDEO}检索“I2C mpu6050”；文档框架第2章《I2C子系统–mpu6050驱动实验》；{BOOT}Half day3。',
 f'{FIRE}框架第2章；[Linux I2C功能](https://docs.kernel.org/i2c/functionality.html)、[I2C协议](https://docs.kernel.org/i2c/i2c-protocol.html)；器件datasheet按实际型号另存链接。',
 '先核实际器件型号/电平，列ID与数据寄存器表；实现独立驱动或已支持接口的最小读取，按手册一次读取完整样本并解析；逻辑分析仪对照地址/ACK/数据字节，与C解码结果逐项对齐，输出raw/value/unit/valid/reason。',
 '模拟NACK、超时、少字节和无效ID；不能在驱动仍占用时并行i2c裸写抢设备；错误不返回假0读数。',
 '每个数据位有来源，符号与单位明确；正常和失败均有记录；没传感器则模拟部分可完成，真实波形和器件状态保留未验。',
 'P1：以后接IIO；P2：姿态融合/医学角度算法不是本周目标。'),
('SPI与缓冲_数据怎样到引脚',
 'SPI时钟有了但数据错，怎样从模式、CS边界和内存布局查起？',
 'P0：CPOL/CPHA、位序、字长、CS、全双工、message/transfer、长度/stride。',
 f'{FIREVIDEO}检索“SPI子系统 OLED”；文档框架第3章《SPI子系统–OLED屏实验》；{BOOT}总线框架主题补充。',
 f'{FIRE}框架第3章；[Linux SPI概览](https://docs.kernel.org/spi/spi-summary.html)；实际器件datasheet的时序和命令表。',
 '画命令/地址/数据在一个CS周期内的位置，选已核电平的器件或安全回环；实现明确长度的transfer，发00/55/AA/FF与递增序列；同时保存内存dump和线上的bit顺序，比较批量/分次传输的CS差别。',
 '错CPHA、错位序、CS过早释放和长度差1；通过抓时序解释结果，不能仅改配置到“碰巧显示”。',
 '能从波形找出一个字节的8个采样边沿；传输失败有超时/错误；解释buffer生命周期，不把显示成功算成SPI全部掌握。',
 'P1：批量传输优化；P2：完整图形GUI不做。'),
('UART16550冲刺_寄存器与错误恢复',
 '用一周限定冲刺，把UART从收发函数推进到初始化、FIFO、状态、错误和恢复。先用主机寄存器模型隔离ISA/启动难度，真实QEMU MMIO迁移留W25～26。',
 'P0：确认16550模型而非16050；访问宽度/步长、DLAB、波特率分频、LSR、FIFO、轮询超时；i.MX UART另有寄存器。',
 f'{MIT}LEC9 Interrupts的UART路径；{FIREVIDEO}检索“裸机 UART串口通讯”，对应裸机第12章，比较不同IP。',
 f'[TI TL16C550D官方手册](https://www.ti.com/lit/ds/symlink/tl16c550d.pdf)的DETAILED DESCRIPTION与寄存器定义；[QEMU serial.c官方实现](https://github.com/qemu/qemu/blob/master/hw/char/serial.c)核模型差异，不能把TI自动流控特性直接套QEMU；MIT的kernel/uart.c作阅读参照；{FIRE}裸机第12章。',
 '复用W02寄存器模拟器，按TI手册扩展DLAB别名/LSR/FIFO最小模型，先明确每个状态位和读写副作用；通过reg_read/reg_write接口写init/收发/timeout，测试输入和模拟时钟可控，不直接解引用假物理地址；接入已有ring并统计溢出/错误，重复初始化和恢复，输出与i.MX原生UART差异表。',
 '模拟TX不就绪、RX突发超过容量、parity状态和重复init；主机模型只证明程序对指定状态的处理，真实波形/硬件错误未验。',
 '本周交付限定寄存器模型及驱动逻辑，有超时、统计和每位解释，不能称真实16550驱动已验收；W25～26再迁移QEMU验证MMIO/IRQ，不把启动代码学习偷偷塞入本周。',
 'P1：真板原生UART波形；P2：RS485自动方向/TTY全栈留后续。'),
('中断与延后工作_不丢事件',
 '设备事件怎样从引脚/状态寄存器变成可等待的用户态事件，何时必须确认中断？',
 'P0：IRQ来源/屏蔽/确认、ISR、threaded IRQ/延后工作、wait queue、超时、去抖；共享中断判源。',
 f'{FIREVIDEO}检索“中断子系统 按键中断”；{MIT}LEC9；{BOOT}Half day6。',
 f'{FIRE}框架第4章；[Linux generic IRQ](https://docs.kernel.org/core-api/genericirq.html)；{BOOT}进程/睡眠/中断教材。',
 '只在现有Linux实验板的独立按键驱动上画IRQ来源/控制器/确认路径，不并行新做RISC-V IRQ；IRQ只取必要状态，把去抖和处理交给允许的上下文，复用W13模块框架；用户端阻塞等待事件并支持超时/停止，保存事件序号与IRQ计数。',
 '注入重复事件、无状态中断、处理变慢和停止竞态；不在不允许睡眠的上下文调用睡眠函数；QEMU和Linux实验分别保存上下文图。',
 '能画设备→IRQ controller→handler→queue→用户的完整路径；无源时不误认共享IRQ；关闭后不再访问释放对象；相同突发输入可解释丢弃策略。',
 'P1：中断延迟统计；P2：GIC全部寄存器，待W22专题。'),
('进程信号IPC_停止与恢复',
 '拍摄与上传分开后，信号、退出和回收如何协调，为什么收到SIGTERM不等于已经清理完？',
 'P0：fork/exec/wait、fd继承、pipe/Unix socket、sigaction、EINTR、信号屏蔽、async-signal-safe。',
 f'{JYY}第14讲进程、第15讲地址空间；{CSAPP}10-15/10-20，CSAPP3e第8章；优先选中文主讲。',
 '[Linux signal(7)](https://man7.org/linux/man-pages/man7/signal.7.html)、[signal-safety(7)](https://man7.org/linux/man-pages/man7/signal-safety.7.html)、[wait(2)](https://man7.org/linux/man-pages/man2/wait.2.html)。',
 '将实验台分采集/处理两个进程，明确各自拥有的fd；用pipe通知事件/退出，信号handler只做允许的最小动作；父进程停止接任务、通知子进程、回收并记录退出原因，使用合成任务复现。',
 '子进程异常退出、系统调用被打断、重复SIGTERM、继承fd未关导致EOF不来；不在handler里随便printf/malloc或拿锁。',
 '能解释signal与硬件IRQ区别；没有僵尸进程/关闭卡死的已知路径；给出fd生命周期与重启边界；不以kill -9作为正常退出方案。',
 'P1：signalfd只在Linux专用接口需求时补；P2：完整服务管理框架。'),
('线程同步背压_系统内如何协调',
 '采集不能被语音或上传阻塞，队列满、取消和停止同时发生时怎样保持一致？',
 'P0：mutex/cond、谓词循环、有界队列、锁顺序、背压、超时、取消与join；volatile不解决数据竞争。',
 f'{JYY}第5讲、第9讲同步、第12讲并发Bugs，按队列故障选段；不追求本周全看。',
 '[Linux pthreads(7)](https://man7.org/linux/man-pages/man7/pthreads.7.html)；N1570 5.1.2.4/7.17；[Linux volatile文档](https://docs.kernel.org/process/volatile-considered-harmful.html)。',
 '把ring封装为有界线程队列，写等待谓词与容量策略；用采集/处理/记录三个角色模拟当前工作，记录任务ID和单调时钟；实现停止接收、排空或取消、唤醒所有等待者、join、最后释放的顺序。',
 '慢消费者、队列满时停止、空队列停止、两把锁反序、重复完成；另构建TSan，不能用ASan+TSan一起跑。',
 '至少100轮自动开始/停止无已知死锁，记录机器与负载，不称长期稳定；能解释每把锁保护什么；故意故障能定位并回归。',
 'P2：lock-free/RCU实现，先用锁写对。'),
('六个月核心验收_设备诊断作品',
 '把基础落成自己可接管的作品，而不是再添一串课程名。',
 'P0：C正确性、设备路径、故障分层、系统退出、版本复现；首次完整作品与岗位能力对照。',
 f'不增加新课。回查{JYY}第26～27讲输入输出/驱动、{FIREVIDEO}相关专题；按失败项点看。',
 '本计划04阶段门槛、05项目任务和06必查清单；锁定所用内核/工具版本的官方资料，不用master结果冒充旧BSP。',
 '整合字节解析、GPIO/PWM或一个可用外设、事件队列与CLI，功能范围先冻结；自选一个过去靠AI的模块，独立解释并修改边界，记录本人贡献；在干净目录复现构建与实验，形成第一版README/故障报告/版本和回退说明。',
 '盲测3个未知故障，至少各来自C内存、外设路径、并发退出；没有硬件波形的项明确未验，不能用模拟补写。',
 '五项关键维度全部通过，能演示真实工作问题如何被底层证据定位；发布前审查授权/脱敏，仅本地准备，不自动上传GitHub。',
 'P1：此时可开始搜BSP/平台软件/诊断岗位要求做差距复核；工资与录用不作承诺。'),
]

from 深化周 import WEEKS as ADVANCED_WEEKS
WEEKS += ADVANCED_WEEKS

def overlaps(start, end):
    return [(a, b, why) for a, b, why in BREAKS
            if start <= date.fromisoformat(b) and end >= date.fromisoformat(a)]

def generate():
    assert len(WEEKS) == 40, '应有40个学习周，不能生成半套日历'
    assert START.weekday() == 0
    weekly = ROOT / '逐周'
    weekly.mkdir(exist_ok=True)
    current = START
    rows, calendar, manifest = [], [], []
    for number, row in enumerate(WEEKS, 1):
        title, why, core, video, docs, lab, fault, accept, extra = row
        while overlaps(current, current + timedelta(days=6)):
            calendar.append((current, current + timedelta(days=6), '休息', overlaps(current, current + timedelta(days=6))[0][2]))
            current += timedelta(days=7)
        end = current + timedelta(days=6)
        assert not overlaps(current, end)
        filename = f'第{number:02d}周_{title}.md'
        steps = lab.split('；')
        assert len(steps) == 3, (number, steps)
        phase = '核心段' if number <= 20 else '后续深化段'
        prev = f'[上一周](第{number-1:02d}周_{WEEKS[number-2][0]}.md)' if number > 1 else '[总路线](../01_总路线与能力优先级.md)'
        nxt = f'[下一周](第{number+1:02d}周_{WEEKS[number][0]}.md)' if number < 40 else '[阶段总结](../04_阶段总结与晋级门槛.md)'
        text = f'''# 第{number:02d}学习周：{title.replace('_', '：')}

参考日期：{current}～{end}（北京时间）。{phase}。实际执行前核对[假期日历](../02_日历与中国假期.md)；正式调休或公司加班与本周冲突时整周顺延，不在假期补课。状态：未开始。

## 工作问题与门槛

{why}

先修：{'完成W01前环境准备并确认独立实验目录；无需先刷课。' if number == 1 else '上一学习周的必过项有源码、输入与调试证据；失败项未解决先重复上一周。'} 本周重要性：{core}

## 精确选课与官方阅读

视频主看/补看：{video}

文字与源码：{docs}

视频建议合计1～2小时，必要补看到3小时须挤掉选做，不挤编码。课程章节与手册章节分开，跨年MIT课程不要混编号。资料核验与播放/字幕限制见[课程表](../资料/01_C与系统课程章节核查.md)和[硬件架构表](../资料/02_外设架构QEMU与PCIe核查.md)。

## 每天做什么：正常周15小时

| 时间 | 具体动作与产物 |
|---|---|
| 周一 2h | 先写本周问题的预期图/表，再看指定视频、查手册。标出数据来源、控制/通知来源、对象或资源的归属。不能只抄笔记。 |
| 周二 2h | {steps[0]} |
| 周三 2h | {steps[1]} |
| 周四 2h | {steps[2]} |
| 周五 2h | 开始故障注入：{fault} |
| 周六 5h | 2h定位/修复，2h正常与失败回归，1h闭卷解释和填写周报。没做完顺延，选做首先删减。 |
| 周日 | 休息，无看课和补债要求。 |

## 本周必过项

{accept}

验收同时检查：功能正确、机制解释、独立实现、故障定位、他人可复现。可查手册，不能现场复制生成答案。至少一个30～60行或等价小任务由本人从空白完成，解释每个长度、指针、状态位和失败分支。

## 要留下的文件

在实验仓库的`evidence/W{number:02d}/`保存：输入与预期、源码版本/构建命令、实际结果、一次故障的现场/根因/修复前后、三张图（数据/通知/资源），以及`周报.md`。临时故障样例独立存放，不污染工作产品。周报写清哪些由本人完成、哪些来自AI，以及模拟/板端软件/波形分别过了什么。

选看与延期：{extra}

未过：只保留最小复现，记录卡点并重复本周；后续日期整体顺延，不跨门槛硬赶。{prev} · {nxt} · [全部周目录](../03_逐周目录.md)
'''
        (weekly / filename).write_text(text, encoding='utf-8')
        rows.append(f'| W{number:02d} | {current}～{end} | [{title.replace("_", "：")}](逐周/{filename}) | {phase} |')
        calendar.append((current, end, f'W{number:02d}', title.replace('_', '：')))
        manifest.append({'week': number, 'start': str(current), 'end': str(end), 'file': '逐周/' + filename})
        current += timedelta(days=7)
    (ROOT / '03_逐周目录.md').write_text('# 逐周目录\n\n学习周编号不等于自然周；休息窗口已跳过。起始日是默认执行假设，不是硬截止日期。\n\n| 学习周 | 参考日期 | 打开任务 | 范围 |\n|---|---|---|---|\n' + '\n'.join(rows) + '\n', encoding='utf-8')
    holiday_intro = '''# 日历与中国假期

编排时区：Asia/Shanghai。默认从2026-10-19开始，W01～W20为约六个月核心段，W21～W40为后续深化段。周数表示学习单元，遇假期冻结编号。

## 官方事实与本计划假设

截至本轮2026-10-19检索，未查到国务院办公厅2027年完整调休通知。不能把推算日期写成官方放假安排。[中国政府网政策库](https://sousuo.www.gov.cn/zcwjk/policyDocumentLibrary?q=%E8%8A%82%E5%81%87%E6%97%A5%E5%AE%89%E6%8E%92%E7%9A%84%E9%80%9A%E7%9F%A5&t=zhengcelibrary)用于以后更新；[2026年正式通知](https://www.gov.cn/zhengce/content/202511/content_7047090.htm)仅用于说明已发布年份，不能顺推2027调休。

[香港天文台2027公历农历对照表](https://www.hko.gov.hk/tc/gts/time/calendar/pdf/files/2027.pdf)只用于确认节日历法位置，**不是中国大陆放假/补班表**。

下面是本计划主动预留的完整休息窗口，比法定节日宽，包含返乡和可能调休周边，不宣称它们全是法定假日。春节预留四周。休息期间没有看视频、作业、复习、补债或自动提醒要求。

| 个人休息窗口 | 用途 | 状态 |
|---|---|---|
'''
    holiday_intro += '\n'.join(f'| {a}～{b} | {why} | 个人预留，待官方/公司排班核对 |' for a,b,why in BREAKS)
    holiday_intro += '''

正式通知发布后：把所有官方休息日并入窗口；若补班使原学习周预算不足，也冻结该学习周。新增假期优先休息，后面日期顺延；已经预留的春节休息不因“实际假期少几天”被自动塞课。公司另有年休假/停工/出差同样执行此规则。

正常周周一～周五每天2h、周六5h、周日休息，共15h。忙周不足预算则重复该学习单元，不挤用休息时间。此日历是无返工情况下的参考，不是必须追赶的最后期限。

## 全部自然周

| 起始 | 截止 | 安排 | 主题或休息原因 |
|---|---|---|---|
'''
    holiday_intro += '\n'.join(f'| {a} | {b} | {w} | {why} |' for a,b,w,why in calendar)
    holiday_intro += f'\n\n本版：40学习周、{sum(w == "休息" for _,_,w,_ in calendar)}个完整休息周，参考结束{current-timedelta(days=1)}。日期更新以本文件及逐周文件同时重建为准。\n'
    (ROOT / '02_日历与中国假期.md').write_text(holiday_intro, encoding='utf-8')
    (ROOT / '_维护' / '日程核对.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    assert len(list(weekly.glob('第*周_*.md'))) == 40
    print(json.dumps({'weeks': len(manifest), 'start': manifest[0]['start'], 'core_end': manifest[19]['end'], 'end': manifest[-1]['end'], 'rest_weeks': sum(w == '休息' for _,_,w,_ in calendar)}, ensure_ascii=False))

if __name__ == '__main__':
    generate()
