'''
Created on Jul 29, 2013

@author: Clay
'''

#import modules, initialize pygame    
import pygame, random
pygame.init()

#displays the app in a set size window
screen = pygame.display.set_mode((640, 480))

#class for player avatar
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("turrican_right.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.movex = 0
        self.movey = 0
        
        if not pygame.mixer:
            print("problem with sound")
        else:
            pygame.mixer.init()
            self.sndRun = pygame.mixer.Sound("")
            self.sndShoot = pygame.mixer.Sound("")
            self.sndDead = pygame.mixer.Sound("")
            self.sndMusic = pygame.mixer.Sound("")
            self.sndMusic.play(-1)
            
    def update(self):
        1

#class for keeping track of score
class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 5
        self.score = 0
        #self.coins = 0
        self.font = pygame.font.SysFont("None", 50)
        
    def update(self):
        #displays lives (as 1ups), the score, and coins
        self.text = "lives: %d, score: %d" % (self.lives, self.score)
        self.image = self.font.render(self.text, 1, (255, 255, 0))
        self.rect = self.image.get_rect()

#class for the intro screen
class Intro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #displays a separate start screen
        self.image = pygame.image.load("")
        self.rect = self.image.get_rect()
        
        if not pygame.mixer:
            print("problem with sound")
        else:
            pygame.mixer.init(48000)
            #loads separate menu music
            self.sndMenu = pygame.mixer.Sound("")
            self.sndMenu.play(-1)


def game():
    
    pygame.display.set_caption("Platformer Test v1")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0)) 
    
    bg = Surface((32,32))
    bg.convert()
    bg.fill(Color("#000000"))  
    
    up  = left = right = False
    
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            #added the ability to quit to the menu if escape key pressed
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False 
    
    
def main():
    donePlaying = False
    score = 0
    while not donePlaying:
        donePlaying = instructions(score)
        if not donePlaying:
            score = game()


if __name__ == "__main__":
    main()
    