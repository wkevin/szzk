# 深圳中考

## 数据提取

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

## 开发环境

- quarto：把 .qmd（markdown 扩展格式）文件渲染成 html，并运行其中的代码段。
  - 相关文件：nbs/\_quarto.yml
- nbdev：基于 .ipynb 或 .qmd 文件生成 python lib，其中处理 .qmd 文件会使用 quarto，即：Quarto 是 nbdev 的渲染与发布引擎。
  - 相关文件：settings.ini，setup.py，MANIFEST.in, nbs/nbdev.yml
  - settings.ini:
    - lib_path：存放 python lib 的文件夹
    - nbs_path: 存放 noteboo（ .ipynb, .qmd）的文件夹
    - doc_path：存放生成的 html 的文件夹
  - nbdev 可自动生成 \_quarto.yml，让 Quarto 的项目配置与 settings.ini 保持同步

### 新建项目

```
pip install nbdev
nbdev_install_quarto            # 安装 Quarto
nbdev_new                       # 初始化项目
nbdev_install_hooks             # 设置 hook，清理 metadata
```

### 从源码恢复项目

- `pip install nbdev` & `pip install -e .` 利用 setup.py 安装项目及其依赖包

或

- 手工安装 nbdev 及其依赖包
  ```bash
  pip install notebook nbdev
  pip install pandas numpy
  pip install matplotlib plotly pyecharts
  ```

然后安装 quarto：

```
nbdev_install_quarto
```

或 [quarto](https://quarto.org/docs/get-started/)

### 撰写、预览文档

- 编辑 notebooks（.ipynb, .qmd）了，文件中可插入 nbdev 指令。
- 预览文档：
  - `nbdev_preview`
  - 安装 quarto VSCode 扩展 —— qmd 文件中每个代码段会有 `Run Cell` 按钮(`Ctrl-Shift-Enter`

### 生成文档

```
nbdev_preview          # 使用 Quarto 实时预览文档
nbdev_docs             # 生成 Quarto 文档站点，到 doc_path 指定路径中
```

### 生成 python lib

```
nbdev_export     # Notebook → Python 模块
nbdev_release    # 导出模块并发布
```

### release & publish

参考 .github/workflows/
