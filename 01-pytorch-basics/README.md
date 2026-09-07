# 01. PyTorch 基础

按顺序运行，每个脚本头部的注释里写了这一课要掌握的知识点。

| 脚本 | 内容 | 核心知识点 |
| --- | --- | --- |
| `01_tensor_basics.py` | 张量基础 | shape/dtype/device、运算、索引、广播、GPU 搬运 |
| `02_autograd.py` | 自动求导 | requires_grad、backward、.grad、手写训练循环 |
| `03_mlp_moons.py` | 双月分类 | nn.Module、DataLoader、完整训练循环、模型存取 |
| `04_cnn_mnist.py` | 手写数字识别 | Conv2d/MaxPool、torchvision 数据集、CrossEntropyLoss、Dropout |

运行方式（在仓库根目录或本目录下均可）：

```powershell
conda activate torch
python 01-pytorch-basics/01_tensor_basics.py
python 01-pytorch-basics/02_autograd.py
python 01-pytorch-basics/03_mlp_moons.py
python 01-pytorch-basics/04_cnn_mnist.py
```

数据集、权重、图片分别输出到仓库根目录的 `data/`、`checkpoints/`、`outputs/`。
