from PIL import Image


def negative(pixel):
    for i in range(len(pixel)):
        pixel[i] = 255-pixel[i]
    return pixel


def only_red(pixel):
    pixel[1] = 0
    pixel[2] = 0
    return pixel


def only_green(pixel):
    pixel[0] = 0
    pixel[2] = 0
    return pixel


def only_blue(pixel):
    pixel[0] = 0
    pixel[1] = 0
    return pixel


def layer_red(pixel, level=0):
    pixel = only_red(pixel)
    pixel[0] &= 2**level
    pixel[0] *= 255
    return pixel


def layer_blue(pixel, level=0):
    pixel = only_blue(pixel)
    pixel[2] &= 2 ** level
    pixel[2] *= 255
    return pixel


def layer_green(pixel, level=0):
    pixel = only_green(pixel)
    pixel[1] &= 2 ** level
    pixel[1] *= 255
    return pixel


def edit_image(img, func, level=None):
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if not level:
                result = tuple(func(list(pixels[i, j])))
            else:
                result = tuple(func(list(pixels[i, j]), level))
            pixels[i, j] = result

    if not level:
        img.save('stegano/{0}.png'.format(func.__name__))
    else:
        img.save('stegano/{0}{1}.png'.format(func.__name__, level))



for i in range(0, 8):
    img = Image.open('picture.png', 'r')
    edit_image(img, negative)
    img = Image.open('picture.png', 'r')
    edit_image(img, layer_red, i)
    img = Image.open('picture.png', 'r')
    edit_image(img, layer_blue, i)
    img = Image.open('picture.png', 'r')
    edit_image(img, layer_green, i)
