"""
实战3
代码10-2
验证码分割程序
将每个验证码分割成单独的字符
存入相应的文件夹中
"""
import cv2 as cv                                            # 引入cv2模块
import os                                                   # 引入os模块
import numpy as np                                          # 引入numpy模块


def cut_apart(img):                                         # 切割函数
    cut_result = np.zeros(30*30*4, dtype='uint8')
    cut_result = np.reshape(cut_result, (4, 30, 30))        # 新建空白数组存储切割结果
    for i in range(4):                                      # 获取分割
        cut_result[i, :, :] = img[:, i*30:i*30+30]
    return cut_result                                       # 返回分割结果数组


def save_apart(path, m):                                    # 保存分割结果函数
    filenames = os.listdir(path)                            # 读取每个文件的文件名
    for i in range(m):                                      # 遍历所有样本
        img = cv.imread(f'{path}/{filenames[i]}')           # 读取样本
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)      # 转成灰度图
        thresh1, img_bin = cv.threshold(img_gray, 200, 255, cv.THRESH_BINARY_INV)  # 转换成二值图
        cut_result = cut_apart(img_bin)                     # 开始切割

        # 存到相应的文件夹中
        for j in range(4):
            path1 = f'./sample/train_seg/{filenames[i][-8 + j]}'
            img_seg = cut_result[j, :, :]
            s = filenames[i][-8 + j]

            if (ord(s) >= 97) & (ord(s) <= 122):                        # 判断是否为小写字母
                path1 = f'./sample/train_seg/{filenames[i][-8 + j]}0'   # 在小写字母后面加0用来和大写字母区分

            if os.path.exists(path1):       # 判断路径是否存在，若存在即保存到相应的文件夹
                cv.imwrite(f'{path1}/{filenames[i][-8 + j]}_{i}.png', img_seg)
            else:
                os.mkdir(path1)             # 路径不存在，则新建文件夹之后再存入
                cv.imwrite(f'{path1}/{filenames[i][-8 + j]}_{i}.png', img_seg)
        print('\r' + f'当前第{i + 1}个', end=' ', flush=True)  # 动态显示分割过程


if __name__ == '__main__':                # 主程序
    path = './sample/train'               # 要分割验证码的文件夹的路径
    m = 700                               # 样本数量
    if os.path.exists(path):              # 判断路径是否存在
        save_apart(path, m)               # 保存分割函数

    else:
        print(f'路径{path}不存在')