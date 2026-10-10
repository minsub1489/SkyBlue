import pygame as pg
import os, time, random, math

pg.init()

w = 1600
h = w * (9/16)

screen = pg.display.set_mode((w, h))

clock = pg.time.Clock()

main = True
ingame = True

keys = [0,0,0,0]
keyset = [0,0,0,0]

maxframe = 60
fps = 0

gst = time.time()
Time = time.time() - gst

ty = 0
tst = Time

t1 = []
t2 = []
t3 = []
t4 = []

Cpath = os.path.dirname(__file__)
Fpath = os.path.join("font")

rate =""

ingame_font_rate = pg.font.Font(os.path.join(Fpath, 'ingame_font.ttf'), int(w/23))
rate_text = ingame_font_rate.render(str(rate), False, (255,255,255))

def sum_note(n):
    if n == 1:
        ty = 0
        tst = Time + 2
        t1.append([ty, tst])
    if n == 2:
        ty = 0
        tst = Time + 2
        t2.append([ty, tst])
    if n == 3:
        ty = 0
        tst = Time + 2
        t3.append([ty, tst])
    if n == 4:
        ty = 0
        tst = Time + 2
        t4.append([ty, tst])

speed = 2

notesumt = 0

a=0
aa=0

combo = 0
combo_effect = 0
combo_effect2 = 0
miss_anim = 0
last_combo = 0
combo_time = Time + 1

rate_data = [0,0,0,0]

global effect_sound
effect_sound = pg.mixer.Sound('water_droplet.wav')

def rating(n):
  global combo, miss_anim, last_combo, combo_effect, combo_effect2, combo_time, rate
  if abs(Time - rate_data[n - 1]) < 2 and abs(Time - rate_data[n - 1]) >= 1:
    last_combo = combo
    miss_anim = 1
    combo = 0 
    combo_effect = 0.2
    combo_time = Time + 1
    combo_effect2 = 1.3
    rate = "WORST"
  if abs(Time - rate_data[n - 1]) < 1 and abs(Time - rate_data[n - 1]) >= 0.35:
    last_combo = combo
    miss_anim = 1
    combo = 0 
    combo_effect = 0.2
    combo_time = Time + 1
    combo_effect2 = 1.3
    rate = "BAD"
  if abs(Time - rate_data[n - 1]) < 0.35 and abs(Time - rate_data[n - 1]) >= 0.07:
    combo_effect = 0.2
    combo_time = Time + 1
    combo_effect2 = 1.3
    rate = "GOOD"
    combo += 1
  if abs(Time - rate_data[n - 1]) < 0.07 and abs(Time - rate_data[n - 1]) >= 0.035:
    combo_effect = 0.2
    combo_time = Time + 1
    combo_effect2 = 1.3
    rate = "GREAT"
    combo += 1
  if abs(Time - rate_data[n - 1]) < 0.035 and abs(Time - rate_data[n - 1]) >= 0:
    combo_effect = 0.2
    combo_time = Time + 1
    combo_effect2 = 1.3
    rate = "PERFECT"
    combo += 1


while main :
    while ingame :

        if len(t1) > 0:
            rate_data[0] = t1[0][1]
        if len(t2) > 0:
            rate_data[1] = t2[0][1]
        if len(t3) > 0:
            rate_data[2] = t3[0][1]
        if len(t4) > 0:
            rate_data[3] = t4[0][1]

        if Time > 0.2 * notesumt:
            notesumt += 1
            while a==aa:
                a=random.randint(1,4)
            sum_note(a)
            aa=a
        
        Time = time.time() - gst

        fps = clock.get_fps()
        
        ingame_font_combo = pg.font.Font(os.path.join(Fpath, 'ingame_font.ttf'), int((w/38) * combo_effect2))
        combo_text = ingame_font_combo.render(str(combo), False, (255,255,255))

        rate_text = ingame_font_rate.render(str(rate), False, (255,255,255))
        rate_text = pg.transform.scale(rate_text, (int(w / 110 * len(rate)* combo_effect2), int((w/58 * combo_effect * combo_effect2))))

        ingame_font_miss = pg.font.Font(os.path.join(Fpath, 'ingame_font.ttf'), int((w/38 * miss_anim)))  
        miss_text = ingame_font_miss.render(str(last_combo), False, (255,0,0))
        
        if fps == 0:
            fps = maxframe

        for event in pg.event.get():
            if event.type == pg.QUIT:
                main = False
                ingame = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_d:
                    pg.mixer.Sound.play(effect_sound)
                    keyset[0] = 1
                    if len(t1) > 0:
                        if t1[0][0] > h/3:
                            rating(1)
                            del t1[0]
                if event.key == pg.K_f:
                    pg.mixer.Sound.play(effect_sound)
                    keyset[1] = 1
                    if len(t2) > 0:
                        if t2[0][0] > h/3:
                            rating(2)
                            del t2[0]
                if event.key == pg.K_j:
                    pg.mixer.Sound.play(effect_sound)
                    keyset[2] = 1
                    if len(t3) > 0:
                        if t3[0][0] > h/3:
                            rating(3)
                            del t3[0]
                if event.key == pg.K_k:
                    pg.mixer.Sound.play(effect_sound)
                    keyset[3] = 1
                    if len(t4) > 0:
                        if t4[0][0] > h/3:
                            rating(4)
                            del t4[0]
            if event.type == pg.KEYUP:
                if event.key == pg.K_d:
                    keyset[0] = 0
                if event.key == pg.K_f:
                    keyset[1] = 0
                if event.key == pg.K_j:
                    keyset[2] = 0
                if event.key == pg.K_k:
                    keyset[3] = 0


        screen.fill((135,206,250))
        
        if fps == 0:
            fps = 60

        keys[0] += (keyset[0] - keys[0]) / (3 * (maxframe / fps))
        keys[1] += (keyset[1] - keys[1]) / (3 * (maxframe / fps))
        keys[2] += (keyset[2] - keys[2]) / (3 * (maxframe / fps))
        keys[3] += (keyset[3] - keys[3]) / (3 * (maxframe / fps))

        if Time > combo_time:
            combo_effect += (0 - combo_effect) / (7 * (maxframe / fps))
        if Time < combo_time:
            combo_effect += (1 - combo_effect) / (7 * (maxframe / fps))

        combo_effect2 += (2- combo_effect2) / (7 * (maxframe / fps))

        miss_anim += (4- miss_anim) / (14 * (maxframe / fps))

        pg.draw.rect(screen, (135,206,250), (w / 2 - w / 8, -int(w / 100), w / 4, h + int(w / 50)))       #gear background
        
        for i in range(7):
            i += 1
            pg.draw.rect(screen, (200 - ((200 / 7) * i), 200 - ((200 / 7) * i), 200 - ((200 / 7) * i)), (w / 2 - w / 8 + w / 32 - (w / 32) * keys[0], (h / 12) * 9 - (h / 30) * keys[0] * i, w / 16 * keys[0], (h / 35)/ i))
        for i in range(7):
            i += 1
            pg.draw.rect(screen, (200 - ((200 / 7) * i), 200 - ((200 / 7) * i), 200 - ((200 / 7) * i)), (w / 2 - w / 16 + w / 32 - (w / 32) * keys[1], (h / 12) * 9 - (h / 30) * keys[1] * i, w / 16 * keys[1], (h / 35)/ i))
        for i in range(7):
            i += 1
            pg.draw.rect(screen, (200 - ((200 / 7) * i), 200 - ((200 / 7) * i), 200 - ((200 / 7) * i)), (w / 2 + w / 32 - (w / 32) * keys[2], (h / 12) * 9 - (h / 30) * keys[2] * i, w / 16 * keys[2], (h / 35)/ i))
        for i in range(7):
            i += 1
            pg.draw.rect(screen, (200 - ((200 / 7) * i), 200 - ((200 / 7) * i), 200 - ((200 / 7) * i)), (w / 2 + w / 16 + w / 32 - (w / 32) * keys[3], (h / 12) * 9 - (h / 30) * keys[3] * i, w / 16 * keys[3], (h / 35)/ i))

        pg.draw.rect(screen, (255, 255, 255), (w / 2 - w / 8, -int(w / 100), w / 4, h + int(w /50)), int(w / 100))       #gear line

        #note========================================================================================================================
        
        for tile_data in t1:
            tile_data[0] = (h / 12) * 9 + (Time - tile_data[1]) * 350 * speed * (h/900)
            pg.draw.rect(screen, (255, 255, 255), (w / 2 - w / 8, tile_data[0] - h / 100, w /16, h / 50))
            if tile_data[0] > h - (h/9):
                last_combo = combo
                miss_anim = 1
                combo = 0 
                combo_effect = 0.2
                combo_time = Time + 1
                combo_effect2 = 1.3
                rate = "Miss"
                t1.remove(tile_data)
        for tile_data in t2:
            tile_data[0] = (h / 12) * 9 + (Time - tile_data[1]) * 350 * speed * (h/900)
            pg.draw.rect(screen, (255, 255, 255), (w / 2 - w / 16, tile_data[0] - h / 100, w /16, h / 50))
            if tile_data[0] > h - (h/9):
                last_combo = combo
                miss_anim = 1
                combo = 0 
                combo_effect = 0.2
                combo_time = Time + 1
                combo_effect2 = 1.3
                rate = "Miss"
                t2.remove(tile_data)
        for tile_data in t3:
            tile_data[0] = (h / 12) * 9 + (Time - tile_data[1]) * 350 * speed * (h/900)
            pg.draw.rect(screen, (255, 255, 255), (w / 2, tile_data[0] - h / 100, w /16, h / 50))        
            if tile_data[0] > h - (h/9):
                last_combo = combo
                miss_anim = 1
                combo = 0 
                combo_effect = 0.2
                combo_time = Time + 1
                combo_effect2 = 1.3
                rate = "Miss"
                t3.remove(tile_data)       
        for tile_data in t4:
            tile_data[0] = (h / 12) * 9 + (Time - tile_data[1]) * 350 * speed * (h/900)
            pg.draw.rect(screen, (255, 255, 255), (w / 2 + w / 16, tile_data[0] - h / 100, w /16, h / 50))     
            if tile_data[0] > h - (h/9):
                last_combo = combo
                miss_anim = 1
                combo = 0 
                combo_effect = 0.2
                combo_time = Time + 1
                combo_effect2 = 1.3
                rate = "Miss"
                t4.remove(tile_data)        

        pg.draw.rect(screen, (135,206,250), (w / 2 - w / 8, (h / 12) * 9, w / 4, h / 2))
        pg.draw.rect(screen, (255, 255, 255), (w / 2 - w / 8, (h / 12) * 9, w / 4, h / 2), int(h / 100))
        
        miss_text.set_alpha(255 - (255/4 * miss_anim))
        screen.blit(combo_text, (w/2 - rate_text.get_width()/2, (h/20)*2 - combo_text.get_height()/2))
        screen.blit(rate_text, (w/2 - rate_text.get_width()/2, (h/12)*8 - rate_text.get_height()/2))
        screen.blit(miss_text, (w/2 - miss_text.get_width()/2, (h/20)*2 - miss_text.get_height()/2))

        pg.display.flip()
        clock.tick(maxframe)



pg.quit()