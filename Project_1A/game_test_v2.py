'''

    Doodle Ship!
    Name: Clay Holmes
    Filename: doodleShip_v2.py
    Date Started: July 27, 2013
    Version: 2.0
    Description: 
    
'''
    
import pygame, random, math
pygame.init()

screen = pygame.display.set_mode((800, 600))


class Ship(pygame.sprite.Sprite):
    def __init__(self, shell):        
        self.shell = shell
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        
        self.charge = 10
        self.dir = 0
        self.frame = 0
        self.delay = 0
        self.pause = 0

        self.image = self.imgList[0]
        #scaled by a factor of 1.5 the original size
        self.image = pygame.transform.scale(self.imgList[self.frame], (120, 100))
        self.rect = self.image.get_rect()
        
        #loads the sound/music for the game
        if not pygame.mixer:
            print("problem with sound")
        else:
            pygame.mixer.init(48000, 16, 2, 4096)
            self.sndMusic = pygame.mixer.Sound("Assets/Sound/level1a.ogg")
            self.sndShoot = pygame.mixer.Sound("Assets/Sound/ship_shoot.ogg")
            self.sndMusic.play(-1)
        
    
    #loads master image and puts the offsets into an array    
    def loadImages(self):
        imgMaster = pygame.image.load("Assets/Images/ship_spritesheet.png")
        imgMaster = imgMaster.convert()
        
        self.imgList = []
        
        imgSize = (120, 100)
        offset = ((42,38), (240, 38), (440, 38), (640, 38))
            
        for i in range(4):
            tmpImg = pygame.Surface(imgSize)
            tmpImg.blit(imgMaster, (0, 0), (offset[i], imgSize))
            transColor = tmpImg.get_at((1, 1))
            tmpImg.set_colorkey(transColor)
            self.imgList.append(tmpImg)
    
    def update(self):
        self.checkClick()
        self.pause += 1
        if self.pause >= self.delay:
            self.pause = 0
            self.frame += 1
            if self.frame >= len(self.imgList):
                self.frame = 0
            
            #functionality for controlling Mario with the mouse
            mousex, mousey = pygame.mouse.get_pos()
            self.rect.center = (75, mousey)    
            self.image = pygame.transform.scale(self.imgList[self.frame], (120, 100))
    
    def checkClick(self):
        #keys = pygame.key.get_pressed()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.sndShoot.play()
            self.shell.x = self.rect.centerx
            self.shell.y = self.rect.centery
            self.shell.speed = self.charge
            self.shell.dir = self.dir

#Borrowed from turretFire.py
class Shell(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        
        self.image = pygame.image.load("Assets/Images/bullet.png")
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()
        self.rect.center = (-100, -100)
        
        self.speed = 0
        self.dir =0
        self.reset()
        
    def update(self):
        self.calcVector()
        self.calcPos()
        self.checkBounds()
        self.rect.center = (self.x, self.y)
   
    def calcVector(self):
        radians = self.dir * math.pi / 180
        
        self.dx = self.speed * math.cos(radians)
        self.dy = self.speed * math.sin(radians)
        self.dy *= -1
    
    def calcPos(self):
        self.x += self.dx
        self.y += self.dy
    
    def checkBounds(self):
        screen = self.screen
        if self.x > screen.get_width():
            self.reset()
        if self.x < 0:
            self.reset()
        if self.y > screen.get_height():
            self.reset()
        if self.y < 0:
            self.reset()
    
    def reset(self):
        """ move off stage and stop"""
        self.x = -100
        self.y = -100
        self.speed = 0

class Squirmbot(pygame.sprite.Sprite):
    def __init__(self, shell1):
        self.shell = shell1
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        
        self.charge = 10
        self.dir = 180
        self.frame = 0
        self.delay = 3
        self.pause = 0
        
        self.timer = 30
        
        self.dx = random.randrange(6, 12)
        #self.dy = random.randrange(-4, 4)

        self.image = self.imgList[0]
        self.image = pygame.transform.scale(self.imgList[self.frame], (180, 175))
        self.rect = self.image.get_rect()
        
        #loads the sound/music for the game
        if not pygame.mixer:
            print("problem with sound")
        else:
            pygame.mixer.init(48000, 16, 2, 4096)
            self.sndShoot = pygame.mixer.Sound("Assets/Sound/squirm_shoot.ogg")
        
        self.reset()
        
    def loadImages(self):
        imgMaster = pygame.image.load("Assets/Images/squirmy.png")
        imgMaster = imgMaster.convert()
        
        
        #image array to hold each image from an image master
        self.imgList = []
        
        imgSize = (180, 175)
        offset = ((9, 15), (218, 15), (428, 15), (620, 15))
            
        for i in range(4):
            tmpImg = pygame.Surface(imgSize)
            tmpImg.blit(imgMaster, (0, 0), (offset[i], imgSize))
            transColor = tmpImg.get_at((0, 0))
            tmpImg.set_colorkey(transColor)
            self.imgList.append(tmpImg)
    
    def update(self):
        self.timer -= 1
        self.checkTimer()
        self.pause += 1
        if self.pause >= self.delay:
            self.pause = 0
            self.frame += 1
            if self.frame >= len(self.imgList):
                self.frame = 0
            
            
                
            self.image = pygame.transform.scale(self.imgList[self.frame], (180, 175))
    
        #moves the coins in a direction set through the rest function
        #self.rect.centery += self.dy
        self.rect.centerx -= self.dx
        if self.rect.right < (screen.get_width() - 800):
            self.reset()
            
    def checkTimer(self):
        if self.timer <= 0:
            self.sndShoot.play()
            self.shell.x = self.rect.centerx
            self.shell.y = self.rect.centery
            self.shell.speed = self.charge
            self.shell.dir = self.dir   
            
    def reset(self):
        self.rect.right = 1000
        self.rect.centery = random.randrange(100, screen.get_height())
        #coin movement is randomized based on ranges provided
        self.dx = random.randrange(3, 9)
        self.timer = 30

class Shell1(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        
        self.image = pygame.image.load("Assets/Images/bullet1.png")
        self.image = pygame.transform.scale(self.image, (47, 7))
        self.rect = self.image.get_rect()
        self.rect.center = (-100, -100)
        
        self.speed = 0
        self.dir =0
        self.reset()
        
    def update(self):
        self.calcVector()
        self.calcPos()
        self.checkBounds()
        self.rect.center = (self.x, self.y)
   
    def calcVector(self):
        radians = self.dir * math.pi / 180
        
        self.dx = self.speed * math.cos(radians)
        self.dy = self.speed * math.sin(radians)
        self.dy *= -1
    
    def calcPos(self):
        self.x += self.dx
        self.y += self.dy
    
    def checkBounds(self):
        screen = self.screen
        if self.x > screen.get_width():
            self.reset()
        if self.x < 0:
            self.reset()
        if self.y > screen.get_height():
            self.reset()
        if self.y < 0:
            self.reset()
    
    def reset(self):
        """ move off stage and stop"""
        self.x = -100
        self.y = -100
        self.speed = 0


class Crunchflyer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        
        self.frame = 0
        self.delay = 2
        self.pause = 0
        
        self.dx = random.randrange(6, 12)
        self.dy = random.randrange(-4, 4)

        self.image = self.imgList[0]
        self.image = pygame.transform.scale(self.imgList[self.frame], (104, 66))
        self.rect = self.image.get_rect()
        
        self.reset()
        
    def loadImages(self):
        imgMaster = pygame.image.load("Assets/Images/crunchies.png")
        imgMaster = imgMaster.convert()
        
        
        #image array to hold each image from an image master
        self.imgList = []
        
        imgSize = (208, 132)
        offset = ((24, 21), (266, 21), (492, 21), (708, 21))
            
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
            
            
                
            self.image = pygame.transform.scale(self.imgList[self.frame], (104, 66))
    
        #moves the coins in a direction set through the rest function
        #self.rect.centery += self.dy
#        self.followMouse()
        self.rect.centerx -= self.dx
        if self.rect.right < (screen.get_width() - 800):
            self.reset()        
    
#    def followMouse(self):
#        (mouseX, mouseY) = pygame.mouse.get_pos()
#        self.dx = self.rect.centerx - mouseX
#        self.dy = self.rect.centery - mouseY
#        self.dy *= -1
            
    def reset(self):
        self.rect.right = 1000
        self.rect.centery = random.randrange(100, screen.get_height())
        #coin movement is randomized based on ranges provided
        self.dx = random.randrange(3, 9)


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Assets/Images/cloud.png")
        self.image = self.image.convert()        
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (100, 100))
        transColor = self.image.get_at((1, 1))
        self.image.set_colorkey(transColor)
        self.reset()
        
        #sets the horizontal movement
        self.dx = random.randrange(5, 9)
    
    def update(self):
        self.rect.centerx -= self.dx
        if self.rect.right < (screen.get_width() - 800):
            self.reset()
            
    def reset(self):
        self.rect.right = 900
        self.rect.centery = random.randrange(50, 200)

class Cloud1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Assets/Images/cloud1.png")
        self.image = self.image.convert()        
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (100, 100))
        transColor = self.image.get_at((1, 1))
        self.image.set_colorkey(transColor)
        self.reset()
        
        #sets the horizontal movement
        self.dx = random.randrange(5, 12)
    
    def update(self):
        self.rect.centerx -= self.dx
        if self.rect.right < (screen.get_width() - 800):
            self.reset()
            
    def reset(self):
        self.rect.right = 900
        self.rect.centery = random.randrange(250, 550)

class Mountain(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Assets/Images/mountains.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        transColor = self.image.get_at((1, 1))
        self.image.set_colorkey(transColor)
        self.dx = 3
        self.reset()
        
    def update(self):
        self.rect.right -= self.dx
        #COME BACK HERE TO CHANGE MOUNTAIN RESET
        if self.rect.right <= 2097:
            self.reset() 
    
    def reset(self):
        self.rect.left = -10
        
class Paper(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Assets/Images/level1.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dx = 5
        self.reset()
        
        #loads the sound/music for the game
        if not pygame.mixer:
            print("problem with sound")
        else:
            pygame.mixer.init(4800, 16, 2, 4096)
            self.sndIntro = pygame.mixer.Sound("Assets/Sound/heavy.ogg")
            self.sndGameOver = pygame.mixer.Sound("Assets/Sound/end_game.ogg")
        
    def update(self):
        self.rect.right -= self.dx
        if self.rect.right <= 990:
            self.reset() 
    
    def reset(self):
        self.rect.left = 0

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
            self.checkHealth()
            self.image = imageMaster            
            self.rect = self.image.get_rect()
            self.rect.center = (self.x, self.y)
            print "health: " + self.healthStatus
        def checkHealth(self):
            if self.healthStatus == 6:
                self.imageMaster = self.imageFull
            elif self.healthStatus == 5:
                self.imageMaster = self.imageSevenfive
            elif self.healthStatus == 4:
                self.imageMaster = self.imageSix
            elif self.healthStatus == 3:
                self.imageMaster = self.imageFive
            elif self.healthStatus == 2:
                self.imageMaster = self.imageTwo
            elif self.healthStatus == 1:
                self.imageMaster = self.imageZero

        
def game():
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Doodle Ship!")

        background = pygame.Surface(screen.get_size())
        background.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        
        ship_bullets = []
        for shell in range(1, 10):
            shell = Shell(screen)
            ship_bullets.append(shell)
                
        #shell = Shell(screen)
        shell1 = Shell1(screen)
        ship = Ship(shell)
        paper = Paper()
        
        #cloud = Cloud()
        #cloud1 = Cloud1()
        
        clouds = []
        for cloud in range(1, 4):
            cloud = Cloud()
            clouds.append(cloud)
            
        clouds1 = []
        for cloud1 in range(1, 4):
            cloud1 = Cloud1()
            clouds1.append(cloud1)
        
        
        squirmy = Squirmbot(shell1)  
        #health count for bot 
        squirmyLife = 5    
        crunchy = Crunchflyer()
        
        mountain = Mountain()
        
        health = Healthbar()
        scoreboard = Scoreboard()
        
        scoreSprite = pygame.sprite.Group(scoreboard, health)
        allSprites = pygame.sprite.OrderedUpdates(paper, mountain, clouds, ship_bullets, ship, clouds1)
        enemySprites = pygame.sprite.OrderedUpdates(shell1, squirmy, crunchy)
        #setSprites = pygame.sprite.OrderedUpdates(cloud, cloud1)        
        
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
            
            hitBot = pygame.sprite.collide_mask(ship, squirmy)
            if hitBot:
                #ship.sndCrash.play()
                scoreboard.health -= 1
                health.healthStatus -= 1
                if scoreboard.health <= 0:
                    keepGoing = False
                if hitBot:
                    squirmy.reset()
                    
            bulletHitBot1 = pygame.sprite.collide_mask(shell, squirmy)
            if bulletHitBot1:
                scoreboard.score += 100
                shell.reset()
                squirmyLife -= 1
                if squirmyLife == 0:
                    squirmy.reset()
                    squirmyLife = 5
                
            
            
            #allSprites.clear(screen, background)
            allSprites.update()
            enemySprites.update()
            scoreSprite.update() 
            allSprites.draw(screen)
            enemySprites.draw(screen)                       
            scoreSprite.draw(screen)
            
            pygame.display.flip()
        
        
        ship.sndMusic.stop()
        #return mouse cursor
        pygame.mouse.set_visible(True)
        return scoreboard.score
        
def instructions(score):
    pygame.display.set_caption("Doodle Ship!")

    paper = Paper()
    paper.sndIntro.play()
    
    allSprites = pygame.sprite.OrderedUpdates(paper)
    insFont = pygame.font.SysFont("Comic Sans MS", 35)
    insLabels = []
    instructions = (
    "Doodle Ship.     Last score: %d" % score ,
    "Instructions:  You take command,",
    "of the Doodle Attack Ship 'Wazo'.",
    "",
    "Shoot emeny ships, known as 'Squiggies',",
    "and avoid the evil erasers! (They will",    
    "literally erase your health!",
    "Apart from those dangers, collect",
    "health kits to heal, enjoy the scenery.",
    "",
    "good luck!",
    "",
    "click to start, escape to quit..."
    )
    
    for line in instructions:
        tempLabel = insFont.render(line, 2, (0, 0, 0))
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
        
    paper.sndIntro.stop()    
    pygame.mouse.set_visible(True)
    return donePlaying

def postGame(score):
    pygame.display.set_caption("Doodle Ship!")

    paper = Paper()
    paper.sndGameOver.play()
    
    allSprites = pygame.sprite.OrderedUpdates(paper)
    mesFont = pygame.font.SysFont("Comic Sans MS", 45)
    mesLabels = []
    goMessage = (
    "Doodle Ship.     Last score: %d" % score ,
    "",
    "",
    "",
    "Game Over!",
    "",    
    "Click to return to Main Menu",
    "or Press Escape to Quit."
    )
    
    for line in goMessage:
        tempLabel = mesFont.render(line, 2, (0, 0, 0))
        mesLabels.append(tempLabel)
 
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

        for i in range(len(mesLabels)):
            screen.blit(mesLabels[i], (50, 30*i))

        pygame.display.flip()
        
    paper.sndGameOver.stop()    
    pygame.mouse.set_visible(True)
    return donePlaying


def main():
    donePlaying = False
    score = 0
    while not donePlaying:
        donePlaying = instructions(score)
        if not donePlaying:
            score = game()
            donePlaying = postGame(score)
        
if __name__ == "__main__":
    main()
