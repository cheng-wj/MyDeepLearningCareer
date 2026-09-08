"""
P23 损失函数与反向传播
知识点：
  - 分类常用 nn.CrossEntropyLoss()（输入是未过 softmax 的 logits）
  - 回归常用 nn.MSELoss() / nn.L1Loss()
  - 算完 loss 后调用 loss.backward() 反向传播，梯度进 .grad
练习：造 1 张图的 logits（shape (1,10)）和真实标签，算交叉熵损失。
"""
import torch
from torch import nn

# TODO: logits = torch.tensor([[...10个分数...]], dtype=torch.float32)
# TODO: target = torch.tensor([3])          # 真实类别
# TODO: loss_fn = nn.CrossEntropyLoss()
# TODO: loss = loss_fn(logits, target)；print(loss)
# TODO: loss.backward()，看网络参数的 .grad
