"""
P04 Python学习中的两大法宝函数：dir() 和 help()
用法示例：
  - dir(torch)            看一个模块/对象里有什么
  - dir(torch.cuda)       看 cuda 相关的属性和方法
  - help(torch.cuda.is_available)   看某个函数怎么用
练习：随便挑一个你好奇的对象（torch、torch.Tensor、一个张量 x），
先用 dir() 列出它的成员，再挑一个方法用 help() 看文档。
"""
import torch

print(dir(torch)[:5])
print(dir(torch.cuda)[:5])
help(torch.cuda.is_available)
# print([n for n in dir(torch) if not n.startswith('_')])

# TODO: 用 dir() 查看 torch 和 torch.cuda 的成员
# TODO: 用 help() 查看 is_available / 其他你感兴趣的函数的说明
