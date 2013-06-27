""" 
    side scroller
    Name: Clay Holmes
    Filename: sideScroller_v4.py
    Date Started: June 26, 2013
    Version: 4.0
    Description: Added in coins to help increase score and lives
    
"""
 
#import modules, initialize pygame    
import pygame, random
pygame.init()

#displays the app in a set size window
screen = pygame.display.set_mode((640, 480))

#create a class to control the 'plane' 
class Mario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Assets/mario.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        
        if not pygame.mixer:
            print("problem with sound")
        else:
            pygame.mixer.init()
            self.sndYay = pygame.mixer.Sound("Sound/smb3_power-up.ogg")
            self.sndOops = pygame.mixer.Sound("Sound/smb3_pipe.ogg")
            self.sndOneUp = pygame.mixer.Sound("Sound/smb3_1-up.ogg")
            self.sndCoin = pygame.mixer.Sound("Sound/smb3_coin.ogg")
            #self.sndMenu = pygame.mixer.Sound("menu.ogg")
            #self.sndMusic = pygame.mixer.Sound("engine.ogg")
            #self.sndMusic.play(-1)
    #sets where the sprite will be on screen and how it
    #moves based on mouse movement (y axis) 
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (50, mousey)
                
class Star(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Assets/star.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = 5
    
    def update(self):
        self.rect.centerx -= self.dx
        if self.rect.right < (screen.get_width() - 640):
            self.reset()
            
    def reset(self):
        self.rect.right = 640
        self.rect.centery = random.randrange(0, screen.get_height())
        
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Assets/coin.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = 8
    
    def update(self):
        self.rect.centerx -= self.dx
        if self.rect.right < (screen.get_width() - 640):
            self.reset()
            
    def reset(self):
        self.rect.right = 640
        self.rect.centery = random.randrange(0, screen.get_height())
      
class Koopa(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Assets/koopa.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()

    def update(self):
        self.rect.centery += self.dy
        self.rect.centerx -= self.dx
        if self.rect.right < (screen.get_width() - 640):
            self.reset()
    
    def reset(self):
        self.rect.right = 640
        self.rect.centery = random.randrange(0, screen.get_height())
        self.dx = random.randrange(3, 9)
        self.dy = random.randrange(-2, 2)
    
class MKingdom(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Assets/background1.gif")
        self.rect = self.image.get_rect()
        self.dx = 5
        self.reset()
        
    def update(self):
        self.rect.right -= self.dx
        if self.rect.right == 640:
            self.reset() 
    
    def reset(self):
        self.rect.left = 0

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 5
        self.score = 0
        self.coins = 0
        self.font = pygame.font.SysFont("None", 50)
        
    def update(self):
        self.text = "1ups: %d, stars: %d, coins: %d" % (self.lives, self.score, self.coins)
        self.image = self.font.render(self.text, 1, (255, 255, 0))
        self.rect = self.image.get_rect()

class Intro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Assets/mario_start.gif")
        self.rect = self.image.get_rect()
    
def game():
    pygame.display.set_caption("Mario Flyer!")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    mario = Mario()
    star = Star()
    coin1 = Coin()
    coin2 = Coin()
    coin3 = Coin()
    koopa1 = Koopa()
    koopa2 = Koopa()
    koopa3 = Koopa()
    mKingdom = MKingdom()
    scoreboard = Scoreboard()
    
    #variable used to gain extra lives by reaching multiples of 1000 on the scoreboard 
    oneUp = 1000
    
    #coin variables to give extra lives and stars when certain amounts of coins are collected
    coinCheck = 10
    coinCheck2 = 50

    friendSprites = pygame.sprite.OrderedUpdates(mKingdom, star, mario)
    coinSprites = pygame.sprite.Group(coin1, coin2, coin3)
    koopaSprites = pygame.sprite.Group(koopa1, koopa2, koopa3)
    scoreSprite = pygame.sprite.Group(scoreboard)

    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        
        #check collisions
        
        if mario.rect.colliderect(star.rect):
            mario.sndYay.play()
            star.reset()
            scoreboard.score += 100

        coinGrab = pygame.sprite.spritecollide(mario, coinSprites, False)
        if coinGrab:
            mario.sndCoin.play()
            scoreboard.coins += 1
            if scoreboard.coins == coinCheck:
                mario.sndYay.play()
                scoreboard.score += 100
                coinCheck += 10
            if scoreboard.coins == coinCheck2:
                mario.sndOneUp.play()
                scoreboard.lives += 1
                coinCheck2 += 50
            for theCoin in coinGrab:
                theCoin.reset()

        hitKoopas = pygame.sprite.spritecollide(mario, koopaSprites, False)
        if hitKoopas:
            mario.sndOops.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                keepGoing = False
            for theKoopa in hitKoopas:
                theKoopa.reset()
                
        #mario gains a 1-up and the 1up variable is increased by 500        
        if scoreboard.score == oneUp:
            mario.sndOneUp.play()
            scoreboard.lives += 1
            oneUp += 1000
       
        friendSprites.update()
        coinSprites.update()
        koopaSprites.update()
        scoreSprite.update()
        
        friendSprites.draw(screen)
        coinSprites.draw(screen)
        koopaSprites.draw(screen)
        scoreSprite.draw(screen)
        
        pygame.display.flip()
     
    #mario.sndMusic.stop()
    #return mouse cursor
    pygame.mouse.set_visible(True) 
    return scoreboard.score
    
def instructions(score):
    pygame.display.set_caption("Mario Flyer!")

    intro = Intro()
    
    allSprites = pygame.sprite.Group(intro)
    insFont = pygame.font.SysFont(None, 50)
    insLabels = []
    instructions = (
    "Mario Flyer.  Last score: %d" % score +" stars",
    "Instructions:  You are Mario,",
    "collecting stars in the Mushroom",
    "Kingdom.",
    "",
    "Fly over a star to collect it,",
    "but be careful not to fly too close",    
    "to the flying ducks. Mario doesn't",
    "take kindly to angry birds.",
    "Steer with the mouse.",
    "",
    "good luck!",
    "",
    "click to start, escape to quit..."
    )
    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (255, 255, 255))
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
        
    #mario.sndMusic.stop()    
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
    
    
