# Kaggle 使用 GitHub 仓库

## 公开仓库

在 Kaggle Notebook 的第一个代码单元运行：

```python
!git clone https://github.com/zheng-tian-cheng/homecredit.git /kaggle/working/homecredit

import sys
sys.path.insert(0, "/kaggle/working/homecredit/src")
```

更新代码时运行：

```python
!git -C /kaggle/working/homecredit pull --ff-only
```

## 私有仓库

不要把 GitHub Token 直接写进 Notebook。先在 Kaggle 的 **Add-ons → Secrets** 新建名为 `GITHUB_TOKEN` 的密钥，然后运行：

```python
from kaggle_secrets import UserSecretsClient

token = UserSecretsClient().get_secret("GITHUB_TOKEN")
owner = "zheng-tian-cheng"
repo = "homecredit"
clone_url = f"https://x-access-token:{token}@github.com/{owner}/{repo}.git"

!git clone {clone_url} /kaggle/working/homecredit

import sys
sys.path.insert(0, "/kaggle/working/homecredit/src")

# 避免令牌留在仓库的 remote 配置中。
!git -C /kaggle/working/homecredit remote set-url origin https://github.com/{owner}/{repo}.git
```

密钥建议使用 GitHub fine-grained personal access token，只授予这个仓库的只读 Contents 权限。日常修改建议在 GitHub 或本地编辑器完成，经分支和 Pull Request 合并；Kaggle 主要用于执行。

## 数据路径

在 Kaggle 右侧面板添加比赛数据后：

```python
from homecredit.paths import get_data_root

DATA_ROOT = get_data_root()
print(DATA_ROOT)
```

也可以通过环境变量覆盖路径，用小样本做轻量测试：

```python
import os
os.environ["HOME_CREDIT_DATA_ROOT"] = "/path/to/small/sample"
```

## 保存结果

Kaggle 的可写目录是 `/kaggle/working`。大型模型与中间结果保留在 Kaggle Output/Dataset 中；GitHub 只提交指标表、图表或文字总结等小文件。
