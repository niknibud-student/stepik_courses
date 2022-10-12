from PIL import Image, ImageDraw, ImageFont

def make_meme(image, top_text='', bottom_text=''):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('impact.ttf', 50)
    white_color = (255, 255, 255)
    text_width = draw.textlength(top_text, font)  # ширина данного текста с данным шрифтом
    draw.text((image.width / 2 - text_width / 2, 10), top_text, white_color, font)
    return image

def main():    
    with Image.open("templates/boromir.jpg") as image:
        image = make_meme(image, 'Sample Text')
        image.save('meme_result.jpg')
        image.show()


if __name__ == '__main__':
    main()