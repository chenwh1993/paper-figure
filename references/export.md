# 在最终尺寸下导出

把下面的 `script_dir` 指向本技能的 `scripts` 目录。保留绘图脚本里读取原始数据、分组、阈值和排序的语句，方便下次改图时重跑。下列代码中的变量来自实际用户数据。

## Matplotlib

```python
import sys
sys.path.insert(0, str(script_dir))
from panel import panel_style, size_mm, save_panel
import matplotlib.pyplot as plt

with panel_style():
    fig, ax = plt.subplots(figsize=size_mm(85, 65), layout="constrained")
    ax.scatter(x, y, s=1, c=cell_colors, linewidths=0, rasterized=True)
    ax.set(xlabel="UMAP 1", ylabel="UMAP 2", aspect="equal")
    for name, (tx, ty) in group_label_positions.items():
        ax.text(tx, ty, name, ha="center")
    save_panel(fig, output_dir / "cell_states")
    plt.close(fig)
```

- **火山图**给散点 `rasterized=True`，在之后用 `axhline`、`axvline`、`annotate` 单独画阈值和标签。图例使用矢量标记，分组字典复用同一组颜色。
- **大热图**用 `pcolormesh(..., rasterized=True, edgecolors="none")` 画矩阵体，或 `imshow(..., interpolation="nearest", aspect="auto")`。单独创建色标。如色标需要逐段可编辑，可用 `cb.solids.set_rasterized(False)`。彩色注释条、行列分隔线、标签和树单独绘制。
- **全矢量图**用常规点、线、误差线和文字。细密散点设置在具体 artist 上。避免整轴栅格化、将图截屏作为底图或把文字转路径。面板已按毫米建好，导出时保留画板边界。
- Arial 可显示的数学字符优先使用 Unicode，如 α、β、−、µ。使用数学排版、描边文字或外部模板时特别核验字体和可选中文本。

## R

```r
source(file.path(script_dir, "panel.R"), encoding = "UTF-8")
library(ggplot2)
p <- ggplot(df, aes(UMAP_1, UMAP_2, colour = subtype)) +
  ggrastr::rasterise(geom_point(size = 0.35, stroke = 0), dpi = 600, dev = "ragg") +
  scale_colour_manual(values = subtype_colours) +
  coord_equal() + labs(x = "UMAP 1", y = "UMAP 2") + panel_theme()
save_panel(function() print(p), file.path(output_dir, "cell_states"), 85, 65)
```

- `geom_text`、`annotate("text", ...)` 和 `ggrepel` 等图内文字独立设 `family="Arial", size=8/ggplot2::.pt`。主题管理轴、图例和分面文字。ggplot2 版本支持时也可用 `size=8, size.unit="pt"`。
- `ComplexHeatmap::Heatmap(..., use_raster=TRUE)` 将矩阵主体嵌入为图像。行列名字、分面标题、注释与图例文字显式设 `grid::gpar(fontfamily="Arial", fontsize=8)`。包的 `raster_quality` 是相对倍率，按矩阵显示的物理宽和嵌入图像像素核算分辨率，增加倍率后再核看。保留需要识别的稀有信号。聚合取均值可能使它消失。用 `save_panel(function() ComplexHeatmap::draw(ht), ...)`。
- 基础依赖为 ggplot2、svglite、systemfonts、R 自带的 Cairo PDF 设备，以及 PATH 中带 PyMuPDF 的 Python。R 的原生 PDF 设备会把页面边界取整到整点。助手只修正页面框以保留指定毫米尺寸。ggrastr 和 ragg 用于密集 ggplot 图层。此 Windows 个人安装附带独立 R 缓存，通过 `source` 自动识别。若命令行的 C.UTF-8 区域设置令中文路径不可见，使用 en_US.UTF-8 启动该次 Rscript。

## 交付前核对

```text
python "<skill>/scripts/check_panel.py" "<输出目录>/cell_states" --mm 85 65 --mode mixed --label "UMAP 1"
python "<skill>/scripts/check_panel.py" "<输出目录>/paired" --mm 88 65 --mode vector --label "Score"
```

在 PDF 中核对真实页面尺寸、文字能被选中、字体和字号，以及位图与路径的数量。在 SVG 中核对文本节点和内嵌图片。保留证据时区分输出文件检查与 Illustrator 实开检查。图像的有效分辨率可用嵌入像素数除以其在画板上的英寸宽度。小矩阵按原始格数呈现时另核查行列有没有被合并。以最终大小预览，重点看裁切、标注遮挡、分组和比例尺可读性。

绘图设备的说明见 [Matplotlib 分层栅格化](https://matplotlib.org/stable/gallery/misc/rasterization_demo.html)、[ggrastr](https://github.com/VPetukhov/ggrastr)、[svglite 文字](https://svglite.r-lib.org/articles/fonts.html) 和 [ComplexHeatmap 矩阵栅格化](https://jokergoo.github.io/ComplexHeatmap-reference/book/a-single-heatmap.html#heatmap-as-raster-image)。
