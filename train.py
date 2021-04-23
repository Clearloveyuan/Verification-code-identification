"""
实战3
代码10-5
识别验证码的卷积神经网络训练程序
"""
from net_model import CNN                                 # 引入网络模型
import torch                                                # 引入torch模块
import torch.nn as nn                                       # 引入torch.nn模块
import numpy as np                                          # 引入np模块

cnn = CNN().cuda()                                          # 加载网络结构并传入GPU

for epoch in range(1000):
    m = 20                                  # 每个字符的样本数
    x = np.load('train_set.npy')            # 加载训练集
    x = torch.tensor(x).float().cuda()      # 转换成FloatTensor类型并传入GPU
    y = np.zeros(62*m)                      # 创建空白标签数组
    k = 0
    for i in range(62):
        for j in range(m):
            y[k] = i
            k += 1                          # 标签赋值
    y = torch.tensor(y).long().cuda()       # 标签转化成LongTensor类型并传入GPU

    optimizer = torch.optim.Adam(cnn.parameters(), lr=0.001)        # Adam优化器
    loss_func = nn.CrossEntropyLoss()                               # 损失函数

    out = cnn(x)                                                    # 输出结果
    loss = loss_func(out, y)                                        # 计算loss值
    optimizer.zero_grad()                                           # 清除梯度
    loss.backward()                                                 # 反向传播
    optimizer.step()                                                # 进行优化
    if epoch % 25 == 0:                                             # 每25epoch显示
        print(f'epoch:{epoch}')
        print(loss.data)                                            # 打印loss数据
        loss_cpu = loss.cpu()                                       # loss值传回CPU
        if loss_cpu.data.detach().numpy() < 0.05:                   # loss值小于0.05时停止训练
            break

torch.save(cnn, 'net.pkl')                                          # 保存网络
