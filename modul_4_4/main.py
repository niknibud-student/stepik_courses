from PIL import Image, ImageDraw, ImageFont
from os import listdir


def input_parametres():
    print('Введите цифру - шаблон для мема')
    files = listdir('templates')
    for i, file in enumerate(files):
        print(f'{file} - {i+1}')
    digit = int(input())
    if digit < 1 or digit - 1 > len(files):
        print('Вы ввели неверный номер шаблона')
        quit()
    top_text = input('Введите текст сверху (Enter, чтобы пропустить)')        
    bottom_text = input('Введите текст снизу (Enter, чтобы пропустить)')        
    return files[digit - 1], top_text, bottom_text


def draw_text(image, type, text):
    draw = ImageDraw.Draw(image)
    font_size = 50
    font = ImageFont.truetype('impact.ttf', font_size)
    white_color = (255, 255, 255)
    # ширина и высота данного текста с данным шрифтом
    text_width = draw.textlength(text, font) 
    text_height = font_size * 1.15
    # зависит от расположения
    y_start = 10 if type == 'top' else image.height - text_height - 10
    
    draw.text((image.width / 2 - text_width / 2, y_start), 
              text, white_color, font)


def make_meme(image, top_text='', bottom_text=''):
    draw_text(image, 'top', top_text)
    draw_text(image, 'bottom', bottom_text)
    return image


def main():
    image_name, top_text, bottom_text = input_parametres()
    with Image.open(f'templates/{image_name}') as image:
        image = make_meme(image, top_text, bottom_text)
        image.save('meme_result.jpg')
        image.show()


if __name__ == '__main__':
    main()