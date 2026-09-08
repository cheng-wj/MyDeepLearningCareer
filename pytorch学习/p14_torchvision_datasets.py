"""
P14 torchvision 中的数据集使用
知识点：
  - datasets.CIFAR10(root="data", train=True/False, download=True, transform=...)
  - 数据集对象可以用索引取样本：img, label = dataset[0]
  - 数据集自带 .classes 类别名
练习：下载 CIFAR10（10类彩色小图），取几个样本看看。
"""
from torchvision import datasets, transforms

# TODO: 定义 transform（ToTensor）
# TODO: train_set = datasets.CIFAR10(root=..., train=True, download=True, transform=...)
# TODO: 打印 len(train_set)、train_set.classes
# TODO: 取 img, label = train_set[0]，打印 img.shape 和 label
