# 国庆 7 天 PyTorch 入门计划（C# 开发者版）

> 视频教程：https://www.bilibili.com/video/BV1hE411t7RN  
> 适用对象：有 C# 开发经验，但没有 Python / PyTorch 基础  
> 目标：7 天从零入门 PyTorch，能理解核心概念，能跑通 MNIST 训练流程  
> 说明：7 天可以做到“入门 + 能动手”，但达不到“熟练掌握”。熟练掌握通常需要 3～6 个月项目实践。

---

## 一、总目标

7 天结束后，你应该能做到：

- 能独立创建 Python 虚拟环境，安装 PyTorch
- 能读懂基础 Python 代码，能写类、函数、循环、列表推导式
- 理解 Tensor、Autograd、`nn.Module`、损失函数、优化器、训练循环
- 能跑通 MNIST 手写数字识别训练
- 能保存和加载模型
- 能修改简单网络结构、学习率、batch size
- 能看懂大部分 PyTorch 入门教程和开源训练脚本的基础部分

暂时不要求：

- 复现复杂论文
- 分布式训练
- 混合精度
- 模型部署优化
- 独立完成真实工业项目

---

## 二、学习原则

1. **不要先学完 Python 再学 PyTorch**  
   前 2 天集中补 Python 和 NumPy，第 3 天开始边看视频边写 PyTorch。

2. **不要追求看完所有视频**  
   “我是土堆”的教程很细，7 天不可能全部消化。目标是跑通完整流程。

3. **以代码为主线**  
   每个概念至少写一遍、跑一遍、改一遍。

4. **遇到不懂的先跳过**  
   比如 BatchNorm、复杂数学推导，先知道怎么用，后面再补原理。

5. **利用 C# 经验**  
   面向对象、调试、工程结构、强类型思维都能迁移。

---

## 三、每日时间安排

假设每天投入 8 小时，共约 54 小时。  
如果每天不足 8 小时，优先保 Day 3～Day 6。

| 天数 | 主题 | 时间 | 产出 |
|---|---|---|---|
| Day 1 | Python 核心语法 + 环境搭建 | 8h | 能写基础 Python 脚本 |
| Day 2 | Python 面向对象 + NumPy | 8h | 能读懂类，会数组操作 |
| Day 3 | PyTorch 环境 + Tensor 基础 | 8h | 跑通第一个 Tensor 程序 |
| Day 4 | Autograd + 数据处理 | 8h | 理解自动求导，会用 DataLoader |
| Day 5 | 神经网络构建 | 8h | 用 `nn.Module` 搭出网络 |
| Day 6 | 训练流程跑通 | 8h | 训练 MNIST，loss 下降 |
| Day 7 | 优化技巧 + 复盘 | 6h | 完整训练脚本 + 笔记 |

---

## Day 1：Python 核心语法 + 环境搭建

### 上午：环境与基础语法

- 安装 Python 3.10+
- 编辑器选择：
  - VS Code + Python + Jupyter 扩展
  - 或 PyCharm
  - 或 Visual Studio 2022，安装 Python 开发工作负载
- 创建虚拟环境：

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

- 写 Hello World
- 学习基础语法：
  - 变量与动态类型
  - `if / elif / else`
  - `for / while`
  - 函数 `def`
  - `list`、`dict`、`tuple`
  - 字符串格式化 `f"{name}"`

### 下午：C# 对照 + 小练习

重点对照：

| C# | Python |
|---|---|
| `for (int i=0; i<n; i++)` | `for i in range(n)` |
| `List<T>` | `list` |
| `Dictionary<K,V>` | `dict` |
| LINQ `Where/Select` | 列表推导式 |
| `using` | `with open(...) as f:` |
| `this` | `self` |
| `Main` | `if __name__ == "__main__":` |
| NuGet | pip |
| `.csproj` | `requirements.txt` |

练习 20 个小程序：

- 阶乘
- 斐波那契
- 列表去重
- 字典遍历
- 文件读写
- 简单统计

**Day 1 产出**：能独立写出 50 行以内的 Python 脚本。

---

## Day 2：Python 面向对象 + NumPy

### 上午：面向对象

- `class` 定义
- `__init__`
- `self`
- 实例方法
- 继承
- 模块导入

重点理解：

```python
class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}")
```

`self` 类似 C# 的 `this`，但必须显式写在方法参数里。

### 下午：NumPy

- 创建数组：`np.array`、`np.zeros`、`np.ones`、`np.random.randn`
- 形状：`shape`、`reshape`
- 索引与切片
- 广播
- 矩阵乘法 `@`
- `axis` 概念

用 NumPy 实现：

- 矩阵加法、乘法
- 求均值、最大值
- 简单线性回归前向计算

**Day 2 产出**：能读懂简单 Python 类，能用 NumPy 做基础数组运算。

---

## Day 3：PyTorch 环境 + Tensor 基础

### 视频参考

大致对应 P1～P5，以实际视频为准：

- P1：PyTorch 环境配置
- P2：编辑器选择
- P3～P5：Tensor 基础操作

### 上午：安装与 Tensor

安装：

```bash
pip install torch torchvision torchaudio numpy matplotlib jupyter
```

如果有 NVIDIA 显卡，去 PyTorch 官网选择对应 CUDA 版本命令。

学习：

- `torch.tensor()`
- `torch.zeros()`、`torch.ones()`、`torch.randn()`
- Tensor 与 NumPy 的关系
- Tensor 的优势：
  - 可以用 GPU
  - 可以自动求导

### 下午：形状操作与 GPU

- `view`
- `reshape`
- `squeeze`
- `unsqueeze`
- `.to("cuda")`
- `shape`、`dtype`、`device`

动手：把 Day 2 的 NumPy 练习用 Tensor 重写一遍。

**Day 3 产出**：能创建、变换、移动 Tensor，理解 shape。

---

## Day 4：Autograd + 数据处理

### 视频参考

大致对应 P6～P10，以实际视频为准。

### 上午：自动求导 Autograd

核心理解：

> Autograd 相当于 PyTorch 自动帮你实现链式法则。你只写前向计算，调用 `.backward()`，PyTorch 自动算梯度。

示例：

```python
import torch

x = torch.tensor(2.0, requires_grad=True)
y = x**2 + 3*x + 1
y.backward()

print(x.grad)  # 7.0
```

学习：

- `requires_grad=True`
- `loss.backward()`
- `.grad`
- 梯度清零 `optimizer.zero_grad()`

### 下午：Dataset 与 DataLoader

- `Dataset`：数据集合抽象
- `DataLoader`：批量加载、打乱、并行
- 使用 `torchvision.datasets.MNIST`
- 可视化几张图片

**Day 4 产出**：理解自动求导，能用 DataLoader 加载 MNIST。

---

## Day 5：神经网络构建

### 视频参考

大致对应 P11～P16，以实际视频为准。

### 上午：`nn.Module`

- `nn.Module` 是所有网络的基类
- `__init__` 里定义层
- `forward` 里定义数据流动
- `nn.Linear`
- `nn.ReLU`
- `nn.Sequential`

C# 类比：

> `nn.Module` ≈ 一个基类，你继承它，在 `__init__` 里组装组件，在 `forward` 里写逻辑。

### 下午：搭一个 MLP

目标网络：

- 输入 784，28×28 像素
- 隐藏层 128
- 输出 10，对应 0～9

示例结构：

```python
import torch.nn as nn

model = nn.Sequential(
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
)
```

**Day 5 产出**：能用 `nn.Module` 或 `nn.Sequential` 搭出简单网络。

---

## Day 6：训练流程跑通

### 视频参考

大致对应 P17～P22，以实际视频为准。

### 上午：损失函数与优化器

- 分类损失：`nn.CrossEntropyLoss`
- 优化器：`torch.optim.SGD`、`torch.optim.Adam`

### 下午：完整训练循环

训练五步：

```python
for x, y in dataloader:
    pred = model(x)              # 1. 前向
    loss = loss_fn(pred, y)      # 2. 算损失
    optimizer.zero_grad()        # 3. 清空旧梯度
    loss.backward()              # 4. 反向求导
    optimizer.step()             # 5. 更新参数
```

关键坑点：

- 忘记 `optimizer.zero_grad()`，梯度会累加
- CPU 和 GPU 张量混用会报错
- 训练时 `model.train()`
- 验证时 `model.eval()`
- 数据要 `.to(device)`
- 维度对不上是常见错误

目标：MNIST 验证集准确率 > 90%。

**Day 6 产出**：跑通完整训练，看到 loss 下降。

---

## Day 7：优化技巧 + 复盘

### 上午：补全视频后半段

- 学习率调度
- 保存模型：

```python
torch.save(model.state_dict(), "model.pth")
```

- 加载模型：

```python
model.load_state_dict(torch.load("model.pth"))
```

- GPU 加速
- TensorBoard 可选

### 下午：整理与复盘

- 把 7 天代码整理成可复用训练脚本模板
- 写学习笔记：
  - 每个概念和 C# 的对照
  - 踩过的坑
  - 常用代码片段
- 尝试改超参数：
  - 学习率
  - 隐藏层大小
  - batch size
  - 优化器

**Day 7 产出**：一份自己的 PyTorch 入门笔记 + 一个可运行训练脚本。

---

## 四、C# 与 PyTorch 概念对照

| C# / .NET | PyTorch / Python |
|---|---|
| `this` | `self` |
| `List<T>` | `list` |
| `Dictionary<K,V>` | `dict` |
| LINQ | 列表推导式 |
| `using` | `with` |
| NuGet | pip |
| `.csproj` | `requirements.txt` |
| 多维数组 | Tensor |
| 接口 / 基类 | `nn.Module` |
| 方法 | `forward` |
| `IEnumerable<Batch>` | `DataLoader` |
| 参数更新器 | `optimizer.step()` |
| 自动反向传播 | `loss.backward()` |

---

## 五、常见坑点

- 忘记 `optimizer.zero_grad()`
- 训练时忘记 `model.train()`
- 验证时忘记 `model.eval()`
- CPU 张量和 GPU 张量混用
- 数据没有 `.to(device)`
- shape 对不上
- Python 缩进就是语法，没有大括号
- 每个项目要用虚拟环境，不要全局乱装包
- 复制代码不运行，等于没学
- 遇到报错不读错误信息

---

## 六、常用命令

```bash
# 创建虚拟环境
python -m venv .venv

# 激活 Windows
.venv\Scripts\activate

# 激活 macOS / Linux
source .venv/bin/activate

# 安装依赖
pip install torch torchvision torchaudio numpy matplotlib jupyter

# 启动 Jupyter
jupyter notebook
```

---

## 七、7 天结束检查清单

- [ ] 能创建并激活 Python 虚拟环境
- [ ] 能写 Python 函数、类、列表推导式
- [ ] 能用 NumPy 做数组运算
- [ ] 能创建 Tensor，并理解 shape
- [ ] 能理解 `requires_grad` 和 `backward()`
- [ ] 能用 `Dataset` 和 `DataLoader` 加载数据
- [ ] 能用 `nn.Module` 搭一个 MLP
- [ ] 能写完整训练循环
- [ ] 能训练 MNIST 并看到 loss 下降
- [ ] 能保存和加载模型
- [ ] 有一份自己的学习笔记和可复用脚本

---

## 八、如果时间不够的压缩版

如果每天只能投入 3～4 小时，按这个优先级：

1. Day 1：Python 基础 + 环境
2. Day 2：NumPy + Tensor
3. Day 3：Autograd + DataLoader
4. Day 4：`nn.Module` + 网络搭建
5. Day 5：训练循环
6. Day 6：MNIST 跑通
7. Day 7：保存模型 + 复盘

压缩版仍然可以让你入门，但项目练习会少很多。

---

## 九、最后提醒

7 天能让你从“完全没接触”到“能跑通并理解基础流程”。  
但“熟练掌握 PyTorch”需要后续继续做项目，尤其是：

- 自己找数据集
- 自己写 Dataset
- 自己改网络
- 自己调参
- 自己复现小论文
- 自己部署模型

国庆 7 天最好的结果不是“学完”，而是“入门并跑通第一个模型”。