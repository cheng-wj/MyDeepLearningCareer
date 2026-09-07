# MyDeepLearningCareer

我的深度学习学习仓库，从 PyTorch 基础开始，逐步走向 CV、目标检测和更复杂的项目。

## 环境

- conda 环境 `torch`（Python 3.12，PyTorch 2.11 + CUDA 12.8）
- 安装依赖：

```powershell
conda activate torch
pip install -r requirements.txt --index-url https://download.pytorch.org/whl/cu128
```

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
