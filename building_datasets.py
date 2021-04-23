"""
实战3
代码10-3
构建训练集程序
将训练集每个字符的前20个样本存入一个npy文件中
"""
import cv2 as cv                                                   # 引入OpenCV模块
import numpy as np                                                 # 引入numpy模块
import os                                                          # 引入os模块


if __name__ == '__main__':                                         # 主程序
    m = 20                                                         # 单个字符的样本数量
    x = np.zeros(62*m*1*32*32)
    x = np.reshape(x, (62*m, 1, 32, 32))                           # 构造4维矩阵
    n = 0
    for label in range(62):                                        # 区分不同的字符来遍历所有字符文件夹
        if label < 10:
            label0 = label
        elif (label >= 10) & (label < 36):
            label0 = chr(label+55)
        elif label >= 36:
            label0 = chr(label+61) + '0'                            # 如果是小写字母就在末尾加0
        filenames = os.listdir(f'./sample/train_seg/{label0}')      # 获得对应字符文件夹中的所有文件名

        for i in range(m):                                          # 处理文件夹中的字符文件
            img = cv.imread(f'./sample/train_seg/{label0}/{filenames[i]}')  # 读取样本
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)               # 灰度化处理
            img = cv.resize(img, (32, 32))                          # 调整到网络输入规定的尺寸
            img = np.reshape(img, (1, 32, 32))                      # 调整为3位矩阵，1为通道数
            x[n] = img/255                                          # 简单归一化处理
            n += 1
    np.save('train_set.npy', x)                                     # 保存为npy文件
    print('生成成功')