import colorgram


image = "broncos.jpg"



#rbg stand for red, green, blud
def getrgb(path):
    colors = colorgram.extract(path, 6)
    rgb_lis = [color.rgb for color in colors]

    return rgb_lis


#HSL stands for hue, saturation, and lightness.
def gethsl(path):
    colors = colorgram.extract(path, 6)
    hsl_lis = [color.hsl for color in colors]

    return hsl_lis

# print(getrgb(image))
# print(gethsl(image))