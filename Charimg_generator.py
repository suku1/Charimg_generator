import os
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2

def makeimage(fontpath='', txt='test', imgsize=(128, 128, 3), txtsize=128, name='data', folder=''):
    img = np.ones(imgsize, np.uint8) * 255#白背景
    color = (0, 0, 0)#文字色
    font = ImageFont.truetype(fontpath, txtsize)

    img = Image.fromarray(img)
    ImageDraw.Draw(img).text((0, 0), txt, font=font, fill=color)
    img = np.array(img)
    cv2.imwrite(os.path.join(folder, name + '.png'), img)

def main():
    txt = 'Sample'#文字
    size = (192, 512, 3)#画像サイズ
    tsize = 128#フォントサイズ
    folder = 'Sample'#保存フォルダ

    font_ls = os.listdir('C:\Windows\Fonts')#フォントのリスト取得
    exlist = ['ttf', 'TTF', 'ttc', 'otf', 'TTC']#読み込む拡張子
    for f in font_ls:
        if f.rsplit('.', 1)[1] in exlist:
            print(f + ' 完了')
            font = os.path.join('C:\Windows\Fonts', f)
            makeimage(fontpath=font, txt=txt, imgsize=size, txtsize=tsize, name=f, folder=folder)


if __name__ == '__main__':
    main()
