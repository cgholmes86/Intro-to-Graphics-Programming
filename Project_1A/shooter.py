'''
Created on Jul 27, 2013

@author: Clay
'''

#import modules, initialize pygame    
import pygame, random
pygame.init()

#displays the app in a set size window
screen = pygame.display.set_mode((640, 480))

#create a class to control Mario

class scoreBox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        
        self.image = self.imgList[0]
        #scaled by a factor of 1.5 the original size
        self.image = pygame.transform.scale(self.imgList[self.frame], (192, 34))
        self.rect = self.image.get_rect()
        
    #loads master image and puts the offsets into an array    
    def loadImages(self):
        imgMaster = pygame.image.load("Assets/Images/38084.png")
        imgMaster = imgMaster.convert()
        
        self.imgList = []
        
        imgSize = (192, 34)
        offset = ((30, 6))
            
        for i in range(1):
            tmpImg = pygame.Surface(imgSize)
            tmpImg.blit(imgMaster, (36, 6), (offset[i], imgSize))
            transColor = tmpImg.get_at((1, 1))
            tmpImg.set_colorkey(transColor)
            self.imgList.append(tmpImg)
    
    def update(self):
        
        self.rect.center = (100, 100)    
        self.image = pygame.transform.scale(self.imgList[self.frame], (192, 34))
        
        
def main():
        screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("TEST")

        background = pygame.Surface(screen.get_size())
        background.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        score = scoreBox()
        
        
        allSprites = pygame.sprite.OrderedUpdates(scoreBox)
        
        clock = pygame.time.Clock()
        keepGoing = True
        while keepGoing:
            clock.tick(30)
            pygame.mouse.set_visible(False)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False
                                   
            
            #allSprites.clear(screen, background)
            allSprites.update()
            allSprites.draw(screen)
            
            pygame.display.flip()
        
        #return mouse cursor
        pygame.mouse.set_visible(True)
        
if __name__ == "__main__":
    main()
