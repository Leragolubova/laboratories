from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageFont

s = Image.open('тузик.jpg')
s.show()

print(s.format, s.size, s.palette)

hor = ImageOps.mirror(s)
hor.save('гор.jpg')
ver = ImageOps.flip(s)
ver.save('вер.jpg')


image1 = Image.open('1.jpg')
image2 = Image.open('2.jpg')
image3 = Image.open('3.jpg')
image4 = Image.open('4.jpg')
image5 = Image.open('5.jpg')

e1 = image1.filter(ImageFilter.FIND_EDGES)
e2 = image2.filter(ImageFilter.FIND_EDGES)
e3 = image3.filter(ImageFilter.FIND_EDGES)
e4 = image4.filter(ImageFilter.FIND_EDGES)
e5 = image5.filter(ImageFilter.FIND_EDGES)

e1.save('_1.jpg')
e2.save('_2.jpg')
e3.save('_3.jpg')
e4.save('_4.jpg')
e5.save('_5.jpg')

image = Image.open('тузик.jpg')
draw = ImageDraw.Draw(image)

bl = (3, 7, 12)
font = ImageFont.truetype("myfont.ttf", 40)
draw.text((0, 0), "Лера и её друзья", fill=bl, font=font)
image.show()
image.save('тузик2.jpg')
