"""
P18 神经网络-卷积层
知识点：
  - nn.Conv2d(in_channels, out_channels, kernel_size, stride=1, padding=0)
  - 输入形状 (N, C, H, W)，输出通道数 = out_channels
  - 配合 P14 的 CIFAR10（3通道彩色图）练最直观
"""
import torch
from torch import nn

# TODO: conv = nn.Conv2d(3, 6, kernel_size=3, stride=1, padding=0)
# TODO: 取 CIFAR10 的一张图，unsqueeze(0) 凑成 batch
# TODO: 输出 = conv(输入)，打印输入输出 shape，对照公式理解 H、W 的变化
# 输出尺寸公式：H_out = (H + 2*padding - kernel_size) // stride + 1
