# MyDeepLearningCareer

我的深度学习学习仓库，从 PyTorch 基础开始，逐步走向 CV、目标检测和更复杂的项目。

## 环境

- Anaconda 装在 `D:\anaconda`（conda 26.7.3，base 为 Python 3.14）
- conda 环境 `torch` 建在 `E:\conda\envs\torch`（Python 3.12.14）
- 实测版本：PyTorch 2.11.0+cu128 / torchvision 0.26.0+cu128 / torchaudio 2.11.0+cu128，`torch.cuda.is_available()` = **True**
- 显卡：NVIDIA GeForce RTX 2060 SUPER（8GB，驱动 617.14，CUDA 12.8）
- 重建环境：

```powershell
conda create -n torch python=3.12 -y
conda activate torch
# 国内下载 cu128 版用南京大学镜像（官方源在国内很慢；清华源只有 CPU 版，会装错）
pip install torch torchvision torchaudio --index-url https://mirror.nju.edu.cn/pytorch/whl/cu128/
```

> 激活环境后如果 `conda` 命令不认，直接用绝对路径调用：
> `E:\conda\envs\torch\python.exe xxx.py`

## 学习路线

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
