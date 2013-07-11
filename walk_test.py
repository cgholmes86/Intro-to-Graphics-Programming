'''
Created on Jul 4, 2013

WORKS!!!!!!!!!!!!!!!!!

@author: Clay
'''

import pygame
pygame.init()


class Koopa(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        
        self.frame = 0
        self.delay = 7
        self.pause = 0

        self.image = self.imgList[0]
        self.image = pygame.transform.scale(self.imgList[self.frame], (48, 84))
        self.rect = self.image.get_rect()
        
    def loadImages(self):
        imgMaster = pygame.image.load("Assignment 4/Assets/koopa_sheet.gif")
        imgMaster = imgMaster.convert()
        
        self.imgList = []
        
        imgSize = (16, 28)
        offset = ((0, 0), (40, 0), (80, 0), (120, 0))
            
        for i in range(4):
            tmpImg = pygame.Surface(imgSize)
            tmpImg.blit(imgMaster, (0, 0), (offset[i], imgSize))
            transColor = tmpImg.get_at((1, 1))
            tmpImg.set_colorkey(transColor)
            self.imgList.append(tmpImg)
    
    def update(self):
        self.pause += 1
        if self.pause >= self.delay:
            self.pause = 0
            self.frame += 1
            if self.frame >= len(self.imgList):
                self.frame = 0
                
            self.image = pygame.transform.scale(self.imgList[self.frame], (48, 84))
            self.rect = self.image.get_rect()
            self.rect.center = (400, 100)

class Shield(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        
        self.frame = 0
        self.delay = 3
        self.pause = 0

        self.image = self.imgList[0]
        self.image = pygame.transform.scale(self.imgList[self.frame], (66, 100))
        self.rect = self.image.get_rect()
        
    def loadImages(self):
        imgMaster = pygame.image.load("turrican_sprite.gif")
        imgMaster = imgMaster.convert()
        
        self.imgList = []
        
        imgSize = (32, 40)
        offset = ((192, 39), (224, 39), (256, 39), (288, 39), (320, 39), (352, 39), (384, 39), (416, 39))
        
        '''
        offset = []
        
        for row in range (1):
            for col in range(8):
                temprow = row
                if row > 1:
                    temprow = row*38
                tempcol = col*32
                
                offset.append((tempcol, temprow))

        '''
            
        for i in range(8):
            tmpImg = pygame.Surface(imgSize)
            tmpImg.blit(imgMaster, (0, 0), (offset[i], imgSize))
            transColor = tmpImg.get_at((1, 1))
            tmpImg.set_colorkey(transColor)
            self.imgList.append(tmpImg)
    
    def update(self):
        self.pause += 1
        if self.pause >= self.delay:
            self.pause = 0
            self.frame += 1
            if self.frame >= len(self.imgList):
                self.frame = 0
                
            self.image = pygame.transform.scale(self.imgList[self.frame], (66, 100))
            self.rect = self.image.get_rect()
            self.rect.center = (400, 250)


class TRight(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        
        self.frame = 0
        self.delay = 2
        self.pause = 0

        self.image = self.imgList[0]
        self.image = pygame.transform.scale(self.imgList[self.frame], (66, 100))
        self.rect = self.image.get_rect()
        
    def loadImages(self):
        imgMaster = pygame.image.load("turrican_sprite.gif")
        imgMaster = imgMaster.convert()
        
        self.imgList = []
        
        imgSize = (32, 38)
        offset = ((513, 0), (545, 0), (577, 0), (608, 0), (640, 0), (672, 0), (704, 0), (736, 0), (768, 0), (800, 0), (832, 0), (864, 0), (896, 0), (929, 0))

        for i in range(14):
            tmpImg = pygame.Surface(imgSize)
            tmpImg.blit(imgMaster, (0, 0), (offset[i], imgSize))
            transColor = tmpImg.get_at((1, 1))
            tmpImg.set_colorkey(transColor)
            self.imgList.append(tmpImg)
    
    def update(self):
        self.pause += 1
        if self.pause >= self.delay:
            self.pause = 0
            self.frame += 1
            if self.frame >= len(self.imgList):
                self.frame = 0
                
            self.image = pygame.transform.scale(self.imgList[self.frame], (66, 100))
            self.rect = self.image.get_rect()
            self.rect.center = (400, 250)



class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("level1.gif")
        self.rect = self.image.get_rect()
            
def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Using a multi-image master file for walk test")
    
    background = pygame.Surface(screen.get_size())
    background.fill((0,0,0))
    screen.blit(background, (0, 0))
    
    turricanr = TRight()
    shield = Shield()
    level = Background()
    koopa = Koopa()
    
    shieldchk = 0
    
    allSprites = pygame.sprite.Group(level, turricanr, koopa)
    shieldSprite = pygame.sprite.Group()
    
    clock = pygame.time.Clock()
    keepGoing = True
    
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_g:
                        if shieldchk == 0:
                            shieldSprite = pygame.sprite.Group(shield)
                            shieldchk += 1
                        elif shieldchk == 1: 
                            shieldSprite = pygame.sprite.Group()
                            shieldchk -= 1
            
    
        allSprites.clear(screen, background)
        shieldSprite.clear(screen, background)
        allSprites.update()
        shieldSprite.update()
        allSprites.draw(screen)
        shieldSprite.draw(screen)
        
        pygame.display.flip()
        
if __name__ == "__main__":
    main()
