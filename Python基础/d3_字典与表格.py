"""
D3 · 字符串 + 字典（关卡，对应计划 P27～P41）

知识点：
  - 元组：不可变，可以当字典的 key
  - 字符串常用方法：split / join / strip / replace / startswith
  - f-string：f"{name}={value:.2f}"，比 % 和 .format() 顺手
  - 字典：增删改查、遍历 items()、key 不存在时的默认值
  - 字典推导式：{k: v for k, v in ...}
  - zip：把多个序列「按位置」配对；enumerate：带下标遍历

关卡要求：
  用 zip + enumerate + f-string 对齐，输出一张「序号-实测值-偏差-是否超差」表格。

为什么字典这一集最重要：
  PyTorch 的 model.state_dict() 返回的就是一个字典；配置参数、训练日志、
  各类「名字 → 值」的传参，全是字典。这一集不牢，后面读源码会一直卡。

提示（API 关键词）：
  "a,b,c".split(",")            → ['a','b','c']
  ",".join(["a","b"])           → 'a,b'
  d.items() / d.keys() / d.get(k, 默认值)
  {k: v for k, v in pairs}
  zip(a, b)                     → 配对成元组
  enumerate(seq, start=1)       → 带序号

TODO:
  1. 准备两组等长列表：实测值列表、目标值列表
  2. 用 zip 把它们配对，算出偏差，组成一个字典
  3. 用字典推导式生成 {序号: 偏差} 的字典
  4. 用 enumerate + f-string 打印对齐的表格（序号/实测值/偏差/是否超差）
  5. 找出偏差最大的那个序号并打印（提示：max(dict, key=dict.get)）
"""
# TODO: 在下面写你的代码
