"""
D4 · 函数（关卡，对应计划 P42～P53）

知识点：
  - def 定义、位置参数 vs 关键字参数、默认值
  - 默认值必须是「不可变对象」——def f(x=[]) 是经典坑，每次调用共享同一个列表
  - *args（收集成元组）、**kwargs（收集成字典）
  - 单独的 * 放在参数中间：def f(a, *, b=1) —— b 只能用关键字传，位置传会报错
  - 返回值：return 可以返回多个值（本质是返回元组）
  - 类型注释与文档字符串：def f(x: int, y: str = "a") -> bool:，以及用三引号包起来的文档字符串
  - 高阶函数：map / filter / zip、lambda、sort(key=...)

关卡要求：
  1. 写出 def fit(pts, *, deg=2, save=None)，并解释 * 的作用
  2. 写一个带 **kwargs 的函数，把多余参数收集起来打印
  3. 写一个带类型注释和 docstring 的函数（认得出这个格式，才读得懂 PyTorch 源码）

为什么这一集是 PyTorch 的门槛：
  torch.nn.Module 的 __init__、forward、以及 **kwargs 式的可选参数，全是这个语法。
  很多「看不懂 PyTorch 源码」的根源，就是 Python 函数语法不熟，不是深度学习难。

提示（API 关键词）：
  def f(a, b=2, *args, **kwargs): ...
  f(a=1, b=2)                  关键字调用
  f(1, 2, 3, 4)                多余的位置参数进 args
  f(1, x=2, y=3)               多余的关键字参数进 kwargs
  f"{x=}"                      调试神器：连变量名一起打印
  list(map(func, seq)) / list(filter(func, seq))

TODO:
  1. 写 fit 函数：入参 pts（点列表）、deg（默认 2）、save（默认 None）
     返回按 deg 次多项式拟合出的系数（提示：numpy.polyfit）
  2. 调用它三次：一次用默认参数、一次用关键字改 deg、一次故意用位置参数传 deg
     —— 第三次应该报错，报错信息读一遍，记下它说的是哪种错误
  3. 写带 **kwargs 的 show_config(**cfg) 函数
  4. 写一个带类型注释的函数，docstring 里写清参数和返回值
"""
# TODO: 在下面写你的代码
