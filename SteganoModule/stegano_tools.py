from PIL import Image
import argparse


def negative(pixel):
    '''
    Функция конвертирования изображения в негатив
    :param pixel: пиксель изображения
    :return: инвертированный пиксель
    '''
    for i in range(len(pixel)):
        pixel[i] = 255 - pixel[i]
    return pixel


def only_red(pixel):
    '''
    Функция фильтрации только красного цвета
    :param pixel: пиксель изображения
    :return: только красная составляющая пикселя
    '''
    pixel[1] = 0
    pixel[2] = 0
    return pixel


def only_green(pixel):
    '''
    Функция фильтрации только зеленого цвета
    :param pixel: пиксель изображения
    :return: только зеленая составляющая пикселя
    '''
    pixel[0] = 0
    pixel[2] = 0
    return pixel


def only_blue(pixel):
    '''
    Функция фильтрации только синего цвета
    :param pixel: пиксель изображения
    :return: только синяя составляющая пикселя
    '''
    pixel[0] = 0
    pixel[1] = 0
    return pixel


def layer_red(pixel, level=0):
    '''
    Функция фильтрации только красного цвета и только определенного слоя
    :param pixel: пиксель изображения
    :param level: уровень слоя
    :return: только красная составляющая пикселя
    '''
    pixel = only_red(pixel)
    pixel[0] &= 2 ** level
    pixel[0] *= 255
    return pixel


def layer_blue(pixel, level=0):
    '''
    Функция фильтрации только синего цвета и только определенного слоя
    :param pixel: пиксель изображения
    :param level: уровень слоя
    :return: только синяя составляющая пикселя
    '''
    pixel = only_blue(pixel)
    pixel[2] &= 2 ** level
    pixel[2] *= 255
    return pixel


def layer_green(pixel, level=0):
    '''
    Функция фильтрации только зеленого цвета и только определенного слоя
    :param pixel: пиксель изображения
    :param level: уровень слоя
    :return: только зеленая составляющая пикселя
    '''
    pixel = only_green(pixel)
    pixel[1] &= 2 ** level
    pixel[1] *= 255
    return pixel


def edit_image(img, func, level=None, output_path=None):
    '''
    Главная функция изменения изображения
    :param img: объект изображения
    :param func: функция, применяющаяся к каждому пикселю
    :param level: уровень слоя (при необходимости)
    :param output_path: путь сохранения ихмененной картинки
    :return:
    '''
    if not output_path:
        output_path = '{0}{1}.{2}'.format(func.__name__, level, img.format)

    print('Applying function {0}, level {1}'.format(func, level))
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if not level:
                result = tuple(func(list(pixels[i, j])))
            else:
                result = tuple(func(list(pixels[i, j]), level))
            pixels[i, j] = result

    img.save(output_path)


def all_layers(image_path):
    '''
    Реализация параметра all_layers
    :param image_path: путь изображения
    :return: None
    '''
    for func in [layer_blue, layer_green, layer_red]:
        for i in range(0, 8):
            img = Image.open(image_path, 'r')
            edit_image(img, func, i)


def main(arguments):
    router = {
        'green': only_green,
        'blue': only_blue,
        'red': only_red,
        'layer_green': layer_green,
        'layer_blue': layer_blue,
        'layer_red': layer_red,
        'negative': negative,
        'all_layers': all_layers,
    }

    img = Image.open(arguments.image_path, 'r')

    if args.act == 'all_layers':
        all_layers(arguments.image_path)
    elif arguments.act in ['layer_blue', 'layer_green', 'layer_red']:
        edit_image(img, router[arguments.act], int(arguments.layer), output_path=arguments.output_path)
    else:
        edit_image(img, router[arguments.act], output_path=arguments.output_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Stego script')
    parser.add_argument('-i', action="store", dest="image_path", help="Image path")
    parser.add_argument('-a', action="store", dest="act", help="Action with image [green, blue, red, layer_green, "
                                                               "layer_blue, layer_red, negative, all_layers]")
    parser.add_argument('-l', action="store", dest="layer", help="Layer number (for specific actions)")
    parser.add_argument('-o', action="store", dest="output_path", help="Output path [dont use for all_layers]")

    args = parser.parse_args()
    main(args)
