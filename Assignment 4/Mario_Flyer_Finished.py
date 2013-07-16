""" 
    Mario Flyer!
    Name: Clay Holmes
    Filename: Mario_Flyer_Finished.py
    Date Started: July 15, 2013
    Version: 6a
    Description: Mario Flyer, a side-scrolling adventure starring everyone's 
                favourite Italian plumber!  Take to the skies as Mario using
                his famous Tanooki suit (racoon suit) to collect as many 
                mushrooms as possible to increase your score and even give you
                extra 1Ups.  Collect coins to increase your score as well.  
                But be aware of the evil Koopas who will try and stop you from
                collecting the mushrooms and coins.  Also look out for Bullet
                Bill, as he is helping the pesky Koopas too. 
    
    
                Fixes from last version: Removed extra bullet bills as they 
                were overlapping each other and making the game end sooner 
                if hit by what seemed like 1
    
"""
 
#import modules, initialize pygame    
import pygame, random
pygame.init()

#displays the app in a set size window
screen = pygame.display.set_mode((640, 480))

#create a class to control Mario

class Mario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        
        self.frame = 0
        self.delay = 0
        self.pause = 0

        self.image = self.imgList[0]
        #scaled by a factor of 1.5 the original size
        self.image = pygame.transform.scale(self.imgList[self.frame], (36, 42))
        self.rect = self.image.get_rect()
        
        #loads the sound/music for the game
        if not pygame.mixer:
            print("problem with sound")
        else:
            pygame.mixer.init(48000)
            self.sndYay = pygame.mixer.Sound("Sound/smb3_power-up.ogg")
            self.sndOops = pygame.mixer.Sound("Sound/smb3_pipe.ogg")
            self.sndOneUp = pygame.mixer.Sound("Sound/smb3_1-up.ogg")
            self.sndCoin = pygame.mixer.Sound("Sound/smb3_coin.ogg")            
            self.sndEnd = pygame.mixer.Sound("Sound/smb3_player_down.ogg")
            self.sndMusic = pygame.mixer.Sound("Sound/sky_theme.ogg")            
            self.sndStart = pygame.mixer.Sound("Sound/smb3_new_world.ogg")
            self.sndMusic.play(-1)
    
    #loads master image and puts the offsets into an array    
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
            
            #functionality for controlling Mario with the mouse
            mousex, mousey = pygame.mouse.get_pos()
            self.rect.center = (50, mousey)    
            self.image = pygame.transform.scale(self.imgList[self.frame], (36, 42))

class Mushroom(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Assets/mushroom.gif")
        self.image = self.image.convert()        
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (18, 18))
        self.reset()
        
        #sets the horizontal movement
        self.dx = 7
    
    def update(self):
        self.rect.centerx -= self.dx
        if self.rect.right < (screen.get_width() - 640):
            self.reset()
            
    def reset(self):
        self.rect.right = 680
        self.rect.centery = random.randrange(0, screen.get_height())

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        
        self.frame = 0
        self.delay = 5
        self.pause = 0
        
        self.dx = random.randrange(6, 12)
        #self.dy = random.randrange(-4, 4)

        self.image = self.imgList[0]
        self.image = pygame.transform.scale(self.imgList[self.frame], (13, 15))
        self.rect = self.image.get_rect()
        
        self.reset()
        
    def loadImages(self):
        imgMaster = pygame.image.load("Assets/coin_animate.gif")
        imgMaster = imgMaster.convert()
        
        
        #image array to hold each image from an image master
        self.imgList = []
        
        imgSize = (13, 17)
        offset = ((0, 0), (18, 0), (28, 0), (42, 0), (56, 0))
            
        for i in range(5):
            tmpImg = pygame.Surface(imgSize)
            tmpImg.blit(imgMaster, (0, 0), (offset[i], imgSize))
            transColor = tmpImg.get_at((0, 1))
            tmpImg.set_colorkey(transColor)
            self.imgList.append(tmpImg)
    
    def update(self):
        self.pause += 1
        if self.pause >= self.delay:
            self.pause = 0
            self.frame += 1
            if self.frame >= len(self.imgList):
                self.frame = 0
            
            
                
            self.image = pygame.transform.scale(self.imgList[self.frame], (13, 15))
    
        #moves the coins in a direction set through the rest function
        #self.rect.centery += self.dy
        self.rect.centerx -= self.dx
        if self.rect.right < (screen.get_width() - 640):
            self.reset()        
            
    def reset(self):
        self.rect.right = 640
        self.rect.centery = random.randrange(0, screen.get_height())
        #coin movement is randomized based on ranges provided
        self.dx = random.randrange(3, 9)
        #self.dy = random.randrange(-3, 3)

class Koopa(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        
        self.frame = 0
        self.delay = 7
        self.pause = 0
        
        self.dx = random.randrange(10, 15)
        self.dy = random.randrange(-3, 7)

        self.image = self.imgList[0]
        self.image = pygame.transform.scale(self.imgList[self.frame], (24, 42))
        self.rect = self.image.get_rect()
        
        self.reset()
        
    def loadImages(self):
        imgMaster = pygame.image.load("Assets/koopa_sheet.gif")
        imgMaster = imgMaster.convert()
        
        #array for image master
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
            
            
                
            self.image = pygame.transform.scale(self.imgList[self.frame], (24, 42))
            
        self.rect.centery += self.dy
        self.rect.centerx -= self.dx
        if self.rect.right < (screen.get_width() - 640):
            self.reset()        
            
    def reset(self):
        self.rect.right = 640
        self.rect.centery = random.randrange(0, screen.get_height())
        self.dx = random.randrange(6, 12)
        self.dy = random.randrange(-4, 4)

class Bulletbill(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Assets/bill.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (38, 36))
        self.reset()
        
        self.dx = 12
        #custom timer to have bullet bill appear periodically
        #instead of once he reaches the edge of the screen/hits Mario
        self.countdown = 300
        
        if not pygame.mixer:
            print("problem with sound")
        else:
            pygame.mixer.init(48000)
            #sound for when bullet bill appears
            self.sndThud = pygame.mixer.Sound("Sound/thud.ogg")
            self.sndThud.play()
    
    def update(self):
        self.rect.centerx -= self.dx
        self.countdown -= 1
        if self.rect.right < (screen.get_width() - 640):
            if self.countdown <= 0:
                self.reset()
                self.sndThud.play()
            
    def reset(self):
        #resets bill and his countdown timer
        self.rect.right = 680
        self.rect.centery = random.randrange(0, screen.get_height())
        self.countdown = 300
        
   
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
        #displays lives (as 1ups), the score, and coins
        self.text = "1ups: %d, score: %d, coins: %d" % (self.lives, self.score, self.coins)
        self.image = self.font.render(self.text, 1, (255, 255, 0))
        self.rect = self.image.get_rect()

class Intro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #displays a separate start screen from the game scroll
        self.image = pygame.image.load("Assets/mario_start.gif")
        self.rect = self.image.get_rect()
        
        if not pygame.mixer:
            print("problem with sound")
        else:
            pygame.mixer.init(48000)
            #loads separate menu music
            self.sndMenu = pygame.mixer.Sound("Sound/world_map.ogg")
            self.sndMenu.play(-1)
    
def game():
    pygame.display.set_caption("Mario Flyer!")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    mario = Mario()    
    #plays the start sound once, as the game transitions from menu to game screen
    mario.sndStart.play()
    mushroom = Mushroom()
    #creates an array of coins, easier to add/remove as necessary
    coins = []
    for coin in range(1, 8):
        coin = Coin()
        coins.append(coin)
    
    bill = Bulletbill()
    #creates an array for koopas, makes it easier to add/remove as necessary
    koopas = []
    for koopa in range(1,7):
        koopa = Koopa()
        koopas.append(koopa)

    mKingdom = MKingdom()
    scoreboard = Scoreboard()
    
    #variable used to gain extra lives by reaching multiples of 1000 on the scoreboard 
    oneUp = 1000
    
    #coin variables to give extra lives and mushroom score when certain amounts of coins are collected
    coinCheck = 25
    coin1UpCheck = 50

    friendSprites = pygame.sprite.OrderedUpdates(mKingdom, mushroom, mario)
    coinSprites = pygame.sprite.Group(coins)
    koopaSprites = pygame.sprite.Group(koopas)
    billSprites = pygame.sprite.Group(bill)
    scoreSprite = pygame.sprite.Group(scoreboard)

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

        
        #check collisions
        
        if mario.rect.colliderect(mushroom.rect):
            mario.sndYay.play()
            mushroom.reset()
            scoreboard.score += 100
         
        #for coins, does 2 checks; 1 to add coins to to coin counter,
        #1 to add to another counter that adds points to the scoreboard
        #when a certain amount of coins are collected   
        coinGrab = pygame.sprite.spritecollide(mario, coinSprites, False)
        if coinGrab:
            mario.sndCoin.play()
            scoreboard.coins += 1
            if scoreboard.coins == coinCheck:
                mario.sndYay.play()
                scoreboard.score += 100
                coinCheck += 25
            if scoreboard.coins == coin1UpCheck:
                mario.sndOneUp.play()
                scoreboard.lives += 1
                coin1UpCheck += 50
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
        
        #because of bullet bill's timed updates (to make him more like his
        #Mario game counterpart) if mario hits bullet bill, bullet bill
        #is removed from the screen rather than calling for his reset function       
        hitBill = pygame.sprite.spritecollide(mario, billSprites, False)
        if hitBill:
            mario.sndOops.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
               keepGoing = False
            for theBill in hitBill:
                bill.rect.right = -100
            
                
        #mario gains a 1-up and the 1up variable is increased by 500        
        if scoreboard.score == oneUp:
            mario.sndOneUp.play()
            scoreboard.lives += 1
            oneUp += 1000
       
        friendSprites.update()
        coinSprites.update()
        koopaSprites.update()
        billSprites.update()
        scoreSprite.update()
        
        friendSprites.draw(screen)
        coinSprites.draw(screen)
        koopaSprites.draw(screen)
        billSprites.draw(screen)
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
    "mushrooms, increase score by 100.",
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
    
    
