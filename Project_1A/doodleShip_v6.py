'''

    Doodle Ship!
    Name: Clay Holmes
    Filename: doodleShip_v5.py
    Date Started: Aug 3, 2013
    Version: 5.0
    Description: 
    
'''
    
import pygame, random, math, os.path
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((800, 600))

class Ship(pygame.sprite.Sprite):
    def __init__(self, shell):        
        pygame.sprite.Sprite.__init__(self)
        self.shell = shell
        self.loadImages()
        self.shellcount = 0
        self.charge = 15
        self.dir = 0
        self.frame = 0
        self.delay = 0
        self.pause = 0
        

        self.image = self.imgList[0]
        
        self.image = pygame.transform.scale(self.imgList[self.frame], (120, 100))
        self.rect = self.image.get_rect()
        
        #loads the sound/music for the game
        if not pygame.mixer:
            print("problem with sound")
        else:
            pygame.mixer.init(48000, 16, 2, 4096)
            self.sndMusic = pygame.mixer.Sound("Assets/Sound/true_level1.ogg")
            self.sndShoot = pygame.mixer.Sound("Assets/Sound/ship_shoot.ogg")
            self.sndCrash = pygame.mixer.Sound("Assets/Sound/ship_hit.ogg")
            self.sndCrash.set_volume(0.2)
            self.sndShoot.set_volume(0.5)
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
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        
        
        self.frame = 0
        self.delay = 3
        self.pause = 0
        
        #health count for bot 
        self.Life = 3 
        self.timer = 90
        
        self.dx = random.randrange(6, 12)

        self.image = self.imgList[0]
        self.image = pygame.transform.scale(self.imgList[self.frame], (180, 175))
        self.rect = self.image.get_rect()
        
        #loads the sound/music for the game
        if not pygame.mixer:
            print("problem with sound")
        else:
            pygame.mixer.init(48000, 16, 2, 4096)
            self.sndShoot = pygame.mixer.Sound("Assets/Sound/squirm_shoot.ogg")
            self.sndShoot.set_volume(0.1)
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
        #self.checkTimer()
        self.pause += 1
        if self.pause >= self.delay:
            self.pause = 0
            self.frame += 1
            if self.frame >= len(self.imgList):
                self.frame = 0
            
            
                
            self.image = pygame.transform.scale(self.imgList[self.frame], (180, 175))
    
        #moves in a direction set through the rest function
        self.rect.centerx -= self.dx
        if (self.rect.right < (screen.get_width() - 800)) or (self.Life == 0):
            self.reset()
            
    #def checkTimer(self):
        #if self.timer <= 0:
            #self.sndShoot.play()   
            
    def reset(self):
        self.rect.centery = random.randrange(100, screen.get_height())
        self.rect.right = 1000        
        #movement is randomized based on ranges provided
        self.dx = random.randrange(3, 9)
        self.timer = 90
        self.Life = 3

class Crunchflyer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        
        self.frame = 0
        self.delay = 2
        self.pause = 0
        
        self.dx = random.randrange(12, 15)
        self.dy = random.randrange(-6, 6)

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
    
        #moves the enemy in a direction set through the rest function

        self.rect.centerx -= self.dx
        self.rect.centery -= self.dy
        if self.rect.right < (screen.get_width() - 800):
            self.reset()        

            
    def reset(self):
        self.rect.right = 1000
        self.rect.centery = random.randrange(100, screen.get_height())
        #movement is randomized based on ranges provided
        self.dx = random.randrange(12, 18)
        self.dy = random.randrange(-4, 4)

class HealthPack(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        
        self.frame = 0
        self.delay = 2
        self.pause = 0
        
        self.counter = 0
        
        self.dx = random.randrange(6, 12)

        self.image = self.imgList[0]
        self.image = pygame.transform.scale(self.imgList[self.frame], (97, 78))
        self.rect = self.image.get_rect()
        
        self.countdown = 900
        self.reset()
        
    def loadImages(self):
        imgMaster = pygame.image.load("Assets/Images/health_pack.png")
        imgMaster = imgMaster.convert()
        
        
        #image array to hold each image from an image master
        self.imgList = []
        
        imgSize = (194, 156)
        offset = ((54, 12), (260, 12), (466, 12), (260, 12), (56, 12), (670, 12), (872, 12), (670, 12))
            
        for i in range(8):
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
            
            
                
            self.image = pygame.transform.scale(self.imgList[self.frame], (97, 78))
    
        #moves the healthpack in a direction set through the rest function
        if self.counter <= 1:
            self.rect.centerx = -200
            self.countdown -= 1
            if self.countdown <= 0:
                    self.reset()
        else:
            self.countdown -= 1
            self.rect.centerx -= self.dx
            if self.rect.right < (screen.get_width() - 800):
                if self.countdown <= 0:
                    self.reset()        
            
    def reset(self):
        self.rect.right = 900
        self.rect.centery = random.randrange(0, screen.get_height())
        #healthpack movement is randomized based on ranges provided
        self.dx = random.randrange(3, 9)
        self.countdown = 1200
        self.counter += 1

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
        self.dx = 5
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
            self.sndIntro = pygame.mixer.Sound("Assets/Sound/levela.ogg")
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
        self.font = pygame.font.SysFont("Comic Sans MS", 45)
        
    def update(self):
        self.text = "Score: %d, Health: %d" % (self.score, self.health)
        self.image = self.font.render(self.text, 1, (0, 0, 0))
        self.rect = self.image.get_rect()

def game():
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Doodle Ship!")

        background = pygame.Surface(screen.get_size())
        background.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        
         #shell = Shell(screen)
        #shell1 = Shell1(screen)
        
        
        #shell = Shell(screen)
        fired_bullets = []
        ship_bullets = []
        for shell in range(10):
           shell = Shell(screen)
           ship_bullets.append(shell)
                
        ship = Ship(shell)
        paper = Paper()
                
        
        clouds = []
        for cloud in range(1, 4):
            cloud = Cloud()
            clouds.append(cloud)
            
        clouds1 = []
        for cloud1 in range(1, 4):
            cloud1 = Cloud1()
            clouds1.append(cloud1)
        
        squirmies = []
        for squirmy in range (1, 3):
            squirmy = Squirmbot()
            squirmies.append(squirmy)  
           
        
        crunchies = []
        for crunchy in range (1, 4):
            crunchy = Crunchflyer()
            crunchies.append(crunchy)
        
        healthPack = HealthPack()
        
        mountain = Mountain()
        
        scoreboard = Scoreboard()
        
        scoreSprite = pygame.sprite.Group(scoreboard)
        allSprites = pygame.sprite.OrderedUpdates(paper, mountain, clouds, shell, ship, clouds1)
        helpSprites = pygame.sprite.OrderedUpdates(healthPack)
        enemySprites = pygame.sprite.OrderedUpdates(squirmies)
        crunchSprites = pygame.sprite.OrderedUpdates(crunchies)        
        
        clock = pygame.time.Clock()
        keepGoing = True
        while keepGoing:
            clock.tick(30)
            pygame.mouse.set_visible(False)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    paper.sndIntro.stop()
                    keepGoing = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paper.sndIntro.stop()
                        keepGoing = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    ship.sndShoot.play()
                    #ship_bullets.append(shell)
                    ship.shells[self.shellcount].x = ship.rect.centerx
                    ship.shell[self.shellcount].y = ship.rect.centery
                    ship.shell[self.shellcount].speed = ship.charge
                    ship.shell[self.shellcount].dir = ship.dir
                    ship.shellcount += 1
                    if ship.shellcount >= 10:
                        ship.shellcount = 0
                    print ship_bullets
            
            hitBot = pygame.sprite.spritecollide(ship, enemySprites, False)
            if hitBot:
                ship.sndCrash.play()
                scoreboard.health -= 1
                if scoreboard.health <= 0:
                    paper.sndIntro.stop()
                    keepGoing = False
                for theBot in hitBot:
                    theBot.Life -= 3
                    theBot.reset()
                    
            crunchHit = pygame.sprite.spritecollide(ship, crunchSprites, False)
            if crunchHit:
                ship.sndCrash.play()
                scoreboard.health -= 1
                if scoreboard.health <= 0:
                    paper.sndIntro.stop()
                    keepGoing = False
                for theCrunch in crunchHit:
                    theCrunch.reset()
                    
            bulletHit = pygame.sprite.spritecollide(shell, enemySprites, False)
            if bulletHit:
                for theBot in bulletHit:                    
                    fired_bullets.append(shell)
                    shell.reset()
                    theBot.Life -= 1
                    if theBot.Life == 0:
                        scoreboard.score += 100
                        theBot.reset()
                        theBot.Life = 3
            
            bulletHit1 = pygame.sprite.spritecollide(shell, crunchSprites, False)
            if bulletHit1:
                for theBot in bulletHit1:
                    fired_bullets.append(shell)
                    scoreboard.score += 50
                    shell.reset()
                    theBot.reset()
                    
            for shell in fired_bullets:
                shell.reset()
                if (shell.x and shell.y) <= -100:
                    fired_bullets.pop()
            
            for shell in ship_bullets:
                if (shell.x and shell.y) <= -100:
                    ship_bullets.pop()
                                
            #Only restores health up to the max amount of health    
            hitHealth = pygame.sprite.collide_mask(ship, healthPack)
            if hitHealth:
                if scoreboard.health == 6:
                    scoreboard.health =+ 0
                    healthPack.rect.centerx = -200
                else:
                    scoreboard.health += 1
                    healthPack.rect.centerx = -200
            
            #allSprites.clear(screen, background)
            allSprites.update()
            #bulletSprites.update()
            enemySprites.update()
            crunchSprites.update()
            helpSprites.update()
            scoreSprite.update()
             
            allSprites.draw(screen)
            #bulletSprites.draw(screen)
            enemySprites.draw(screen)
            crunchSprites.draw(screen)
            helpSprites.draw(screen)                       
            scoreSprite.draw(screen)
            
            pygame.display.flip()
        
        
        ship.sndMusic.stop()
        #return mouse cursor
        pygame.mouse.set_visible(True)
        return scoreboard.score
        
def instructions(score):
    pygame.display.set_caption("Doodle Ship!")

    paper = Paper()
    paper.sndIntro.play(-1)
    
    allSprites = pygame.sprite.OrderedUpdates(paper)
    insFont = pygame.font.SysFont("Comic Sans MS", 35)
    insLabels = []
    instructions = (
    "",
    "Doodle Ship.     Last score: %d" % score ,
    "",
    "Instructions:  You take command,",
    "of the Doodle Attack Ship 'Wazo'.",
    "",
    "Shoot emeny ships, known as 'Squiggies',",
    "and avoid the evil Crunchers!",    
    "",
    "Apart from those dangers, collect",
    "health kits to heal, enjoy the scenery.",
    "",
    "Good luck!",
    "",
    "Click to Start, Escape to Quit..."
    )
    
    for line in instructions:
        tempLabel = insFont.render(line, 3, (0, 0, 0))
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
            #screen.blit(insLabels[i], (50, 30*i))
            screen.blit(insLabels[i], (35, 38*i))

        pygame.display.flip()
           
    pygame.mouse.set_visible(True)
    paper.sndIntro.stop()
    return donePlaying

def postGame(score):
    pygame.display.set_caption("Doodle Ship!")

    paper = Paper()
    paper.sndGameOver.play(-1)
    
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
            screen.blit(mesLabels[i], (45, 38*i))

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
