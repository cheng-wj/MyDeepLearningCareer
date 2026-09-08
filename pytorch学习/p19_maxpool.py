"""
P19 神经网络-最大池化
知识点：
  - nn.MaxPool2d(kernel_size, ceil_mode=False)
  - 池化不改变通道数，让特征图变小、保留主要特征
  - ceil_mode=True 时边缘不够一个窗口也保留
练习：对一个张量（或卷积结果）做池化，看 shape 变化。
注意：MaxPool 输入要求 float 类型。
"""
import torch
from torch import nn

# TODO: x = torch.tensor([...], dtype=torch.float32).reshape(1,1,5,5)
# TODO: pool = nn.MaxPool2d(kernel_size=2, ceil_mode=False)
# TODO: 对比 ceil_mode True/False 时输出 shape 的区别
