from PIL import Image


name = input()
image = Image.open(name)
image_crop = image.crop((100, 150, 400, 900))
image_crop.save(name + name)
