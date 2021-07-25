from natsort import natsorted
from PIL import Image

import imageio
import os

def convert_alpha(filename):
    with Image.open(filename) as srcImage:
        pixels = srcImage.load()
        for i in range(srcImage.size[0]):
            for j in range(srcImage.size[1]):
                if pixels[i,j][3] == 0:
                    pixels[i,j] = (0, 0 , 0, 0)
        srcImage.save(filename)

def convert_alpha_all():
    filenames = list(filter(endswithpng, os.listdir()))
    filenames = natsorted(filenames)
    for filename in filenames:
        convert_alpha(filename)
        # print(f"Converted {filename}")

def create_expanded_image(filename, id, offsetX, offsetY):
    with Image.open(filename) as srcImage:
        newImage = Image.new(srcImage.mode, (64, 64), (0, 0, 0, 0))
        newImage.paste(srcImage, (offsetX+5, offsetY+5))
        newImage.save(f"temp{id}.png")

def calcdiff_expanded_primitive():
    t = 0
    rt = 0
    with Image.open("temp0.png") as image0:
        with Image.open("temp1.png") as image1:
            pixels0 = image0.load()
            pixels1 = image1.load()
            for i in range(image0.size[0]):
                for j in range(image0.size[1]):
                    if pixels0[i,j] != (0, 0, 0, 0) or pixels1[i,j] != (0, 0, 0, 0):
                        t += 1
                        if pixels0[i,j] == pixels1[i,j]:
                            rt += 1
    return (t, rt)


def calcdiff(filename, lastoffsetX, lastoffsetY):
    with Image.open("t1.png") as image:
        image.save("temp0.png")

    min_diff = 1
    max_simi = 50

    loX = 0
    loY = 0

    create_expanded_image(filename, 1, 0, 0)
    with Image.open("temp1.png") as image:
        image.save("t1.png")

    for i in range(-5, 6):
        for j in range(-5, 6):
            create_expanded_image(filename, 1, i+lastoffsetX, j+lastoffsetY)
            (t, rt) = calcdiff_expanded_primitive()
            if rt < max_simi:
                continue
            if max_simi < rt:
                max_simi = rt
                min_diff = 0.01
                loX = i+lastoffsetX
                loY = j+lastoffsetY
                with Image.open("temp1.png") as image:
                    image.save("t1.png")

    return (min_diff, loX, loY)

def endswithpng(filename):
    return filename.endswith(".png")

def run():
    filenames = list(filter(endswithpng, os.listdir()))
    filenames = natsorted(filenames)

    images = []

    start = 0
    end = len(filenames)

    loX = 0
    loY = 0

    create_expanded_image(filenames[start], 0, 0, 0)
    with Image.open("temp0.png") as image:
        image.save("t1.png")
    images.append(imageio.imread("t1.png"))

    print(f"starting file is {filenames[start]}")

    for i in range(start+1, end):
        (diff, loX, loY) = calcdiff(filenames[i], loX, loY)
        print(f"loX = {loX}, loY = {loY}")
        if diff > 0.01:
            imageio.mimsave(f"./exported_gif/{filenames[i-1][:-3]}gif", images)
            print(f"Saved to {filenames[i-1][:-3]}gif")
            images = []
        images.append(imageio.imread("t1.png"))
    if len(images) > 0:
        imageio.mimsave(f"./exported_gif/{filenames[end-1][:-3]}gif", images)

convert_alpha_all()
run()