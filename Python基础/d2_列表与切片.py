"""
D2 · 列表与切片（关卡，对应计划 P13～P26）

知识点：
  - 列表创建、增删改查：append / insert / remove / pop / sort / reverse
  - 索引与负索引：lst[0] 是第一个，lst[-1] 是最后一个
  - 切片 lst[start:stop:step]，左闭右开（stop 取不到）
  - 特殊切片：lst[::-1] 反转，lst[::2] 隔一个取一个
  - 列表推导式：[表达式 for 变量 in 可迭代对象]
  - 浅拷贝 vs 深拷贝：copy.copy / copy.deepcopy，以及赋值只是引用

关卡要求（先口算再运行，全对才算过）：
  给 5 个列表，先在纸上写出每个切片的结果，再运行核对。
  必做切片：[::-1]、[-2:]、[1:4]、[:2]、[::2]、[-3:-1]

最关键的一课 —— 引用语义：
  a = b 只是「两个名字指向同一个对象」，不是复制。
  改 a 里的内容，b 也会变；这跟 C# 的值类型直觉相反，务必用 Python Tutor 跑一遍。

提示（API 关键词）：
  lst.append(x) / lst.insert(i, x) / lst.pop(i) / lst.remove(x)
  lst.index(x) / lst.count(x) / len(lst)
  sorted(lst) / lst.sort(key=lambda x: ...)
  [x for x in lst] / [x * 2 for x in lst if x > 0]
  copy.deepcopy(lst)

TODO:
  1. 建 5 个测试列表
  2. 对每个列表，把上面 6 种切片的「预期结果」先写成注释
  3. 运行核对，把实际结果打印出来
  4. 用列表推导式生成「每个元素的平方」
  5. 演示一次浅拷贝与深拷贝的差异（改副本，看原对象动不动）
"""

# TODO: 在下面写你的代码
