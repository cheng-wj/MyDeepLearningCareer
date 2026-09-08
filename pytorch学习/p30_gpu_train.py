"""
P30-P31 利用 GPU 训练
两种写法（你的 RTX 2060 SUPER + torch 环境都已就绪）：
  写法一：.cuda()
     model = model.cuda();  loss_fn = loss_fn.cuda()
     imgs = imgs.cuda();    labels = labels.cuda()
  写法二（推荐）：device 对象
     device = torch.device("cuda")
     model = model.to(device); loss_fn = loss_fn.to(device)
     imgs = imgs.to(device); labels = labels.to(device)
关键：模型、损失函数、数据 三者必须都在同一张卡上。
验证：print(torch.cuda.is_available()) 应为 True。
"""
import torch

# TODO: 在 P27 训练代码基础上加 device，让整个训练跑在 GPU 上
# TODO: 可以观察任务管理器 GPU 占用，或用 torch.cuda.is_available() 确认
