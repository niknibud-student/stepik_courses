from PIL import Image, ImageDraw, ImageFont
from os import listdir
from typing import List


def input_parametres():
    print('Введите цифру - шаблон для мема')
    files = listdir('modul_4_4/templates')

    for i, file in enumerate(files):
        print(f'{file} - {i+1}')

    digit = int(input())

    if digit < 1 or digit - 1 > len(files):
        print('Вы ввели неверный номер шаблона')
        quit()

    top_text = input('Введите текст сверху (Enter, чтобы пропустить): ')
    bottom_text = input('Введите текст снизу (Enter, чтобы пропустить): ')

    return files[digit - 1], top_text, bottom_text


def draw_outlined_text(draw, pos: tuple, text: str, font) -> None:
    black_color = (0, 0, 0)
    white_color = (255, 255, 255)
    draw.text((pos[0] - 3, pos[1] - 3), text, black_color, font)
    draw.text((pos[0] + 3, pos[1] + 3), text, black_color, font)
    draw.text((pos[0] + 3, pos[1] - 3), text, black_color, font)
    draw.text((pos[0] - 3, pos[1] + 3), text, black_color, font)
    draw.text(pos, text, white_color, font)


def split_text(draw, text: str, font, img_width: int) -> List:
    lines = []
    cur_word = 0
    words = text.split()

    while cur_word != len(words):
        # если даже одно слово длинное, скажем об этом пользователю
        if draw.textlength(words[cur_word], font) > img_width:
            print(f'Слово {words[cur_word]} слишком длинное для этой картинки')
            quit()

        # будем добавлять в текущую сточку слова, пока эта строка влезает
        cur_line = []
        # пока текущая строка с прибавлением нового слова все еще вмещается
        while cur_word < len(words) and \
            draw.textlength(' '.join(cur_line) + words[cur_word], font) < img_width:
            # добавляем к текущей строке новое слово
            cur_line.append(words[cur_word])
            cur_word += 1
        lines.append(' '.join(cur_line))

    return lines


def draw_text(image, type: str, text: str) -> None:
    font_size = 50
    white_color = (255, 255, 255)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('impact.ttf', font_size)
    lines = split_text(draw, text, font, image.width)
    # высота данного текста с данным шрифтом
    text_height = font_size * 1.15

    for i in range(len(lines)):
        # ширина данного текста с данным шрифтом
        text_width = draw.textlength(lines[i], font)
        # зависит от расположения
        if type == 'top':
            y_start = text_height * i + 10
        else:
            y_start = image.height - text_height * len(lines) - 10

        draw_outlined_text(draw, (image.width / 2 - text_width / 2, y_start),
                           text, font)
        draw.text((image.width / 2 - text_width / 2, y_start),
                  text, white_color, font)


def make_meme(image, top_text: str ='', bottom_text: str =''):
    draw_text(image, 'top', top_text)
    draw_text(image, 'bottom', bottom_text)
    return image


def main():
    image_name, top_text, bottom_text = input_parametres()
    with Image.open(f'modul_4_4/templates/{image_name}') as image:
        image = make_meme(image, top_text, bottom_text)
        image.save('meme_result.jpg')
        image.show()


if __name__ == '__main__':
    main()
