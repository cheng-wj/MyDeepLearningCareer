"""
D7 · 毕业考（45 分钟，空文件，不查资料）

规则：
  - 5 题全过 → Python 阶段关闭，进 PyTorch（回到小土堆 P07 Dataset 续上）
  - 任一题不过 → 只补那一天的内容，不要从头重学
  - 先写再跑：每题都先在纸上/注释里写出预期结果，再运行验证

题目：
  1. 读一段 20 行的 nn.Module 代码，逐行口述它的作用
     （代码见下方 NN_MODULE_SNIPPET，先别运行，通读后写说明）
  2. 写 Calibrator：__init__(self, coef) + apply(self, x)，3 个实例放进 list 并循环调用
  3. 写 fit(points, *, degree=2, save=None)，并说明 * 与 **kwargs 的区别
  4. 用字典推导 + zip 把两组测量数据配对，输出残差最大的序号
  5. 给 4 个 numpy 数组，先写出广播后的 shape 再运行验证，全对

验收标准：
  - 每一题都能说清「为什么这么写」，不是「跑出来了」
  - 第 1 题要能答出：self 是什么、super().__init__() 为什么必须有、
    forward 是什么、model(x) 为什么会走到 forward
"""

NN_MODULE_SNIPPET = '''
import torch.nn as nn
import torch.nn.functional as F

class TinyNet(nn.Module):
    def __init__(self, in_dim=10, hidden=32, out_dim=2, dropout=0.1):
        super().__init__()
        self.fc1 = nn.Linear(in_dim, hidden)
        self.fc2 = nn.Linear(hidden, out_dim)
        self.drop = nn.Dropout(dropout)
        self.act = nn.ReLU()

    def forward(self, x):
        x = self.act(self.fc1(x))
        x = self.drop(x)
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)
'''

# TODO: 第 1 题 —— 逐行解释上面的代码（写成注释或字符串都行）


# TODO: 第 2 题 —— Calibrator 类


# TODO: 第 3 题 —— fit 函数 + 解释 * 与 **kwargs 的区别


# TODO: 第 4 题 —— 字典推导 + zip，输出残差最大的序号


# TODO: 第 5 题 —— 4 个 numpy 数组的广播 shape 预测与验证
