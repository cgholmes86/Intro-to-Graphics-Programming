""" 
    side scroller
    Name: Clay Holmes
    Filename: sideScroller_v5.py
    Date Started: June 23, 2013
    Version: 5
    Description: 
    
"""
 
#import modules, initialize pygame    
import pygame, random
pygame.init()

#displays the app in a set size window
screen = pygame.display.set_mode((640, 480))

#create a class to control Mario

class MarioMove(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        
        self.frame = 0
        self.delay = 0
        self.pause = 0

        self.image = self.imgList[0]
        self.image = pygame.transform.scale(self.imgList[self.frame], (24, 28))
        self.rect = self.image.get_rect()
        
        if not pygame.mixer:
            print("problem with sound")
        else:
            pygame.mixer.init(48000)
            self.sndYay = pygame.mixer.Sound("Sound/smb3_power-up.ogg")
            self.sndOops = pygame.mixer.Sound("Sound/smb3_pipe.ogg")
            self.sndOneUp = pygame.mixer.Sound("Sound/smb3_1-up.ogg")
            self.sndCoin = pygame.mixer.Sound("Sound/smb3_coin.ogg")            
            self.sndEnd = pygame.mixer.Sound("Sound/smb3_player_down.ogg")
            #self.sndMenu = pygame.mixer.Sound("menu.ogg")
            self.sndMusic = pygame.mixer.Sound("Sound/sky_theme.ogg")
            self.sndMusic.play(-1)
        
    def loadImages(self):
        imgMaster = pygame.image.load("Assets/mario_move.gif")
        imgMaster = imgMaster.convert()
        
        self.imgList = []
        
        imgSize = (24, 28)
        offset = ((0, 0), (0, 0), (30, 0), (30, 0), (60, 0), (60, 0))
            
        for i in range(6):
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
            
            
            mousex, mousey = pygame.mouse.get_pos()
            self.rect.center = (50, mousey)    
            self.image = pygame.transform.scale(self.imgList[self.frame], (24, 28))
#             self.rect = self.image.get_rect()

class Mushroom(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Assets/mushroom.gif")
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
    def __init__(self, background):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Assets/coin.gif")
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
        self.dy = random.randrange(-3, 3)

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
        self.dx = random.randrange(6, 12)
        self.dy = random.randrange(-4, 4)
   
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
        self.text = "1ups: %d, score: %d, coins: %d" % (self.lives, self.score, self.coins)
        self.image = self.font.render(self.text, 1, (255, 255, 0))
        self.rect = self.image.get_rect()

class Intro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Assets/mario_start.gif")
        self.rect = self.image.get_rect()
        
        if not pygame.mixer:
            print("problem with sound")
        else:
            pygame.mixer.init(48000)
            self.sndMenu = pygame.mixer.Sound("Sound/world_map.ogg")
            self.sndMenu.play(-1)
    
def game():
    pygame.display.set_caption("Mario Flyer!")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    mario = MarioMove()
    mushroom = Mushroom()
    coins = []
    for coin in range(1, 6):
        coin = Coin(background, )
        coins.append(coin)
    
    koopa1 = Koopa()
    koopa2 = Koopa()
    koopa3 = Koopa()
    mKingdom = MKingdom()
    scoreboard = Scoreboard()
    
    #variable used to gain extra lives by reaching multiples of 1000 on the scoreboard 
    oneUp = 1000
    
    #coin variables to give extra lives and mushroom score when certain amounts of coins are collected
    coinCheck = 10
    coinCheck2 = 50

    friendSprites = pygame.sprite.OrderedUpdates(mKingdom, mushroom, mario)
    coinSprites = pygame.sprite.Group(coins)
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False

        
        #check collisions
        
        if mario.rect.colliderect(mushroom.rect):
            mario.sndYay.play()
            mushroom.reset()
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
     
    mario.sndMusic.stop()
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
    "Mario Flyer.  Last score: %d" % score,
    "Instructions:  You are Mario,",
    "collecting stars in the Mushroom",
    "Kingdom.",
    "",
    "Fly over a mushroom to collect it,",
    "but be careful not to fly too close",    
    "to the koopas. If you collect 10",
    "mushroom, score increased by 100.",
    "Steer with the mouse.",
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
        
    intro.sndMenu.stop()    
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
    
    
