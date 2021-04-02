from PIL import Image, ImageDraw


def fruits(size, bg_color, *houses):
    im = Image.new('RGB', size, bg_color)
    #  width - ширина, height - высота
    draw = ImageDraw.Draw(im)
    for elem in houses:
        x, y, r = elem
        draw.ellipse((x - r, y - r, x + r, y + r), fill=((r * 123) % 256, (r * 123) % 256, (r * 123) % 256))
    return im
