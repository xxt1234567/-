import pygame
from sys import exit
import os
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
screensize=[1080,720]

def drawText(content,font,color):
    text = font.render(content, True, color)
    return text

def loaddata_nz():
    path=os.path.join(os.getcwd(),'年度总决赛')
    defpath=os.path.join(os.getcwd(),'default')
    if not(os.path.exists(path)):
        path=defpath
        
    teamfile=os.path.join(path,'teamdatas.xlsx')
    usedef=os.path.exists(teamfile)
    teamdata=[]
    if usedef:
        read=pd.read_excel(teamfile,sheet_name='data').values
        if np.isnan(read[0][2]):
            usedef=False
            path=defpath
    if usedef:
        for i in range(12):
            teamdata.append({})
            teamdata[i]['index']=read[i][0]
            teamdata[i]['name']=read[i][1]
            teamdata[i]['elo']=read[i][2]
            teamdata[i]['group']=read[i][3]
        elo_locked=read[0][4]==1
        set_schedule=read[0][5]==1
    else:
        for i in range(12):
            teamdata.append({})
            teamdata[i]['name']=chr(ord('A')+i)
            teamdata[i]['elo']=1500
            if(i<6):
                teamdata[i]['group']=1
            else:
                teamdata[i]['group']=2
        elo_locked=True
        set_schedule=False
        
    logos=os.path.join(path,'logos')
    for i in range(12):
        logophoto=os.path.join(logos,teamdata[i]['name']+'.jpg')
        teamdata[i]['logo']=pygame.image.load(logophoto).convert()
        
    schedule=[]
    if set_schedule:
        rschedule=pd.read_excel(teamfile,sheet_name='schedule').values
        for i in range(len(rschedule)):
            schedule.append([])
            j=0
            while(j<len(rschedule[0]) and not np.isnan(rschedule[i][j])):
                schedule[i].append((int(rschedule[i][j]),int(rschedule[i][j+1])))
                j+=2
    else:
        group1=[]
        group2=[]
        for i in range(12):
            if teamdata[i]['group']==1:
                group1.append(i)
            else:
                group2.append(i)
        for i in range(6):
            for j in range(6):
                schedule.append((group1[i],group2[j]))
        random.shuffle(schedule)
        for i in range(12):
            schedule[i]=[schedule[3*i],schedule[3*i+1],schedule[3*i+2]]
        schedule=schedule[:12]
    return teamdata,elo_locked,set_schedule,schedule

def showtitle_nz(window,font_20,font_30,teamdata,elo_locked,set_schedule):
    subwindow=pygame.Surface((1080,570),flags=pygame.HWSURFACE)
    subwindow.fill((255,255,255))
    window.blit(subwindow,(0,150))
    window.blit(drawText('大师组：',font_30,(0,0,0)), (10,150))
    window.blit(drawText('精英组：',font_30,(0,0,0)), (550,150))
    window.blit(drawText('队名',font_20,(0,0,0)), (10,200))
    window.blit(drawText('队标',font_20,(0,0,0)), (110,200))
    window.blit(drawText('初始ELO分',font_20,(0,0,0)), (210,200))
    window.blit(drawText('队名',font_20,(0,0,0)), (550,200))
    window.blit(drawText('队标',font_20,(0,0,0)), (650,200))
    window.blit(drawText('初始ELO分',font_20,(0,0,0)), (750,200))
    group1=[]
    group2=[]
    for i in range(12):
        if teamdata[i]['group']==1:
            group1.append(i)
        else:
            group2.append(i)
    for i in range(6):
        window.blit(drawText(teamdata[group1[i]]['name'],font_20,(0,0,0)), (10,265+i*70))
        window.blit(drawText(str(teamdata[group1[i]]['elo']),font_20,(0,0,0)), (210,265+i*70))
        window.blit(drawText(teamdata[group2[i]]['name'],font_20,(0,0,0)), (550,265+i*70))
        window.blit(drawText(str(teamdata[group2[i]]['elo']),font_20,(0,0,0)), (750,265+i*70))
        logo_small1=pygame.transform.scale(teamdata[group1[i]]['logo'],(50,50))
        logo_small2=pygame.transform.scale(teamdata[group2[i]]['logo'],(50,50))
        window.blit(logo_small1,(110,250+i*70))
        window.blit(logo_small2,(650,250+i*70))
    if elo_locked:
        elotext='ELO分固定：是'
    else:
        elotext='ELO分固定：否'
    if set_schedule:
        schtext='自定义赛程：是'
    else:
        schtext='自定义赛程：否'
    window.blit(drawText(elotext,font_30,(0,0,0)), (10,670))
    window.blit(drawText(schtext,font_30,(0,0,0)), (550,670))
    pygame.display.update()
    
pygame.init()
font_20 = pygame.font.SysFont(['华文楷体','microsoftsansserif'],20)
font_50 = pygame.font.SysFont(['华文楷体','microsoftsansserif'],50)
font_30 = pygame.font.SysFont(['华文楷体','microsoftsansserif'],30)
window = pygame.display.set_mode(screensize)
pygame.display.set_caption('王者荣耀赛事模拟系统')

font_rect_title=font_50.size('王者荣耀赛事模拟系统')
font_rect_ls=font_30.size('KPL联赛模拟')
font_rect_tb=font_30.size('挑战者杯模拟')
font_rect_nz=font_30.size('年度总决赛模拟')
font_rect_back=font_20.size('返回')
font_rect_sorry=font_50.size('抱歉，功能暂未开放')
font_rect_title_ls=font_50.size('KPL联赛模拟')
font_rect_title_tb=font_50.size('挑战者杯模拟')
font_rect_title_nz=font_50.size('年度总决赛模拟')
font_rect_info=font_30.size('确认战队信息')
font_rect_begin=font_20.size('开始模拟')
font_rect_reload=font_20.size('重新加载数据')
font_rect_help=font_20.size('帮助')
font_rect_title_help=font_50.size('帮助')
font_rect_info_help=font_50.size('这是一个帮助界面')

font_pos_title=((screensize[0]-font_rect_title[0])//2,10)
sspace=(screensize[0]-font_rect_ls[0]-font_rect_tb[0]-font_rect_nz[0])//4
font_pos_ls=(sspace,font_rect_title[1]+(screensize[1]-font_rect_ls[1]-font_rect_title[1])//2)
font_pos_tb=(sspace*2+font_rect_ls[0],font_rect_title[1]+(screensize[1]-font_rect_ls[1]-font_rect_title[1])//2)
font_pos_nz=(sspace*3+font_rect_ls[0]+font_rect_tb[0],font_rect_title[1]+(screensize[1]-font_rect_ls[1]-font_rect_title[1])//2)

font_pos_back=(10,10)
font_pos_sorry=((screensize[0]-font_rect_sorry[0])//2,(screensize[1]-font_rect_sorry[1])//2)
font_pos_title_ls=((screensize[0]-font_rect_title_ls[0])//2,10)
font_pos_title_tb=((screensize[0]-font_rect_title_tb[0])//2,10)
font_pos_title_nz=((screensize[0]-font_rect_title_nz[0])//2,10)

bspace=(screensize[0]-font_rect_info[0]-font_rect_reload[0]-font_rect_begin[0]-font_rect_help[0])//4
font_pos_info=(10,font_rect_title_nz[1]+20)
font_pos_begin=(bspace+font_rect_info[0],font_rect_title_nz[1]+20)
font_pos_reload=(bspace*2+font_rect_info[0]+font_rect_begin[0],font_rect_title_nz[1]+20)
font_pos_help=(bspace*3+font_rect_info[0]+font_rect_begin[0]+font_rect_reload[0],font_rect_title_nz[1]+20)

font_pos_title_help=((screensize[0]-font_rect_title_help[0])//2,10)
font_pos_info_help=((screensize[0]-font_rect_info_help[0])//2,(screensize[1]-font_rect_info_help[1])//2)

start=True
ls=False
tb=False
nz=False
help=False
pre=None

while True:
    if start:
        window.fill(white)
        window.blit(drawText("王者荣耀赛事模拟系统",font_50,black), font_pos_title)
        window.blit(drawText("KPL联赛模拟",font_30,black), font_pos_ls)
        window.blit(drawText("挑战者杯模拟",font_30,black), font_pos_tb)
        window.blit(drawText("年度总决赛模拟",font_30,black), font_pos_nz)
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
                    if x1 >= font_pos_ls[0] and x1 <= font_pos_ls[0]+font_rect_ls[0] and y1 >= font_pos_ls[1] and y1 <= font_pos_ls[1]+font_rect_ls[1]:
                        lsm=True
                    elif x1 >= font_pos_tb[0] and x1 <= font_pos_tb[0]+font_rect_tb[0] and y1 >= font_pos_tb[1] and y1 <= font_pos_tb[1]+font_rect_tb[1]:
                        tbm=True
                    elif x1 >= font_pos_nz[0] and x1 <= font_pos_nz[0]+font_rect_nz[0] and y1 >= font_pos_nz[1] and y1 <= font_pos_nz[1]+font_rect_nz[1]:
                        nzm=True
                    else:
                        lsm=False
                        tbm=False
                        nzm=False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x1,y1 = event.pos
                    if x1 >= font_pos_ls[0] and x1 <= font_pos_ls[0]+font_rect_ls[0] and y1 >= font_pos_ls[1] and y1 <= font_pos_ls[1]+font_rect_ls[1]:
                        start=False
                        ls=True
                    elif x1 >= font_pos_tb[0] and x1 <= font_pos_tb[0]+font_rect_tb[0] and y1 >= font_pos_tb[1] and y1 <= font_pos_tb[1]+font_rect_tb[1]:
                        start=False
                        tb=True
                    elif x1 >= font_pos_nz[0] and x1 <= font_pos_nz[0]+font_rect_nz[0] and y1 >= font_pos_nz[1] and y1 <= font_pos_nz[1]+font_rect_nz[1]:
                        start=False
                        nz=True
                if lsm:
                    window.blit(drawText("KPL联赛模拟",font_30,red), font_pos_ls)
                else:
                    window.blit(drawText("KPL联赛模拟",font_30,black), font_pos_ls)
                if tbm:
                    window.blit(drawText("挑战者杯模拟",font_30,red), font_pos_tb)
                else:
                    window.blit(drawText("挑战者杯模拟",font_30,black), font_pos_tb)
                if nzm:
                    window.blit(drawText("年度总决赛模拟",font_30,red), font_pos_nz)
                else:
                    window.blit(drawText("年度总决赛模拟",font_30,black), font_pos_nz)
            pygame.display.update()
    if ls:
        window.fill(white)
        window.blit(drawText("返回",font_20,black), font_pos_back)
        window.blit(drawText("KPL联赛模拟",font_50,black), font_pos_title_ls)
        window.blit(drawText("抱歉，功能暂未开放",font_50,black), font_pos_sorry)
        while ls:
            back=False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEMOTION:
                    x1,y1 = event.pos
                    if x1 >= font_pos_back[0] and x1 <= font_pos_back[0]+font_rect_back[0] and y1 >= font_pos_back[1] and y1 <= font_pos_back[1]+font_rect_back[1]:
                        back=True
                    else:
                        back=False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x1,y1 = event.pos
                    if x1 >= font_pos_back[0] and x1 <= font_pos_back[0]+font_rect_back[0] and y1 >= font_pos_back[1] and y1 <= font_pos_back[1]+font_rect_back[1]:
                        ls=False
                        start=True
                if back:
                    window.blit(drawText("返回",font_20,red), font_pos_back)
                else:
                    window.blit(drawText("返回",font_20,black), font_pos_back)
            pygame.display.update()
    if tb:
        window.fill(white)
        window.blit(drawText("返回",font_20,black), font_pos_back)
        window.blit(drawText("挑战者杯模拟",font_50,black), font_pos_title_tb)
        window.blit(drawText("抱歉，功能暂未开放",font_50,black), font_pos_sorry)
        while tb:
            back=False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEMOTION:
                    x1,y1 = event.pos
                    if x1 >= font_pos_back[0] and x1 <= font_pos_back[0]+font_rect_back[0] and y1 >= font_pos_back[1] and y1 <= font_pos_back[1]+font_rect_back[1]:
                        back=True
                    else:
                        back=False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x1,y1 = event.pos
                    if x1 >= font_pos_back[0] and x1 <= font_pos_back[0]+font_rect_back[0] and y1 >= font_pos_back[1] and y1 <= font_pos_back[1]+font_rect_back[1]:
                        tb=False
                        start=True
                if back:
                    window.blit(drawText("返回",font_20,red), font_pos_back)
                else:
                    window.blit(drawText("返回",font_20,black), font_pos_back)
            pygame.display.update()
    if nz:
        window.fill(white)
        window.blit(drawText("返回",font_20,black), font_pos_back)
        window.blit(drawText("年度总决赛模拟",font_50,black), font_pos_title_nz)
        window.blit(drawText("确认战队信息",font_30,black), font_pos_info)
        window.blit(drawText("开始模拟",font_20,green), font_pos_begin)
        window.blit(drawText("重新加载数据",font_20,black), font_pos_reload)
        window.blit(drawText("帮助",font_20,black), font_pos_help)
        teamdata,elo_locked,set_schedule,schedule=loaddata_nz()
        showtitle_nz(window,font_20,font_30,teamdata,elo_locked,set_schedule)
        while nz:
            back=False
            begin=False
            reload=False
            shelp=False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEMOTION:
                    x1,y1 = event.pos
                    if x1 >= font_pos_back[0] and x1 <= font_pos_back[0]+font_rect_back[0] and y1 >= font_pos_back[1] and y1 <= font_pos_back[1]+font_rect_back[1]:
                        back=True
                    elif x1 >= font_pos_begin[0] and x1 <= font_pos_begin[0]+font_rect_begin[0] and y1 >= font_pos_begin[1] and y1 <= font_pos_begin[1]+font_rect_begin[1]:
                        begin=True
                    elif x1 >= font_pos_reload[0] and x1 <= font_pos_reload[0]+font_rect_reload[0] and y1 >= font_pos_reload[1] and y1 <= font_pos_reload[1]+font_rect_reload[1]:
                        reload=True
                    elif x1 >= font_pos_help[0] and x1 <= font_pos_help[0]+font_rect_help[0] and y1 >= font_pos_help[1] and y1 <= font_pos_help[1]+font_rect_help[1]:
                        shelp=True
                    else:
                        back=False
                        begin=False
                        reload=False
                        shelp=False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x1,y1 = event.pos
                    if x1 >= font_pos_back[0] and x1 <= font_pos_back[0]+font_rect_back[0] and y1 >= font_pos_back[1] and y1 <= font_pos_back[1]+font_rect_back[1]:
                        nz=False
                        start=True
                    elif x1 >= font_pos_reload[0] and x1 <= font_pos_reload[0]+font_rect_reload[0] and y1 >= font_pos_reload[1] and y1 <= font_pos_reload[1]+font_rect_reload[1]:
                        teamdata,elo_locked,set_schedule,schedule=loaddata_nz()
                        showtitle_nz(window,font_20,font_30,teamdata,elo_locked,set_schedule)
                    elif x1 >= font_pos_help[0] and x1 <= font_pos_help[0]+font_rect_help[0] and y1 >= font_pos_help[1] and y1 <= font_pos_help[1]+font_rect_help[1]:
                        nz=False
                        help=True
                        pre='nz'
                if back:
                    window.blit(drawText("返回",font_20,red), font_pos_back)
                else:
                    window.blit(drawText("返回",font_20,black), font_pos_back)
                if begin:
                    window.blit(drawText("开始模拟",font_20,red), font_pos_begin)
                else:
                    window.blit(drawText("开始模拟",font_20,green), font_pos_begin)
                if reload:
                    window.blit(drawText("重新加载数据",font_20,red), font_pos_reload)
                else:
                    window.blit(drawText("重新加载数据",font_20,black), font_pos_reload)
                if shelp:
                    window.blit(drawText("帮助",font_20,red), font_pos_help)
                else:
                    window.blit(drawText("帮助",font_20,black), font_pos_help)
            pygame.display.update()
    if help:
        window.fill(white)
        window.blit(drawText("返回",font_20,black), font_pos_back)
        window.blit(drawText("帮助",font_50,black), font_pos_title_help)
        window.blit(drawText("这是一个帮助界面",font_50,black), font_pos_info_help)
        while help:
            back=False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEMOTION:
                    x1,y1 = event.pos
                    if x1 >= font_pos_back[0] and x1 <= font_pos_back[0]+font_rect_back[0] and y1 >= font_pos_back[1] and y1 <= font_pos_back[1]+font_rect_back[1]:
                        back=True
                    else:
                        back=False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x1,y1 = event.pos
                    if x1 >= font_pos_back[0] and x1 <= font_pos_back[0]+font_rect_back[0] and y1 >= font_pos_back[1] and y1 <= font_pos_back[1]+font_rect_back[1]:
                        help=False
                        if(pre=='ls'):
                            ls=True
                        elif(pre=='tb'):
                            tb=True
                        elif(pre=='nz'):
                            nz=True
                        pre=None
                if back:
                    window.blit(drawText("返回",font_20,red), font_pos_back)
                else:
                    window.blit(drawText("返回",font_20,black), font_pos_back)
            pygame.display.update()