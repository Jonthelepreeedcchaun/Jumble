class gen_obj:
    def __init__(i, title = None):
        i.title = title; i.attr_dict = {}; i.attr_list = []; i.attr_valuelist = []
    def append(i, dictionary):
        for this in dictionary:
            new_attr_name = this; new_attr = dictionary[this]
            exec('i.' + new_attr_name + '= new_attr')
            i.attr_dict.update({new_attr_name: new_attr}); i.attr_list.append(new_attr_name); i.attr_valuelist.append(new_attr)
    def delete(i, list):
        for this in list:
            if hasattr(i, this):
                attr_name = this; attr = i.attr_dict[attr_name]
                delattr(i, attr_name)
                del i.attr_dict[attr_name]; i.attr_list.remove(attr_name); i.attr_valuelist.remove(attr)
class json_obj(gen_obj):
    def __init__(i, title = None):
        super().__init__(title); i.savelist = []
    def load(i, path = 'Storage/'):
        import os, json
        for this in os.listdir(path):
            if this[-5:] == ".json":
                with open('Storage/' + this, 'r') as f:
                    i.append({this[:-5]: json.load(f)})
    def update(i, attr, dict):
        exec('i.' + attr + '.update(dict)')
    def save(i, attr):
        import json
        if hasattr(i, attr):
            with open('Storage/' + attr + '.json', 'w', encoding = 'utf-8') as f:
                json.dump(i.attr_dict[attr], f, ensure_ascii = False, indent = 4)
        else:
            print('Jsondata Error: ' + attr + '.json inaccessable')
class keys(gen_obj):
    def __init__(i, title = None):
        super().__init__(title)
        import pygame as pg
        i.keyname = ['i0', 'i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7', 'i8', 'i9', 'MIN', 'EQU', 'PER', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'bk', 'sp', 'tb', 'esc', 'sh', 'enter', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11']
        i.shletters = [')', '!', '@', '#', '$', '%', '^', '&', '*', '(', '_', '+', '>', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', None, ' ', '     ', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        i.letters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '=', '.', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', None, ' ', '     ', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        i.keylist = [pg.K_0, pg.K_1, pg.K_2, pg.K_3, pg.K_4, pg.K_5, pg.K_6, pg.K_7, pg.K_8, pg.K_9, pg.K_MINUS, pg.K_EQUALS, pg.K_PERIOD, pg.K_a, pg.K_b, pg.K_c, pg.K_d, pg.K_e, pg.K_f, pg.K_g, pg.K_h, pg.K_i, pg.K_j, pg.K_k, pg.K_l, pg.K_m, pg.K_n, pg.K_o, pg.K_p, pg.K_q, pg.K_r, pg.K_s, pg.K_t, pg.K_u, pg.K_v, pg.K_w, pg.K_x, pg.K_y, pg.K_z, pg.K_BACKSPACE, pg.K_SPACE, pg.K_TAB, pg.K_ESCAPE, pg.K_LSHIFT, pg.K_RETURN, pg.K_F1, pg.K_F2, pg.K_F3, pg.K_F4, pg.K_F5, pg.K_F6, pg.K_F7, pg.K_F8, pg.K_F9, pg.K_F10, pg.K_F11]
        i.held = None
        for this in i.keylist:
            i.append({i.keyname[i.keylist.index(this)]: 0})
        i.char = {}
        i.shchar = {}
        for this in i.keyname:
            i.char.update({this: i.letters[i.keyname.index(this)]})
            i.shchar.update({this: i.shletters[i.keyname.index(this)]})
class mouse_obj(gen_obj):
    def __init__(i, title = None):
        super().__init__(title)
        i.append({'x': 0, 'y': 0, 'm1': 0, 'm2': 1, 'm3': 2, 'n1': 0, 'n2': 1, 'n3': 2, 't1': 0, 't2': 1, 't3': 2, 't1_v': 0, 't2_v': 1, 't3_v': 2, 'mouse_visible': 1, 'UIheld': 0})
class image(gen_obj):
    def __init__(i, title, filename, path = ''):
        super().__init__(title)
        import pygame as pg
        i.append({'img': pg.image.load(path + filename)}); i.append({'rect': i.img.get_rect()})
        i.append({'x_pos': 0, 'y_pos': 0, 'layer': 0, 'mouse_over': 0, 'selected': 0, 'title': title})
    def draw(i, screen):
        screen.blit(i.img, (i.x_pos, i.y_pos)); i.append({'rect': i.img.get_rect(topleft = (i.x_pos, i.y_pos))})
        i.append({'right': i.rect.w + i.x_pos, 'center': i.rect.center})
class images_obj(gen_obj):
    def __init__(i, title):
        super().__init__(title)
        i.selected = []; i.UImouse_over = []; i.UI_dict = {}
    def retrieve(i, path = None):
        from Structure.Jumble_Imports import image; import os
        for this in os.listdir(path):
            this_str = this
            if path == None: path = ''
            if this_str[-4:] == ".jpg" or this_str[-4:] == ".png":
                os.rename(path + this_str, 'UserImages/' + this_str)
            if path == '': path = None
        for this in os.listdir('UserImages/'):
            this_str = this
            nulllist = []; nullvalue = ''
            for that in this_str:
                if that == ' ': nulllist.append('_')
                else: nulllist.append(that)
            for that in nulllist:
                nullvalue += that
            if this_str[-4:] == ".jpg" or this_str[-4:] == ".png":
                parsed_image = image(nullvalue[:-4], this_str, 'UserImages/'); parsed_image.append({'fileend': this_str[-4:]})
                i.append({nullvalue[:-4]: parsed_image})
    def group(i, other_images_obj, group_keylist):
        for this in group_keylist:
            i.append({this: other_images_obj[this]})
    def generate(i, screen, jsondata = None, mouse = None, UI = None, tkey = None, key = None):
        import random; from Structure.Jumble_Imports import UI_obj
        Images_Sort = []; Image_None_List = []; Images = i.attr_valuelist
        for this in Images:
            Image_None_List.append(None)
            if not this.layer in Images_Sort:
                Images_Sort.append(this.layer)
            elif this.layer in Images_Sort:
                while this.layer in Images_Sort:
                    this.layer += random.uniform(-0.01, 0.01); this.append({'layer': this.layer})
                Images_Sort.append(this.layer)
            Images_Sort = sorted(Images_Sort, key = float)
        for this in Images:
            Image_None_List[Images_Sort.index(this.layer)] = this
        Images = Image_None_List; i.attr_valuelist = Images
        for this in i.attr_valuelist:
            exec('i.' + this.title + '.draw(screen)')
            if not mouse == None:
                if this.rect.collidepoint(mouse.x, mouse.y) and not this.mouse_over:
                    this.append({'mouse_over': 1})
                if not this.rect.collidepoint(mouse.x, mouse.y) and this.mouse_over:
                    this.append({'mouse_over': 0})
                if mouse.t1 and this.mouse_over and this not in i.selected: this.append({'selected': 1, 'x_diff': mouse.x - this.x_pos, 'y_diff': mouse.y - this.y_pos}); i.selected.append(this)
                if not mouse.m1 and hasattr(this, 'x_diff'):
                    this.append({'selected': 0, 'rect': this.img.get_rect(topleft = (this.x_pos, this.y_pos))}); this.delete(['x_diff', 'y_diff'])
                    if this in i.selected:
                        i.selected.remove(this)
                if not len(i.selected):
                    pass
                elif len(i.selected):
                    nullvalue = None
                    for that in i.selected:
                        if nullvalue == None:
                            nullvalue = that.layer
                        else:
                            if that.layer > nullvalue: nullvalue = that.layer
                    for that in i.selected:
                        if not that.layer == nullvalue:
                            i.selected.remove(that)
                if this.selected and this in i.selected and not mouse.UIheld: this.append({'x_pos': mouse.x - this.x_diff, 'y_pos': mouse.y - this.y_diff})
                if not UI == None:
                    if this.mouse_over and not this in i.UImouse_over: i.UImouse_over.append(this)
                    elif not this.mouse_over and this in i.UImouse_over: i.UImouse_over.remove(this)
                    if not len(i.UImouse_over):
                        pass
                    elif len(i.UImouse_over):
                        nullvalue = None
                        for that in i.UImouse_over:
                            if nullvalue == None:
                                nullvalue = that.layer
                            else:
                                if that.layer > nullvalue: nullvalue = that.layer
                        for that in i.UImouse_over:
                            if not that.layer == nullvalue:
                                i.UImouse_over.remove(that)
                    if this.title in i.UI_dict and not i.UI_dict[this.title]:
                        del i.UI_dict[this.title]
                    if mouse.t2 and this in i.UImouse_over:
                        if not this.title in i.UI_dict:
                            i.UI_dict.update({this.title: 1})
                        elif i.UI_dict[this.title]:
                            del i.UI_dict[this.title]
                            UI.created.update({this.title: 0})
        if not UI == None:
            for this in i.UI_dict:
                if i.UI_dict[this]:
                    exec('UI.image_window(screen, mouse, tkey, key, i.' + this + ', i)')
def text_objects(text, font, color = (255, 255, 255)):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()
def message_display(screen, text, x, y, size, color):
    import pygame as pg
    largeText = pg.font.Font(None, size)
    TextSurf, TextRect = text_objects(text, largeText, color = ((255, 255, 255)))
    TextRect.topleft = (x, y)
    screen.blit(TextSurf, TextRect)
    dimension = largeText.render(text, True, color).get_rect()
    return(TextRect)
def type_sort(value):
    try:
        nullvalue = float(value)
        if '.' in str(value): type = 'float'
        else: type = 'int'
    except: type = 'str'
    return type
def parseimages(folder = ''):
    if not os.path.isdir(folder + '/'): return None
    import cv2; images = {}
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None: images[str(filename.split('.')[0])].append(os.path.join(folder,filename))
    if len(images) == 0: return None
    else: return images
def malleable_text(screen, x, y, image, image_attr_list, mouse, tkey, key, size = 25):
    for this in image_attr_list:
        nullvalue = message_display(screen, this + ': ' + str(image.attr_dict[this]), x, y + image_attr_list.index(this)*int(size*0.75), size, (255, 255, 255))
        if nullvalue.collidepoint(mouse.x, mouse.y) and mouse.t1:
            if hasattr(image, 'malleable_text') and image.malleable_text == this: delattr(image, 'malleable_text'); mouse.append({'UIheld': 0}); tkey.held = None
            else: image.malleable_text = this; mouse.append({'UIheld': 1}); tkey.held = str(image.attr_dict[this])
        if hasattr(image, 'malleable_text') and image.malleable_text == this and mouse.t1 and not nullvalue.collidepoint(mouse.x, mouse.y):
            delattr(image, 'malleable_text'); mouse.append({'UIheld': 0}); tkey.held = None
        if hasattr(image, 'malleable_text') and image.malleable_text == this:
            message_display(screen, ' -> ' + tkey.held, nullvalue.right, y + image_attr_list.index(this)*int(size*0.75), size, (255, 255, 255))
            for that in tkey.attr_dict:
                if tkey.attr_dict[that] and not tkey.char[that] == None:
                    if key.sh: tkey.held += tkey.shchar[that]
                    else: tkey.held += tkey.char[that]
            if tkey.bk:
                tkey.held = tkey.held[:-1]
                key.bkcount = 0
            if key.bk: key.bkcount += 1
            if hasattr(key, 'bkcount') and not key.bk: delattr(key, 'bkcount')
            if hasattr(key, 'bkcount') and key.bkcount > 25 and (key.bkcount/5).is_integer():
                tkey.held = tkey.held[:-1]
            if tkey.enter and len(tkey.held) > 0:
                if type_sort(image.attr_dict[this]) == 'float' and type_sort(tkey.held) == 'int':
                    tkey.held += '.0'
                delattr(image, 'malleable_text')
                if type_sort(tkey.held) == type_sort(image.attr_dict[this]):
                    mouse.append({'UIheld': 0})
                    if this == 'title':
                        title_v = image.attr_dict[this]
                    exec('image.append({this: ' + type_sort(tkey.held) + '(tkey.held)})')
                    if this == 'title':
                        return(title_v, tkey.held)
class UI_obj(images_obj):
    def __init__(i, title):
        super().__init__(title)
        i.x_pos = {}; i.y_pos = {}; i.x_len = {}; i.y_len = {}; i.created = {}; i.selected = []; i.right_select = {}; i.left_select = {}; i.bottom_select = {}
    def retrieve(i, path = 'Structure/UI/'):
        from Structure.Jumble_Imports import image; import os
        for this in os.listdir(path):
            if this[-4:] == ".jpg" or this[-4:] == ".png":
                parsed_image = image(this[:-4], this, path)
                i.append({this[:-4]: parsed_image})
    def image_window(i, screen, mouse, tkey, key, image, images):
        import pygame as pg, os; from Structure.Jumble_Imports import text_objects, message_display, malleable_text
        if not image.title in i.created: i.created.update({image.title: 0})
        if not i.created[image.title]:
            if image.center[0] > 960:
                i.x_pos.update({image.title: image.x_pos - 600}); i.y_pos.update({image.title: image.y_pos}); i.x_len.update({image.title: 500}); i.y_len.update({image.title: 500})
            if image.center[0] <= 960:
                i.x_pos.update({image.title: image.right + 100}); i.y_pos.update({image.title: image.y_pos}); i.x_len.update({image.title: 500}); i.y_len.update({image.title: 500})
            i.created.update({image.title: 1})
            if i.y_pos[image.title] < 0: i.y_pos.update({image.title: 0})
        windowbox = pg.draw.rect(screen, ((20, 20, 20)), (i.x_pos[image.title], i.y_pos[image.title] + 12, i.x_len[image.title], i.y_len[image.title] - 12))
        windowbar = pg.draw.rect(screen, ((225, 225, 225)), (i.x_pos[image.title], i.y_pos[image.title], i.x_len[image.title], 12))
        i.X.append({'x_pos': i.x_pos[image.title] + i.x_len[image.title] - 12, 'y_pos': i.y_pos[image.title]})
        i.X.draw(screen)
        if i.X.rect.collidepoint(mouse.x, mouse.y) and mouse.t1:
            i.created.update({image.title: 0})
            images.UI_dict.update({image.title: 0})
            mouse.append({'UIheld': 0})
        if i.created[image.title]:
            if not image.title in i.right_select:
                i.right_select.update({image.title: 0})
            if mouse.x > i.x_pos[image.title] + i.x_len[image.title] - 10 and mouse.x < i.x_pos[image.title] + i.x_len[image.title] + 10 and mouse.y > i.y_pos[image.title] and mouse.y < i.y_pos[image.title] + i.y_len[image.title] and mouse.t1: i.right_select[image.title] = 1
            if i.right_select[image.title]: i.x_len[image.title] = mouse.x - i.x_pos[image.title]; mouse.append({'UIheld': 1})
            if i.x_len[image.title] < 100: i.x_len[image.title] = 100
            if i.right_select[image.title] and not mouse.m1: i.right_select[image.title] = 0; mouse.append({'UIheld': 0})
            if not image.title in i.left_select:
                i.left_select.update({image.title: 0})
            if mouse.x > i.x_pos[image.title] - 10 and mouse.x < i.x_pos[image.title] + 10 and mouse.y > i.y_pos[image.title] and mouse.y < i.y_pos[image.title] + i.y_len[image.title] and mouse.t1: i.left_select[image.title] = 1
            if i.left_select[image.title]: nullvalue = i.x_pos[image.title]; i.x_pos[image.title] = mouse.x; i.x_len[image.title] -= i.x_pos[image.title] - nullvalue; mouse.append({'UIheld': 1})
            if i.x_len[image.title] < 100: i.x_len[image.title] = 100
            if i.left_select[image.title] and not mouse.m1: i.left_select[image.title] = 0; mouse.append({'UIheld': 0})
            if not image.title in i.bottom_select:
                i.bottom_select.update({image.title: 0})
            if mouse.y > i.y_pos[image.title] + i.y_len[image.title] - 10 and mouse.y < i.y_pos[image.title] + i.y_len[image.title] + 10 and mouse.x > i.x_pos[image.title] and mouse.x < i.x_pos[image.title] + i.x_len[image.title] and mouse.t1: i.bottom_select[image.title] = 1
            if i.bottom_select[image.title]: i.y_len[image.title] = mouse.y - i.y_pos[image.title]; mouse.append({'UIheld': 1})
            if i.y_len[image.title] < 100: i.y_len[image.title] = 100
            if i.bottom_select[image.title] and not mouse.m1: i.bottom_select[image.title] = 0; mouse.append({'UIheld': 0})
            if windowbar.collidepoint(mouse.x, mouse.y) and mouse.t1: i.append({'x_diff': mouse.x - i.x_pos[image.title], 'y_diff': mouse.y - i.y_pos[image.title]}); i.selected.append(image.title); mouse.append({'UIheld': 1})
            if image.title in i.selected and not mouse.m1: i.selected.remove(image.title); i.delete(['x_diff', 'y_diff']); mouse.append({'UIheld': 0})
            if image.title in i.selected: i.x_pos.update({image.title: mouse.x - i.x_diff}); i.y_pos.update({image.title: mouse.y - i.y_diff})
            title_v = malleable_text(screen, i.x_pos[image.title], i.y_pos[image.title] + 12, image, ['title', 'x_pos', 'y_pos', 'layer'], mouse, tkey, key)
            if not title_v == None:
                exec('os.rename("UserImages/" + title_v[0] + images.' + title_v[0] + '.fileend, "UserImages/" + title_v[1] + images.' + title_v[0] + '.fileend)')
                exec('images.append({title_v[1]: images.' + title_v[0] + '})')
                images.delete([title_v[0]])
