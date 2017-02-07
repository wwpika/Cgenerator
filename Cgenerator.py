# -*- coding:utf-8 -*-
import pygame
from PIL import Image
import StringIO,os

f=open('te.txt','r')
words=f.readlines()[0].strip()
#print words.decode('utf-8')
f.close()

#该函数用来渲染文字
def pasteWord(words):
	#改变当前工作目录到指定路径
	os.chdir('./word')
	pygame.init()
	font_path='C:\Windows\Fonts\simkai.ttf'
	#create a new Font object from a file
	font=pygame.font.Font(font_path,22)

	text_list=words.split(' ')
	print text_list
	length=len(text_list)
	for i in range(length):
		#对文字进行解码
		print 'text_list[i]:'
		print text_list[i]
		text=text_list[i].decode('utf-8')
		print text
		imgName=text+'.png'
		print imgName

		if os.path.isfile(imgName):
			continue
		else:
			paste(text,font,imgName)

def paste(text,font,imgName,area=(50,30)):#area:坐标
	#PIL.Image.new(mode, size, color=0):Creates a new image with the given mode and size
	im=Image.new('RGB',(100,100),(255,255,255))
	#render(text, antialias, color, background=None):draw text on a new Surface
	
	
	str=text
	rtext=font.render(str,True,(0,0,0),(255,255,255))


	sio=StringIO.StringIO()
	#save(Surface, filename):save an image to disk
	pygame.image.save(rtext,'test.png')
	sio.seek(0)
	#Opens and identifies the given image file
	line=Image.open('test.png')
	#Image.paste(im, box=None, mask=None):Pastes another image into this image
	im.paste(line,area)
	#Saves this image under the given filename
	im.save(imgName)

if __name__=='__main__':
	pasteWord(words)