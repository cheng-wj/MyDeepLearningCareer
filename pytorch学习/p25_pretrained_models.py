"""
P25 现有网络模型的使用及修改（迁移学习入门）
知识点：
  - import torchvision
  - vgg16 = torchvision.models.vgg16(weights=None)          # 随机初始化
  - vgg16_true = torchvision.models.vgg16(weights="DEFAULT") # 预训练权重
  - 修改网络：vgg16.classifier.add_module("add_linear", nn.Linear(1000, 10))
              vgg16.classifier[6] = nn.Linear(4096, 10)
"""
import torchvision
from torch import nn

# TODO: 加载 vgg16(weights=None)，print(vgg16) 看它的结构
# TODO: 用 add_module 给 classifier 末尾加一层输出 10 类
# TODO: 再把 classifier 第 6 层替换成 nn.Linear(4096, 10)
