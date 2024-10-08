import pygame
from sys import exit

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
screensize=[1080,720]

def drawText(content,font,color):
    text = font.render(content, True, color)
    return text

pygame.init()
font1 = pygame.font.SysFont(['华文新魏','microsoftsansserif'],20)
font2 = pygame.font.SysFont(['华文新魏','microsoftsansserif'],50)
window = pygame.display.set_mode(screensize)
pygame.display.set_caption('王者荣耀赛事模拟系统')

fontrectls=font1.size('KPL联赛模拟')
fontrecttb=font1.size('挑战者杯模拟')
fontrectnz=font1.size('年度总决赛模拟')
fontrectback=font1.size('返回')
fontrectsorry=font2.size('抱歉，功能暂未开放')

sspace=(screensize[0]-fontrectls[0]-fontrecttb[0]-fontrectnz[0])//4
fontposls=(sspace,screensize[1]//9*7)
fontpostb=(sspace*2+fontrectls[0],screensize[1]//9*7)
fontposnz=(sspace*3+fontrectls[0]+fontrecttb[0],screensize[1]//9*7)
fontposback=(10,10)
fontpossorry=((screensize[0]-fontrectsorry[0])//2,(screensize[1]-fontrectsorry[1])//2)

start=True
ls=False
tb=False
nz=False

while True:
    if start:
        window.fill(black)
        window.blit(drawText("KPL联赛模拟",font1,green), fontposls)
        window.blit(drawText("挑战者杯模拟",font1,green), fontpostb)
        window.blit(drawText("年度总决赛模拟",font1,green), fontposnz)
        while start:
            lsm=False
            tbm=False
            nzm=False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEMOTION:
                    x1,y1 = event.pos
                    if x1 >= fontposls[0] and x1 <= fontposls[0]+fontrectls[0] and y1 >= fontposls[1] and y1 <= fontposls[1]+fontrectls[1]:
                        lsm=True
                    elif x1 >= fontpostb[0] and x1 <= fontpostb[0]+fontrecttb[0] and y1 >= fontpostb[1] and y1 <= fontpostb[1]+fontrecttb[1]:
                        tbm=True
                    elif x1 >= fontposnz[0] and x1 <= fontposnz[0]+fontrectnz[0] and y1 >= fontposnz[1] and y1 <= fontposnz[1]+fontrectnz[1]:
                        nzm=True
                    else:
                        lsm=False
                        tbm=False
                        nzm=False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x1,y1 = event.pos
                    if x1 >= fontposls[0] and x1 <= fontposls[0]+fontrectls[0] and y1 >= fontposls[1] and y1 <= fontposls[1]+fontrectls[1]:
                        start=False
                        ls=True
                    elif x1 >= fontpostb[0] and x1 <= fontpostb[0]+fontrecttb[0] and y1 >= fontpostb[1] and y1 <= fontpostb[1]+fontrecttb[1]:
                        start=False
                        tb=True
                    elif x1 >= fontposnz[0] and x1 <= fontposnz[0]+fontrectnz[0] and y1 >= fontposnz[1] and y1 <= fontposnz[1]+fontrectnz[1]:
                        start=False
                        nz=True
                if lsm:
                    window.blit(drawText("KPL联赛模拟",font1,red), fontposls)
                else:
                    window.blit(drawText("KPL联赛模拟",font1,green), fontposls)
                if tbm:
                    window.blit(drawText("挑战者杯模拟",font1,red), fontpostb)
                else:
                    window.blit(drawText("挑战者杯模拟",font1,green), fontpostb)
                if nzm:
                    window.blit(drawText("年度总决赛模拟",font1,red), fontposnz)
                else:
                    window.blit(drawText("年度总决赛模拟",font1,green), fontposnz)
            pygame.display.update()
    if ls:
        window.fill(red)
        window.blit(drawText("返回",font1,black), fontposback)
        window.blit(drawText("抱歉，功能暂未开放",font2,black), fontpossorry)
        while ls:
            back=False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEMOTION:
                    x1,y1 = event.pos
                    if x1 >= fontposback[0] and x1 <= fontposback[0]+fontrectback[0] and y1 >= fontposback[1] and y1 <= fontposback[1]+fontrectback[1]:
                        back=True
                    else:
                        back=False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x1,y1 = event.pos
                    if x1 >= fontposback[0] and x1 <= fontposback[0]+fontrectback[0] and y1 >= fontposback[1] and y1 <= fontposback[1]+fontrectback[1]:
                        ls=False
                        start=True
                if back:
                    window.blit(drawText("返回",font1,white), fontposback)
                else:
                    window.blit(drawText("返回",font1,black), fontposback)
            pygame.display.update()
    if tb:
        window.fill(blue)
        window.blit(drawText("返回",font1,black), fontposback)
        window.blit(drawText("抱歉，功能暂未开放",font2,black), fontpossorry)
        while tb:
            back=False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEMOTION:
                    x1,y1 = event.pos
                    if x1 >= fontposback[0] and x1 <= fontposback[0]+fontrectback[0] and y1 >= fontposback[1] and y1 <= fontposback[1]+fontrectback[1]:
                        back=True
                    else:
                        back=False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x1,y1 = event.pos
                    if x1 >= fontposback[0] and x1 <= fontposback[0]+fontrectback[0] and y1 >= fontposback[1] and y1 <= fontposback[1]+fontrectback[1]:
                        tb=False
                        start=True
                if back:
                    window.blit(drawText("返回",font1,white), fontposback)
                else:
                    window.blit(drawText("返回",font1,black), fontposback)
            pygame.display.update()
    if nz:
        window.fill(green)
        window.blit(drawText("返回",font1,black), fontposback)
        window.blit(drawText("抱歉，功能暂未开放",font2,black), fontpossorry)
        while nz:
            back=False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEMOTION:
                    x1,y1 = event.pos
                    if x1 >= fontposback[0] and x1 <= fontposback[0]+fontrectback[0] and y1 >= fontposback[1] and y1 <= fontposback[1]+fontrectback[1]:
                        back=True
                    else:
                        back=False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x1,y1 = event.pos
                    if x1 >= fontposback[0] and x1 <= fontposback[0]+fontrectback[0] and y1 >= fontposback[1] and y1 <= fontposback[1]+fontrectback[1]:
                        nz=False
                        start=True
                if back:
                    window.blit(drawText("返回",font1,white), fontposback)
                else:
                    window.blit(drawText("返回",font1,black), fontposback)
            pygame.display.update()