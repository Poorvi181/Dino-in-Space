import pygame,sys
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Dino in Space")
screen.fill("white")
pygame.display.update()
class Dino(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image= pygame.image.load("Dino.png")
        self.rect= self.image.get_rect()
        self.rect.center= [x,y]
dino1= Dino(100,100)
dinogrp= pygame.sprite.Group()
dinogrp.add(dino1)
while True:
    dinogrp.draw(screen)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()