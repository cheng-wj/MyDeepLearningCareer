# PyTorch 推进表 · 轻松版

> 取代 `国庆节PyTorch推进表.md`（v3，10 天 × 4h）作为**执行依据**。
> v3 文档保留不删，它的「C# ↔ PyTorch 对照表」「常见坑点」「备用命令清单」三节仍然有效、本表直接引用，不重复抄。
>
> **改动原因**：v3 按「10 天连续假期」排期，但 2026 年国庆实际只放 7 天（见下方日历纠错），且 v3 的 4h/天 强度在有工作的背景下基本不可能持续。

---

## 日历纠错（先看这条）

2026 年国庆放假安排（国办发明电〔2025〕7 号）：**10 月 1 日（周四）至 10 月 7 日（周三）放假调休，共 7 天；10 月 10 日（周六）上班。**

| 日期 | 星期 | v3 排的什么 | 实际 |
|---|---|---|---|
| 10-01 | 四 | Day 1 | 假期第 1 天 ✅ |
| 10-02 | 五 | Day 2 | 假期第 2 天 ✅ |
| 10-03 | 六 | Day 3 | 假期第 3 天 ✅ |
| 10-04 | 日 | Day 4 | 假期第 4 天 ✅ |
| 10-05 | 一 | Day 5 | 假期第 5 天 ✅ |
| 10-06 | 二 | Day 6 | 假期第 6 天 ✅ |
| 10-07 | 三 | Day 7 | 假期第 7 天 ✅ |
| 10-08 | 四 | Day 8 | **上班** ❌ |
| 10-09 | 五 | Day 9 | **上班** ❌ |
| 10-10 | 六 | Day 10 | **调休上班** ❌ |

v3 有 3 天（10-08 / 10-09 / 10-10）落在工作日，其中 10-10 还是法定调休上班日。这三天在 v3 里排的是 P27–P29 完整训练套路、P30–P31 GPU、P32 验证——**全是重头戏**。v3 的收尾验收（10 天 commit 齐、checkpoint 落地、29 项勾完）因此从一开始就不可能成立。

**本表的处理**：假期 7 天只排 **5 个学习日**（留 2 天全休），重头戏拆到节后按周慢慢做，不设硬性截止日。

---

## 轻松版的 5 条原则

1. **每天 1.5–2h，不是 4h。** 2h 是有状态时的上限，不是配额。1h 收工也算当天达标。
2. **5 个学习日 + 2 个完整休息日。** 休息日就是休息日，不排「轻量任务」，不留「有空看看」当尾巴。
3. **概念集快进。** P06 / P17 / P33 是概念和源码导览，1.5 倍速或直接看笔记，**不写代码、不算完成度**。
4. **不按集数硬切，按「能跑通什么」切。** 每天的交付物是一个能运行的东西，不是一堆集数。
5. **允许顺延，禁止回补。** 某天没做就空着，不在第二天加倍补。连续两天没做 → 直接降档（见文末），不是硬撑。

> 这条是照搬 Python 学习计划里已经验证过的原则 —— 那边正因为「跟不上就顺延、不硬凑」才没在中途崩掉。

---

## 环境已就绪（2026-10-01 实测，Day 1 的前置已解决）

**这台机器（`DESKTOP-GHMSTA8`）此前没有 PyTorch 环境**，仓库 README 写的「环境已完成」指的是别的机器。2026-10-01 重建，实测结果：

| 项 | 值 |
|---|---|
| Anaconda | `D:\anaconda`（conda 26.7.3，base Python 3.14） |
| `torch` 环境路径 | `E:\conda\envs\torch`（**不在 `D:\anaconda\envs` 下，也不在用户目录 `.conda\envs` 下**） |
| Python | 3.12.14 |
| PyTorch | **2.11.0+cu128** |
| torchvision / torchaudio | 0.26.0+cu128 / 2.11.0+cu128 |
| `torch.cuda.is_available()` | **True** |
| 显卡 | NVIDIA GeForce RTX 2060 SUPER（8GB，驱动 617.14） |
| GPU 实测 | 2000×2000 矩阵乘 ×50 = 0.23s，显存占用 40MB |

**日常怎么用**（开始菜单 → Anaconda Prompt）：
```
conda activate torch
cd E:\MyDeepLearningCareer
python pytorch学习\p04_dir_help.py
```

**不想开 conda 时用绝对路径**（等价，调试方便）：
```
E:\conda\envs\torch\python.exe pytorch学习\p04_dir_help.py
```

### 重装环境时踩过的三个坑（别再踩）

1. **清华源只有 CPU 版。** `pip install torch --index-url .../cu128 -i https://pypi.tuna.tsinghua.edu.cn/simple` 会装成 `2.14.1+cpu`，版本号看着正常但 `cuda.is_available()` 是 False。**`-i` 会顶掉 `--index-url`。**
2. **国内装 cu128 要用南大镜像**：`--index-url https://mirror.nju.edu.cn/pytorch/whl/cu128/`（实测 21.6 MB/s，2.8GB 用 89 秒；官方源慢十几倍）。
3. **阿里云那个路径不能用**：`https://mirrors.aliyun.com/pytorch-wheels/cu128/` 返回 200 但不是 pip 索引格式，pip 报 `No matching distribution`。

### 下一步（明天 10-02）

CIFAR10 **还没下载**（`data/` 下目前只有 MNIST）。Day 2 一开始先跑这句预下载，免得训练时被下载卡住：
```python
from torchvision.datasets import CIFAR10
CIFAR10(root="./data", train=True, download=True)
CIFAR10(root="./data", train=False, download=True)
```

---

## 假期 5 个学习日（10-01 ~ 10-07）

| Day | 日期 | 星期 | 主题 | 视频 | 产出文件 | 时长 |
|---|---|---|---|---|---|---|
| 1 | 10-01 | 四 | 环境自检 + 数据入口 | P04, P06*, P07 | `p04_dir_help.py`, `p07_dataset.py` | 2h |
| 2 | 10-02 | 五 | 数据管线跑通 | P08, P09, P10–P13, P14, P15 | `p08_tensorboard.py`, `p10_transforms.py`, `p14_torchvision_datasets.py`, `p15_dataloader.py` | 2h |
| — | 10-03 | 六 | **休息** | — | — | 0 |
| 3 | 10-04 | 日 | CNN 组件 | P16, P17*, P18–P21 | `p16_nn_module.py`, `p18_conv2d.py`, `p19_maxpool.py`, `p20_relu_sigmoid.py`, `p21_linear.py` | 2h |
| 4 | 10-05 | 一 | Sequential + 训练五步 | P22, P23, P24 | `p22_sequential_cifar.py`, `p23_loss_backward.py`, `p24_optimizer.py` | 2h |
| — | 10-06 | 二 | **休息** | — | — | 0 |
| 5 | 10-07 | 三 | 完整训练跑通 | P27, P28, P29 | `p27_train_cifar.py` | 2.5h |

> ✅ **Day 1 的环境部分已于 2026-10-01 20:35 完成**（下面「环境已就绪」一节）。Day 1 剩下的 P04 / P07 两集顺延到明天（10-02）开头，Day 2 内容整体后移一天，10-04 的 CNN 组件场次可自行决定是否压缩——**不必为了对齐日期硬赶**。

`*` = 概念集，快进即可，不计入完成度。

**Day 2 说明**：P10–P13 四集是「常见 transform 介绍」，**不用逐个学**。挑 `ToTensor` / `Resize` / `RandomCrop` / `Normalize` 四个写进 `p10_transforms.py` 即可，其余用到再回来查。Transforms 的真正用途是塞进 `p15_dataloader.py` 的 pipeline 里跑通一次。

**Day 3 说明**：`p19` / `p20` / `p21` 三个文件都很小（MaxPool / ReLU / Linear 各几行）。时间紧就合并成 `p18_p21_cnn_parts.py` 一个文件，README 进度清单按「同上文件」处理。

**Day 5 说明**：这是假期的收尾和唯一硬目标 —— 写完 `p27_train_cifar.py` 并**真的跑起来**，看 loss 在前 100 step 内有下降趋势。**不要求跑满 epoch，不要求准确率。**

---

## 节后轻量模式（10-08 起，每周 2 次 × 1h，不设硬日期）

10-08、10-09 是工作日，10-10 周六还要调休上班 —— 这三天**不排任何学习任务**。从 10-11（日）之后开始，每周挑 2 个晚上或周末，每次 1h，做不完下周接着做。

| 场次 | 内容 | 集 | 产出 | 时长 |
|---|---|---|---|---|
| E1 | GPU 训练（最省力的一集） | P30, P31 | `p30_gpu_train.py` | 1h |
| E2 | 保存加载 + 验证套路 | P26, P32 | `p32_evaluate.py` | 1.5h |
| E3 | 迁移学习 + 逛源码（**选做**） | P25, P33 | `p25_pretrained_models.py` | 1h |

**E1 是性价比最高的一场** —— 已经有 `p27_train_cifar.py` 了，`p30` 本质就是复制一份加 `.to(device)` 三件套加 `argparse`，不需要重新理解任何新概念。

**E3 可以永远不做。** P25（改预训练 vgg16 最后一层）对自己的 Halcon/CV 工作路线不是必须，P33（逛 torchvision / yolov5 源码）纯属兴趣。心情好就写 10 行笔记交差。

---

## 验收标准（降级版）

| 层级 | 标准 | 什么时候算到 |
|---|---|---|
| **及格** | CIFAR10 跑完 1 epoch，loss 有下降趋势 | 假期 Day 5 |
| 及格 + | 验证脚本能加载 checkpoint 算出 accuracy | 节后 E2 |
| **加分** | test acc > 10% | 随缘，不追 |
| 加分 + | 迁移学习 / GPU 训练都跑过 | 随缘，不追 |
| 不追 | 29 项全勾、10 天 commit 齐、复盘报告 | **已从计划中移除** |

> v3 的「10 天 git commit 齐」「README 29 项全部勾完」这类量化验收，是让人不想开始的典型来源。本表只验收「能跑通的东西」，不验收「完成的动作数」。

---

## 降档规则（比 fallback 更重要）

某天时间不够、状态差、或者卡住了，按这个顺序砍，**砍完就收工，当天结束**：

1. 先砍概念集（P06 / P17 / P33）—— 本来就快进，不心疼
2. 再砍 transforms 里不常用的那几个
3. 再砍 TensorBoard（P08 / P09，纯工具，不影响后面任何一集）
4. 绝对不砍 **Day 5 的训练跑通** —— 那是整个假期的意义所在
5. 如果连 Day 5 都做不完 → 直接把 P25–P33 整段推到节后，假期只求「数据管线 + 模型组件 + 训练五步」三块自己写过一遍

**连续两天没做**，不要问「怎么补偿」，直接问「这个计划是不是又排太满了」——如果是，就按上面砍，别硬撑。Python 计划就是这么暂停的，已经验证过这个模式。

---

## 每日自检（3 个问题，1 分钟）

- 今天的产出文件**跑起来了吗**？（不是「写完了吗」，是「跑了吗」）
- `git status` 干净吗？（本仓库 commit 自由，不强制每天提交）
- 今天是不是在做「能跑通的东西」，而不是在「看完集数」？

---

## 引用（内容在 v3 文档里，本表不重复）

- **C# ↔ PyTorch 对照表** → `国庆节PyTorch推进表.md` 第四节
- **常见坑点**（`num_workers` 在 Windows 报错、`zero_grad` 忘记、Compose 顺序写反…）→ 第五节
- **备用命令**（conda 激活、TensorBoard 启动、GPU 自检）→ 第六节
- **进度清单勾选** → `pytorch学习/README.md`（学完一集勾一集，勾不勾都不影响是否继续）
- **降级路径**（CUDA 不可用时换 MNIST）→ 本表 E1 场次说明

---

## 修订记录

### v2（2026-10-01 晚）— 环境实测落地，Day 1 前置完成

**起因**：本表 v1 写完后实测发现，这台机器**根本没有 PyTorch 环境**——仓库两处 README 声称的「conda 环境 torch 已完成 / PyTorch 2.11 + CUDA」不成立（描述的是别的机器）。Day 1 的「环境自检」不是例行公事，而是必须先解决的前置。

**实际动手做的事**：

1. 定位到 Anaconda 装在 `D:\anaconda`（目录名不是 `anaconda3`），conda 26.7.3 + base Python 3.14
2. `conda create -n torch python=3.12 -y` → 环境实际落在 `C:\Users\chengwenjie\.conda\envs\torch`，**不在 `D:\anaconda\envs` 下**（conda 新版默认行为）〔**此处路径记录有误，实际为 `E:\conda\envs\torch`，见文末 21:30 订正**〕
3. PyTorch 装**错两次**后修正：
   - 第一次混用 `--index-url cu128` + `-i 清华源`，`-i` 顶掉了 `--index-url`，装成 `2.14.1+cpu`（版本号正常但 CUDA 不可用）→ 卸载重来
   - 第二次用阿里云 `mirrors.aliyun.com/pytorch-wheels/cu128/`，返回 200 但非 pip 索引格式，`No matching distribution` → 换源
   - 第三次用南大镜像 `mirror.nju.edu.cn/pytorch/whl/cu128/`，成功，21.6 MB/s
4. 验收：`torch 2.11.0+cu128` / `torchvision 0.26.0+cu128` / `torchaudio 2.11.0+cu128`，`cuda.is_available() = True`，GPU 实测 2000×2000 矩阵乘 ×50 = 0.23s
5. 修正两处 README 的环境描述为实测值（仓库根 `README.md`、`pytorch学习/README.md`），补上真实路径与国内镜像安装命令
6. 本表新增「环境已就绪」一节（实测表 + 日常用法 + 三个踩坑点 + CIFAR10 未下载的提醒），Day 1 行加完成标注

**Day 1 状态**：环境部分 ✅ 完成（20:35），P04 / P07 两集顺延到 10-02 开头，Day 2 整体后移一天。**不强行对齐日期。**

### 轻松版（2026-10-01）— 取代 v3 作为执行依据

**起因**：用户要求「制定一个合理的也比较轻松的计划」。核查后发现 v3 有硬伤——按 10 天连续假期排期，但 2026 国庆实际只放 7 天，**10-08 / 10-09 是工作日、10-10 是调休上班日**，而 v3 恰好把「完整训练套路 + GPU + 验证 + 复盘」这四个最重的环节全排在这三天，加上 4h/天 的强度与工作冲突，验收目标（10 天 commit 齐、29 项勾完）从一开始就不成立。

**核心改动**：

1. **日历纠错**：放假按官方通知确认为 10-01 ~ 10-07 共 7 天，10-10 调休上班；v3 的 Day 8–10 作废
2. **强度减半**：4h/天 → 1.5–2h/天（Day 5 为 2.5h），并写明「2h 是上限不是配额」
3. **加休息日**：假期 7 天排 5 个学习日，10-03 / 10-06 全休且不留尾巴任务
4. **重头戏后移**：P26–P33（保存加载、完整训练套路、GPU、验证、迁移学习、源码）从假期移到节后「每周 2 次 × 1h」的轻量模式，不设硬截止日
5. **去掉量化验收**：「10 天 commit 齐」「29 项全勾」「复盘报告」改为不追；及格线降为「CIFAR10 跑完 1 epoch 且 loss 下降」
6. **概念集剥离**：P06 / P17 / P33 标为快进、不写代码、不计完成度
7. **transforms 选学**：P10–P13 不逐个学，只写 ToTensor / Resize / RandomCrop / Normalize 四个
8. **降档规则重写**：从 v3 的「每天必做 / 可砍」二分表，改成 5 级递进砍法 + 「连续两天没做就重排计划」的自检，删掉 v3 里「P30/P31 必须独立文件成 argparse 脚本」这类硬性形式要求
9. **文件合并授权**：时间紧时 `p19`/`p20`/`p21` 可合并为一个文件，README 按「同上文件」勾选
10. **新增前置检查**：Day 1 开头做 GPU 自检 + 提前触发 CIFAR10 下载（当前 `data/` 下只有 MNIST，CIFAR10 尚未下载），把「首次训练时卡在下载」的风险挪到假期第一天暴露

**未改动**：v3 文档本身保留不删（其 C# 对照表、坑点清单、命令清单三节仍被本表引用）；本仓库 README、进度清单、19 个骨架文件均未改动。

### 2026-10-01 21:30 — 环境路径订正（第三次不实描述修正）

**起因**：接入项目核对环境时实测发现，上面 v2 记录的 `torch` 环境路径**是错的**——`C:\Users\chengwenjie\.conda\envs\` 下只有一个 `.conda_envs_dir_test` 目录，没有 `torch` 环境。`conda env list` 显示实际位置是 **`E:\conda\envs\torch`**。

版本号全部属实，**只有路径错**：`torch 2.11.0+cu128` / `torchvision 0.26.0+cu128` / `torch.cuda.is_available() = True` / GPU `NVIDIA GeForce RTX 2060 SUPER` 均已复测通过。

**影响**：上一条 commit 声称「README 两处不实描述订正」，但订正后的路径仍不可用——按 README 复制命令会直接报 `CommandNotFoundException`。上一节「环境已就绪」里的三个路径引用（实测表、日常用法、备用命令）以及根 `README.md`、`pytorch学习/README.md` 里的同类描述，全部照抄了同一个错路径。

**已修**：上述 5 处路径统一改为 `E:\conda\envs\torch`。v2 记录保留原文并加订正标注，不抹掉历史。

**教训固化**：环境信息写「实测」之前要真的执行一次 `conda env list` 或直接调用 `python.exe` 验证，不能凭安装日志推断落盘位置——`conda create` 的实际落盘目录既不在 `D:\anaconda\envs` 也不在用户 `.conda\envs`，而是被 `envs_dirs` 配置指到了 `E:\conda\envs`。
