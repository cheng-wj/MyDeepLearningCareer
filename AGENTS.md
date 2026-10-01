# AGENTS.md

个人深度学习学习仓库：从 PyTorch 基础起步，逐步走向 CV、目标检测和自研项目。当前主线是跟练小土堆《PyTorch深度学习快速入门教程》（B 站 BV1hE411t7RN），用户有 C# / Halcon CV 开发背景，Python 与 PyTorch 是新领域。

## ⚠️ 最重要的一条：不要替用户写练习

`pytorch学习/pXX_*.py` 是**练习骨架**，只有知识点提示、API 关键词和 `# TODO`，实现必须由用户自己写。这是本仓库存在的根本原因（见 `pytorch学习/README.md`：实现自己写，不要抄视频代码）。

- 不要把这些 TODO 补全成完整实现
- 可以指出概念、API 签名、报错原因、官方文档链接
- 正确做法：解释思路、给最小片段示范、指出 traceback 的真实问题，然后把实现交回用户
- `01-pytorch-basics/` 的四课是已完成的参考实现，可以直接引用对照

## 环境

conda 环境 `torch` **实际路径 `E:\conda\envs\torch`**（Python 3.12.14 / PyTorch 2.11.0+cu128 / torchvision 0.26.0+cu128，`torch.cuda.is_available()` = True，RTX 2060 SUPER 8GB）。

```powershell
# 方式一：绝对路径（最稳，任何终端都能用）
E:\conda\envs\torch\python.exe pytorch学习\p04_dir_help.py

# 方式二：conda 激活
conda activate torch
cd E:\MyDeepLearningCareer
python pytorch学习\p04_dir_help.py
```

装依赖：`pip install -r requirements.txt --index-url https://mirror.nju.edu.cn/pytorch/whl/cu128/`
国内装 cu128 版只用南大镜像；**不要混用 `-i` 清华源**，它会顶掉 `--index-url` 并装成 CPU 版（版本号看着正常但 CUDA 不可用）。

## 项目结构

- `01-pytorch-basics/` — 已完成的四课：张量、autograd、MLP 双月、MNIST CNN
- `pytorch学习/` — 小土堆教程跟练骨架（`p04` … `p32`）+ 进度清单 + 两份推进表
- `data/` `checkpoints/` `outputs/` `logs/` — 运行产物，已 gitignore，不入库
- `requirements.txt` / `README.md` / `.gitignore`

## 执行依据

`pytorch学习/PyTorch推进表_轻松版.md` 是**当前唯一执行依据**（取代 v3 的 `国庆节PyTorch推进表.md`，但 v3 的 C# ↔ PyTorch 对照表、常见坑点、备用命令三节仍被引用，勿删）。修订记录写在该文档末尾。

节奏原则：1.5–2h/天是上限不是配额；允许顺延、禁止回补；只验收「能跑通的东西」，不验收完成的动作数。

## 代码风格

- 注释和文档字符串用中文，把知识点写清楚，不只是描述代码在做什么
- 每个脚本都能独立 `python xxx.py` 直接跑，不依赖其他脚本的 import
- 打印关键指标（loss、accuracy、显存），让"跑通了"是可验证的
- 数据集 `root="./data"` 相对仓库根目录；权重进 `checkpoints/`，日志进 `logs/`
- 无测试框架、无 lint 配置、无 CI —— 验证方式就是**把脚本跑起来看输出**

## 提交约定

- 默认分支 `main`，本仓库 commit 自由，**不强制每天提交**（推进表明确写了不要用"commit 齐不齐"当验收）
- 历史 commit message 用中文，格式如 `2026年10月1日-21点24分：PyTorch 推进表轻松版 + 环境实测落地`
- 未经用户要求不要自行 commit 或 push

## 文档一致性

README 和推进表里的环境信息**曾经两次写成不实内容**，改环境后必须同步订正这三处：
根 `README.md`、`pytorch学习/README.md`、`pytorch学习/PyTorch推进表_轻松版.md`。写"实测"之前先真的跑一遍验证。

## 工作流约定

- **练习/任务完成 → 主动同步推进表顶部 callout，不用每次问**（2026-10-02 定）。
  适用范围：本仓库所有 `pXX_*.py` 跟练完成时。callout 位置：[PyTorch推进表_轻松版.md](pytorch学习/PyTorch推进表_轻松版.md) 标题下、原「取代 v3」说明之前。
  原口径「完成 → 问要不要更新 → 等确认 → 改」改为「完成 → 直接改 callout + 汇报」。
  起因：用户原话「我弄完了你应该主动更新进度」。
