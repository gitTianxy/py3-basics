# coding=utf8
"""
PIL, Python Imaging Library
已经是Python平台事实上的图像处理标准库了。PIL功能非常强大，但API却非常简单易用。

Pillow
由于PIL仅支持到Python 2.7，加上年久失修，于是一群志愿者在PIL的基础上创建了兼容的版本，
名字叫Pillow，支持最新Python 3.x，又加入了许多新特性，因此，我们可以直接安装使用Pillow。
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from random import randint


class ChaptChaDemo:
    """
    生成验证码图片
    """

    def __init__(self, dest):
        self.dest = dest
        self.chaptcha()

    def chaptcha(self):
        # 240 x 60:
        width = 60 * 4
        height = 60
        image = Image.new('RGB', (width, height), (255, 255, 255))
        # 创建Font对象:
        font = ImageFont.truetype('Arial.ttf', 36)
        # 创建Draw对象:
        draw = ImageDraw.Draw(image)
        # 填充每个像素:
        for x in range(width):
            for y in range(height):
                draw.point((x, y), fill=self.__rndColor())
        # 输出文字:
        for t in range(4):
            draw.text((60 * t + 10, 10), self.__rndChar(), font=font, fill=self.__rndColor2())
        # 模糊:
        image = image.filter(ImageFilter.BLUR)
        image.save(self.dest, 'jpeg')

    # 随机字母:
    def __rndChar(self):
        return chr(randint(65, 90))

    # 随机颜色1:
    def __rndColor(self):
        return (randint(64, 255), randint(64, 255), randint(64, 255))

    # 随机颜色2:
    def __rndColor2(self):
        return (randint(32, 127), randint(32, 127), randint(32, 127))


def img_blur(src, dest):
    with Image.open(src) as im:
        print("---blur", src)
        im.filter(ImageFilter.BLUR).save(dest, 'jpeg')


def img_resize(src, dest):
    with Image.open(src) as im:
        w, h = im.size
        im.thumbnail((w // 2, h // 2))
        print(f"---resize img from {w}x{h} to {w//2}x{h//2}")
        im.save(dest, 'jpeg')


if __name__ == '__main__':
    src = '../data/cat.jpg'
    img_resize(src, './cat_resize.jpg')
    img_blur(src, './cat_blur.jpg')
    ChaptChaDemo('./chaptcha.jpg')
