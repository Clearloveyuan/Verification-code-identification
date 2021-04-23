"""
实战3
代码10-7
模拟验证码识别的实际应用程序
"""
import cv2 as cv                                    # 引入cv模块
from string_segmentation import cut_apart           # 引入cut_part函数
from test import discriminate                       # 引入discriminate函数
import torch                                        # 引入torch模块

if __name__ == '__main__':      # 主程序
    img = cv.imread('./sample/test/715_Q7DZ.png')   # 读取图片
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 灰度化处理
    thresh1, img_bin = cv.threshold(img_gray, 200, 255, cv.THRESH_BINARY_INV)  # 转换成二值图
    cut_result = cut_apart(img_bin)                 # 切割图片
    dis_result = discriminate(cut_result)  # 分辨字符
    string_result = [''] * 4  # 创建空白列表存放最后转换的结果
    s = torch.max(dis_result.data, 1)[1].data  # 找到最大下标
    for j in range(4):  # 判断下标对应的字符
        if s[j] < 10:  # 数字
            string_result[j] = str(s[j].data.cpu().numpy())
        elif (s[j] >= 10) & (s[j] < 36):  # 大写字母
            string_result[j] = chr(s[j] + 55)
        elif s[j] >= 36:  # 小写字母
            string_result[j] = chr(s[j] + 61)
    ss = ''.join(string_result)         # 拼接成字符串
    print(f'验证码为：{ss}')            # 打印最后结果
    cv.imshow('yzm', img)               # 显示所识别的图片
    cv.waitKey(0)                       # 定格显示
