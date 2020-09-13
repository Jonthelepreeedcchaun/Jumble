import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys, datetime, time, json, random, pygame as pg, threading; from platform import system
pg.init()
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
from Structure.Jumble_Imports import *
key = keys(); tkey = keys(); tkey_v = keys(); nkey = keys(); mouse = mouse_obj()
jsondata = json_obj('jsondata')
jsondata.load()

images = images_obj('images')
images.retrieve()

UI = UI_obj('UI')
UI.retrieve()

data = gen_obj('data')
data.append({"start_time": time.time(), "frames": 0, "mouse_visible": 1, "screenlist": [(0, 0), pg.FULLSCREEN], "screenlist_v": [(screen.get_width(), screen.get_height()), pg.RESIZABLE], "Bg": [0, 0, 0]})
running = 1
while running:
    if key.sh*key.esc: break
    if not data.screenlist == data.screenlist_v: screen = pg.display.set_mode(*data.screenlist)
    data.screenlist_v = data.screenlist
    mouse.x, mouse.y = pg.mouse.get_pos(); mouse.m1, mouse.m3, mouse.m2 = pg.mouse.get_pressed()
    mouse.t1 = 0; mouse.t3 = 0; mouse.t2 = 0
    if mouse.m1 and not mouse.t1_v: mouse.t1 = 1; mouse.t1_v = 1
    if not mouse.m1: mouse.t1_v = 0
    if mouse.m3 and not mouse.t3_v: mouse.t3 = 1; mouse.t3_v = 1
    if not mouse.m3: mouse.t3_v = 0
    if mouse.m2 and not mouse.t2_v: mouse.t2 = 1; mouse.t2_v = 1
    if not mouse.m2: mouse.t2_v = 0
    pg.mouse.set_visible(mouse.mouse_visible)
    for this in tkey.keyname:
        exec('tkey.' + this + '= 0')
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = 0
        if event.type == pg.KEYDOWN:
            for this in key.keylist:
                if this == event.key: exec('tkey.' + key.keyname[key.keylist.index(this)] + '= 1'); exec('key.' + key.keyname[key.keylist.index(this)] + '= 1'); exec('nkey.' + key.keyname[key.keylist.index(this)] + '= 0')
        if event.type == pg.KEYUP:
            for this in key.keylist:
                if this == event.key: exec('key.' + key.keyname[key.keylist.index(this)] + '= 0'); exec('nkey.' + key.keyname[key.keylist.index(this)] + '= 1')
        if event.type == pg.VIDEORESIZE:
            if not data.screenlist[1] == pg.FULLSCREEN: screen = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
    if tkey.F11:
        if data.screenlist[1] == pg.FULLSCREEN: data.screenlist = [(900, 600), pg.RESIZABLE]
        elif data.screenlist[1] == pg.RESIZABLE: data.screenlist = [(1920, 1080), pg.FULLSCREEN]

    images.generate(screen, mouse, UI)

    pg.time.wait(1); pg.display.flip(); screen.fill((data.Bg[0], data.Bg[1], data.Bg[2])); data.frames += 1
data.append({'elapsed_time': time.time() - data.start_time}); jsondata.update('runtime', {str(datetime.datetime.now()): 'FPS: ' + str(data.frames/data.elapsed_time), 'images' + str(datetime.datetime.now())[11:24]: str(images.attr_list)})
jsondata.save('runtime')
sys.exit()
