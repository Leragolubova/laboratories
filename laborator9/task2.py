import os
from PIL import Image, ImageFilter



def check_extension(filename):
    spl = os.path.splitext(filename)
    return spl[1] != '.jpg' or spl[1] != '.png'


def update_image(path, out_path):
    im = Image.open(path)
    edg = im.filter(ImageFilter.FIND_EDGES)
    return (edg, im.filename)


ipath = input()
opath = input()

begin = os.getcwd()

os.chdir(ipath)
pictures = []

for fl in os.listdir():
    if check_extension(fl):
        print('cannot process fl: {}, skip it'.format(fl))
        continue

    pictures.append(update_image(fl, opath))


os.chdir(begin + "/" + opath)
index = 0
for pic in pictures:
    pic[0].save(str(index) + '-' + pic[1])
    index += 1

