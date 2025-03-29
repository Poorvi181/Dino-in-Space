import pygame,sys
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Dino in Space")
screen.fill("white")
pygame.display.update()
class Dino(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image= pygame.image.load("GameDev2/Dino.png")
        self.rect= self.image.get_rect()
        self.rect.center= [x,y]
    def update(self,key_pressed):
        if key_pressed[pygame.K_UP]:
            self.rect.move_ip(0,-2)
        if key_pressed[pygame.K_DOWN]:
            self.rect.move_ip(0,2)
        if key_pressed[pygame.K_LEFT]:
            self.rect.move_ip(-2,0)
        if key_pressed[pygame.K_RIGHT]:
            self.rect.move_ip(2,0)

dino1= Dino(100,100)
dinogrp= pygame.sprite.Group()
dinogrp.add(dino1)
dino2= Dino(300,150)
dinogrp.add(dino2)
dino3= Dino(150,300)
dinogrp.add(dino3)
dino4= Dino(100,300)
dinogrp.add(dino4)
while True:
    screen.fill("white")
    dinogrp.draw(screen)
    key_pressed=pygame.key.get_pressed()
    dino1.update(key_pressed)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
