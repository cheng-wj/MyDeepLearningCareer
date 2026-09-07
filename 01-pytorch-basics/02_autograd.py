"""
第 2 课：自动求导(autograd)与训练循环
=====================================
知识点：
  1. requires_grad=True 的张量，PyTorch 会自动记录对它的所有运算
  2. 调用 loss.backward() 后，梯度自动累积到 .grad 属性里 —— 这就是反向传播
  3. 优化步骤：梯度清零 -> 前向算损失 -> backward 反向传播 -> 更新参数
  4. 本课不用 nn.Module，手写一个线性回归，把"训练"这件事看个透

任务：拟合一条直线 y = 3x + 2，带噪声。
模型只有两个参数：权重 w 和偏置 b。
"""
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"使用设备: {device}\n")

torch.manual_seed(0)

# ---- 造数据：y = 3x + 2 + 噪声 ----
true_w, true_b = 3.0, 2.0
X = torch.linspace(-5, 5, 100, device=device).unsqueeze(1)   # shape (100, 1)
noise = 0.3 * torch.randn(X.shape, device=device)
y = true_w * X + true_b + noise

# ---- 待学习的参数：初始随便给，requires_grad=True 告诉 PyTorch 要追踪梯度 ----
w = torch.tensor(0.0, device=device, requires_grad=True)
b = torch.tensor(0.0, device=device, requires_grad=True)

lr = 0.05       # 学习率
n_epochs = 200

for epoch in range(1, n_epochs + 1):
    # 1. 前向传播：用当前 w, b 预测
    y_pred = w * X + b

    # 2. 算损失：均方误差 MSE
    loss = ((y_pred - y) ** 2).mean()

    # 3. 反向传播：自动算出 loss 对 w、b 的偏导，存进 w.grad / b.grad
    loss.backward()

    # 4. 更新参数（torch.no_grad() 里更新，否则更新动作本身也会被记录进计算图）
    with torch.no_grad():
        w -= lr * w.grad
        b -= lr * b.grad

    # 5. 梯度清零！不清零的话 .grad 会一直累加（这是新手最常踩的坑）
    w.grad.zero_()
    b.grad.zero_()

    if epoch % 40 == 0 or epoch == 1:
        print(f"epoch {epoch:3d} | loss {loss.item():.4f} | w = {w.item():.3f} | b = {b.item():.3f}")

print(f"\n训练结束：学到的 w = {w.item():.3f}（真实 {true_w}），b = {b.item():.3f}（真实 {true_b}）")
print("可以看到参数自动收敛到了真实值 —— 这就是深度学习训练最核心的机制。")
