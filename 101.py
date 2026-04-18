from PIL import Image
from PIL import ImageFont, ImageDraw
img = Image.open('otkritka.jpg')
res = img.crop((200, 100, 800, 800))
res.save('croped.jpg')