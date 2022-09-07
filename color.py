import colorgram as cg


image = "broncos.jpg"

#rbg stand for red, green, blud
def getrgb(path):
    colors = cg.extract(path, 2**32) #2**32 will get all as many colors as possible without repeat
    rgb_lis = [color.rgb for color in colors]

    return rgb_lis


#HSL stands for hue, saturation, and lightness.
def gethsl(path):
    colors = cg.extract(path, 2**32)
    hsl_lis = [color.hsl for color in colors]

    return hsl_lis

print(getrgb(image))
# print(gethsl(image))