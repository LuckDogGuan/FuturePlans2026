# AMD、Intel、NVIDIA：中国半导体软件岗位核查

> 历史职责样本：核查时间2026-10-05。下文“当前/可申请/报价”只指当时快照，本轮未重新核在招状态。仅用于对照芯片岗位能力，执行日程以规划/后续安排为准。

核查日期：2026-10-05。这里记录具体招聘证据与个人差距，不是已选定路线，也不是录用或收入预测。

## 先看结论

这三家公司确实需要 Linux/C/C++ 底层软件人员，但“公司属于半导体”不意味着每个软件职位都符合你的方向。按你的要求，优先研究**Linux 内核/驱动与平台软件、嵌入式固件、GPU 开发/诊断工具、用户态设备运行时**；Qt 界面经验作为加分。AI 应用、模型研发、普通后台、视频处理不作为主线。

当前约 4 年仪器应用经验不能直接计作招聘要求中的 3～5 年驱动、固件或芯片诊断经验。即将取得的**产品设计自考本科**也不能直接等同 CS/EE/CE 相关本科。写了 equivalent experience 的岗位存在核实跨专业路径的空间，但仍要由招聘方确认自考、专业及实践经验的接受口径。

**本文件全部中国职位都没有核到明确的中国薪资及日常工时，因此均未标为“已证明税前 ≥15K”。** 美元薪资、宣传性“competitive salaries”、网页薪资占位值 0 均不作为中国薪资证据。可以作为长期目标岗位，投递前另查具体招聘报价、底薪、保证薪数和团队工时。

## 1. NVIDIA：具体岗位与条件

前四个岗位通过雇主官网详情接口核到 posted=true、canApply=true。可申请只表示页面状态，不表示符合条件。

| 精确职位与官方链接 | ID / 地点 / 发布日期 | 主要职责和硬条件 | 学历与专业边界 | 对你的判断 |
|---|---|---|---|---|
| [System Software Engineer, GPU Development Tools](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/China-Shanghai/System-Software-Engineer--GPU-Development-Tools_JR2016503-1) | JR2016503；上海；2026-04-24 | 芯片高层模型、测试 API、trace 工作流、执行/调试工具；2+年；强 C/C++；流利书面及口语英语。系统调试、driver、GPU API、仿真为加分 | 明文 CS/CE 或相关专业本科以上；该条未写 equivalent experience | **有价值的专项准备参照**。年限文字较低，但强 C/C++、系统工具、英语尚须实际证明；产品设计专业需要先询问 HR。模型指芯片模型，不是大模型应用；界面不是工作主项 |
| [Senior System Software Engineer, CPU](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/China-Shenzhen/Senior-System-Software-Engineer--CPU_JR2025929) | JR2025929；深圳，另上海；2026-09-20 | Tegra/Vera CPU 诊断软件栈、device driver、故障定位和修复；EE/CS BS/MS；5+年相关行业经验；强 C/C++、SoC 架构与软硬件调试；Linux kernel/ARM/diagnostics 加分 | EE/CS BS/MS；未写 equivalent experience | **远期诊断研发目标**。是开发驱动/诊断软件，不能当成只运行测试脚本的测试岗位；你的相关底层经验尚不足 |
| [Senior Firmware Engineer](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/China-Beijing/Senior-Firmware-Engineer_JR2021590) | JR2021590；北京；2026-08-05 | PCIe 网络设备低层 C 固件；5+年固件设计开发；硅后问题定位、功能实现/验证、客户一线支持；专业英语。Linux/Python 加分 | EE/CS/CE B.Sc. **or equivalent experience** | **跨专业可核实的远期固件路径**，仍需要固件实践。职责明确有客户现场问题和及时响应，健康边界必须单独核实；不能因外企就推定不加班 |
| [Senior System GPU Performance Engineer](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/China-Shanghai/Senior-System-GPU-Performance-Engineer_JR2026089) | JR2026089；上海；2026-09-30 | 8+年 GPU/系统性能、硅后特性或软硬件优化；GPU/内存/互连架构，频率/功耗/量产分档，受控实验与根因定位；Python及C/C++等分析开发 | EE/CE/CS/Systems 或相关本科/硕士，**or equivalent experience** | **长期深度目标**。不是跑 benchmark 即可，需要架构、硅后与性能优化责任；目前不是转行入口 |

### 工时危险的明确反例

[Silicon Performance, Power and Binning Tools Engineer，JR2025703](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/China-Shanghai/Silicon-Performance--Power-and-Binning-Tools-Engineer_JR2025703)，上海，2026-09-18，官网可申请。虽是硅片产品工具，正文主要包含 LLM agents/MCP/RAG、数据与 Web 工作流，并明确说支持问题可能在非办公时间出现：**“support questions don't always wait for business hours”**。按你不做 AI 应用与健康优先的要求，不推荐为主线。这个例子只证明该具体职位有此风险，不能推广成整个 NVIDIA 的工作制。

### 只有搜索快照，当前状态未确认的样本

- [Senior System Software Engineer，JR2012441，上海](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/Senior-System-Software-Engineer_JR2012441)：Jetson/Tegra BSP、flashing、OTA、secure boot，5+年 Embedded/SoC system software，kernel/driver、C/Python/Shell及英语；相关本科/硕士 **or equivalent experience**。本轮官方详情接口受限，不能当作已确认在招。
- [Senior System Software Engineer, Modeling and Validation，JR2022344，上海](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/Senior-System-Software-Engineer--Modeling-and-Validation_JR2022344)：C-model、emulation、silicon bring-up 的底层平台软件与验证基础设施；3+年相关经验，C/C++/Python、Linux、MMIO/中断/内存等；相关 BS/MS **or equivalent experience**。同样仅核到官网索引正文，当前可申请状态未确认。这里 modeling 指芯片执行模型；validation 有开发基础设施及根因调试责任，需区别于手工测试。

## 2. AMD：方向真实，但本轮样本不是低门槛转行岗位

三条官网网页均实时返回 200，存在 Apply，正文注明 existing vacancy；发布日期来自该页面的 JobPosting 元数据。未实际提交申请。

| 精确职位与官方链接 | ID / 地点 / 发布日期 | 工作与技术要求 | 学历和专业 | 对你的判断 |
|---|---|---|---|---|
| [Linux Kernel & OS Enablement Engineer](https://careers.amd.com/careers-home/jobs/87894) | 87894；页头上海，正文上海或深圳；2026-07-08 | EPYC 平台 Linux kernel/OS 功能与性能，发行版适配、backport、验证、稳定性与客户问题；preferred 8～15年 kernel/OS/system software；调度/内存/虚拟化，KVM/QEMU、debug/profiling、开源贡献 | CS/CE 或相关本科 **required**，硕士 preferred；未写 equivalent experience | **长期内核/系统软件参照**。不能把你的总工作年限作为 kernel 年限；产品设计专业与明文相关本科门槛存在差距 |
| [Firmware Engineer](https://careers.amd.com/careers-home/jobs/92127) | 92127；上海；2026-09-09 | 实际是 IO Diagnostic Engineering：CPU/GPU IO 诊断测试内容开发、仿真/硅后 bring-up、自动化、根因调试；preferred BS+8年或MS+6年；Linux/C/C++、PCIe/DMA/IOMMU、x86/ARM、英语 | CS/Computer/EE 本科或硕士 **or equivalent**，硕士 preferred。此处未明确写 equivalent experience | **诊断软件/验证研发远期目标**。不是纯固件产品功能研发，也不是无代码手工测试；专业替代口径要问 HR。需要较强硬件与平台经验 |
| [Software Development Engineer](https://careers.amd.com/careers-home/jobs/91273) | 91273；上海；2026-09-02 | Windows native C++、Qt/QML UI、IPC、gRPC、异步与性能；界面开发处于核心职责 | CS/CE/Software 或相关本科/硕士；明文 **Equivalent professional experience may also be considered** | **按你的要求排除主项**。虽然现有 Qt 有衔接，进入 AMD 继续以 Qt/QML 为主要责任并不满足你的转型目标 |

另有 [AI Framework Eng.，78999](https://careers.amd.com/careers-home/jobs/78999?lang=en-us) 及 [AI Software Engineer，89398](https://careers.amd.com/careers-home/jobs/89398)。其技术重点是深度学习框架、模型、训练/推理与算子性能，不能因为有 Linux C++ 就自动归入你的首选底座路线；本次不优先。

**标题陷阱例子**：[Test Engineer，92242](https://careers.amd.com/careers-home/jobs/92242) 的主要责任是工厂 NPI/量产支持、PCBA/电路及现场测试，Linux/Python 是部分工具。它与 CPU/GPU 驱动或 Runtime 研发不是同一职业方向；不能只看到芯片公司、Linux、3+年就认定合适。

## 3. Intel：当前样本与历史岗位必须分开

本轮通过 Intel 雇主招聘接口检索上海、北京、成都，并查看相关详情。结果是一个时间点与检索范围的证据，**不是“Intel 永远没有国内驱动/固件社招”**。

| 具体官方岗位 | 状态、地点、日期 | 内容与门槛 | 对你的判断 |
|---|---|---|---|
| [System Firmware Engineer，JR0281588](https://intel.wd1.myworkdayjobs.com/en-US/External/job/System-Firmware-Engineer_JR0281588-1) | 上海；本轮详情接口返回404；官网搜索快照存在。具体原发布日期未核到 | 系统固件/BIOS/UEFI、低层软件调试、可复用组件；相关 EE/CE 本科或 equivalent；6～8年相关经验；C/C++/Python、英语。equivalent 未明确为实践经验 | **历史长期职责参考，不列当前可投**；不能把 indexed Apply 文本当作今天开放状态 |
| [Cloud and AI System Engineer，JR0286408](https://intel.wd1.myworkdayjobs.com/External/job/PRC-Shanghai/Cloud-and-AI-System-Engineer_JR0286408) | 上海；2026-08-12；官网可申请；**Job Type=College Grad** | 服务器/机架软硬件集成、问题定位、平台性能；相关 CS/EE 本科+0～1年相关经验，或相关硕士；C/C++/Python、体系结构 | 内容部分接近平台软件，但**校招口径和相关专业须核**；不是本轮给你的社招入口推荐。你的“自考本科即将毕业”不自动等于有校招资格 |
| [Platform Power Thermal Performance Engineer，JR0286409](https://intel.wd1.myworkdayjobs.com/External/job/PRC-Shanghai/Platform-Power-Thermal-Performance-Engineer_JR0286409) | 上海；2026-08-12；官网可申请；**Job Type=College Grad** | AI 服务器 CPU/GPU/内存/IO 性能验证、受控实验、根因调查；明确 upcoming graduates、相关硕士或以上；Linux、脚本、架构及PCIe/CXL/NUMA等 | **当前学历/招聘类型不符合，排除**。不能包装成与你当前条件匹配的性能研发职位 |

当前上海 [AI framework engineer，JR0287327](https://intel.wd1.myworkdayjobs.com/External/job/PRC-Shanghai/AI-framework-engineer_JR0287327) 的正文为 **Student / Intern**，不能因列表类别或职位名没有 Intern 就按社招判断。模型压缩、LLM/框架和 AI 应用类也不作为你的主线。

本轮没有核到两个同时符合“中国在招社招、Linux 底座、当前年限/学历相近”的 Intel 具体岗位，因此不以校招和实习凑推荐数量。后续可直接在 [Intel 官方招聘入口](https://intel.wd1.myworkdayjobs.com/External) 搜 `System Firmware`、`Linux Kernel`、`Device Driver`、`Platform Software`、`Silicon Validation`，核对 Job Type 和实际职责。

## 4. 对转行方向的具体含义

这是基于上述职责的推断，不是招聘方承诺：

1. **GPU/CPU 开发工具或诊断软件工程师**：Linux C/C++、测试 API、trace、寄存器/中断/内存行为、可复現故障与修复，可能比直接追求顶层芯片架构岗位更容易拆成学习项目。仍须接受开发工具也有专业、英语和底层经验筛选。
2. **嵌入式 Linux 驱动/BSP 工程师 → 平台系统软件/内核工程师**：已有 i.MX6ULL Pro 可以练设备树、driver 与用户态接口、启动/日志和错误恢复。完成板上练习不等于拥有 PCIe GPU 内核驱动经验，但基础有真实关联。
3. **固件工程师 → SoC/PCIe 固件研发工程师**：C、体系结构、寄存器/中断、RTOS/boot、调试与软硬件协同。愿意补硬件可以拓宽路径；客户支持占比高、硅后救火、实验室与发布高峰要单独核实。
4. **GPU/NPU 用户态 Runtime 工程师**：设备资源、内存、队列、同步和错误恢复值得继续查国内雇主的明确岗位。不能用本轮模型/框架岗位替代它，不能凭模拟队列项目宣称能做真实 GPU Runtime。

你现有 UI/流程经验可帮助工具可用性、接口和交付沟通；核心竞争力要变成上述代码与故障定位责任。先看岗位要承担什么，再定基础和小项目；不要为进某个品牌而接受明显与主线冲突的工作。

## 5. 薪资和工时：未核实项与面试核查

本文件的官网 JD 没有给中国工资和固定上下班时间，故不能说 AMD/Intel/NVIDIA 一定满足你的税前 15K 和健康要求，也不能说外企统一 955/965。

- 薪资核查：合同底薪、保证薪数、绩效条件、股票及其归属、试用期、招聘地区。把保证现金收入与不保证部分分开。
- 工时核查：最近三个月团队通常几点结束、周末发生频率；硅后 bring-up/量产/客户发布高峰持续多久；是否跨时区晚会、值班或非办公时间响应。
- 职责核查：自己拥有多少底层代码，做开发与根因修复还是执行既有测试；客户现场支持比例，是否要承担持续救火。
- 学历核查：明确说“产品设计自考本科即将取得+仪器软件实践”，问专业与学历形式是否接受；equivalent experience 要哪些可验证证据。

没有证据的回答记为“待确认”。NVIDIA JR2025703 的非办公时间支持是一个已发现的具体危险；其他岗位客户支持/全球协作只表示需核查，不能据此确定实际加班频率。

## 6. 大型企业补充：Arm 与 NXP

下面是大企业的额外具体职责参照，不替代前三家公司核查。也未披露中国薪资与固定工时。

| 官方岗位 | 状态与地点 | 技术、专业边界与个人适配 |
|---|---|---|
| [Arm Staff Software Engineer (GPU Customer Engineering)](https://careers.arm.com/job/shanghai/staff-software-engineer-gpu-customer-engineering/33099/101070670048) | ID 2026-19393；上海；2026-09-24；官网有 Apply | Android/Linux 内核态 GPU 驱动，DRM/KMS/GEM/IOMMU/DMA，C、GDB/perf/ftrace、内存/功耗；要求已有 kernel/driver 经验、英语、直接客户协作和偶尔出差。未列明确学历/年限。**驱动专项远期参照**，不是图像处理算法职位，但需要补 GPU 图形栈，不能按当前经验当即满足 |
| [Arm Staff/Senior Software Engineer (SW Performance)](https://careers.arm.com/en/job/shanghai/staff-senior-software-engineer-sw-performance/33099/101067459488) | ID 2025-13856；上海；页面发布日期2026-09-24，职位ID年份不当作发布日期；官网有 Apply | 优化 Mali Vulkan/ANGLE driver、减 driver overhead、应用到驱动热点分析；C/C++、图形标准、profiling/modeling；CS/数学/物理等相关大学学历 **or equivalent experience**。**用户态 GPU driver/performance 远期参照**；UI 经验不能代替图形标准与性能分析实践 |
| [NXP 2027Y Campus - Software Engineer - Linux BSP & Driver Development](https://nxp.wd3.myworkdayjobs.com/careers/job/Shanghai-Pudong/XMLNAME-2027Y-Campus---Software-Engineer---Linux-BSP---Driver-Development_R-10066602) | R-10066602；上海浦东；2026-09-29；官网接口确认可申请；**2027届校招** | i.MX SoC Linux driver、bring-up、kernel 维护与 upstream；Embedded C、OS 内存/并发/中断、ARM Cortex-A、读原理图/datasheet；CS/CE/EE或相关技术专业2027届本科以上。i.MX板实践加分。**技术清单与你现有板子直接有关，招聘身份/专业尚不符合已核要求，不当作社招推荐** |

Arm 页面说 hybrid 模式由具体团队与岗位需要决定，不能据此推出固定远程、955 或低加班。NXP 的 wellness/mentorship 宣传也不能当作工时保证。

## 核查方法与限制

- NVIDIA/Intel：官方网页与雇主 Workday 公共详情接口；记录 startDate、canApply、posted 与 Job Type；没有登录、提交申请或联系他人。
- AMD：官方网页实时可访问，JobPosting 元数据确认日期，正文确认职责。数据里的 baseSalary=0/USD 是未披露占位，已排除。
- 部分旧网页在搜索中仍有正文，而实时详情受限或已404；本文件区分了状态。网站后续可能更改。
- 只调查中国软件职位，没有把海外职位薪资折算、数字 IC/RTL/制造工艺等硬件路线混成当前转行推荐。
