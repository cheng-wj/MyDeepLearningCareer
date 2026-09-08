"""
P22 搭建小实战：Sequential 的使用
任务：给 CIFAR10（3通道 32x32）搭一个完整的小卷积网络，
     用 nn.Sequential 把层按顺序装起来。
参考结构（自己写，写完对照）：
  Conv2d(3, 32, 5, padding=2) -> ReLU -> MaxPool2d(2)   # 32 -> 16
  Conv2d(32, 32, 5, padding=2) -> ReLU -> MaxPool2d(2)  # 16 -> 8
  Conv2d(32, 64, 5, padding=2) -> ReLU -> MaxPool2d(2)  # 8 -> 4
  Flatten -> Linear(64*4*4, 64) -> Linear(64, 10)
验证：喂一个 (1,3,32,32) 的张量，输出 shape 应该是 (1, 10)。
"""
import torch
from torch import nn

class CifarNet(nn.Module):
    def __init__(self):
        super().__init__()
        # TODO: 用 nn.Sequential 搭完整网络

    def forward(self, x):
        # TODO
        return x

# TODO: 实例化，输入 torch.ones((1,3,32,32))，打印输出 shape
