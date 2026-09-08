# PyTorch 学习（跟练小土堆教程）

配套视频：小土堆《PyTorch深度学习快速入门教程》
链接：https://www.bilibili.com/video/BV1hE411t7RN （共 33 集，约 10 小时）

## 怎么用这个文件夹

1. 看一集视频，然后打开对应的 `pXX_*.py` 练习文件
2. 文件里只有知识点提示和 API 关键词，**实现自己写，不要抄视频代码**
3. 写完跑通，再回来勾掉下面清单
4. 报错先自己读 traceback 最后三行，实在卡住再问

已完成的环境：conda 环境 `torch`（PyTorch 2.11 + CUDA），运行前 `conda activate torch`。
数据集自动下载到仓库根目录 `data/`，权重放 `checkpoints/`，TensorBoard 日志放 `logs/`，均已 gitignore。

## 进度清单

- [x] P01 PyTorch 环境配置（已完成）
- [x] P02 编辑器安装配置（PyCharm / VS Code 都已就绪）
- [x] P03 FAQ：cuda.is_available 返回 False（环境已验证 True）
- [ ] P04 两大法宝函数 dir() / help() → `p04_dir_help.py`
- [x] P05 PyCharm/Jupyter 使用（环境已就绪，可跳过）
- [ ] P06 加载数据初认识（概念，看视频即可）
- [ ] P07 Dataset 类代码实战 → `p07_dataset.py`
- [ ] P08 TensorBoard（一）→ `p08_tensorboard.py`
- [ ] P09 TensorBoard（二）→ 同上文件
- [ ] P10 Transforms（一）→ `p10_transforms.py`
- [ ] P11 Transforms（二）→ 同上文件
- [ ] P12 常见 Transforms（一）→ 同上文件
- [ ] P13 常见 Transforms（二）→ 同上文件
- [ ] P14 torchvision 数据集使用 → `p14_torchvision_datasets.py`
- [ ] P15 DataLoader 的使用 → `p15_dataloader.py`
- [ ] P16 nn.Module 基本骨架 → `p16_nn_module.py`
- [ ] P17 土堆说卷积操作（可选，概念向，看懂即可）
- [ ] P18 卷积层 Conv2d → `p18_conv2d.py`
- [ ] P19 最大池化 MaxPool → `p19_maxpool.py`
- [ ] P20 非线性激活 ReLU/Sigmoid → `p20_relu_sigmoid.py`
- [ ] P21 线性层 Linear → `p21_linear.py`
- [ ] P22 Sequential 搭建 CIFAR10 小网络 → `p22_sequential_cifar.py`
- [ ] P23 损失函数与反向传播 → `p23_loss_backward.py`
- [ ] P24 优化器 → `p24_optimizer.py`
- [ ] P25 现有网络模型的使用及修改 → `p25_pretrained_models.py`
- [ ] P26 模型保存与读取 → `p26_save_load.py`
- [ ] P27 完整训练套路（一）→ `p27_train_cifar.py`
- [ ] P28 完整训练套路（二）→ 同上文件
- [ ] P29 完整训练套路（三）→ 同上文件
- [ ] P30 利用 GPU 训练（一）→ `p30_gpu_train.py`
- [ ] P31 利用 GPU 训练（二）→ 同上文件
- [ ] P32 完整的模型验证套路 → `p32_evaluate.py`
- [ ] P33 完结：看看开源项目（去 GitHub 逛 torchvision、ultralytics/yolov5 的源码）

## 和仓库已有课程的关系

`../01-pytorch-basics/` 里是四课已经写完整的示例（张量、autograd、MLP 双月、MNIST CNN）。
跟练到对应集数时可以打开对照，但建议先自己写、写完再看。
