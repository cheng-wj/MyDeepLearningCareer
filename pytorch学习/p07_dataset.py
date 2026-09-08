"""
P07 Dataset 类代码实战
知识点：
  - 继承 torch.utils.data.Dataset，必须实现 __init__ / __len__ / __getitem__ 三个方法
  - __getitem__(self, index) 返回 (数据, 标签)
  - 常用搭配：os / pathlib 拼路径，PIL.Image.open 读图
提示：课程里用的是 ants/bees 图片文件夹；你也可以先跳过图片数据，
     P14 用 torchvision 自带的 CIFAR10 更省事，这个文件等手头有图片再练。
"""
from torch.utils.data import Dataset

# TODO: 写一个 MyDataset(Dataset)
#   __init__: 保存数据路径/列表
#   __len__ : 返回样本总数
#   __getitem__: 根据 index 返回 (图片, 标签)

# TODO: 实例化，用 len() 和 obj[0] 验证
