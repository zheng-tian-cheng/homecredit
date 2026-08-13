# Home Credit Credit Risk Model Stability

这是一个双人协作的 Home Credit 项目：**GitHub 只负责代码与版本管理，Kaggle 负责读取大数据和运行训练任务**。

## 项目边界

- GitHub：Notebook、Python 源码、配置、文档和小型结果摘要
- Kaggle：Home Credit 原始数据、CPU/RAM/GPU、模型训练和大型中间产物
- 本地电脑：Git 操作、代码编辑和轻量检查；不要求下载或加载完整数据集

> 不要把 Kaggle 数据、模型文件、密钥或大型中间结果提交到本仓库。`.gitignore` 已覆盖常见格式。

## 目录结构

```text
.
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_baseline_lightgbm.ipynb
│   ├── 05_validation.ipynb
│   ├── 06_stability_analysis.ipynb
│   └── 07_final_model.ipynb
├── src/homecredit/
│   ├── paths.py
│   ├── preprocessing.py
│   ├── features.py
│   └── model.py
├── tests/
├── KAGGLE_SETUP.md
└── requirements.txt
```

## 在 Kaggle 中运行

1. 新建 Kaggle Notebook，添加比赛数据集 `home-credit-credit-risk-model-stability`。
2. 打开 Notebook 的 Internet（若比赛规则允许），克隆本仓库。
3. 把仓库加入 Python 路径，运行对应 Notebook 或导入 `src/homecredit` 中的函数。

完整命令见 [KAGGLE_SETUP.md](KAGGLE_SETUP.md)。代码默认从以下位置读取 Kaggle 数据：

```text
/kaggle/input/home-credit-credit-risk-model-stability
```

## 双人协作约定

仓库地址：<https://github.com/zheng-tian-cheng/homecredit>

仓库当前为 private。仓库所有者先在 GitHub 的 **Settings → Collaborators → Add people** 输入队友的 GitHub 用户名并发送邀请；队友接受后即可克隆和推送分支：

```bash
git clone https://github.com/zheng-tian-cheng/homecredit.git
cd homecredit
```

每个人从 `main` 创建自己的功能分支，例如：

```bash
git switch main
git pull
git switch -c feature/eda
```

完成一个小任务后提交并推送，再通过 Pull Request 合并：

```bash
git add notebooks/01_eda.ipynb src/homecredit/features.py
git commit -m "feat: add initial EDA"
git push -u origin feature/eda
```

建议避免两个人同时修改同一个 Notebook。可复用逻辑放进 `src/homecredit/`，Notebook 主要负责实验编排和结果展示，这样更容易审查和合并。

## 本地轻量检查

本地无需数据即可运行路径与导入测试：

```bash
python -m unittest discover -s tests
```
