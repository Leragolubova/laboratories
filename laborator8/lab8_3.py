from PIL import Image, ImageDraw, ImageFont


name = input()
inf = input()
image = Image.open(name)
im_crop = image.crop((10, 700, 400, 900))
im_crop.save('1' + name)


fnt = ImageFont.truetype('ttf.ttf', 40)
draw = ImageDraw.Draw(image)
draw.text((0, 0), inf + ', поздравляем!', font=fnt, fill=('#1C0606'))

image.save('image.png')
