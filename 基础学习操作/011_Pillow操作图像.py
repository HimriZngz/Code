from PIL import Image, ImageFilter, ImageDraw, ImageFont

# im = Image.open('d:/k/2.bmp')
#
# w, h = im.size
# print('Image size is: %s x %s' % (w, h))
#
# im.thumbnail((w//2, h//2))
# print('Image chang to: %s x %s' % (w//2, h//2))
# im.save('d:/k/2_缩略图.jpg', 'jpeg')

# im = Image.open('d:/k/3.bmp')
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('d:/k/3_模糊.jpg', 'jpeg')

import random


def rndChar():
    return chr(random.randint(65, 90))


def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


width = 240
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 36)
draw = ImageDraw.Draw(image)
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
for t in range(4):
    draw.text((60*t+10, 10), rndChar(), font=font, fill=rndColor2())
image = image.filter(ImageFilter.BLUR)
image.save('d:/k/验证码2.jpg', 'jpeg')