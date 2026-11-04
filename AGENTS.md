# AGENTS.md

个人深度学习学习仓库：从 PyTorch 基础起步，逐步走向 CV、目标检测和自研项目。当前主线是跟练小土堆《PyTorch深度学习快速入门教程》（B 站 BV1hE411t7RN），用户有 C# / Halcon CV 开发背景，Python 与 PyTorch 是新领域。

## ⚠️ 最重要的一条：不要替用户写练习

`pytorch学习/pXX_*.py` 是**练习骨架**，只有知识点提示、API 关键词和 `# TODO`，实现必须由用户自己写。这是本仓库存在的根本原因（见 `pytorch学习/README.md`：实现自己写，不要抄视频代码）。

- 不要把这些 TODO 补全成完整实现
- 可以指出概念、API 签名、报错原因、官方文档链接
- 正确做法：解释思路、给最小片段示范、指出 traceback 的真实问题，然后把实现交回用户
- `01-pytorch-basics/` 的四课是已完成的参考实现，可以直接引用对照

## 环境

**两台机都能跑本仓库，路径和版本全不一样 —— 动手前先 `hostname` 认机器，别抄错解释器路径。**

| 项 | 个人机 `DESKTOP-GHMSTA8` | 公司机 `DESKTOP-R4RRO1S` |
|---|---|---|
| 仓库路径 | `E:\MyDeepLearningCareer` | `D:\个人文件\我的仓库\MyDeepLearningCareer` |
| **解释器** | `E:\conda\envs\torch\python.exe` | `D:\anaconda3\envs\torch\python.exe` |
| conda 根 | `D:\anaconda`（conda 26.7.3） | `D:\anaconda3`（conda 24.5.0） |
| Python | 3.12.14 | 3.11.16 |
| PyTorch / torchvision | 2.11.0+cu128 / 0.26.0+cu128 | 2.14.0+cu126 / 0.29.0+cu126 |
| GPU | RTX 2060 SUPER（8GB），驱动 617.14 | RTX 2060（6GB），驱动 591.74 |
| 显卡架构 | Turing sm_61 | Turing sm_61（一致，代码通用） |
| `torch.cuda.is_available()` | True | True（2026-11-02 实测 GPU matmul 通过） |
| `data/` | MNIST + CIFAR10 已就绪 | **空，要重新下载** |

```powershell
# 方式一：绝对路径（最稳，任何终端都能用）—— 换机器就换这一行
E:\conda\envs\torch\python.exe pytorch学习\p04_dir_help.py          # 个人机
D:\anaconda3\envs\torch\python.exe pytorch学习\p04_dir_help.py       # 公司机

# 方式二：conda 激活
conda activate torch
python pytorch学习\p04_dir_help.py
```

装依赖：`pip install -r requirements.txt --index-url https://mirror.nju.edu.cn/pytorch/whl/cu128/`（公司机按 cu126 换 URL）
国内装 GPU 版只用南大镜像；**不要混用 `-i` 清华源**，它会顶掉 `--index-url` 并装成 CPU 版（版本号看着正常但 CUDA 不可用）。

> 完整双机对照表在 [PyTorch推进表_半月制.md](pytorch学习/PyTorch推进表_半月制.md) 第八节（含实测日期与踩坑指向）。

## 项目结构

- `01-pytorch-basics/` — 已完成的四课：张量、autograd、MLP 双月、MNIST CNN
- `pytorch学习/` — 小土堆教程跟练骨架（`p04` … `p32`）+ 进度清单 + 推进表（当前执行依据 `PyTorch推进表_半月制.md`；更早的三份旧表存档）
- `Python基础/` — Python 语法阶段（2026-11-04 起，先于 PyTorch 主线）：`Python学习计划-7天.md` + 关卡骨架 `d1`–`d7` + `numpy与Tensor对照.md`
- `data/` `checkpoints/` `outputs/` `logs/` — 运行产物，已 gitignore，不入库
- `requirements.txt` / `README.md` / `.gitignore`

## 执行依据

`pytorch学习/PyTorch推进表_半月制.md` 是**当前唯一执行依据**（2026-10-28 取代 `PyTorch推进表_场次制.md`；场次制表及更早的 `PyTorch推进表_轻松版.md`、v3 `国庆节PyTorch推进表.md` 保留不删、不再改动，其环境实测、踩坑记录、C# ↔ PyTorch 对照表、常见坑点、备用命令仍被引用）。修订记录写在该文档末尾。

**当前阶段（2026-11-04 起）**：第九节「Python 前置阶段」**先于** S1 —— 用户看 P07 视频后判断 Python 语法不过关，改走 `Python基础/Python学习计划-7天.md`（小甲鱼 86 集选看，7 天约 14h）。Python 毕业线达成后才回 S1，PyTorch 主线整体顺延。**不要在 Python 阶段催他写 P07**。

`Python基础/d1`–`d7` 同样是**练习骨架** —— 只写知识点提示和 TODO，实现必须用户自己写（与 `pXX_*.py` 同规矩，勿代笔）。

节奏原则（2026-10-28 按真实工作作息定）：每周 4 场 —— **工作日晚 2h × 最多 2 场 + 周末晚 3.5h × 2 场**；单场时长是上限不是配额，到点就收；允许顺延、禁止回补；只验收「能跑通的东西」，不验收完成的动作数。每场含「开场 15 分钟跑上一场脚本」与「15 分钟保底动作」，防链条断掉。

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
根 `README.md`、`pytorch学习/README.md`、`pytorch学习/PyTorch推进表_半月制.md`（第八节环境速查 = **双机对照表，个人机 / 公司机各一列**，2026-11-02 起）。
写"实测"之前先真的跑一遍验证；`PyTorch推进表_场次制.md` 已退役、保留不删不再改动，里面的单机口径以半月制表第八节为准。
**改环境的口径**：两台机都要能直接用 → 写成对照表，不要用一机的值覆盖另一机；用户在哪台机跑，就对照哪一列。

## 工作流约定

- **练习/任务完成 → 主动同步推进表顶部 callout，不用每次问**（2026-10-02 定）。
  适用范围：本仓库所有 `pXX_*.py` **和 `Python基础/d1`–`d7`** 跟练完成时。callout 位置：[PyTorch推进表_半月制.md](pytorch学习/PyTorch推进表_半月制.md) 标题下、取代说明之前。
  原口径「完成 → 问要不要更新 → 等确认 → 改」改为「完成 → 直接改 callout + 汇报」。
  起因：用户原话「我弄完了你应该主动更新进度」。
  顺延说明：档期过了还没做的场次，callout 里写「下一场仍是 Sx + 顺延不回补」，**不写成已做**。
