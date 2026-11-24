# 科研图怎么选，文章配色怎么用

先写出读者要判断的关系，再决定每一个点、格子或线段代表谁。下面的例子来自单细胞、空间组学、肿瘤免疫、临床队列和方法学论文，适合在绘制论文面板前按问题查阅。

[可筛选的文献与配色索引](../assets/图例与配色索引.xlsx) · [Illustrator ASE 色板](../assets/论文配色.ase)

索引中的本地原文链接指向整理时的文献目录。换机查阅时，可按索引里的文件名或 DOI 定位论文。

## 同一份数据，可以回答三个不同的问题

假设有患者 ID、治疗时间点、细胞类型、UMAP 坐标和表达矩阵。想看 **T 细胞在哪里**，用所有细胞共用的 UMAP 坐标，以灰色作背景、用一种颜色突出 T 细胞。想看 **治疗后 T 细胞比例是否变化**，先在每位患者、每个时间点计算 T 细胞占所选分母的比例，再把同一患者的前后两个点相连。想看 **哪些基因发生变化**，用按研究设计获得的基因效应与校正后 P 值画火山图。三幅图中的一个点依次代表一个细胞、一名患者在某个时间点的比例、一个基因。用于统计推断的独立重复由研究设计决定。

Chen 等的 Fig. 1E–F 将细胞嵌入与患者级比例并排展示。Fig. 6C、6E、6I 又分别展示了细胞状态、差异基因和治疗前后的个体变化。可用这些图号和作者代码检查自己的面板是否保留了正确的数据层级。[论文](https://doi.org/10.1016/j.ccell.2024.06.009) · [Fig. 1 脚本](https://github.com/yqq-chen/CRC_ICB/blob/cc186b2881a3104f62e0729b036971e6991528b7/Figure1.R) · [Fig. 6 脚本](https://github.com/yqq-chen/CRC_ICB/blob/cc186b2881a3104f62e0729b036971e6991528b7/Figure6.R)

## 按研究问题选图

### 样本、分组与临床随访

| 要展示什么 | 观测单位与作图方式 | 解读时要保留什么 | 实例 |
| --- | --- | --- | --- |
| 分组后的连续测量 | 一名患者或一个独立样本一个观测。抖动点叠箱线。样本很少时逐点显示并标 n | 箱线给中位数和四分位。生物学重复与同一患者的多个细胞分开计算。 | [Chen et al. · Cancer Cell 2024 · 1F](https://doi.org/10.1016/j.ccell.2024.06.009) |
| 同一对象前后变化 | 患者 ID、时间点、测量值。配对点连线或差值点图，增加组别时分面 | 用 ID 连接，显示有缺测的单点。连续多个时间点使用真实时间间距。 | [Chen et al. · Cancer Cell 2024 · 6I](https://doi.org/10.1016/j.ccell.2024.06.009) |
| 组内分布与重叠 | 每个群体的连续观测或已归一化的密度。小提琴、山脊或直方图。比较样本差异时另画样本级汇总 | 组间固定分箱或带宽。小样本优先原始点。当密度各自归一化时加样本数。 | [Chen et al. · Cancer Cell 2024 · 6D](https://doi.org/10.1016/j.ccell.2024.06.009) |
| 连续变量间关系 | 每个独立单位都有一对 x、y 值。散点图，按问题配拟合线与区间。过密时用六边形分箱 | 给出尺度、模型与区间含义。重复测量用个体轨迹或相应模型。 | [Chen et al. · Cancer Cell 2024 · 6B](https://doi.org/10.1016/j.ccell.2024.06.009) |
| 比例与组成 | 每个样本的组分计数与分母。看构成用 100% 堆积条。比较某组分用逐样本的比例点 | 注明分母是全部细胞、某一谱系或某空间区。汇总方式会改变患者权重。 | [Wu et al. · Nature Genetics 2021 · 8b、8c](https://doi.org/10.1038/s41588-021-00911-1) |
| 风险或亚组效应 | 每项估计及上下界，注明模型与人群。森林图将点估计、区间和数字按行对齐 | 比值型用参考值 1 并考虑对数刻度，差值型参考值为 0。区别区间估计与显著性。 | [Aung et al. · Nature Genetics 2025 · 3c](https://doi.org/10.1038/s41588-025-02351-7) |
| 随访期间的时间结局 | 患者的起点、时长、事件或删失、分组。KM 阶梯曲线加删失标记和在险人数表 | 写明时间零点及事件。按后续检测分组时明确 landmark。竞争风险需采用相应累计发生函数。 | [Nakamura · Fig. 2a,b](https://www.nature.com/articles/s41591-024-03254-6) |
| 谁的肿瘤缩小，谁持续治疗得更久？ | 72 位患者，各有基线与随访病灶测量、治疗起止及应答评估日期。最佳变化用每人一柱的瀑布图。治疗经过用每人一行的泳道，横轴为月，分段颜色识别治疗阶段，菱形标评估事件，箭头标随访仍在进行。 | 最佳变化丢失时间顺序。生存或无进展概率应从原始时间与删失状态另估。两幅图重排时保留患者 ID。 | [L088 · Fig. 1b–c](https://doi.org/10.1038/s41392-024-02031-8) |
| 怎样展示同一肿瘤不同取材区的异质性？ | 组织芯与所属肿瘤构成两层。A 纳入 LUAD 65 个组织芯/35 个肿瘤，LUSC 48 个组织芯/23 个肿瘤。A 按组织芯对齐肿瘤区和间质区的细胞密度，B 以水平线连接同一肿瘤的多个组织芯，C 给空间实例。 | 组织芯列数不等于独立患者数。图中须标出跨列的归属关系，组间推断要考虑同一肿瘤内相关。 | [L122 · Fig. 2A–C](https://doi.org/10.1158/2159-8290.CD-23-1380) |

### 表达、细胞状态与分子特征

| 要展示什么 | 观测单位与作图方式 | 解读时要保留什么 | 实例 |
| --- | --- | --- | --- |
| 单细胞身份与连续状态 | 细胞 ID、同一嵌入的两列坐标、类别或评分。类别 UMAP 加图例，另用同一坐标展示评分或高亮细胞 | 对照组共用坐标范围与点大小。群的面积和间距不能直接估计患者丰度或发育时间。 | [Chen et al. · Cancer Cell 2024 · 6C](https://doi.org/10.1016/j.ccell.2024.06.009) |
| 比较细胞类型的标记物 | 基因 × 细胞群的表达强度与检出率。点矩阵，点面积编码检出率、颜色编码平均表达或 Z 分数 | 分别标明两种单位。按样本或群聚合、行标准化及省略小点的规则都影响解读。 | [Oliveira et al. · Nature Genetics 2025 · 4c](https://doi.org/10.1038/s41588-025-02193-3) |
| 展示差异表达全貌 | 每个特征的 log₂FC 与 P 或校正后 P。火山图。只需呈现少数效应时改用排序点和区间 | 注明比较方向和校正方法。零 P 值需要按计算精度截断并标注。只标预定或有依据的特征。 | [Chen et al. · Cancer Cell 2024 · 6E](https://doi.org/10.1016/j.ccell.2024.06.009) |
| 许多样本与特征的联合模式 | 有行列标签和样本注释的二维矩阵。热图配列注释和树状图。标签拥挤时选关键行或分块 | 说明原值、log 值或行 Z 分数，标明聚类方向和距离。同一色域用于需要对比的面板。 | [Wu et al. · Nature Genetics 2021 · 8a](https://doi.org/10.1038/s41588-021-00911-1) |
| 推断轨迹与命运概率 | 每个细胞的状态、推断时间或终末状态概率。同一嵌入按分支分面，另画基因随拟时序变化 | 用相同的 0–1 范围比较概率。分支和时间均需与模型假设一并解释。 | [CellRank · Fig. 2e,f](https://www.nature.com/articles/s41592-021-01346-6) |
| 拷贝数与染色体结构 | 按真实基因组位置排序的样本 × 基因组区段。按染色体分段作热图或信号轨迹，按样本或亚克隆分行 | 中性色对齐拷贝基线。标明是表达推断值还是 DNA 实测值及区段宽度。 | [Yu et al. · Cancer Discovery 2026 · 2A–C](https://doi.org/10.1158/2159-8290.CD-26-0099) |
| 全基因组关联位置 | 每次检验的染色体、位置、P 值或效应。Manhattan 图标位置与显著性。需要比较效应时另配效应量图 | 单变异与聚合检验阈值分开。尖峰的高度表示显著性。 | [WGS–pQTL · Fig. 2a–e](https://www.nature.com/articles/s41588-025-02095-4) |
| 两个共用位置轴上的信号 | 多个样本的基因组窗口或空间定位。堆叠轨迹、共同坐标轴和标出的观察窗 | 保持参考组装、轴范围和单位一致。局部放大保留原位置参照。 | [Bhat et al. · Nature 2024 · 1b](https://doi.org/10.1038/s41586-024-07429-6) |
| 不同风险组的基因组增减发生在哪里，同一肿瘤还带有哪些事件？ | 两个风险组的肿瘤样本，每例具有基因突变和拷贝数事件。A 沿染色体按位置绘制向上增益与向下缺失的群体频率。B 以样本为列，将突变、增益、缺失分行对齐，并标风险组。 | 频率轨道已按组聚合，不能据此判断两个事件共存于同一病例。共现应回到样本矩阵，并区分未测和无事件。 | [L048 · Fig. 8A–B](https://doi.org/10.1007/s12672-024-01187-7) |
| 哪些上调基因仅被某几个癌种共有？ | 每个癌种各有一个肿瘤内皮细胞上调基因集合。计数单位为去重基因。用 UpSet 点阵的实心点和连线指定癌种组合，列顶柱高表示该互斥组合的基因数。 | 原图使用 distinct 交集。包含交集与互斥交集会得到不同计数。先统一基因 ID、背景集和纳入阈值。 | [L166 · Supplementary Fig. S5D](https://doi.org/10.1093/nsr/nwae231) |
| 同一扩增克隆出现在哪几种 T 细胞状态？ | 从单细胞 TCR 与状态注释得到扩增的 CD8 克隆型，并统计各克隆在三种状态中的细胞数。C 以克隆型为行、状态为列，格色表示该克隆的细胞数。A 的矩阵汇总亚群间共享程度，B 另示嵌入上的推断方向场。 | 共享克隆型可支持共同克隆来源，横断面状态分布及 velocity 不足以确定单细胞真实迁移方向。组间比较保留患者层级。 | [L258 · Fig. 3A–C](https://doi.org/10.1016/j.ccell.2025.01.001) |
| 状态的先后关系是否与真实采样时段相符？ | 四个采样时点的肠类器官细胞、状态注释和表达矩阵。轨迹路标是计算得到的状态位置。a 在同一 UMAP 上逐面板高亮每个真实时点，b 叠加拟合的分支，c 沿路标排序表达热图。 | 采样时点与推断伪时间是不同变量。轨迹顺序不是细胞谱系证据，分支也不能换算为真实时长。 | [L109 · Fig. 3a–c](https://doi.org/10.1038/s41592-021-01391-1) |

### 空间、成像与相互作用

| 要展示什么 | 观测单位与作图方式 | 解读时要保留什么 | 实例 |
| --- | --- | --- | --- |
| 找到组织中的区域和边界 | 细胞或空间 bin 的物理坐标、切片、区域或信号。组织总览加 ROI 放大，并排显示位置上的分类或表达 | 固定方向与长宽比，配校准的比例尺。距离或丰度结论需样本级量化。 | [Oliveira et al. · Nature Genetics 2025 · 3a–c、4a](https://doi.org/10.1038/s41588-025-02193-3) |
| 空间邻域是否富集 | 细胞坐标、类型及邻接或置换统计量。组织图配细胞类型对 × 类型对的富集热图 | 报告邻域定义、置换单位与 Z=0 的含义。空间邻近不能独自证明相互作用。 | [Squidpy · Fig. 2d,e](https://www.nature.com/articles/s41592-021-01358-2) |
| 细胞分割或影像方法的准确度 | 同一原始视野、实例轮廓、测试集指标。原图叠轮廓，配按训练量或对象大小的性能曲线 | 真实视野比例不变，给匹配阈值、指标定义及测试集覆盖范围。 | [Cellpose 2.0 · Fig. 3a–d](https://www.nature.com/articles/s41592-022-01663-4) |
| 比较两套接触图或分数 | 相同窗口、相同分辨率的二维矩阵和成对分数。并列矩阵，配分数散点、边缘分布和代表窗口 | 共用色标。讲清分数方向、归一化，以及比较的是窗口还是样本。 | [染色质接触图 · Fig. 2](https://www.nature.com/articles/s41592-025-02630-5) |
| 多组学调控关联 | 每个细胞类型的调控子特异度和表达，或区域到基因的权重。双变量点图或同一坐标上的连接弧线，只标重点 | 在图例中分别写明面积、颜色和边宽。推断连线描述模型给出的关联。 | [SCENIC+ · Fig. 2c、2g](https://www.nature.com/articles/s41592-023-01938-4) |
| 哪些配体与相邻肿瘤区域的靶基因共同变化？ | 成对的免疫浸润 ROI 与毗邻肿瘤 ROI。在区域对之间估计发送区配体与接收区靶基因的表达相关。a 将配体与靶基因分置两段弧，连线透明度对应相关强度。d 单列推断网络，用箭头标示模型中的作用方向。 | 空间相关和网络预测不能确认实测的细胞通讯或因果方向。多 ROI 来自同一患者时应保留其嵌套关系。 | [L067 · Fig. 5a, d](https://doi.org/10.1038/s42003-024-06426-9) |
| 淋巴结构位于边界哪一侧，组织结构与患者怎样分别计数？ | C 上行为 902 个 TLS 到肿瘤边界的距离，下行为 144 位有周边 TLS 的患者各自的最大距离。D 涉及 178 位患者。将结构级距离和患者级最大距离分成两个密度图，明确边界零点。D 用带宽显示患者在周边和内部两种成熟度分类间的联合人数。 | 两条密度曲线的分母与统计量不同。带状关联对应同期分类，不代表随时间成熟或迁移。 | [L101 · Fig. 1C–D](https://doi.org/10.1016/j.ccell.2024.07.006) |
| 哪些细胞类型常组成同一空间邻域，这种邻域在组织上位于哪里？ | 251 个成像视野。每个中心细胞取 20 个近邻，构成 20 种邻域。预后分析的单位为患者。用细胞组成热图概括邻域，再用邻域类别色将代表视野的 Voronoi 分区绘回原坐标。 | Voronoi 多边形是根据坐标构造的空间分区。解读真实细胞边界需分割证据。结局推断以患者汇总频率为单位。 | [L146 · Fig. 3A–C](https://doi.org/10.1016/j.ccell.2025.01.012) |

### 模型与方法比较

| 要展示什么 | 观测单位与作图方式 | 解读时要保留什么 | 实例 |
| --- | --- | --- | --- |
| 不同方法的性能取舍 | 同一任务下方法 × 指标 × 模拟重复或数据集。按方法分面，分别画灵敏度和错误发现率。保留重复点 | 共享任务的结果可配对。总分要说明方向、尺度与权重。组间对齐任务难度。 | [Dann et al. · Nature Biotechnology 2022 · 2c、2e](https://doi.org/10.1038/s41587-021-01033-z) |
| 检测或分类性能 | 个体真实类别与连续预测分数。ROC 比较灵敏度与假阳性率。阳性稀少时并列 PR 图 | 按独立测试集计算，PR 基线是测试集阳性率。报告数据切分与阈值来源。 | [Chen et al. · Cancer Cell 2024 · 6G](https://doi.org/10.1016/j.ccell.2024.06.009) |
| 已知真值时，恢复成功率和基因检出性能如何随条件变化？ | d 每档信噪比有 20 次模拟重复。e 预测单位为基因。f 比较模拟与推断的程序使用度。d 各方法逐信噪比连接恢复成功率。e 横轴明确写 FDR、纵轴灵敏度。f 用真值–估计值散点展示偏差。 | FDR 和假阳性率的分母不同，因此 e 不能按常规 ROC/AUC 解释。模拟结果只支持相应的信号与噪声范围。 | [L246 · Fig. 2d–f](https://doi.org/10.7554/eLife.43803) |
| 空间蛋白预测在独立患者中有多准确？ | 结直肠与前列腺验证队列分别为 12 和 18 位独立患者。按标志物在每位患者内计算预测与实测单细胞表达的 Pearson 相关。a 每点一位患者，按标志物绘患者均值与 bootstrap 95% CI。c 在对应组织区域并列 H&E、预测和实测信号。 | 单细胞用于计算患者内指标，不能将细胞数当作验证样本量。相关性也不能排除系统偏差或替代校准指标。 | [L283 · Fig. 4a, c](https://doi.org/10.1038/s43018-026-01270-8) |
| 细胞注释具体混淆了哪些类别？ | 带参考类群的单细胞及其留一交叉验证预测，每列按该参考亚群中的细胞总数归一化。矩阵横轴列参考类、纵轴列预测类。用连续色深表示分配到格内的百分比，关注非对角格，保留样本量。 | 每列比例不是总体准确率。细胞级留一验证不能直接说明模型对新患者或新中心的泛化能力。 | [L046 · Fig. 1D](https://doi.org/10.1016/j.isci.2024.109928) |

区分双变量点图的两个图例尤其重要。在结直肠癌 Visium HD 论文 Fig. 4c 中，面积是表达该基因的细胞比例，颜色是平均表达。在 SCENIC+ 的 Fig. 2c 中，面积是调控子特异度，颜色是转录因子表达。复用相同图型时，图例、单位和筛选条件也要随数据重新写。[Visium HD Fig. 4](https://doi.org/10.1038/s41588-025-02193-3) · [SCENIC+ Fig. 2](https://www.nature.com/articles/s41592-023-01938-4#Fig2)

## 论文配色

复用颜色前先确定颜色表示类别、连续量、相对参考值的方向，还是只为了突出一个目标。按组名固定颜色映射。多面板保持同一分组颜色和连续尺度。需要照顾灰度印刷或常见色觉差异时，为关键比较同时使用形状、线型或直接标注。组织切片原色和免疫荧光通道另行解释。

| 来源与面板 | 适用场景 | 颜色与角色 | 取值依据 |
| --- | --- | --- | --- |
| [Chen et al. Fig. 1F](https://github.com/yqq-chen/CRC_ICB/blob/cc186b2881a3104f62e0729b036971e6991528b7/Figure1.R#L93) | 离散分组 | CR #5778A2 · PR #DCB44B · SD #8A281E | 代码原值 |
| [Chen et al. Fig. 6E](https://github.com/yqq-chen/CRC_ICB/blob/cc186b2881a3104f62e0729b036971e6991528b7/Figure6.R#L171) | 高亮与背景 | 背景 #BEBEBE · 显著 #BD4739 | 代码原值 |
| [Chen et al. Fig. 1E](https://doi.org/10.1016/j.ccell.2024.06.009) | 离散分组 | T cell #B6454E · Innate lymphoid #F68F35 · B cell #7FC6E1 · Myeloid #2888B6 · Stromal #8467AC · Epithelial #B49AC9 | 图面取样 |
| [Oliveira et al. Fig. 4a](https://github.com/10XGenomics/HumanColonCancer_VisiumHD/blob/df5801cf5e681b33b5026626989a7635fdf26b99/Figures/Figure_4.R#L99) | 区域与背景 | 周边 50 µm #1E90FF · 其余组织 #D3D3D3 · 肿瘤 #FF3030 | 代码原值 |
| [Yu et al. Fig. 2A–C](https://github.com/VividKai/SpatialBC/blob/f854197edb9730a9fc215ce1022a44474446f99c/Fig2.R#L305) | 有中心的连续量 | 0.93 #377EB8 · 1.00 #FFFFFF · 1.07 #E41A1C | 代码原值 |
| [Yu et al. Fig. 2A–C](https://github.com/VividKai/SpatialBC/blob/f854197edb9730a9fc215ce1022a44474446f99c/Fig2.R#L236) | 顺序渐变 | 低 #E5E5E5 · 2 #C6D9F0 · 3 #9BBCE1 · 4 #709FD2 · 5 #4582C3 · 高 #1A65B4 | 代码原值 |
| [Aung et al. Fig. 3d](https://doi.org/10.1038/s41588-025-02351-7) | 二组随访 | Low #0B4F8F · High #E72333 | 图面取样 |
| [Single-cell spatial immune landscapes of primary and… Fig. 1b · PDF p.2](https://doi.org/10.1038/s41586-022-05680-3) | 空间多重成像通道 | Ki67 #FFB600 · GFAP #E2C79B · CD31 #00B761 · CD68 #9337FF · MPO #FF2500 · CD3 #FFFF03 · Cancer（癌细胞） #DCDCDC | 图面取样 |
| [Prognostic value of GARS in bladder cancer and its r… Fig. 4B · PDF p.11](https://doi.org/10.21037/tcr-23-2148) | 突变瀑布图 / OncoPrint | Missense_Mutation #33A02C · Nonsense_Mutation #E31A1C · Splice_Site #FF7F00 · Frame_Shift_Ins #6A3D9A · Frame_Shift_Del #1F78B4 · In_Frame_Del #FFFF99 · Multi_Hit #000000 | 图面取样 |
| [muscat detects subpopulation-specific state transiti… Fig. 3 · PDF p.6](https://doi.org/10.1038/s41467-020-19894-4) | UpSet交集柱内的基因类别 | EE #4069E0 · DE #CC0000 · DP #FF6346 · DM #FFA500 · DB #FFD700 | 图面取样 |
| [Squidpy Fig. 2e](https://github.com/theislab/squidpy_reproducibility/blob/407b151c1b7d657dd46a99cd9d924b13ec2d9afa/notebooks/graph_figures/merfish.ipynb) | 作者指定 Matplotlib 色图及数值范围。HEX 为色图取值换算 | 低端 #3B4CC0 · 中点附近 #DDDCDC · 高端 #B40426 | 作者指定色图换算 |

配色索引共 29 组。其中 23 组包含可用 HEX（共 86 个有角色的色样），另有 6 组只记录文章给出的色名、色板名或作用。作者代码原值来自显式 HEX、R 命名色或明确指定且可复算的离散色板。图面取样只取已辨认的图例块或线条，按 PDF 的 RGB 渲染读取。透明度、色彩管理和排版可能改变外观。色板文件只收有数值的组。完整记录包含来源和图号。[配色记录](palettes.json)

在 Illustrator 的「色板」面板菜单选择「打开色板库」→「其他库」，选择交付的 ASE 文件。每个组名对应工作簿的「色板组 ID」，色样名中保留了角色和 HEX。

## 九篇新增开放获取论文

| 论文 | 期刊与年份 | 可回查的面板 | 开放许可与代码 |
| --- | --- | --- | --- |
| [ctDNA-based molecular residual disease and survival in resectable colorectal cancer](https://www.nature.com/articles/s41591-024-03254-6) | Nature Medicine 2024 | Fig. 2a,b、Fig. 2c,d | CC BY-NC-ND 4.0。图级，作者 R Markdown 含生存估计、在险表及分组配色。约 219–231 行对应全队列 DFS。 [作者资源](https://github.com/Natera-TMED/Nakamura-et-al_CIRCULATE-JP-Galaxy-2024/blob/9aea1b36d32e6749452f6aefb6d6eab7775a4a9a/CIRCULATE%20Galaxy%20Nakamura%20et%20al%202024.Rmd) [开放全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC11564113/) |
| [Whole-genome sequencing analysis identifies rare, large-effect noncoding variants and regulatory regions associated with circulating protein levels](https://www.nature.com/articles/s41588-025-02095-4) | Nature Genetics 2025 | Fig. 2a–e、Fig. 3a,b | CC BY 4.0。分析仓库可核，含遗传检验与 Fig. 6 的出图脚本。Fig. 2–3 的最终绘图脚本未定位。 [作者资源](https://github.com/ExeterGenetics/WGS_50k_Proteins_2024/tree/29b86ad5632e7609820bffc43457bb8a4e2a61da/) [开放全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC11906349/) |
| [Benchmarking atlas-level data integration in single-cell genomics](https://www.nature.com/articles/s41592-021-01336-8) | Nature Methods 2022 | Fig. 2a–c、Fig. 3a | CC BY 4.0。图级，作者 R 函数 plotSingleTaskRNA 生成单任务得分表，复现仓库还提供汇总散点图和嵌入可视化。 [作者资源](https://github.com/theislab/scib-reproducibility/blob/3afbffd3674726e5146797be21cf6bd7470a2c5f/visualization/plotSingleTaskRNA.R) [开放全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC8748196/) |
| [CellRank for directed single-cell fate mapping](https://www.nature.com/articles/s41592-021-01346-6) | Nature Methods 2022 | Fig. 2e、Fig. 2f | CC BY 4.0。图级，作者提供 Fig. 2–3 胰腺分析 notebook，可定位 fate_probabilities 及 gene_trends 图块。 [作者资源](https://github.com/theislab/cellrank_reproducibility/blob/c1b9232caacd15fdd16914007fab4890b136109f/notebooks/fig_2_pancreas_main/ML_2021-09-21_fig_2_and_3_pancreas_main.ipynb) [开放全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC8828480/) |
| [Squidpy: a scalable framework for spatial omics analysis](https://www.nature.com/articles/s41592-021-01358-2) | Nature Methods 2022 | Fig. 2d,e、Fig. 2h,i | CC BY 4.0。图级，MERFISH notebook 生成空间邻域统计与热图，仓库另含 Slide-seqV2 的共现分析。 [作者资源](https://github.com/theislab/squidpy_reproducibility/blob/407b151c1b7d657dd46a99cd9d924b13ec2d9afa/notebooks/graph_figures/merfish.ipynb) [开放全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC8828470/) |
| [SCENIC+: single-cell multiomic inference of enhancers and gene regulatory networks](https://www.nature.com/articles/s41592-023-01938-4) | Nature Methods 2023 | Fig. 2c、Fig. 2g | CC BY 4.0。图级，作者 Figure_2.md 含绘图代码。该文件的 DotPlot 段以 d 标注，正式发表图注为 2c，以图型和变量交叉核对。 [作者资源](https://github.com/aertslab/scenicplus_analyses/blob/81c961927674fd4a15026247afbfc827b7646eeb/Figure_2.md) [开放全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC10482700/) |
| [Cellpose 2.0: how to train your own model](https://www.nature.com/articles/s41592-022-01663-4) | Nature Methods 2022 | Fig. 3a–d、Fig. 3e,f | CC BY 4.0。论文指定 paper/2.0 的 Fig. 2–3 复现目录。已核 train_subsets.py 生成训练量与测试结果，未将其标为最终拼版脚本。 [作者资源](https://github.com/MouseLand/cellpose/blob/a54cb48849b7e225a81e8e43dcb042d42427f543/paper/2.0/train_subsets.py) [开放全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC9718665/) |
| [Comparing chromatin contact maps at scale: methods and insights](https://www.nature.com/articles/s41592-025-02630-5) | Nature Methods 2025 | Fig. 2、Fig. 3a,b | CC BY 4.0。分析级，作者仓库有计算与归一化示例 notebook，可核查评分方向、缩放及输入。未定位完全对应主图 2 成品的出图脚本。 [作者资源](https://github.com/pollardlab/contact_map_scoring/blob/d6f199759f72daff68b3672c66eef32c285df777/notebooks/Process%20and%20Normalize%20Scoring%20Results.ipynb) [开放全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC11978506/) |
| [Plasma proteomic associations with genetics and health in the UK Biobank](https://www.nature.com/articles/s41586-023-06592-6) | Nature 2023 | Fig. 2a、Fig. 4a | CC BY 4.0。已核期刊与 PMC 全文及 Data availability。本次未定位 Fig. 2a、4a 的作者绘图文件。 [开放全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC10567551/) |

## 可编辑拼版

按最后置入 Illustrator 的尺寸出图。多面板先分配整行宽度，再从每块宽度中扣掉标签、刻度、图例与必要留白。具体图型的起始尺寸、已发表面板的实测值和 180 mm 样张见[论文子图尺寸与拼版](panel-sizing.md)。

普通配对图、森林图、误差线或 KM 曲线保留矢量。UMAP 和火山图只栅格化细胞或基因点，大热图只栅格化矩阵主体，空间图保留原始影像分辨率。轴、图例符号、色标刻度、阈值线、标签、聚类树和比例尺保留矢量。个人预设用 600 dpi 绘制密集点层。[可运行的导出方法](export.md)

## 资料覆盖与核对口径

- 本地目录有 327 个实际 PDF 文件，按 SHA-256 去重后为 318 份。逐一检查 6 个压缩包，另有 1 个仅在包内的表注 PDF，合计 319 份独立文件内容、8,203 页。包含论文版本、补充材料、评论和期刊报告表。同一篇文章的不同版本可能对应多个文件。
- 对所有 PDF 逐页提取可用文本，对每份至少目检一页代表性图、表或文档内容。两份无原生文字的文件通过页面图像核看。工作簿的「逐份核看」保留文件、图号、物理页码、观察及 115 条配色语义。另检查了 Word 补充图注、源表、演示文稿和数据文件。
- 「图注定位」有 2,667 条自动识别的编号标题，涉及 270 份 PDF。用于定位，跨页拆分、正文引用和图注排版会造成漏项或误匹配。代表图逐份核验，逐张面板和全部作者脚本没有穷举。深读案例中，能对应到作者文件的已记录固定版本链接。其余区分分析代码、图注和图面观察。
- 补充检索按单细胞基准、空间邻域、轨迹、成像分割、遗传与蛋白组、临床随访的展示缺口选取案例。将“高分”按 Nature、Nature Methods、Nature Genetics、Nature Medicine 这些期刊执行，未用某年影响因子作阈值。按标题及 DOI 与本地比对，核对期刊或 PMC 全文、图号与开放许可。适用性来自具体图注与数据设计。
- SciDraw 首页实数为 172 张示例卡片、38 个导航入口。用其扩展候选图型，如云雨图、分面相关图、UpSet、桑基图、泳道图和森林图。科研推断、单位、配色归属及原始代码以各论文或代码来源为准。此整理使用了程序提取和 AI 辅助的图页核对。[SciDraw 图库](https://scidraw.msttnote.cn/)
