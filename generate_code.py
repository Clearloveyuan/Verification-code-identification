"""
实战3
代码10-1
生成验证码程序
生成样本m个
宽100，高30，背景白色，字符绿色
"""
from PIL import Image                                   # 引入PIL模块中的Image模块
from PIL import ImageDraw                               # 引入PIL模块中的ImageDraw模块
from PIL import ImageFont                               # 引入PIL模块中的ImageFont模块
import random                                           # 引入random模块


def getStr():                                           # 获取随机字符串
    random_num = str(random.randint(0, 9))              # 随机数字
    random_low_alpha = chr(random.randint(97, 122))     # 随机小写字母
    random_upper_alpha = chr(random.randint(65, 90))    # 随机大写字母
    random_char = random.choice([random_num, random_low_alpha, random_upper_alpha])  # 随机选择一种字符
    return random_char   # 返回选择的字符


if __name__ == '__main__':
    m = 5  # 生成的样本数量
    for i in range(1000):
        # 创建一幅图像，参数分别是RGB模式。宽100，高30，白色
        image = Image.new('RGB', (120, 30), 'white')

        # 将Image对象传如draw对象中，准备画图
        draw = ImageDraw.Draw(image)

        # 读取一个font字体对象参数是ttf的字体文件的目录，以及字体的大小
        font = ImageFont.truetype("JOKERMAN.ttf", size=25)

        random_str = ['']       # 创建空列表存储生成的字符
        for j in range(4):      # 循环5次，获取5个随机字符串
            random_char = getStr()              # 获得随机生成的字符
            random_str.append(random_char)      # 添加到之前创建的空列表中

            # 在图片上一次写入得到的随机字符串,参数是：定位，字符串，颜色，字体
            draw.text((5 + j * 30, -4), random_char, 'green', font=font)

        string = ''.join(random_str)            # 将列表中存储生成的字符拼接成字符串，用于后面保存文件时命名

        # 保存为png格式的图片
        image.save(f'./sample/{i}_{string}.png')

        print('\r' + f'当前第{i+1}个', end=' ', flush=True)     # 动态显示生成过程
    print('生成成功！')