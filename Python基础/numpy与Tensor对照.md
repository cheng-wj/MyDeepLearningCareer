# numpy ↔ torch.Tensor 对照表

> 计划第五节第 2 条要的东西：shape / 广播 / 布尔索引 —— **Python 通往 PyTorch 的那座桥**。
> 语法阶段用 `py -3`（numpy 2.4.6），PyTorch 阶段用 conda `torch` 环境（torch 2.14.0+cu126，numpy 同为 2.4.6）—— 两边 API 基本一致，本表两边通用。

## 一、numpy 和 Tensor 是一回事

`torch.Tensor` 就是「能在 GPU 上跑、能求导」的 numpy 数组。**95% 的 numpy 写法在 Tensor 上原样可用**，只是多了两个参数：

| numpy | torch | 差别 |
|---|---|---|
| `np.array([1,2,3])` | `torch.tensor([1,2,3])` | tensor 默认 CPU、int64 |
| `np.array([1,2,3], dtype=np.float32)` | `torch.tensor([1,2,3], dtype=torch.float32)` | dtype 一一对应 |
| `a.shape` | `a.shape` | 一样是 `torch.Size`（本质 tuple） |
| `a.reshape(2,3)` | `a.reshape(2,3)` / `a.view(2,3)` | 一样 |
| `a.T` | `a.T` | 一样（PyTorch 里 `.T` 对 >2 维会报错，用 `permute`） |
| `np.zeros((2,3))` | `torch.zeros(2,3)` | **Tensor 用 `torch.zeros(2,3)`，元组可省略** |
| `np.random.randn(2,3)` | `torch.randn(2,3)` | 一样 |
| `a + b` | `a + b` | 一样，广播规则完全相同 |
| `a.sum()` / `a.mean()` | `a.sum()` / `a.mean()` | 一样 |
| `a.astype(np.float32)` | `a.float()` / `a.to(torch.float32)` | Tensor 多一个 `.to(device)` |
| `a.copy()` | `a.clone()` | **Tensor 必须显式 clone**，赋值只是引用 |
| `np.save(...)` | `torch.save(...)` | 保存格式不同，各存各的 |

**互转**：

```python
t = torch.randn(2, 3)
a = t.numpy()            # Tensor → ndarray（要求 CPU、且不requires_grad）
t2 = torch.from_numpy(a)  # ndarray → Tensor（共享内存，改一个另一个跟着变）
```

## 二、shape 与广播（九成 bug 在这里）

**广播规则**（numpy 和 Tensor 完全一致）：

> 从**最右**的维度开始逐轴对齐；某一轴两者之一为 `1` 就能拉伸；否则必须相等，否则报错。

```python
a = torch.randn(3, 1, 32, 32)   # (N, C, H, W)
b = torch.randn(32, 32)          #       (H, W)
a + b                            # → (3, 1, 32, 32)：b 自动补成 (1,1,32,32)
```

**必记的三个形状陷阱**：

1. `a.reshape(3, 32, 32)` 和 `a.reshape(3, -1)` 结果一样；`-1` 表示「这一维你自己算」，全篇只能出现一次。
2. `torch.zeros(2, 3)` 是 **2 行 3 列**；`torch.zeros(3, 2)` 是 3 行 2 列。写反了不会报错，只会让后面 loss 算不出来 —— 所以**每层后面打 `.shape`**。
3. 索引 `a[0]` 出来的是**一维**张量（去掉第 0 维），不是二维。想要二维用 `a[0:1]`（切片保留维）或 `a[0].unsqueeze(0)`。

## 三、布尔索引与掩码（分割/筛选数据要用）

```python
mask = a > 0            # 和 a 同形状的布尔张量
a[mask]                # 取所有正数，结果是一维
a[mask] = 0            # 把负数和 0 归零（原位修改）
idx = torch.tensor([0, 2, 3])
a[idx]                  # 按序号取，和 mask 两套机制
```

⚠️ **Tensor 的布尔索引返回副本**，改它不会影响原张量；numpy 里也是副本，但 Tensor 容易让人误以为原位改了 —— 记不住就用 `a[mask] = 0` 这种原位写法。

## 四、跟 PyTorch 直接挂钩的三点

1. **`requires_grad`**：Tensor 多一个属性。`torch.randn(2,3, requires_grad=True)` 之后 `.sum().backward()` 才有梯度；numpy 数组没这回事。
2. **device**：`a.device` / `a.to('cuda')`。语法阶段先不管，PyTorch 阶段 P30 再说。
3. **`numel()` vs `size`**：`a.size()` 是**形状**（tuple），`a.numel()` 是**元素总数**（int）。`len(a)` 只给第一维长度 —— 这三个别混，debug 时常用。

## 五、调试三件套（记不住就 print）

```python
print(a.shape)          # 形状
print(a.dtype)          # 类型
print(a.device)         # 在哪
print(a)                # 实际值
```

---

> 相关：`Python学习计划-7天.md` 第五节第 2 条 ｜ PyTorch 阶段参考 `pytorch学习/README.md`
