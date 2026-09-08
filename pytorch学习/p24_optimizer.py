"""
P24 优化器
知识点：
  - torch.optim.SGD(model.parameters(), lr=0.01)
  - torch.optim.Adam(model.parameters(), lr=1e-3)
  - 训练一步三件事：optimizer.zero_grad() -> loss.backward() -> optimizer.step()
练习：拿 P22 的 CifarNet 和 P15 的 DataLoader，写 1 个 batch 的更新，
     打印更新前后某个参数的变化。
完整训练循环在 P27-P29 再写。
"""
import torch

# TODO: 准备 model、loss_fn、optimizer
# TODO: 取一批数据 imgs, labels
# TODO: zero_grad -> forward 算 loss -> backward -> step
