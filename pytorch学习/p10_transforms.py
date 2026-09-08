"""
P10-P13 Transforms 的使用
知识点：
  - from torchvision import transforms
  - transforms.ToTensor()          PIL图片 / numpy数组 -> Tensor
  - transforms.Normalize(mean, std)  归一化（传入每个通道的均值标准差）
  - transforms.Resize((h, w))       缩放
  - transforms.RandomCrop(size)     随机裁剪（数据增强）
  - transforms.Compose([...])       把多个 transform 串成流水线
思路：transform 就是一个"函数"，把 PIL 图片传进去得到处理后的结果。
"""
from torchvision import transforms
from torchvision import datasets
from torch.utils.data import DataLoader

# TODO: 创建一条 Compose 流水线：Resize -> ToTensor（可以再加 Normalize）
# TODO: 用它处理一张 PIL 图片（或直接套在 CIFAR10 的 transform= 参数上）
# TODO: 打印处理前后的 type 和 shape，体会 ToTensor 做了什么
