from PIL import Image, ImageDraw, ImageFont

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
    with Image.open("templates/boromir.jpg") as image:
        image = make_meme(image, 
                          'Нельзя так просто взять', 
                          'и сразу написать идеальное приложение')
        image.save('meme_result.jpg')
        image.show()


if __name__ == '__main__':
    main()