"""
if 语句 + f-string 速查（C# → Python 对照）

跑法（仓库根目录）：
    E:\\conda\\envs\\torch\\python.exe Python基础\\速查\\if语句速查.py

每段下面都写了「应该看到什么」，自己跑一遍对一下。
"""

print("=== 1. 基本三分支 if / elif / else ===")
x = 5
if x > 10:
    print("  大")
elif x > 3:
    print("  中")          # ← 应该看到：中（x=5 不 >10，但 >3）
else:
    print("  小")

print("=== 2. 只有 if（没有 else 就是没有'否则'分支）===")
if x == 5:
    print("  等于5")        # ← 应该看到：等于5

print("=== 3. 逻辑运算 and / or / not ===")
a, b = True, False
print("  a and b =", a and b)   # False
print("  a or b  =", a or b)    # True
print("  not a   =", not a)     # False

print("=== 4. 短路：and/or 右边可能根本不求值 ===")
print("  0 and 1/0 →", 0 and 1 / 0)   # 0（右边不求值，所以没报 ZeroDivisionError）
print("  1 or 1/0  →", 1 or 1 / 0)    # 1（同理）

print("=== 5. 优先级：not > and > or，比较 > 逻辑 ===")
print("  True or False and False  =", True or False and False)    # True（and 先算）
print("  (True or False) and False=", (True or False) and False)  # False

print("=== 6. 真值判断：哪些算 False ===")
for v in [0, 1, "", "a", None, [], [1], 0.0]:
    print(f"  {v!r:>6} → {bool(v)}")
# 0 / "" / None / [] / 0.0 都是 False，其余 True

print("=== 7. 三元表达式（相当于 C# 的 ?: ）===")
print("  ", "合格" if x > 3 else "不合格")   # 合格

print("=== 8. f-string 格式说明符 ===")
v = 99.94
dev = v - 100.0
print(f"  {{v:.3f}}    → {v:.3f}")        # 99.940
print(f"  {{dev:+.3f}}  → {dev:+.3f}")     # -0.060（+ 号强制带正负号）
print(f"  {{v:.1f}}    → {v:.1f}")        # 99.9
print(f"  {{dev:.1%}}  → {dev:.1%}")      # -6.0%（百分比）

print("=== 9. d1 本练习要用的两种写法 ===")
standard, tolerance = 100.0, 0.05

# 写法A：先算好判定结果，再拼字符串（推荐，两台机器都能跑）
for i, val in enumerate([99.94, 100.02, 100.07, 99.98, 100.051]):
    deviation = val - standard
    ok = abs(deviation) <= tolerance          # 注意用 <=，不要用 ==
    flag = "OK" if ok else "NG"
    print(f"  {i + 1} 号 {val:.3f}  偏差 {deviation:+.3f}  → {flag}")

# 写法B：把判断直接塞进 f-string 的大括号里
#        ⚠️ 这种嵌套引号只有 Python 3.12+ 支持（个人机 3.12.14 可以，
#           公司机 3.11.16 会报 SyntaxError）—— 所以优先用写法A
