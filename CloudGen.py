from PIL import Image, ImageDraw
import math

shape= [(1,2),(2,2),(4,1),(10,1),(2,1)]
altitude = [390, 240, 90]
color = [1, 0.9]
size = [10, 50, 100, 150]
rain = [False,True]

def drawDottedLine(draw, x1y1, x2y2, col):
    norm = math.sqrt((x2y2[0]-x1y1[0])**2 + (x2y2[1]-x1y1[1])**2)
    alpha = math.pi/2 if x1y1[1]-x2y2[1] == 0 else math.atan((x2y2[0]-x1y1[0])/(x1y1[1]-x2y2[1]))
    print(norm, alpha)
    for i in range(0,int(norm/32)):
        draw.line((x1y1[0]+i*2*16*math.sin(alpha),x1y1[1]+i*2*16*math.cos(alpha),x1y1[0]+(i*2+1)*16*math.sin(alpha),x1y1[1]+(i*2+1)*16*math.cos(alpha)), fill= col)

def drawBackground(draw):
    drawDottedLine(draw, (0,90), (512,90), 'grey')
    drawDottedLine(draw, (0,240), (512,240), 'grey')
    drawDottedLine(draw, (0,390), (512,390), 'grey')
    draw.rectangle((0,490,512,512), fill = '#4C9900', outline ='grey')

"""

"""

def drawCloud(draw,im,sh, si, alt, col,ra):
    im2 = Image.open("simple_cloud.png")
    im2 = im2.resize((si*sh[0],si*sh[1]))
    im2 = im2.point(lambda p: p * col)
    if ra :
        for x in range(0, int(si*sh[1]/5)):
            drawDottedLine(draw, (int(256-si*sh[0]/2)+x*5,alt), (int(256-si*sh[0]/2)+x*5,490), '#0000CC')
    im.paste(im2,(int(256-si*sh[0]/2), int(alt-si*sh[1]/2)), im2)

def launchCreation():
    im = Image.new("RGB", (512,512),  '#99CCFF')
    draw = ImageDraw.Draw(im)
    drawBackground(draw)
    drawCloud(draw, im,shape[1],size[1],altitude[0], color[0], rain[0])
    im.save("Clouds/img"+str(0)+str(0)+str(0)+".png", "PNG")

launchCreation()
