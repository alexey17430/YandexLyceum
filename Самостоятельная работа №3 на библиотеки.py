from PIL import Image, ImageDraw


def direction(image, color):
    pixels = image.load()
    x, y = image.size
    ans_x = list()
    ans_y = list()
    for i in range(x):
        for j in range(y):
            if pixels[i, j] == color:
                ans_x.append(i)
                ans_y.append(j)
    ans_x = sum(ans_x) // len(ans_x)
    ans_y = sum(ans_y) // len(ans_y)
    return abs(ans_x - x // 2), abs(ans_y - y // 2)
