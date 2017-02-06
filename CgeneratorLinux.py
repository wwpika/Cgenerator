#coding:utf-8

# 导入必要的模块
import pygame
import Image
import StringIO,os

# 打开文件，读取文件内容
f = open('word.txt','r')
words = f.readlines()[0]
f.close()

def pasteWord(words):
    '''定义一个渲染文字的函数'''

    # 初始化pygame，并加载字体
    os.chdir('./word')
    pygame.init()
    font_path = "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"
    font = pygame.font.Font(font_path,22)

    # 以空格分割字符串，遍历每一个汉字，对没有渲染的文字进行处理
    text_list = words.split(' ')
    length = len(text_list)
    for i in range(length):
        text = text_list[i].decode('utf-8','ignore')
        imgName = text_list[i] + '.png'
        if os.path.isfile(imgName):
            continue
        else:    
            paste(text,font,imgName)

def paste(text,font,imgName,area=(5,3)):
    '''创建新的白色图片文件，并对文字进行渲染，最后使用Image模块令其生成图片'''

    im = Image.new('RGB', (30,30), (255,255,255))
    rtext = font.render(text, True, (0,0,0), (255,255,255))

    # 将渲染结果rtext保存到StringIO对象中，再使用Image模块读取该对象
    sio = StringIO.StringIO()
    pygame.image.save(rtext, sio)
    sio.seek(0)
    line = Image.open(sio)
    im.paste(line, area)
    im.save(imgName)

# 运行该文件的时候执行pasteWord函数
if __name__ == '__main__':
    pasteWord(words)