"""
D5 · 类与对象（关卡，对应计划 P59～P66）⭐ 全场最重的一天

知识点：
  - class 定义、实例化，实例属性写在 __init__ 里（self.xxx = ...）
  - self 是「当前实例自己」，每个方法第一个参数必须写 self（调用时不用传）
  - __init__ 是构造函数；super().__init__() 调父类构造函数 —— 多重继承里必须这么写
  - 继承 class 子类(父类):，重写（override）父类方法
  - 多态与鸭子类型：「长得像就能用」，Python 不检查类型
  - 特殊方法（魔术方法）：__str__ / __repr__ 决定 print 出来长什么样

关卡要求（空文件默写）：
  1. 写一个 Calibrator 类：__init__(self, coef) 存系数，apply(self, x) 算补偿值
     （补偿值 = x * coef 或按你定的公式，说清就行）
  2. 实例化 3 个（不同系数），放进一个 list，用 for 循环调用 apply
  3. 再写一个子类 EnhancedCalibrator，用 super().__init__() 调父类，再重写 apply
  4. 给类写 __str__，让 print(实例) 有意义

为什么这是 PyTorch 的门槛正中心：
  torch.nn.Module 就是这样写的 —— __init__ 里用 self.xxx = nn.Conv2d(...) 注册子模块，
  forward(self, x) 里写前向，model(x) 会自动去调 forward。
  本文件写完，P16 那集你会觉得「哦，就这」。

提示（API 关键词）：
  class A:
      def __init__(self, x):
          self.x = x
      def method(self, y):
          return self.x + y
  class B(A):
      def __init__(self, x, z):
          super().__init__(x)
          self.z = z
  def __str__(self):
      return f"Calibrator(coef={self.coef})"

TODO:
  1. 写 Calibrator 类
  2. 实例化 + 放进 list + 循环调用
  3. 写子类 EnhancedCalibrator，用 super().__init__()
  4. 写 __str__，print 出一个实例看看
"""
# TODO: 在下面写你的代码
