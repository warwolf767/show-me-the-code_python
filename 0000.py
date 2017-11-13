
#-*-coding:utf8-*-
__author__ = "ice wolf"

# 第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def main():
    img = Image.open("test.jpg")
    print(img.format, img.size, img.mode)
    width, height = img.size
    font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)
    draw = ImageDraw.Draw(img)
    draw.text((width-55, 0), unicode('99+', 'utf-8'), (255, 0, 0), font=font)
    img.show()
    img.save("target.jpg")

if __name__ == '__main__':
    main()
