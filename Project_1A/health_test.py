'''
Created on Aug 5, 2013

@author: Clay
'''

import pygame, random
pygame.init()

screen = pygame.display.set_mode((640, 480))

class Plane(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("plane.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        
     
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (mousex, 430)
                
class Island(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("island.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dy = 5
    
    def update(self):
        self.rect.centery += self.dy
        if self.rect.top > screen.get_height():
            self.reset()
            
    def reset(self):
        self.rect.top = 0
        self.rect.centerx, self.rect.centery = pygame.mouse.get_pos()

class Ocean(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ocean.gif")
        self.rect = self.image.get_rect()
        self.dy = 5
        self.reset()
        
    def update(self):
        self.rect.bottom += self.dy
        if self.rect.bottom >= 1440:
            self.reset() 
    
    def reset(self):
        self.rect.top = -960

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.health = 6
        self.score = 0
        self.font = pygame.font.SysFont("Comic Sans MS", 50)
        
    def update(self):
        self.text = "Score: %d" % (self.score)
        self.image = self.font.render(self.text, 1, (0, 0, 0))
        self.rect = self.image.get_rect()

class Healthbar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        #self.font = pygame.font.SysFont("Comic Sans MS", 50)
        self.healthStatus = 6
        
        self.imageFull = pygame.image.load("Assets/Images/health_full.png")
        self.imageFull = self.imageFull.convert()
        self.imageSevenfive = pygame.image.load("Assets/Images/health_75.png")
        self.imageSevenfive = self.imageSevenfive.convert()
        self.imageSix = pygame.image.load("Assets/Images/health_60.png")
        self.imageSix = self.imageSix.convert()
        self.imageFive = pygame.image.load("Assets/Images/health_50.png")
        self.imageFive = self.imageFive.convert()
        self.imageTwo = pygame.image.load("Assets/Images/health_20.png")
        self.imageTwo = self.imageTwo.convert()
        self.imageZero = pygame.image.load("Assets/Images/health_0.png")
        self.imageZero = self.imageZero.convert()
        
        #self.text = "Health: "
        self.imageMaster = self.imageFull
        self.image = self.imageMaster
        self.rect = self.image.get_rect()
        self.x = 475
        self.y = 40
        self.rect.center = (self.x, self.y)
        
        def update(self):
            self.image = imageMaster
            self.rect = self.image.get_rect()
            self.rect.center = (self.x, self.y)
            print "health: " + self.healthStatus
                
def game():
    pygame.display.set_caption("Mail Pilot!")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    plane = Plane()
    island1 = Island()
    island2 = Island()
    island3 = Island()
    ocean = Ocean()
    scoreboard = Scoreboard()
    health = Healthbar()


    friendSprites = pygame.sprite.OrderedUpdates(ocean, plane)
    cloudSprites = pygame.sprite.Group(island1, island2, island3)
    scoreSprite = pygame.sprite.Group(scoreboard, health)

    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        
        #check collisions
       
        hitClouds1 = pygame.sprite.collide_mask(plane, island1)
        hitClouds2 = pygame.sprite.collide_mask(plane, island2)
        hitClouds3 = pygame.sprite.collide_mask(plane, island3)
        if hitClouds1 or hitClouds2 or hitClouds3:
            scoreboard.health -= 1
            health.healthStatus -= 1
            print health.healthStatus
            if scoreboard.health <= 0:
                keepGoing = False
            if hitClouds1:
                island1.reset()
            if hitClouds2:
                island2.reset()
            if hitClouds3:
                island3.reset()
        
        friendSprites.update()
        cloudSprites.update()
        scoreSprite.update()
        
        friendSprites.draw(screen)
        cloudSprites.draw(screen)
        scoreSprite.draw(screen)
        
        pygame.display.flip()
    
    #return mouse cursor
    pygame.mouse.set_visible(True) 
    return scoreboard.score
    
def instructions(score):
    pygame.display.set_caption("Mail Pilot!")

    plane = Plane()
    ocean = Ocean()
    
    allSprites = pygame.sprite.OrderedUpdates(ocean, plane)
    insFont = pygame.font.SysFont(None, 50)
    insLabels = []
    instructions = (
    "Mail Pilot.     Last score: %d" % score ,
    "Instructions:  You are a mail pilot,",
    "delivering mail to the islands.",
    "",
    "Fly over an island to drop the mail,",
    "but be careful not to fly too close",    
    "to the clouds. Your plane will fall ",
    "apart if it is hit by lightning too",
    "many times. Steer with the mouse.",
    "",
    "good luck!",
    "",
    "click to start, escape to quit..."
    )
    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (255, 255, 0))
        insLabels.append(tempLabel)
 
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
                donePlaying = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True
    
        allSprites.update()
        allSprites.draw(screen)

        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))

        pygame.display.flip()
          
    pygame.mouse.set_visible(True)
    return donePlaying
        
def main():
    donePlaying = False
    score = 0
    while not donePlaying:
        donePlaying = instructions(score)
        if not donePlaying:
            score = game()


if __name__ == "__main__":
    main()