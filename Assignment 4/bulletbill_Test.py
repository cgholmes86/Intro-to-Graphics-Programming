'''
side scroller
    Name: Clay Holmes
    Filename: bulletbill_Test.py
    Date Started: July 12, 2013
    Version: 0
    Description: Taking away elements of mailpilot.py (islands, clouds)
                 and making the scrolling background move in a horizontal motion.
                 Worked out how to get the background to loop properly
'''
    
import pygame, random
pygame.init()

screen = pygame.display.set_mode((640, 480))

class Plane(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("plane.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        
        if not pygame.mixer:
            print("problem with sound")
        else:
            pygame.mixer.init()
            self.sndYay = pygame.mixer.Sound("yay.ogg")
            self.sndThunder = pygame.mixer.Sound("thunder.ogg")
        
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (50, mousey)

class Bulletbill(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Assets/bill.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = 5
        self.countdown = 500
    
    def update(self):
        self.rect.centerx -= self.dx
        self.countdown -= 1
        print self.countdown
        if self.rect.right < (screen.get_width() - 640):
            if self.countdown <= 0:
                self.reset()
            
    def reset(self):
        self.rect.right = 640
        self.rect.centery = random.randrange(0, screen.get_height())
        self.countdown = 500
        
class Ocean(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Assets/background1.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dx = 5
        self.reset()
        
    def update(self):
        self.rect.right -= self.dx
        if self.rect.right == 640:
            self.reset() 
    
    def reset(self):
        self.rect.left = 0
        
def main():
        screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Mail Pilot! mpOcean.py - scrolling background")

        background = pygame.Surface(screen.get_size())
        background.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        plane = Plane()
        ocean = Ocean()
        bill = Bulletbill()
        
        allSprites = pygame.sprite.OrderedUpdates(ocean, plane)
        enemySprite = pygame.sprite.OrderedUpdates(bill)
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
            enemySprite.update()
            allSprites.draw(screen)
            enemySprite.draw(screen)
            
            pygame.display.flip()
        
        #return mouse cursor
        pygame.mouse.set_visible(True)
        
if __name__ == "__main__":
    main()
