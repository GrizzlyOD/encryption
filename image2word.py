from PIL import Image
import argparse
ascii_char = list("01 ")

def getchar(r,g,b,alpha=256):
    if alpha == 0:
        return ''
    length = len(ascii_char)
    gray = int(0.2126*r+0.7152*g+0.0722*b)
    unit = (256.0+1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    im = "u=2705646185,1415118418&fm=11&gp=0.jpg"
    img = Image.open(im)
    text = ''
    print(img.size)
    img = img.resize((int(img.size[0]/10),int(img.size[1]/10)), Image.NEAREST)
    # img = img.resize((80,80), Image.NEAREST)
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            text += getchar(*img.getpixel((j, i)))
        text += '\n'
    with open("./output.txt",'w') as f:
            f.write(text)
    print(text)


