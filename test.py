"""
实战3
代码10-6
识别验证码的卷积神经网络测试程序
"""
import numpy as np                                  # 引入numpy模块
from net_model import CNN                           # 引入网络模型
import os                                           # 引入os模块
import cv2 as cv                                    # 引入cv2模块
from string_segmentation import cut_apart           # 引入cut_part函数
import torch                                        # 引入torch模块


def discriminate(cut_result):   # 分辨字符函数
    net = CNN().cuda()
    net = torch.load('net.pkl')                              # 读取网络
    cut_result_resize = np.zeros(4*32*32, dtype='uint8')     # 新建一数组用来存放改变尺寸后的切割结果
    cut_result_resize = np.reshape(cut_result_resize, (4, 1, 32, 32))   # 更改成可以输入的张量
    for i in range(4):
        cut_result_resize[i, 0, :, :] = cv.resize(cut_result[i, :, :], (32, 32))    # 改变每个字符的尺寸
    x = torch.tensor(cut_result_resize).float().cuda()              # 转换成tensor变量，传入GPU
    y = net(x)                                               # 传入网络得到结果
    return y                                                 # 返回结果


if __name__ == '__main__':
    filenames = os.listdir('./sample/test')                  # 读取所有测试集文件
    c_n = 0                                                  # 正确数量
    error = 0
    for i in range(300):                                     # 遍历文件循环
        img = cv.imread(f'./sample/test/{filenames[i]}')     # 读取图片
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)       # 转换为灰度图像
        thresh1, img_bin = cv.threshold(img_gray, 200, 255, cv.THRESH_BINARY_INV)  # 转换成二值图
        cut_result = cut_apart(img_bin)                      # 切割图片
        dis_result = discriminate(cut_result)                # 分辨字符
        string_result = [''] * 4                             # 创建空白列表存放最后转换的结果
        s = torch.max(dis_result.data, 1)[1].data            # 找到最大下标
        for j in range(4):                                   # 判断下标对应的字符
            if s[j] < 10:                                    # 数字
                string_result[j] = str(s[j].data.cpu().numpy())
            elif (s[j] >= 10) & (s[j] < 36):                 # 大写字母
                string_result[j] = chr(s[j] + 55)
            elif s[j] >= 36:                                 # 小写字母
                string_result[j] = chr(s[j] + 61)
        if filenames[i][-8:-4] == ''.join(string_result):    # 判断结果与标签是否一致
            c_n += 1
        # print('\r' + f'正在识别，当前第{i+1}个', end=' ', flush=True)     # 动态显示生成过程
    # print('')
        else:
            ss = ''.join(string_result)
            error += 1
            print(f'错误{error}：正确结果为{filenames[i][-8:-4]}，识别为{ss}')
    print(f'识别完成！准确率为：{c_n/300}')



