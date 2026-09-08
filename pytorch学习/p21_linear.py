"""
P21 神经网络-线性层及其他层
知识点：
  - nn.Linear(in_features, out_features)
  - 卷积/池化后的特征图要先"拉平"再进全连接层：
      torch.flatten(x, start_dim=1)  或  x.reshape(x.size(0), -1)
练习：把 CIFAR10 一张图 (3,32,32) 拉平成 3072，过 Linear(3072, 10)。
"""
import torch
from torch import nn

# TODO: x = torch.ones((64, 3, 32, 32))   # 模拟一批 CIFAR 图片
# TODO: flat = torch.flatten(x, start_dim=1)，打印 shape
# TODO: linear = nn.Linear(3*32*32, 10)，打印 linear(flat).shape
