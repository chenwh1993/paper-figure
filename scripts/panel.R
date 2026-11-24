# Final-size graphics for ggplot2 and grid. A draw callback preserves grid layouts.
# Pick up the optional private Windows package library installed with this skill.
if (.Platform$OS.type == "windows") {
  local({
    minor <- strsplit(R.version$minor, ".", fixed = TRUE)[[1]][1]
    version <- paste0("R-", R.version$major, ".", minor)
    cache <- file.path(Sys.getenv("LOCALAPPDATA"), "Codex", "paper-figure", version)
    if (dir.exists(cache)) .libPaths(c(cache, .libPaths()))
  })
}

.paper_figure_dir <- dirname(normalizePath(sys.frame(1)$ofile))

panel_theme <- function() {
  pt8 <- ggplot2::element_text(size = 8, family = "Arial")
  ggplot2::theme_classic(base_size = 8, base_family = "Arial") +
    ggplot2::theme(
      text = pt8, axis.text = pt8, axis.title = pt8, strip.text = pt8,
      legend.text = pt8, legend.title = pt8, plot.title = pt8,
      plot.subtitle = pt8, plot.caption = pt8, plot.tag = pt8
    )
}

save_panel <- function(draw, stem, width_mm = 85, height_mm = 65) {
  if (!requireNamespace("svglite", quietly = TRUE))
    stop("The R panel export requires svglite.")
  families <- systemfonts::system_fonts()$family
  if (!any(tolower(families) == "arial"))
    stop("Install Arial or select a system that has Arial.")
  dir.create(dirname(stem), showWarnings = FALSE, recursive = TRUE)
  render <- function(open_device) {
    open_device()
    device_id <- grDevices::dev.cur()
    on.exit(grDevices::dev.off(device_id))
    draw()
  }
  width <- width_mm / 25.4
  height <- height_mm / 25.4
  render(function() grDevices::cairo_pdf(paste0(stem, ".pdf"), width = width,
         height = height, family = "Arial", pointsize = 8, fallback_resolution = 600))
  # R's Cairo device rounds the PDF page to integer points.
  script <- file.path(.paper_figure_dir, "pdf_page_size.py")
  status <- system2("python", c(shQuote(script), shQuote(paste0(stem, ".pdf")),
                               as.character(width_mm), as.character(height_mm)))
  if (status != 0) stop("Could not set the PDF artboard to the requested dimensions.")
  render(function() svglite::svglite(paste0(stem, ".svg"), width = width,
         height = height, pointsize = 8, system_fonts = list(sans = "Arial")))
  invisible(stem)
}

