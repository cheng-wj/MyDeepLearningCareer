# 使用decimal来精准计算浮点数
import decimal

a = decimal.Decimal("0.1")
b = decimal.Decimal("0.2")
print(a + b)

# 短路逻辑
# 短路逻辑的核心思想：从左到右，只有当第一个操作数的值无法确定逻辑运算的结果时，
# 才对第二个操作数进行求值
