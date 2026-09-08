"""
P08/P09 TensorBoard 的使用
知识点：
  - from torch.utils.tensorboard import SummaryWriter
  - writer = SummaryWriter("logs")
  - writer.add_scalar("标题", 数值y, 步数x)      画曲线
  - writer.add_image("标题", 图片, 步数, dataformats="HWC")  画图片
  - writer.close()
查看：终端运行  tensorboard --logdir=logs  然后浏览器打开提示的地址
注意：add_scalar 标题相同但 x/y 对不上时曲线会乱，换标题或清空 logs 文件夹
"""
from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image

# TODO: 写 writer，用 for 循环画 y = x 和 y = 2x 两条 add_scalar 曲线
# TODO（选做）：用 add_image 显示一张图片（numpy 数组，注意 dataformats="HWC"）
# 记得 writer.close()
