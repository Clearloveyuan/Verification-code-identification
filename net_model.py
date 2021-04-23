"""
实战3
代码10-4
识别验证码的网络模型
输入固定尺寸为32*32
"""
import torch.nn as nn                        # 引入torch.nn模块


class CNN(nn.Module):                        # 创建类
    def __init__(self):
        super(CNN, self).__init__()
        self.conv = nn.Sequential(          # 卷积网络
            nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, stride=1, padding=1),  # ->(16, 32, 32)
            nn.ReLU(inplace=True),
            nn.Conv2d(in_channels=16, out_channels=16, kernel_size=3, stride=1, padding=1),  # ->(16, 32, 32)
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2),  # (16, 16, 16)

            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1),  # ->(32, 16, 16)
            nn.ReLU(inplace=True),
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=3, stride=1, padding=1),  # ->(32, 16, 16)
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2),  # (32, 8, 8)
        )
        self.out = nn.Sequential(         # 全连接网络
            nn.Linear(32 * 8 * 8, 256),
            nn.ReLU(inplace=True),
            nn.Linear(256, 128),
            nn.ReLU(inplace=True),
            nn.Linear(128, 62)
        )

    def forward(self, x):                  # 前向传播函数
        x = self.conv(x)
        x = x.view(x.size(0), -1)          # 特征图展开成一维
        output = self.out(x)
        return output