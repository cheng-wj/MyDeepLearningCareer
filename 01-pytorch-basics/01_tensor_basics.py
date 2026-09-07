"""
第 1 课：张量基础
=================
知识点：
  1. 张量(Tensor)就是 PyTorch 里的"多维数组"，类似 numpy.ndarray，但可以跑在 GPU 上
  2. 形状(shape)、数据类型(dtype)、设备(device) 是张量最重要的三个属性
  3. 常见操作：算术、索引、变形(reshape)、广播(broadcasting)
  4. 张量在 CPU/GPU 之间搬运用 .to(device)
"""
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"本次计算使用的设备: {device}\n")

# ---- 1. 创建张量 ----
a = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
print("a ="); print(a)
print(f"形状 shape = {a.shape}   维度 ndim = {a.ndim}   类型 dtype = {a.dtype}\n")

zeros = torch.zeros(2, 3)          # 全 0
ones = torch.ones(2, 3)            # 全 1
rand = torch.rand(2, 3)            # [0,1) 均匀随机
arange = torch.arange(0, 10, 2)    # 类似 range
print(f"zeros:\n{zeros}")
print(f"rand:\n{rand}")
print(f"arange: {arange}\n")

# ---- 2. GPU 搬运 ----
a_gpu = a.to(device)
print(f"a 在 CPU 上: {a.device}")
print(f"a 搬到 GPU 后: {a_gpu.device}")
print("注意：两个张量做运算时必须在同一个设备上，否则会报错。\n")

# ---- 3. 算术运算（逐元素） ----
x = torch.tensor([1.0, 2.0, 3.0])
y = torch.tensor([10.0, 20.0, 30.0])
print(f"x + y = {x + y}")
print(f"x * y = {x * y}        # 逐元素相乘，不是矩阵乘法")
print(f"x @ y = {x @ y}        # @ 才是点积/矩阵乘法: 1*10+2*20+3*30\n")

# ---- 4. 索引和切片（和 numpy 一模一样） ----
m = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"m:\n{m}")
print(f"m[0]    = 第 0 行: {m[0]}")
print(f"m[:, 1] = 第 1 列: {m[:, 1]}")
print(f"m[m > 5] = 布尔索引，挑出大于 5 的数: {m[m > 5]}\n")

# ---- 5. 变形 ----
flat = torch.arange(12)
print(f"flat = {flat}, shape = {flat.shape}")
reshaped = flat.reshape(3, 4)
print(f"reshape(3, 4) 后:\n{reshaped}")
print(f"转置 .T:\n{reshaped.T}\n")

# ---- 6. 广播(broadcasting)：不同形状的张量自动对齐运算 ----
# 一个 (3,) 的向量和一个 (3,3) 的矩阵相加，向量会被"复制"到每一行
scores = torch.tensor([[80.0, 90.0, 70.0],
                       [60.0, 75.0, 85.0]])
bonus = torch.tensor([5.0, 5.0, 5.0])   # 每人每科加 5 分
total = scores + bonus
print(f"广播加分:\n{total}")

# 和 numpy 互相转换（numpy 只能在 CPU 上）
back_to_numpy = total.cpu().numpy()
print(f"\n转成 numpy: type = {type(back_to_numpy)}")
