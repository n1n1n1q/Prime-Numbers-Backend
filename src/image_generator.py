"""
Texture generation
"""
import textwrap
import random
from PIL import Image, ImageDraw, ImageFont
import sieve
TEXTURE_PATH = "assets/backrooms.png"
FONT_PATH = "assets/caskadiya.ttf"
FONT_SIZE = 60
SIEVE_NUM = 1000000
SAVE_PATH = "res/result_image"
ITERATIONS = 30
for i in range(ITERATIONS):
    texture_image= Image.open(TEXTURE_PATH)

    numbers_layout = Image.new('RGBA', texture_image.size, (255,255,255,0))
    font = ImageFont.truetype(FONT_PATH,FONT_SIZE)

    draw = ImageDraw.Draw(numbers_layout)

    primes = sieve.eratosthenes_sieve(SIEVE_NUM)
    primes = [random.choice(primes) for _ in range(100)]
    primes_txt = ' '.join([str(num) for num in primes])
    wrapped = textwrap.fill(primes_txt,width=28)

    draw.text((0,0),wrapped,fill=(0,0,0,200),font=font)

    combined_img = Image.alpha_composite(texture_image.convert('RGBA'), numbers_layout)
    result_img = combined_img.convert('RGB')
    result_img.save(SAVE_PATH+str(i)+'.jpg')
# result_img.show()
