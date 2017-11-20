from PIL import Image, ImageDraw
import math
"""
im = Image.new("RGB", (128, 128))
pix = im.load()
for x in range(128):
    for y in range(128):
        pix[x,y] = (255,0,0)

im.save("test.png", "PNG")
"""

def fillLines(draw, x0,y0):
    for i in range(10):
        draw.line((x0, y0+(i*15), x0+150, y0+(i*15)), fill = 'black', width=3)

def drawCircle(draw, x0, y0, t):
    inside = ('black' if t == 'filled' else 'white')
    draw.ellipse((x0, y0, x0+150, y0+150), fill = inside, outline ='black')
    if t == 'lines':
        for i in range(10):
            tmp = math.sqrt(75**2-(y0+(i*15)-(y0+75))**2)
            draw.line(((x0+75) - tmp,y0+(i*15), (x0+75) + tmp, y0+(i*15)), fill = 'black', width=3)

def drawTriangle(draw, x0, y0, t):
    inside = ('black' if t == 'filled' else 'white')
    draw.polygon((x0+75,y0,x0,y0+150,x0+150,y0+150), fill = inside, outline ='black')
    if t == 'lines':
        for i in range(10):
            tmp = 10
            xA = int(-(y0+(i*15)-(y0+2*(x0+75)))/2)
            xB = int((y0+(i*15)-(y0-2*(x0+75)))/2)
            draw.line((xA, y0+(i*15), xB, y0+(i*15)), fill = 'black', width=3)

        # fillLines(draw,x0,y0)

def drawSquare(draw, x0, y0, t):
    inside = ('black' if t == 'filled' else 'white')
    draw.rectangle((x0,y0,x0+150,y0+150), fill = inside, outline ='black')
    if t == 'lines':
        fillLines(draw,x0,y0)

def drawShape(draw,k,x0,y0):
    typeDef = 'empty'
    if k > 2:
        typeDef = 'filled'
    if k > 5:
        typeDef = 'lines'
    if k%3 == 0:
        drawCircle(draw, x0,y0,typeDef)
    if k%3 == 1:
        drawTriangle(draw, x0,y0,typeDef)
    if k%3 == 2:
        drawSquare(draw, x0,y0,typeDef)

def drawShape2(draw,k,x0,y0):
    typeDef = 'empty' if k < 2 else 'filled'
    if k%2 == 0:
        drawCircle(draw, x0,y0,typeDef)
    if k%2 == 1:
        drawSquare(draw, x0,y0,typeDef)

def launchCreation(nbCat):
    im = Image.new("RGB", (512,512), "white")
    draw = ImageDraw.Draw(im)
    for i in range(nbCat*nbCat):
        for j in range(nbCat*nbCat):
            for k in range(nbCat*nbCat):
                if nbCat == 2:
                    drawShape2(draw,i,10,10)
                    drawShape2(draw,j,180,180)
                    drawShape2(draw,k,341,341)
                else:
                    drawShape(draw,i,10,10)
                    drawShape(draw,j,180,180)
                    drawShape(draw,k,341,341)
                im.save("ImagesTest"+"/img"+str(i)+str(j)+str(k)+".png", "PNG")
                im = Image.new("RGB", (512,512), "white")
                draw = ImageDraw.Draw(im)

launchCreation(3)
