"""
实战2
代码8-2
测试样本集程序
从数据集中读出cat.69和dog.70
"""
import cv2 as cv                            # 引入OpenCV模块
import numpy as np                          # 引入numpy模块

train_set = np.load('cat_train_set.npy')     # 读取训练集
test_set = np.load('cat_test_set.npy')       # 读取测试集
img1 = train_set[69, 0, :, :]                # 训练集第70个图片
img2 = test_set[30, 0, :, :]                 # 测试集第31个图片
img1 = img1.astype(np.uint8)
img2 = img2.astype(np.uint8)                 # 由float型转换成uint8
cv.imshow('cat.69.jpg', img1)
cv.imshow('dog.70.jpg', img2)                # 显示图片
cv.waitKey(0)