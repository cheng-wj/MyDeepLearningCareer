"""
D1 · 公差判定脚本（关卡，对应计划 P3～P12）

知识点：
  - 变量赋值、数字类型（int / float）、字符串
  - 布尔类型 True / False，以及比较运算的结果就是布尔
  - 短路逻辑：and / or 的含义，以及 `and` 的优先级高于 `or`
  - 运算符优先级：`not` > `and` > `or`，比较 > 逻辑
  - if / elif / else 的分支，Python 用缩进表示代码块（没有大括号）
  - for 循环 + range，以及遍历列表
  - print 的 f-string 写法：f"序号 {i} 值 {v:.3f}"

关卡要求（不看资料写出来）：
  给定一组实测值，逐个算偏差、判是否超差、打印一张结果表，最后统计合格/不合格数量。

注意（新手最容易错的两点）：
  1. 浮点数不能用 == 判断边界。判超差要用 > 而不是 != 之类的写法
  2. 缩进错了就是语法错误，if 体和 for 体的缩进层级要一致（统一 4 个空格）

TODO:
  1. 定义 标准值、上下公差、实测值列表 三个变量
  2. 用 for 遍历实测值，算偏差、判断超差，打印一行结果
  3. 统计合格数与不合格数，最后打印汇总

期望输出（写完自己对照，合格 2 / 不合格 3）：
  1 号 99.940  偏差 -0.060  → NG      ← 超差
  2 号 100.020 偏差 +0.020  → OK
  3 号 100.070 偏差 +0.070  → NG      ← 超差
  4 号 99.980  偏差 -0.020  → OK
  5 号 100.051 偏差 +0.051  → NG      ← 浮点边界坑：实际是 0.05100000000000456
  汇总：合格 2 个，不合格 3 个
"""

# 标准值 100.0，公差 ±0.05
# 实测值列表：[99.94, 100.02, 100.07, 99.98, 100.051]
#
# 提示（API 关键词）：
#   for i in range(len(values)):        遍历下标
#   for i, v in enumerate(values):      遍历下标和值
#   abs(x)                              绝对值
#   if ... : elif ... : else :          分支
#   f"{v:.3f}"                          保留 3 位小数

# TODO: 在下面写你的代码
#
# ┌────────────────────────────────────────────────────────────┐
# │ ① 自己写的版本（2026-11-13 深夜）—— 保留作对照，逻辑正确、  │
# │    结果正确（合格2/不合格3），只是打印格式没对齐              │
# └────────────────────────────────────────────────────────────┘
#
# def check_tolerance(values,standard,tolerance):
#     ok_count=0
#     ng_count=0
#     for i in range(len(values)):
#         if abs(values[i]-standard)>tolerance:
#             ng_count += 1
#             print(i,"号",values[i],",NG")
#         else:
#             ok_count+=1
#             print(i,"号",values[i],",OK")
#     return ok_count,ng_count
#
# if __name__ == "__main__":
#     values = [99.940,100.020,100.070,99.980,100.051]
#     standard = 100.0
#     tolerance = 0.05
#     ok,ng=check_tolerance(values,standard,tolerance)
#     print("OK总计:",ok,",NG总计:",ng)
#     pass


# ┌────────────────────────────────────────────────────────────┐
# │ ② 改进版本 —— 打印格式对齐期望输出：序号从1起、补偏差列、   │
# │    小数固定3位。改动点见每行右侧注释                          │
# └────────────────────────────────────────────────────────────┘
def check_tolerance(values, standard, tolerance):
    ok_count = 0
    ng_count = 0
    # enumerate(values, start=1)：i 从 1 开始数，v 就是值本身（不用再写 values[i]）
    for i, v in enumerate(values, start=1):
        deviation = v - standard  # 带符号的偏差
        if abs(deviation) > tolerance:  # 用 > 判超差，不用 ==（浮点边界）
            flag = "NG"
            ng_count += 1
        else:
            flag = "OK"
            ok_count += 1
        # :.3f 固定3位小数；:+.3f 强制带正负号
        print(f"{i} 号 {v:.3f}  偏差 {deviation:+.3f}  → {flag}")
    return ok_count, ng_count


if __name__ == "__main__":
    values = [99.940, 100.020, 100.070, 99.980, 100.051]
    standard = 100.0
    tolerance = 0.05

    ok, ng = check_tolerance(values, standard, tolerance)
    print(f"汇总：合格 {ok} 个，不合格 {ng} 个")
