from PIL import Image
from PIL import ImageFont, ImageDraw
dict = {"День рождения": 'otkritka.jpg', "Новый год": 'otkritka2.jpg', "8 марта": 'otkritka3.jpg', "23 февраля": 'otkritka4.jpg'}
font = ImageFont.truetype("arialbd.ttf", 40)
a = input('Ваш праздник: ')
img = Image.open(dict[a])
imgdrow = ImageDraw.Draw(img)
name = input('Имя: ')
if a in dict:
    imgdrow.text((10, 10), (f"{name} , поздравляю!"), font=font)
    img.save('img.png')
    img2 = Image.open('img.png')
    img2.show()
else:
    print("вы опечатались")
