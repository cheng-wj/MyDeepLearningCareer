"""
P20 神经网络-非线性激活
知识点：
  - nn.ReLU(inplace=False)：负数变 0，正数不变
  - nn.Sigmoid()：压到 (0,1)
  - 非线性激活让网络能学复杂的非线性关系
练习：对有正有负的张量分别过 ReLU 和 Sigmoid，打印结果。
"""
import torch
from torch import nn

# TODO: x = torch.tensor([-2., -1., 0., 1., 2.]).reshape(1,1,1,-1)
# TODO: 分别用 nn.ReLU() 和 nn.Sigmoid() 处理并打印
