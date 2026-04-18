from PIL import Image
from PIL import ImageFont, ImageDraw
dict = {"День рождения": 'croped.jpg', "Новый год": 'otkritka2.jpg', "8 марта": 'otkritka3.jpg', "23 февраля": 'otkritka4.jpg'}
a = input('Ваш праздник: ')
if a in dict:
    img = Image.open(dict[a])
    img.show()
else:
    print("вы опечатались")