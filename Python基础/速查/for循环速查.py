"""
for 循环速查（C# → Python 对照）

跑法（仓库根目录）：
    E:\\conda\\envs\\torch\\python.exe Python基础\\速查\\for循环速查.py

每段下面都写了「应该看到什么」，自己跑一遍对一下。
"""

values = [99.94, 100.02, 100.07]

print("=== 形式1：只要值（相当于 C# 的 foreach）===")
# 应该看到：值 = 99.94 / 100.02 / 100.07 各一行
for v in values:
    print("  值 =", v)

print("=== 形式2：下标 + 值（enumerate，最常用）===")
# 应该看到：下标 0 值 = 99.94 … 下标 2 值 = 100.07
for i, v in enumerate(values):
    print("  下标", i, "值 =", v)

print("=== 形式3：只要下标（相当于 C# 的 for (int i=0; i<n; i++)）===")
# 应该看到：和形式2 一样的三行
for i in range(len(values)):
    print("  下标", i, "值 =", values[i])

print("=== range 的三种写法 ===")
# range(3)        → [0, 1, 2]           起点0、终点3（不含3）
# range(2, 5)     → [2, 3, 4]           从2到5（不含5）
# range(0, 10, 2) → [0, 2, 4, 6, 8]     从0到10（不含10），步长2
print("  range(3)        →", list(range(3)))
print("  range(2, 5)     →", list(range(2, 5)))
print("  range(0, 10, 2) →", list(range(0, 10, 2)))

print("=== break / continue ===")
# break    → 直接跳出整个循环
# continue → 跳过本次，继续下一次
# 下面这段应该只打印两行：合格 99.94、合格 100.02（到 i==1 时 break，100.07 那轮不执行）
for i, v in enumerate(values):
    if v > 100.05:
        print("  超差，跳过:", v)
        continue
    print("  合格:", v)
    if i == 1:
        break

print("=== 空循环体：pass 占位 ===")
# Python 里 if 体不能是空的，写个 pass 占位
for i in range(2):
    if i == 0:
        pass
    else:
        print("  i =", i)
