"""
第 4 课：CNN 手写数字识别（MNIST）
==================================
知识点：
  1. 卷积层 nn.Conv2d：在图像上滑动小窗口(卷积核)，自动学边缘、笔画等局部特征
  2. 池化层 nn.MaxPool2d：下采样，让特征图变小、视野变大
  3. 为什么 CNN 比全连接更适合图像：参数少、会利用空间结构
  4. torchvision.datasets：加载标准数据集（自动下载），DataLoader 分批
  5. 多分类用 CrossEntropyLoss（内含 softmax），预测取 argmax
  6. Dropout：训练时随机丢弃部分神经元，抑制过拟合

任务：识别 28x28 的手写数字（0-9），测试准确率约 99%。
"""
from pathlib import Path

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

ROOT = Path(__file__).resolve().parents[1]

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
MNIST_MEAN = (0.1307,)
MNIST_STD = (0.3081,)


class CNN(nn.Module):
    """Conv -> Pool -> Conv -> Pool -> 全连接 -> 全连接。"""
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.fc1 = nn.Linear(64 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 10)
        self.dropout = nn.Dropout(0.25)

    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), 2)   # 28x28 -> 14x14
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)   # 14x14 -> 7x7
        x = torch.flatten(x, 1)
        x = self.dropout(F.relu(self.fc1(x)))
        return self.fc2(x)


def main():
    BATCH_SIZE = 128
    EPOCHS = 5
    LR = 1e-3

    print(f"使用设备: {device}")

    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(MNIST_MEAN, MNIST_STD),
    ])

    data_dir = ROOT / "data"
    train_set = datasets.MNIST(data_dir, train=True, download=True, transform=transform)
    test_set = datasets.MNIST(data_dir, train=False, download=True, transform=transform)
    train_loader = DataLoader(train_set, batch_size=BATCH_SIZE, shuffle=True)
    test_loader = DataLoader(test_set, batch_size=512, shuffle=False)

    model = CNN().to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=LR)
    criterion = nn.CrossEntropyLoss()

    def evaluate():
        model.eval()
        correct = total = 0
        with torch.no_grad():
            for xb, yb in test_loader:
                xb, yb = xb.to(device), yb.to(device)
                pred = model(xb).argmax(dim=1)
                correct += (pred == yb).sum().item()
                total += yb.size(0)
        return correct / total

    for epoch in range(1, EPOCHS + 1):
        model.train()
        total_loss = 0.0
        for xb, yb in train_loader:
            xb, yb = xb.to(device), yb.to(device)
            optimizer.zero_grad()
            loss = criterion(model(xb), yb)
            loss.backward()
            optimizer.step()
            total_loss += loss.item() * yb.size(0)

        acc = evaluate()
        print(f"epoch {epoch} | train loss {total_loss / len(train_set):.4f} | test acc {acc:.4f}")

    ckpt = ROOT / "checkpoints" / "mnist_cnn.pt"
    torch.save(model.state_dict(), ckpt)
    print(f"模型权重已保存到 {ckpt}")


if __name__ == "__main__":
    main()
