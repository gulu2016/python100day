import colorgram

# Extract 6 colors from an image.
# s172-1-1-1 抽取图片中最多的6中颜色
colors = colorgram.extract('learn.jpg', 6)

# s172-1-1-2 将抽取的颜色按照rgb格式打印出来
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r,g,b)
    print(rgb)
    print()

