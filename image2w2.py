from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import matplotlib.pyplot as plt
import numpy as np




#读取图片信息
filepath = "./nanase.jpg"
savefilepath = "./output_nanase.jpg"
word = list("俺のお嫁nanase")
img = Image.open(filepath)
pix = img.load()
width = img.size[0]
height = img.size[1]


#创建新图片
scale = 2 #
step = 5 #
canvas = np.ndarray((height*scale, width*scale, 3), np.uint8)
canvas[:, :, :] = 255
new_image = Image.fromarray(canvas)
draw = ImageDraw.Draw(new_image)

#创建绘制对象
# font = ImageFont.truetype("consola.ttf", 10, encoding="unic")
font = ImageFont.truetype('simsun.ttc', 10)


#开始绘制
pix_count = 0 #像素统计
word_len = len(word)
for y in range(height):
    for x in range(width):
        if x % step == 0 and y % step == 0:
            draw.text((x*scale, y*scale), word[pix_count%word_len], pix[x, y], font)
            pix_count += 1

# 保存
new_image.save(savefilepath)

print(pix_count)
new_image.show()


