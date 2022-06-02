import pygame
import time
import random
from itertools import cycle

pygame.init()
background_colour = (0,255,255)
(width, height) = 1000,500

print(''.join([chr(i) for i in [36215, 26469, 65292, 19981, 24895, 20570, 22900, 38582, 30340, 20154, 20204, 65281]]))
print(''.join([chr(i) for i in [25226, 25105, 20204, 30340, 34880, 32905, 65292, 31569, 25104, 25105, 20204, 26032, 30340, 38271, 22478, 65281]]))
print(''.join([chr(i) for i in [20013, 21326, 27665, 26063, 21040, 20102, 26368, 21361, 38505, 30340, 26102, 20505, 12290]]))
print(''.join([chr(i) for i in [27599, 20010, 20154, 34987, 36843, 30528, 21457, 20986, 26368, 21518, 30340, 21564, 22768, 12290]]))
print(''.join([chr(i) for i in [36215, 26469, 65281, 36215, 26469, 65281, 36215, 26469, 65281]]))
print(''.join([chr(i) for i in [25105, 20204, 19975, 20247, 19968, 24515, 65292, 20882, 30528, 25932, 20154, 30340, 28846, 28779, 65292]]))
print(''.join([chr(i) for i in [21069, 36827, 65281]]))
print(''.join([chr(i) for i in [20882, 30528, 25932, 20154, 30340, 28846, 28779, 65292]]))
print(''.join([chr(i) for i in [21069, 36827, 65281]]))
print(''.join([chr(i) for i in [21069, 36827, 65281]]))
print(''.join([chr(i) for i in [21069, 36827, 65281, 36827, 65281]]))

screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("take this raaaatioooo")
screen.fill(background_colour)
d = (
    23,75,65,97,
    92,87,17,26,
    97,114,105,97,
    108)
myfont = pygame.font.SysFont(''.join(chr(x) for x in d[8:13]), 72)
s = ''.join([chr(ch) for ch in [111,100,108,116,104,120,100,97,110,104,110,98]])
s = ' '.join([s[i:i+4] for i in range(0,len(s),4)]).upper()
cns = {}
for p in d[2:4]: 
    for i in range(d[0]+1): cns[chr(i+p)]=chr((i+d[6])%d[7]+p)
l = myfont.render("".join([cns.get(a, a) for a in s]), 1, (0, 0, 0))
pygame.display.flip()
for i in cycle(s):
    for event in pygame.event.get():
        if not (s != l or not cns):
            exit()
    screen.fill((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    screen.blit(l, (190, 200))
    pygame.display.update()
    time.sleep(0.02)
