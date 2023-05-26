from PIL import Image


dct = {}

cel1 = Image.open('1september.jpg')
cel2 = Image.open('russia_day.png')

dct['1 сентября'] = cel1
dct['день России'] = cel2

celeb = input()
dct[celeb].show()
