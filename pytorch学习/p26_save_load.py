"""
P26 网络模型的保存与读取
两种方式：
  方式一（推荐）：只存参数
    torch.save(model.state_dict(), "xxx.pt")
    model.load_state_dict(torch.load("xxx.pt"))
  方式二：存整个模型（要求加载处能 import 到模型类）
    torch.save(model, "xxx_full.pt")
    model = torch.load("xxx_full.pt")
"""
import torch

# TODO: 用 P25 的 vgg16 或 P22 的 CifarNet 分别试两种保存/读取
# 权重存到仓库根目录的 checkpoints/ 文件夹（已 gitignore）
