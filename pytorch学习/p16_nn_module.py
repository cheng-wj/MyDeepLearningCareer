"""
P16 神经网络的基本骨架 nn.Module
知识点：
  - 自定义网络 class MyNet(nn.Module)
  - __init__ 里先 super().__init__()，再定义层
  - forward(self, x) 里写数据怎么流过网络
  - 实例化后直接 model(x) 就会调用 forward
"""
import torch
from torch import nn

class MyNet(nn.Module):
    def __init__(self):
        super().__init__()
        # TODO: 随便定义几个层，比如 nn.Conv2d / nn.Linear

    def forward(self, x):
        # TODO: 写前向传播并 return 结果
        return x

# TODO: net = MyNet()；x = torch.ones((1, 3, 32, 32))；print(net(x).shape)
