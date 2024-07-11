# 深圳中考

## 开发环境

### Install

- 安装 nbdev 及其依赖包
  ```bash
  pip install notebook nbdev
  pip install pandas numpy
  pip install matplotlib plotly pyecharts
  ```
- 安装 [quarto](https://quarto.org/docs/get-started/)
- 安装 quarto VSCode 扩展

### 提取深圳中考招生计划中的人数 Data

- 使用 firefox 打开 pdf 进行 copy 最佳
  - chrome 复制后向 excel 粘贴时会被放在一个 cell 中
  - Ubuntu 的 pdf 阅读器换行处理不好
- 从 `附件1 招生学校计划及代码表` 中提取
  - 学校的信息：新增、更名……
  - AC、D 类人数
- 从 `附件2 深圳市20xx年公办普通高中指标生招生计划表` 中提取指标生的数据
- 数据提取到 Excel 中进行整理
  - 将 （一）、（二）拆分的数据整理成 2 列

### Debug

- 使用 VSCode 中 qmd 文件中每个代码段会有 `Run Cell` 按钮(`Ctrl-Shift-Enter`，我已修改为 F4)
- `nbdev_preview`

### release & publish

参考 .github/workflows/
