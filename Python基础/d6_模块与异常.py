"""
D6 · 模块 + 异常 + 文件读写（关卡，对应计划 P57、P58、P70、P72、P74、P84～P86）

知识点：
  - 索引/切片/迭代协议：__getitem__(self, i) 让对象支持 obj[i]；__iter__ 让 for 能遍历
    —— 这正是下一阶段 Dataset.__getitem__ 的原理
  - 对象调用协议：__call__(self, ...) 让实例能像函数一样调用 model(x)
    —— 这正是 model(x) 为什么会跑 forward 的答案
  - 类方法 @classmethod、静态方法 @staticmethod（认得出来即可）
  - 模块与包：import、from x import y、if __name__ == "__main__": 的作用
  - 异常：try / except / else / finally、raise、自定义异常
  - 文件读写：with open(...) as f:（用完自动关闭）

关卡要求：
  1. 把 D5 写的类拆成独立文件 calibrator.py
  2. 另写一个文件 import 它并调用（注意 import 路径和 if __name__ == "__main__"）
  3. 读一个 CSV，用 try/except 跳过坏行

为什么 __getitem__ / __call__ 这两集最重要：
  PyTorch 的 Dataset 只要求你有 __getitem__ 和 __len__；
  nn.Module 的 model(x) 走的是 __call__。这两条协议撑起了整个框架的易用性。

提示（API 关键词）：
  class Box:
      def __getitem__(self, i): return self.items[i]
      def __len__(self): return len(self.items)
      def __call__(self, x): return x * 2
  from calibrator import Calibrator
  try:
      v = int(s)
  except ValueError as e:
      print("跳过坏行", s, e)
  with open("f.csv", "r", encoding="utf-8") as f:
      for line in f: ...

TODO:
  1. 把 D5 的类移到 calibrator.py
  2. 在本文件 import 它并跑通一遍
  3. 写一个带 __getitem__ 和 __len__ 的小类（模拟 Dataset 的协议），验证 len 和 obj[0]
  4. 写一个带 __call__ 的类，验证 obj(x) 能调用
  5. 读 CSV + try/except 跳过坏行（可以自己造一个带坏行的 csv）
"""
# TODO: 在下面写你的代码
