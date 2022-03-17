from PIL import Image, ImageFilter
import os

size_300 = (300, 300)
size_700 = (700, 700)

for f in os.listdir("."):
    if f.endswith(".jpg"):
        #print(f)
        i = Image.open(f)
        fn, fext = os.path.splitext(f)

        i.thumbnail(size_700)
        i.save("700/{}_700{}.png".format(fn, fext))
        #print(fn, fext)

        i.thumbnail(size_300)
        i.save("300/{}_300{}.png".format(fn, fext))

image1 = Image.open("Danusa.png")
#image1.show()
#print(help(image1))
image1.rotate(90).save("Danusa_90.png")

image1.convert(mode="L").save("Danusa_modeL.png")

image1.filter(ImageFilter.GaussianBlur(10)).save("Danusa_blur.png")

