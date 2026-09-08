"""
P32 完整的模型验证（测试）套路
知识点：
  - 准备测试集 CIFAR10(train=False) + DataLoader
  - model.eval() + with torch.no_grad():  测试时不算梯度，省内存
  - outputs.argmax(1) 得到每张图的预测类别
  - 统计：总正确数 / 总样本数 = 准确率
练习：加载 P30 训练好的权重，在测试集上算准确率。
"""
import torch

# TODO: 加载模型和权重；model.eval()
# TODO: with torch.no_grad(): 遍历测试集，累计 correct 和 total
# TODO: print(f"准确率: {correct/total:.2%}")
