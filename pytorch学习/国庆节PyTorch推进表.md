# 国庆 10 天 PyTorch 推进表（精简版）

## 元信息

- **日期范围**：2026-10-01（周四）~ 2026-10-10（周六），共 10 天
- **配套视频**：小土堆《PyTorch深度学习快速入门教程》 https://www.bilibili.com/video/BV1hE411t7RN （P01-P33，约 10 小时）
- **适用对象**：有 C# / .NET 开发经验，已装好 conda 环境 `torch`（PyTorch 2.11 + CUDA），编辑器已就绪
- **目标**：把 README 进度清单中 **P04-P33 共 29 集**全部跑通，最终用 CIFAR10 训练脚本在 GPU 上跑出 loss 下降、保存 checkpoint、能用验证套路评测
- **前置状态**：
  - 已完成：P01 / P02 / P03 / P05
  - 数据集目录：`../data/`（torchvision 自动下载）
  - 权重目录：`../checkpoints/`
  - TensorBoard 日志目录：`../logs/`
  - 仓库已有示例：`../01-pytorch-basics/`（Tensor / Autograd / MLP 双月 / MNIST CNN）
  - 写代码前一律 `conda activate torch`
  - **每日学习时间安排**：上午自由 / 休息 / 处理杂事；**全部学习任务压到下午 14:00-18:00（4h，含中间休息 15 分钟）**

---

## 一、总目标

10 天结束你应该能做到：

- [x] 用 dir() / help() 查任何 PyTorch 对象
- [x] 写自定义 Dataset / DataLoader，理解 transform pipeline
- [x] 用 TensorBoard 看 loss 曲线和图片
- [x] 继承 nn.Module 搭 CNN（Conv2d + MaxPool + ReLU + Linear）
- [x] 手写 5 步训练循环（forward → loss → zero_grad → backward → step）
- [x] 加载预训练模型并修改最后一层
- [x] 保存 / 加载 state_dict
- [x] 用 GPU 训练（`.to(device)` 三件套）
- [x] 写出独立可跑的模型验证脚本
- [x] 逛 torchvision / ultralytics 等开源源码，知道入口在哪

10 天**不**要求：

- 不要求复现 SOTA
- 不要求分布式 / 混合精度 / 模型部署
- 不要求自己设计网络

---

## 二、学习原则

1. **代码优先**：每集看完立刻写 `pXX_*.py`，跑通再勾选 README 清单
2. **照抄不算学**：视频代码只作参考，文件里只有关键词，**自己实现**
3. **报错先读 traceback 最后三行**，卡住超过 20 分钟再问
4. **GPU 永远用 `.to(device)` 三件套**（model / data / label），不要让一半在 CPU 一半在 CUDA
5. **每天结束前 `git add -A && git commit -m "dayX: ..."`**，10 天后仓库有完整轨迹

---

## 三、总时间安排表（10 天 × 4h = 40h）

| 天 | 日期 | 周 | 主题 | 视频集 | 下午 14:00-18:00（4h） |
|---|---|---|---|---|---|
| Day 1 | 10-01 | 四 | 工具与数据初识 | P04, P06, P07 | 视频 50 分钟 + 写 p04/p07 + C# 小抄 + Tensor 预热 |
| Day 2 | 10-02 | 五 | TensorBoard + Transforms 上半 | P08, P09, P10, P11 | 视频 + p08 + Compose 基础 5 个 transform |
| Day 3 | 10-03 | 六 | Transforms 下半 + DataLoader | P12, P13, P14, P15 | 视频 + p10 补完 + p15 + CIFAR10 提前下载 |
| Day 4 | 10-04 | 日 | nn.Module + Conv2d 概念 | P16, P17, P18 | 视频 + p16/p18 + 卷积 shape 计算 |
| Day 5 | 10-05 | 一 | MaxPool + ReLU + Linear | P19, P20, P21 | 视频 + p19/p20/p21 + 拼一个 block |
| Day 6 | 10-06 | 二 | Sequential + Loss + Optimizer | P22, P23, P24 | 视频 + p22/p23/p24 + zero_grad 直观教学 |
| Day 7 | 10-07 | 三 | Pretrained + Save/Load | P25, P26 | 视频 + p25/p26 |
| Day 8 | 10-08 | 四 | 完整训练套路 | P27, P28, P29 | 视频 + GPU 自检 + p27 跑通 1-3 epoch |
| Day 9 | 10-09 | 五 | GPU + 验证套路 | P30, P31, P32 | 视频 + p30 + 跑 CIFAR10 + p32 骨架 |
| Day 10 | 10-10 | 六 | 开源 + 复盘 | P33 | p32 完善 + 逛 torchvision/yolov5 + 合成 dataset + notes + README |

合计 40h。**上午自由 / 休息 / 处理杂事**；下午 14:00-18:00 中间休息 15 分钟。

---

## Day 1（10-01 周四）工具与数据初识

### 下午 14:00-18:00（4h）

> 上午：自由 / 休息 / 处理杂事

- [ ] 14:00-14:15 P04 视频，跟着视频对 `torch.tensor`、一个 nn.Module 实例分别跑 `dir()`、`help()`，把输出粘到笔记
- [ ] 14:15-14:25 P06 视频，**只看不写**——目标是脑子里有这张图：`Dataset` 负责"一条样本怎么读"，`DataLoader` 负责"一批怎么打包"，Transforms 负责"读进来后怎么变"
- [ ] 14:25-14:50 P07 视频，重点看 `__init__ / __len__ / __getitem__` 三个魔法方法
- [ ] 14:50-15:30 写 `p04_dir_help.py`：挑 3 个对象（`torch.Tensor`、`torch.nn.Linear`、`torch.utils.data.Dataset`）逐个跑 `dir()` / `help()`，把关键属性写到注释里
- [ ] 15:30-16:30 写 `p07_dataset.py`：实现一个 `MyDataset`：
  - 接受一个图片文件夹路径，扫描所有 `.jpg`
  - `__getitem__` 返回 `(PIL.Image, label_idx)`
  - 跑通 `len(ds)` 和 `ds[0]`
- [ ] 16:30-17:00 写 C# ↔ Python 类比小抄到 `notes/day1_cs_cheatsheet.md`（`self` ↔ `this`、`__init__` ↔ 构造函数、`__getitem__` ↔ 索引器、`with` ↔ `using`、`if __name__ == "__main__":` ↔ `Main`、`list` ↔ `List<T>`、`dict` ↔ `Dictionary<K,V>`）
- [ ] 17:00-17:30 **Tensor 形状预热**：手敲 5 个 `torch.zeros/randn/reshape/view/squeeze` 的小实验，先熟悉 shape 概念（提前为 Day 4 铺路）
- [ ] 17:30-18:00 调试 + 笔记整理

数据来源：`../data/hymenoptera_data/`（如果之前没下载，去 torchvision 文档找 ants/bees 链接手动下 5 张图放进去也行；**Day 10 会补一个用 `torch.randn` 的合成 dataset**，避免数据不全时跑不通）

### 产出标准

- [ ] 能在 10 秒内查到任意 PyTorch 类的可用方法
- [ ] 自定义 Dataset 子类能迭代、能索引
- [ ] `notes/day1_cs_cheatsheet.md` 已写
- [ ] **晚上** `git add -A && git commit -m "day1: dir/help + Dataset 入门"`

---

## Day 2（10-02 周五）TensorBoard + Transforms 上半

### 下午 14:00-18:00（4h）

> 上午：自由 / 休息 / 处理杂事

- [ ] 14:00-14:40 P08 + P09 视频，重点记 `SummaryWriter("logs/xxx")` → `add_scalar / add_image / add_graph` → `tensorboard --logdir=logs`
- [ ] 14:40-15:30 写 `p08_tensorboard.py`：画一条 `y=2x` 曲线 + `add_image` 一张图 + 启动 tensorboard 截图存到 `../logs/screenshots/`
- [ ] 15:30-16:00 P10 视频，重点 `Tools` 工具人用法
- [ ] 16:00-16:30 P11 视频，常见 transform 介绍（Resize / CenterCrop / RandomCrop）
- [ ] 16:30-17:30 写 `p10_transforms.py`（覆盖 P10-P11）：演示 ToTensor / Normalize / Resize / RandomCrop / Compose 5 个常用 transform
- [ ] 17:30-18:00 用 Compose 串 `train_transform = [RandomCrop, ToTensor, Normalize]`，验证 callable

### 产出标准

- [ ] TensorBoard 能画出 loss 曲线和图片网格
- [ ] Compose pipeline 跑通
- [ ] **晚上** `git commit -m "day2: TensorBoard + Transforms 上半"`

---

## Day 3（10-03 周六）Transforms 下半 + DataLoader

### 下午 14:00-18:00（4h）

> 上午：自由 / 休息 / 处理杂事

- [ ] 14:00-15:00 P12 + P13 视频，继续常见 transform（RandomHorizontalFlip / ToPILImage / ConvertImageDtype）
- [ ] 15:00-15:30 P14 视频，重点 CIFAR10 / MNIST 的 torchvision API
- [ ] 15:30-15:50 **提前下载 CIFAR10**（避免 Day 9 首次训练时被下载打断）：
  ```python
  from torchvision.datasets import CIFAR10
  CIFAR10(root="../data", train=True, download=True)
  CIFAR10(root="../data", train=False, download=True)
  ```
- [ ] 15:50-16:20 P15 视频，重点 `batch_size / shuffle / num_workers / drop_last`
- [ ] 16:20-17:20 写 `p14_torchvision_datasets.py` + `p15_dataloader.py`：验证 `len()`、`[0]`、DataLoader 4 参数
- [ ] 17:20-18:00 把 P10-P13 所有 transform 合并到 `p10_transforms.py` 跑一遍

### 产出标准

- [ ] `p10_transforms.py` 覆盖 P10-P13 全部 transform
- [ ] CIFAR10 train loader 能迭代，shape 是 `[B, 3, 32, 32]`
- [ ] `../data/cifar-10-batches-py/` 目录已就绪
- [ ] **晚上** `git commit -m "day3: Transforms 下半 + DataLoader + CIFAR10 数据"`

---

## Day 4（10-04 周日）nn.Module + Conv2d 概念

### 下午 14:00-18:00（4h）

> 上午：自由 / 休息 / 处理杂事

- [ ] 14:00-14:20 P17 卷积概念，看懂卷积核怎么滑、stride / padding / channel 关系
- [ ] 14:20-15:00 P16 视频，重点 `__init__` 里 `super().__init__()` + 用 `nn.Module` 必须写成属性才被注册
- [ ] 15:00-15:40 写 `p16_nn_module.py`：写一个最小 `nn.Module` 子类
  ```python
  class TinyNet(nn.Module):
      def __init__(self):
          super().__init__()
          self.fc = nn.Linear(784, 10)
      def forward(self, x):
          return self.fc(x)
  ```
  跑通 `model(torch.randn(2, 784))`，用 `print(model)` 看参数列表
- [ ] 15:40-16:20 P18 视频，重点 Conv2d 参数 `in_channels / out_channels / kernel_size / stride / padding`
- [ ] 16:20-17:20 写 `p18_conv2d.py`：写 `nn.Conv2d(3, 32, 5, padding=2)`，输入 `[1,3,32,32]`，观察输出 shape
- [ ] 17:20-18:00 在笔记里画一张 VGG-like block：`Conv → Conv → Pool → ReLU` 的输入输出尺寸

### 产出标准

- [ ] nn.Module 子类 forward 跑通
- [ ] Conv2d 输出 shape 能算
- [ ] **晚上** `git commit -m "day4: nn.Module + Conv2d"`

---

## Day 5（10-05 周一）MaxPool + ReLU + Linear

### 下午 14:00-18:00（4h）

> 上午：自由 / 休息 / 处理杂事

- [ ] 14:00-15:00 P19 视频 + 写 `p19_maxpool.py`：`MaxPool2d(2)` 对 Conv 输出池化
- [ ] 15:00-16:00 P20 视频 + 写 `p20_relu_sigmoid.py`：对比 `F.relu(x)` 和 `torch.sigmoid(x)` 的输出范围
- [ ] 16:00-17:00 P21 视频 + 写 `p21_linear.py`：把卷积输出 `flatten` 后接 `nn.Linear`，验证维度对得上
- [ ] 17:00-18:00 拼一个 block：输入 `x=[1,3,32,32]`，过 `Conv→Pool→ReLU→Conv→Pool→Flatten→Linear`，全程 print shape

### 产出标准

- [ ] MaxPool / ReLU / Linear 各自跑通
- [ ] 拼出来的 block 能 forward
- [ ] **晚上** `git commit -m "day5: CNN 三大组件"`

---

## Day 6（10-06 周二）Sequential + Loss + Optimizer

### 下午 14:00-18:00（4h）

> 上午：自由 / 休息 / 处理杂事

- [ ] 14:00-15:00 P22 视频 + 写 `p22_sequential_cifar.py`：用 `nn.Sequential` 拼出视频里的 CIFAR10 网络，**别抄，自己根据 Day 4-5 的 block 拼**
- [ ] 15:00-16:00 P23 视频 + 写 `p23_loss_backward.py`：造 `pred=[B,10]`、`label=[B]` 的假数据，验证 `nn.CrossEntropyLoss` + `loss.backward()` + `weight.grad` 非零
- [ ] 16:00-16:45 P24 视频 + 写 `p24_optimizer.py`：接 P23，加 `optim.SGD`，跑 3 步 `zero_grad → forward → loss → backward → step`
- [ ] 16:45-17:30 **zero_grad 直观教学**：注释掉 `zero_grad()` 跑一次，看 loss 爆炸
- [ ] 17:30-18:00 笔记整理

### 产出标准

- [ ] Sequential CIFAR10 网络能 forward 出 `[B,10]`
- [ ] 手动跑通 3 步训练循环，weight 值在更新
- [ ] 看懂 zero_grad 缺位的后果
- [ ] **晚上** `git commit -m "day6: Sequential CIFAR10 + Loss/Opt"`

---

## Day 7（10-07 周三）Pretrained + Save/Load

### 下午 14:00-18:00（4h）

> 上午：自由 / 休息 / 处理杂事

- [ ] 14:00-15:00 P25 视频，加载 `torchvision.models.vgg16(pretrained=True)`，**改 classifier[6]**，跑一个假 batch
- [ ] 15:00-16:00 写 `p25_pretrained_models.py`：冻结 features / 改最后 fc / 跑一个 fake batch
- [ ] 16:00-16:30 P26 视频，重点 `state_dict()` / `load_state_dict()` / `torch.save` / `torch.load`
- [ ] 16:30-17:30 写 `p26_save_load.py`：保存 / 加载自己 Day 6 的 Sequential CIFAR10 网络
- [ ] 17:30-18:00 整合：把 p25 加载预训练 + p26 保存当前 checkpoint 串成一个小脚本

### 产出标准

- [ ] `p25_pretrained_models.py` 跑通
- [ ] `p26_save_load.py` 跑通
- [ ] **晚上** `git commit -m "day7: 预训练 + 保存/读取"`

---

## Day 8（10-08 周四）完整训练套路

### 下午 14:00-18:00（4h）

> 上午：自由 / 休息 / 处理杂事

- [ ] 14:00-14:05 **GPU 自检**（必做，README P03 FAQ 就是为这个场景）：
  ```bash
  nvidia-smi
  python -c "import torch; print(torch.cuda.is_available(), torch.cuda.get_device_name(0))"
  ```
  - ✅ True → 走 GPU 路线
  - ❌ False → **降级方案**：改用 MNIST 数据集 + 2-3 epoch + 接受 CPU 慢速
- [ ] 14:05-14:35 P27 视频，train 套路上半（train / eval 循环框架）
- [ ] 14:35-15:05 P28 视频，train 套路下半（验证 / 准确率计算）
- [ ] 15:05-15:35 P29 视频，train 套路收尾（save / load 整合）
- [ ] 15:35-16:30 写 `p27_train_cifar.py`（覆盖 P27-P29）：完整训练脚本，`train_loader`、`model.to(device)`、`CrossEntropyLoss`、`optim.Adam`，每 100 step 打印 loss，每个 epoch 结束在测试集算 accuracy
- [ ] 16:30-18:00 跑 1-3 个 epoch 看 loss 是否下降（**不要求跑完 10 epoch，只验证流程**；剩下的留 Day 9）

### 产出标准

- [ ] `p27_train_cifar.py` 能跑（至少 1 epoch）
- [ ] loss 在前 100 step 内有下降趋势
- [ ] **晚上** `git commit -m "day8: 完整训练套路"`

---

## Day 9（10-09 周五）GPU + 验证套路

### 下午 14:00-18:00（4h）

> 上午：自由 / 休息 / 处理杂事

- [ ] 14:00-14:30 P30 + P31 视频，重点 `.to(device)` 三件套位置：模型、输入、标签
- [ ] 14:30-15:00 写 `p30_gpu_train.py`：**从 `p27_train_cifar.py` 复制起步**作为基础，加 `argparse`（设备、数据集路径、epoch 数）和显式 `.to(device)` 三件套
- [ ] 15:00-17:00 跑 CIFAR10 训练（GPU 或 CPU fallback），训练结束 `torch.save(model.state_dict(), "../checkpoints/cifar10_day9.pth")`
- [ ] 17:00-17:30 P32 视频，重点 `model.eval()` + `torch.no_grad()` + `argmax` 取预测
- [ ] 17:30-18:00 写 `p32_evaluate.py` 骨架（不要求真跑通，明天可继续完善）

### 产出标准

- [ ] `p30_gpu_train.py` 用 argparse + `.to(device)` 三件套跑通
- [ ] `checkpoints/cifar10_day9.pth` 文件存在
- [ ] `p32_evaluate.py` 骨架已写
- [ ] **晚上** `git commit -m "day9: GPU 训练 + 验证套路"`

---

## Day 10（10-10 周六）开源 + 复盘

### 下午 14:00-18:00（4h）

> 上午：自由 / 休息 / 处理杂事

- [ ] 14:00-14:30 完善 `p32_evaluate.py`：加载 `cifar10_day9.pth`，算 overall + per-class accuracy，保存一张预测可视化图到 `../logs/p32/`
- [ ] 14:30-15:30 **逛 torchvision 源码**（P33，**只看主结构，不逐行读**）：
  - GitHub: `pytorch/vision`，看 `torchvision/models/resnet.py`
  - 重点找：`class BasicBlock`、`class ResNet`、`forward` 实现
  - **记录**：和 Day 6 自己的 Sequential CIFAR10 对比，哪些组件是相同的
- [ ] 15:30-16:30 **逛 ultralytics/yolov5**（P33，**只定位入口，不逐行读**——`train.py` 实际 1k+ 行）：
  - GitHub: `ultralytics/yolov5`
  - 定位：`models/yolov5s.yaml` 的网络结构、`utils/dataloaders.py` 的 DataLoader、`train.py` 的 `def train()` 函数入口行号
  - **记录**：训练循环在第几行、DataLoader 在第几行（不超过 5 行笔记）
- [ ] 16:30-17:00 **补一个合成 dataset**（`p07_dataset.py` 数据源不稳的兜底）：
  ```python
  class SyntheticDataset(Dataset):
      def __len__(self): return 100
      def __getitem__(self, i):
          return torch.randn(3, 32, 32), i % 10
  ```
  用 Day 9 的训练脚本试跑 1 个 batch，验证 `__getitem__` 接口正确
- [ ] 17:00-17:30 写学习笔记 `notes.md`：每个 PyTorch 概念对应 C# 的一句话、踩过的坑、5 步训练循环代码片段
- [ ] 17:30-18:00 更新 `pytorch学习/README.md`：把 29 项勾完

### 产出标准

- [ ] `p32_evaluate.py` 跑出来 overall accuracy > 10%（> 50% 是加分项）
- [ ] 能口述 yolov5 `train.py` 的主循环入口行号
- [ ] `notes.md` 已写
- [ ] README 29 项勾完
- [ ] **晚上** `git commit -m "day10: 验证 + 开源 + 复盘"`

---

## 四、C# 与 PyTorch 速查表

### 语言层

| C# / .NET | Python / PyTorch |
|---|---|
| `this` | `self` |
| `List<T>` | `list` |
| `Dictionary<K,V>` | `dict` |
| LINQ `Where/Select` | 列表推导式 `[x for x in xs if ...]` |
| `using (...) { }` | `with open(...) as f:` |
| `Main` 入口 | `if __name__ == "__main__":` |
| NuGet | pip / conda |
| `.csproj` | `requirements.txt` / `pyproject.toml` |
| `var x = 1;` | `x = 1`（动态类型） |
| `int.Parse(s)` | `int(s)` |
| `string.Format` / `$""` | `f"{name}"` |
| `interface IFoo` | `class Foo: ...` （鸭子类型，不需要接口声明） |
| `null` | `None` |
| `bool` | `bool`（首字母大写：`True / False`） |
| `async / await` | 也有但 PyTorch 训练里基本不用 |
| `record class` / POCO | `@dataclass` / `NamedTuple`（训练日志、checkpoint metadata 常用） |
| `sealed class` / 派生类 | **PyTorch 反向约定**：默认所有类可继承；`nn.Module` **必须继承**（`class Foo(nn.Module)`），不能组合（`sealed` 思路行不通） |
| `IConfiguration` / `CommandLineParser` / `Microsoft.Extensions.Configuration` | `argparse`（Day 9 写 GPU 训练脚本时绕不开，p30_gpu_train.py 必用） |
| `enum` | `Enum` / `Literal[...]`（transform / model 选择时常碰到） |

### 深度学习层

| C# 类比 | PyTorch 概念 |
|---|---|
| 接口 / 抽象基类 | `nn.Module` |
| 派生类构造函数注册依赖 | `super().__init__()` + `self.fc = nn.Linear(...)`（**必须赋值为属性**才被注册） |
| 业务方法 | `forward(self, x)` |
| `IEnumerable<T>` + yield | `DataLoader`（可迭代，按 batch yield） |
| EF Core DbContext | `Dataset`（数据源抽象） |
| AutoMapper pipeline | `torchvision.transforms.Compose([...])` |
| Event 订阅 + 回调 | `SummaryWriter.add_*`（观察者） |
| `IEnumerable.Select().ToList()` | `tensor.view()` / `tensor.reshape()` |
| 矩阵乘法 `A * B` | `A @ B` 或 `torch.matmul(A, B)` |
| 元素乘法 `A .* B` | `A * B`（逐元素） |
| `IDisposable` | 无对应，PyTorch 一般不用手动释放 |
| 日志框架 `ILogger` | `print` / `logging` / TensorBoard |
| 配置中心 `IOptions<T>` | 全局变量 / Hydra / OmegaConf（Day 10 之后才接触） |
| Gradle / MSBuild target | `optimizer.step()`（参数更新器） |
| Reflection `GetMethod()` | `dir(obj)` + `help(obj)`（P04） |
| `var device = ...` | `device = torch.device("cuda" if torch.cuda.is_available() else "cpu")` |
| `null`-check | `tensor is None` / `tensor == None` |
| `IComparable<T>` | tensor 支持 `> < ==` 逐元素比较 |

---

## 五、常见坑点

### 环境 / 运行

- [ ] **忘了 `conda activate torch`** — 跑出来的是 base 环境的 PyTorch
- [ ] **`cuda.is_available()` 返回 False** — 装的是 CPU 版 torch，重新 `pip install torch --index-url https://download.pytorch.org/whl/cu121`；或者按 Day 8 fallback 降级到 MNIST + CPU
- [ ] **路径分隔符** — Windows 用 `\` 但 Python 字符串里 `\` 是转义符，**统一用正斜杠 `/` 或者 `os.path.join`**

### 数据

- [ ] **DataLoader `num_workers > 0` 在 Windows 上会报错** — 先设 0 跑通，再加
- [ ] **图片读不到** — 用 `PIL.Image.open` 验证一下能不能直接打开
- [ ] **Normalize 的 mean / std** — 必须是 3 个值（RGB），不是 1 个
- [ ] **Compose 顺序写反** — `Normalize` 必须接在 `ToTensor` 之后，**Tensor 才有 mean/std 的概念**
- [ ] **CIFAR10 / hymenoptera 首次跑会下载很久** — Day 3 / Day 10 提前手动触发 download

### 模型

- [ ] **层没有赋值为属性** — `self.conv = nn.Conv2d(...)` 而不是 `nn.Conv2d(...)`，否则不参与 `parameters()`
- [ ] **忘了 `super().__init__()`** — 各种 hook（state_dict、cuda）会失效
- [ ] **forward 里写 `if x.shape[0]:`** — 第一次跑就崩，改成 `assert`
- [ ] **想用 sealed class 封 `nn.Module`** — **不行**，PyTorch 要求继承，不能组合

### 训练循环

- [ ] **忘记 `optimizer.zero_grad()`** — 梯度累加，loss 看起来不下降或爆炸
- [ ] **`loss.backward()` 之前没 `loss = loss_fn(pred, label)`** — 报 `NoneType` 没有 backward
- [ ] **CPU 张量喂给 GPU 模型** — 报 `RuntimeError: Expected all tensors to be on the same device`
- [ ] **训练时忘了 `model.train()`** — Dropout / BatchNorm 行为不对
- [ ] **验证时忘了 `model.eval()` + `torch.no_grad()`** — 显存爆炸，结果也不准
- [ ] **shape 对不上** — Linear 输入维度算错，最常见的报错

### 保存 / 加载

- [ ] **`torch.load` 不加 `map_location`** — 在 CPU 机器上加载 GPU checkpoint 报错
- [ ] **只保存了 `model` 没保存 `state_dict`** — 推荐只存 state_dict，体积小、跨版本稳

---

## 六、备用命令清单

### 激活环境

```bash
# conda
conda activate torch
conda deactivate

# venv（如果某天不用 conda）
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS / Linux
```

### 包管理

```bash
# conda
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
conda list | grep torch

# pip
pip install torch torchvision torchaudio
pip freeze > requirements.txt
pip install -r requirements.txt
```

### Jupyter

```bash
# 安装
conda install jupyter notebook
pip install ipykernel
python -m ipykernel install --user --name=torch --display-name "Python (torch)"

# 启动（在项目目录）
jupyter notebook
# 或新版
jupyter lab
```

### TensorBoard

```bash
# 安装（conda 环境里一般已经有，没有就装）
pip install tensorboard

# 启动（在仓库根目录）
tensorboard --logdir=../logs
# 然后浏览器打开 http://localhost:6006
```

### GPU 自检

```bash
nvidia-smi                                  # 看 GPU 占用
python -c "import torch; print(torch.cuda.is_available(), torch.version.cuda)"
```

### 训练时常用开关

```python
torch.manual_seed(42)                       # 复现性
torch.backends.cudnn.benchmark = True       # 输入尺寸固定时加速
```

---

## 七、Day 10 验收 checklist

### 工具与数据

- [ ] P04 dir/help 用熟，能查到任意类的可用方法
- [ ] P06 概念理解（Dataset / DataLoader / Transform 职责划分）
- [ ] P07 自定义 Dataset 子类跑通
- [ ] P08+P09 TensorBoard 能画 scalar 和 image
- [ ] P10-P13 Transforms Compose pipeline 跑通
- [ ] P14 torchvision.datasets.CIFAR10 能加载
- [ ] P15 DataLoader 4 个关键参数会调

### 网络组件

- [ ] P16 nn.Module 子类 forward 跑通
- [ ] P17 卷积概念理解
- [ ] P18 Conv2d 输出 shape 能算
- [ ] P19 MaxPool 输出 shape 能算
- [ ] P20 ReLU / Sigmoid 行为对比
- [ ] P21 Linear 接 Flatten 输出

### 训练与部署

- [ ] P22 Sequential CIFAR10 网络跑通
- [ ] P23 CrossEntropyLoss + backward 跑通
- [ ] P24 optimizer.step() 参数确实在更新
- [ ] P25 加载预训练 vgg16 并修改最后一层
- [ ] P26 state_dict 保存 / 加载跑通
- [ ] P27-P29 完整训练循环跑通
- [ ] P30-P31 模型搬到 GPU 上训练（**p30_gpu_train.py 独立文件，argparse + 三件套**）
- [ ] P32 验证脚本能加载 checkpoint 算 accuracy

### 开源与复盘

- [ ] P33 torchvision/resnet.py 主结构看过
- [ ] P33 ultralytics/yolov5 `train.py` 入口行号定位到
- [ ] `notes.md` 已写
- [ ] README 29 项全部勾完
- [ ] 10 天 git commit 齐

### 最终标志

- [ ] **`checkpoints/cifar10_day9.pth` 存在**，加载后 **loss 单调下降 + test acc > 10%**（> 50% 是加分项）

---

## 八、压缩版 fallback（每天只 2-3h 时的极限砍法）

如果某天状态不好 / 中断，按这个优先级砍：

| 天 | 必做 | 可砍 |
|---|---|---|
| Day 1 | P04 + P07，能跑就行 | C# 小抄 / Tensor 预热全砍 |
| Day 2 | P08 + P10，TensorBoard 画一条曲线 + Compose 基础 | P11 跳过 |
| Day 3 | P14 + P15 | P12 / P13 跳过，Compose 直接抄视频代码 |
| Day 4 | P16 + P18 | P17 卷积概念跳过 |
| Day 5 | P21 Linear | P19 / P20 合并到一个文件 |
| Day 6 | P22 + P23 | P24 用 SGD 不演示 Adam；zero_grad 直观教学跳过 |
| Day 7 | P25 + P26 框架跑通 | pretrained 详细演示跳过 |
| Day 8 | 写出能跑的 `p27_train_cifar.py` | P27-P29 只看一遍，抄视频 train 循环模板 |
| Day 9 | `p30_gpu_train.py` 跑通 + checkpoint 落地 | P32 验证脚本骨架可留到 Day 10 |
| Day 10 | `p32_evaluate.py` 跑通 + P33 逛源码（只定位入口） | 合成 dataset 可跳过 |

压缩版的目标从"全部跑通 + 50% acc"降到"全部写完 + 至少 CIFAR10 能跑 loss 下降"。

---

## 九、节奏自检（每个 Day 开始前问自己）

- [ ] 昨天的产出文件都跑通了？
- [ ] `git log --oneline | head -5` 看看 commit 节奏
- [ ] `git status` 是否有未提交改动？
- [ ] conda 环境是 `torch`？
- [ ] `nvidia-smi` 显存空闲？

10 天结束，仓库应该长这样：

```
pytorch学习/
├── README.md                       # 29 项已勾完
├── 国庆节PyTorch推进表.md          # 本文件
├── notes.md                        # Day 10 写的笔记
├── notes/
│   └── day1_cs_cheatsheet.md       # Day 1 下午的 C# ↔ Python 类比小抄
├── p04_dir_help.py
├── p07_dataset.py
├── p08_tensorboard.py
├── p10_transforms.py               # 覆盖 P10-P13 全部 transform
├── p14_torchvision_datasets.py
├── p15_dataloader.py
├── p16_nn_module.py
├── p18_conv2d.py
├── p19_maxpool.py
├── p20_relu_sigmoid.py
├── p21_linear.py
├── p22_sequential_cifar.py
├── p23_loss_backward.py
├── p24_optimizer.py
├── p25_pretrained_models.py
├── p26_save_load.py
├── p27_train_cifar.py              # Day 8 写
├── p30_gpu_train.py                # Day 9 写（显式 GPU 版本：argparse + 三件套）
├── p32_evaluate.py                 # Day 9 骨架 + Day 10 完善
└── ../checkpoints/cifar10_day9.pth # Day 9 产物
```

---

## 修订记录

### v3（2026-09-30）— 10 天 × 4h 精简版

应用户要求：觉得 7 天 × 8h 弄不完，改成 **10 天 × 4h**。总时长从 56h 降到 40h，节奏更松。

**核心改动**：

1. **日期范围**：2026-10-01（周四）~ 2026-10-10（周六），共 10 天
2. **每日时长**：14:00-18:00（4h，含 15 分钟休息）
3. **P04-P33 重新分配**（29 集 → 10 天）：
   - Day 1 (3 集): P04 / P06 / P07
   - Day 2 (4 集): P08 / P09 / P10 / P11
   - Day 3 (4 集): P12 / P13 / P14 / P15
   - Day 4 (3 集): P16 / P17 / P18
   - Day 5 (3 集): P19 / P20 / P21
   - Day 6 (3 集): P22 / P23 / P24
   - Day 7 (2 集): P25 / P26
   - Day 8 (3 集): P27 / P28 / P29
   - Day 9 (3 集): P30 / P31 / P32
   - Day 10 (1 集): P33
4. **取消原 Day 6 单点风险修订**：原 Day 6 把 P25 挪到 Day 7，现在 P25/P26 自然分到 Day 7，无需特殊处理
5. **压缩版真正 fallback**：每天 4h 是主版本，压缩版砍到 2-3h 是真 fallback（之前 v2 的压缩版"3-4h"已不再是压缩）
6. **验证脚本 p32 拆分**：Day 9 写骨架，Day 10 完善 + 跑通
7. **CIFAR10 checkpoint 路径**：cifar10_day6.pth → **cifar10_day9.pth**
8. **验收 checklist 改为"Day 10 验收"**

**未改动**：C# 对照表、坑点清单、备用命令（这两节独立于天数）

### v2（2026-09-30）— 压到下午

应用户要求：把原来"上午 4h + 下午 4h"的分散安排，**统一压到下午 14:00-22:00（8h）**；上午改为自由/休息 / 处理杂事。

**修改点**：

1. **元信息**：新增"每日学习时间安排"项
2. **总时间安排表**：删除"上午 4h"列，把内容合并到"下午"列，标题改为"下午 14:00-22:00（8h）"
3. **Day 1-7 每天**：删除`### 上午 4h（...）`小节，原上午任务顺延到下午 14:00-22:00 时间盒内（0:00-4:00），与原下午任务（4:00-8:00）合并，用 `#### 视频 + 概念` 和 `#### 代码` 两个子时段标识
4. 每天上午明确标注为 "上午：自由 / 休息 / 处理杂事"
5. 下午含 30 分钟晚餐休息，可分 14:00-18:30 + 19:00-22:00 两段

### v1（2026-09-30）— 初稿

Generator（综合 `deepseek_markdown_20260930_0507e5.md` 的 7 天主题 + `pytorch学习\README.md` 的 P04-P33 集数）→ Adversarial Critic 评审 → 主循环根据评审修订定稿。

**关键修订**（针对评审发现的问题）：

1. **Day 6 单点风险**：把 P25（pretrained models）整集从 Day 6 挪到 Day 7 上午，Day 6 改为 6 集视频 + GPU 自检
2. **GPU 失败 fallback**：Day 6 上午开头加 5 分钟 GPU 自检 + 降级方案
3. **文件路径统一**：Day 6 下午显式建独立 `p30_gpu_train.py`
4. **目标降级**：test acc 主目标从 > 50% 改为 > 10%，50% 作加分项
5. **C# 对照补 4 项**：`record/POCO ↔ @dataclass/NamedTuple`、`sealed class ↔ PyTorch 反向继承约定`、`IConfiguration ↔ argparse`、`enum ↔ Enum/Literal`
6. **Day 5 下午**加 `zero_grad` 缺位直观教学
7. **Day 3 上午**加 CIFAR10 提前下载
8. **Day 7 逛 yolov5** 改为只定位入口
9. **每个 Day** 末尾加 git commit 时点
10. **Day 7 上午**加合成 dataset
11. **Day 1 上午**加 C# 类比小抄 + Tensor 形状预热
12. **压缩版 Day 6** 加"训练全崩的最低可交付物"说明
13. **坑点表**加 "CIFAR10 / hymenoptera 首次跑会下载很久"、"sealed class 封 nn.Module 不行"