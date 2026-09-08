"""
P27-P29 完整的模型训练套路
把前面学的串起来：
  1. 准备 CIFAR10 训练集 + DataLoader
  2. 实例化 P22 的 CifarNet
  3. 损失函数 CrossEntropyLoss + 优化器 SGD/Adam
  4. for epoch in range(轮数): for imgs, labels in loader:
         zero_grad -> 输出 = model(imgs) -> loss -> backward -> step
  5. 每轮打印 loss；选做：用 TensorBoard 画 loss 曲线
"""
# TODO: 完整写出来。卡住就回去看 P22/P23/P24 三个文件。
# 提示：先让 1 个 epoch 跑通，再加外层循环。
