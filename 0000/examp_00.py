from PIL import Image, ImageFont, ImageDraw

def draw_num():
	ima = Image.open('./fire.jpg')
	w, h = ima.size
	fontsize = h//4
	position = w - h//4
	numfont = ImageFont.truetype('$HOME/Ubuntu-C.ttf', fontsize)
	ImageDraw.Draw(ima).text((position, 0), str(4), font=numfont, fill='red')
	ima.save('fire_num.jpg', 'jpeg')

if __name__ == '__main__':
	draw_num()