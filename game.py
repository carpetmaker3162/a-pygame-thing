import pygame
import time
import random

pygame.init()

background_colour = (0,255,255)
(width, height) = 1000,500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("hey bae")
screen.fill(background_colour)
myfont = pygame.font.SysFont("arial", 72)

s = ''.join([chr(ch) for ch in 
[111,100,108,
116,104,120,
100,97,110,
104,110,98]])
s = ' '.join([s[i:i+4] for i in range(0,len(s),4)]).upper()
cns = {}
for ch in (65,97):
    for i in range(26):
        cns[chr(i+ch)]=chr((i+17)%26+ch)

label = myfont.render("".join([cns.get(ch, ch) for ch in s]), 1, (0,0,0))

pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    screen.blit(label, (190, 200))
    pygame.display.update()
    time.sleep(0.01)