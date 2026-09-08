"""
P15 DataLoader 的使用
知识点：
  - DataLoader(dataset, batch_size, shuffle, num_workers, drop_last)
  - batch_size：一次取几张；shuffle：是否打乱；drop_last：凑不齐一批时丢不丢
  - 迭代 DataLoader 拿到的是 (一批图片, 一批标签)，shape 多一个 batch 维
练习：把 P14 的 CIFAR10 套上 DataLoader，打印第一批数据的 shape。
"""
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

# TODO: 拿到 CIFAR10 数据集
# TODO: loader = DataLoader(train_set, batch_size=64, shuffle=True)
# TODO: for imgs, labels in loader: 打印 imgs.shape, labels.shape，break
# 选做：配合 p08 的 TensorBoard，用 writer.add_images 把一批图画进去
