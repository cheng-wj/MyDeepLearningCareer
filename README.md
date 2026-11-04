# MyDeepLearningCareer

我的深度学习学习仓库，从 PyTorch 基础开始，逐步走向 CV、目标检测和更复杂的项目。

## 环境（双机对照）

两台机都能跑本仓库，**版本和路径都不一样** —— 开工前先对一眼自己这台机的解释器路径，别把个人机的路径带到公司机上。

| 项 | 个人机 `DESKTOP-GHMSTA8` | 公司机 `DESKTOP-R4RRO1S` |
|---|---|---|
| 仓库路径 | `E:\MyDeepLearningCareer` | `D:\个人文件\我的仓库\MyDeepLearningCareer` |
| conda 根 | `D:\anaconda`（conda 26.7.3，base Python 3.14） | `D:\anaconda3`（conda 24.5.0，base Python 3.12.4） |
| **解释器（最稳）** | `E:\conda\envs\torch\python.exe` | `D:\anaconda3\envs\torch\python.exe` |
| Python | 3.12.14 | 3.11.16 |
| PyTorch | 2.11.0+cu128 | 2.14.0+cu126 |
| torchvision | 0.26.0+cu128 | 0.29.0+cu126 |
| torchaudio | 2.11.0+cu128 | 未装（本项目用不到） |
| 显卡 | NVIDIA RTX 2060 SUPER（8GB） | NVIDIA RTX 2060（6GB） |
| 显卡架构 | Turing sm_61 | Turing sm_61 —— **一致，代码通用** |
| 驱动 / 驱动支持 CUDA | 617.14 / 12.8 | 591.74 / 13.1 |
| torch 内置 CUDA | cu128 | cu126（cudnn 91002） |
| `torch.cuda.is_available()` | True | True（2026-11-02 实测 GPU matmul 通过） |
| 数据集 `data/` | MNIST + CIFAR10 已就绪 | **空，需重新下载** |

> 个人机列实测于 2026-10-01；公司机列实测于 2026-11-02（脚本链路 `p04` 跑通、CUDA 端到端 matmul 通过、`torch.cuda.is_available()` = True）。
> 公司机只有 C、D 两个盘，没有 E 盘；`F:\我的知识库` 所在的外接硬盘盒未挂载时，记忆库取不到。

### 重建环境

```powershell
# 个人机（cu128）
conda create -n torch python=3.12 -y
conda activate torch
# 国内下载 cu128 版用南京大学镜像（官方源在国内很慢；清华源只有 CPU 版，会装错）
pip install torch torchvision torchaudio --index-url https://mirror.nju.edu.cn/pytorch/whl/cu128/

# 公司机（cu126，公司机上的 torch 环境原本是 2.14.0+cu126 / 0.29.0+cu126）
conda create -n torch python=3.11 -y
conda activate torch
pip install torch torchvision --index-url https://mirror.nju.edu.cn/pytorch/whl/cu126/
```

> 激活环境后如果 `conda` 命令不认，直接用绝对路径调用：
> - 个人机：`E:\conda\envs\torch\python.exe xxx.py`
> - 公司机：`D:\anaconda3\envs\torch\python.exe xxx.py`
>
> 国内装 GPU 版只用南大镜像；**不要混用 `-i` 清华源**（会顶掉 `--index-url`，装成 CPU 版）。

## 学习路线

> 当前进度与推进安排见 `pytorch学习/PyTorch推进表_半月制.md`（2026-10-28 起为唯一执行依据）。
> **当前阶段：Python 基础 7 天**（2026-11-04 起）→ 计划 `Python基础/Python学习计划-7天.md`，关卡骨架 `Python基础/d1`–`d7`，语法卡壳查 `Python基础/numpy与Tensor对照.md`。
> **换工作区 / 换会话时先读 `交接说明.md`** —— 里面有当前状态、下一步和这台机的所有坑。
> 毕业线达成后回 PyTorch 主线 **S1**（P06 快进 + P07 Dataset + P14 torchvision 数据集）。
> （10-28 起的 S1–S4 档期已过且未执行，按「允许顺延、禁止回补」依次往后排。）

- [ ] **00. Python 语法基础**（`Python基础/`，2026-11-04 起，先于 PyTorch）
  - [ ] D1 程序与数据类型 → `d1_公差判定.py`
  - [ ] D2 分支循环 + 列表 → `d2_列表与切片.py`
  - [ ] D3 字符串 + 字典 → `d3_字典与表格.py`
  - [ ] D4 函数（默认参数 / `*args` / `**kwargs`）→ `d4_函数.py`
  - [ ] D5 类与对象 · 上（继承 / `self` / `super()`）→ `d5_类与对象.py`
  - [ ] D6 类与对象 · 下（`__getitem__` / `__call__`）+ 模块异常 → `d6_模块与异常.py`
  - [ ] D7 毕业考（5 题）→ `d7_毕业考.py`
- [x] **01. PyTorch 基础**（`01-pytorch-basics/`）
  - [x] 01 张量基础：创建、形状、GPU、广播
  - [x] 02 自动求导：autograd 与手写训练循环
  - [x] 03 MLP 双月分类：第一个完整训练流程
  - [x] 04 CNN 手写数字识别：MNIST + 卷积网络
- [ ] **02. 计算机视觉进阶**：CIFAR-10、数据增强、迁移学习
- [ ] **03. 目标检测**：YOLO / ultralytics 实战
- [ ] **04. 自己的项目**：选题待定

## 约定

- 每个脚本都可以直接 `python xxx.py` 运行，注释里写清知识点
- 数据集放在 `data/`、模型权重放在 `checkpoints/`、图片放在 `outputs/`，均不入库
