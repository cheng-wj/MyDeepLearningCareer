"""
第 3 课：MLP 双月分类 —— 第一个完整的神经网络训练流程
=====================================================
知识点：
  1. nn.Module：把网络结构写成一个类，__init__ 里定层，forward 里定数据流
  2. nn.Sequential / nn.Linear / nn.ReLU：全连接层和激活函数
  3. DataLoader + TensorDataset：按批次(batch)喂数据
  4. 完整训练循环：zero_grad -> forward -> loss -> backward -> step
  5. 模型存取：torch.save(model.state_dict())
  6. 分类问题用 BCEWithLogitsLoss（二分类），输出概率用 sigmoid

任务：把二维平面上两个月牙形状的点分成两类。
"""
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# 仓库根目录：本文件在 <root>/01-pytorch-basics/ 下，所以 parents[1] 是根目录
ROOT = Path(__file__).resolve().parents[1]

SEED = 42
N_SAMPLES = 1000
NOISE = 0.2
BATCH_SIZE = 64
EPOCHS = 300
LR = 0.01

torch.manual_seed(SEED)
np.random.seed(SEED)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"使用设备: {device}")


def make_moons(n_samples, noise):
    """生成双月形状的二分类数据（纯 numpy，不依赖 sklearn）。"""
    n = n_samples // 2
    theta = np.pi * np.random.rand(n)
    x1, y1 = np.cos(theta), np.sin(theta)               # 上半月
    x2, y2 = 1 - np.cos(theta), -np.sin(theta) + 0.5   # 下半月
    X = np.vstack([np.column_stack([x1, y1]),
                   np.column_stack([x2, y2])])
    y = np.array([0] * n + [1] * n)
    X += noise * np.random.randn(*X.shape)
    idx = np.random.permutation(len(X))
    return X[idx].astype(np.float32), y[idx].astype(np.float32)


class MLP(nn.Module):
    """三层全连接网络：2 维输入 -> 32 -> 32 -> 1 维输出。"""
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(2, 32),
            nn.ReLU(),
            nn.Linear(32, 32),
            nn.ReLU(),
            nn.Linear(32, 1),
        )

    def forward(self, x):
        return self.net(x).squeeze(-1)


def main():
    X, y = make_moons(N_SAMPLES, NOISE)
    n_train = int(0.8 * len(X))
    X_train, X_test = X[:n_train], X[n_train:]
    y_train, y_test = y[:n_train], y[n_train:]

    train_ds = TensorDataset(torch.from_numpy(X_train), torch.from_numpy(y_train))
    train_loader = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True)

    model = MLP().to(device)
    criterion = nn.BCEWithLogitsLoss()          # 二分类损失（内部自带 sigmoid，更稳定）
    optimizer = torch.optim.Adam(model.parameters(), lr=LR)

    X_test_t = torch.from_numpy(X_test).to(device)
    y_test_t = torch.from_numpy(y_test).to(device)

    print("开始训练...")
    acc = 0.0
    for epoch in range(1, EPOCHS + 1):
        model.train()
        total_loss = 0.0
        for xb, yb in train_loader:
            xb, yb = xb.to(device), yb.to(device)
            optimizer.zero_grad()
            loss = criterion(model(xb), yb)
            loss.backward()
            optimizer.step()
            total_loss += loss.item() * len(xb)

        if epoch % 30 == 0 or epoch == 1:
            model.eval()
            with torch.no_grad():
                pred = (torch.sigmoid(model(X_test_t)) > 0.5).float()
                acc = (pred == y_test_t).float().mean().item()
            print(f"epoch {epoch:3d} | train loss {total_loss / n_train:.4f} | test acc {acc:.4f}")

    ckpt = ROOT / "checkpoints" / "moons_mlp.pt"
    ckpt.parent.mkdir(exist_ok=True)
    torch.save(model.state_dict(), ckpt)
    print(f"模型权重已保存到 {ckpt}")

    # ---- 画决策边界：在整个平面网格上预测，看网络学到的分界线 ----
    model.eval()
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 300),
                         np.linspace(y_min, y_max, 300))
    grid = np.column_stack([xx.ravel(), yy.ravel()]).astype(np.float32)
    with torch.no_grad():
        z = torch.sigmoid(model(torch.from_numpy(grid).to(device))).cpu().numpy()
    z = z.reshape(xx.shape)

    plt.figure(figsize=(7, 6))
    plt.contourf(xx, yy, z, levels=50, cmap="RdBu", alpha=0.6)
    plt.contour(xx, yy, z, levels=[0.5], colors="k", linewidths=1)
    plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap="RdBu",
                edgecolors="k", s=18, alpha=0.8)
    plt.title(f"Two Moons - MLP (test acc {acc:.2%})")
    plt.tight_layout()
    out = ROOT / "outputs" / "moons_decision_boundary.png"
    out.parent.mkdir(exist_ok=True)
    plt.savefig(out, dpi=150)
    print(f"决策边界图已保存到 {out}")


if __name__ == "__main__":
    main()
