'''
Created on Jul 11, 2013

@author: Clay
'''
import pygame
import random
pygame.init()

screen = pygame.display.set_mode((640, 480))

class Koopa(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        
        self.frame = 0
        self.delay = 0
        self.pause = 0
        
        self.dx = 3

        self.image = self.imgList[0]
        self.image = pygame.transform.scale(self.imgList[self.frame], (16, 28))
        self.rect = self.image.get_rect()
        self.reset()
        
    def loadImages(self):
        imgMaster = pygame.image.load("Assets/koopa_sheet.gif")
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
            
              
            self.image = pygame.transform.scale(self.imgList[self.frame], (16, 28))
            self.rect = self.image.get_rect()
#             self.rect.center = (400, 250)
            self.rect.centery += self.dy
            self.rect.centerx -= self.dx
            if self.rect.right < (screen.get_width() - 640):
                self.reset()  

    def reset(self):
        self.rect.right = 640
        self.rect.centery = random.randrange(0, screen.get_height())
        self.dx = random.randrange(6, 12)
        self.dy = random.randrange(-4, 4)

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
    
    level = Background()
    koopa = Koopa()
    
    shieldchk = 0
    
    allSprites = pygame.sprite.Group(level, koopa)
    
    clock = pygame.time.Clock()
    keepGoing = True
    
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            
    
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()
        
if __name__ == "__main__":
    main()
