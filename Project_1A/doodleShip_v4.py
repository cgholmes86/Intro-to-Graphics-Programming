'''

    Doodle Ship!
    Name: Clay Holmes
    Filename: doodleShip_v4.py
    Date Started: Aug 3, 2013
    Version: 4.0
    Description: 
    
'''
    
import pygame, random, math, os.path
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((800, 600))

main_dir = os.path.split(os.path.abspath(__file__))[0]

def load_image(file):
    #adapted from aliens.py, found in pygame expamples
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, 'Assets\Images', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface.convert()

class Ship(pygame.sprite.Sprite):
    def __init__(self):        
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        self.screenRect = Rect(0, 0, 800, 600)
        
        self.maxBullets = 5
        self.reloading = 0
        
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
            self.get_pos()
            
    def get_pos(self):
        pos = self.rect.centery
        print "Position", pos
        return pos
                        
class Bullet(pygame.sprite.Sprite):    
    speed = -11
    images = []
    def __init__(self, pos):        
        pygame.sprite.Sprite.__init__(self, self.containers)
        
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        
        def update(self):
            self.rect.move_ip(self.speed, 0)
            if self.rect.left <= 0:
                self.kill()

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


class CyberBullet(pygame.sprite.Sprite):
    speed = 9
    images = []
    def __init__(self, squirmy):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midleft=
                    squirmy.rect.move(-5,0).midleft)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.left <= -20:
            self.kill()

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
        
        self.countdown = 1400
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
        
        Bullet.images = [load_image('bullet.gif')]
        CyberBullet.images = [load_image('bullet1.gif')]

        bullets = pygame.sprite.Group()
        cyberBullets = pygame.sprite.Group()
        lastSquirmy = pygame.sprite.GroupSingle()
                
        ship = Ship()
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
        allSprites = pygame.sprite.OrderedUpdates(paper, mountain, clouds, ship, clouds1)
        helpSprites = pygame.sprite.OrderedUpdates(healthPack)
        enemySprites = pygame.sprite.OrderedUpdates(squirmies)
        crunchSprites = pygame.sprite.OrderedUpdates(crunchies)        
        
        Bullet.containers = bullets, allSprites
        CyberBullet.containers = cyberBullets, allSprites
        
        
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
            ########################            
            #adapted from aliens.py (built-in pygame example)
            #handle player input
            keystate = pygame.key.get_pressed()
            firing = keystate[K_SPACE]
            if not ship.reloading and firing and len(bullets) < ship.maxBullets:
                Bullet(ship.get_pos())
                ship.sndShoot.play()
            ship.reloading = firing
            ########################
            ########################
            hitBot = pygame.sprite.spritecollide(ship, enemySprites, False)
            if hitBot:
                ship.sndCrash.play()
                scoreboard.health -= 1
                for theBot in hitBot:
                    theBot.Life -= 3
                if scoreboard.health <= 0:
                    paper.sndIntro.stop()
                    keepGoing = False
                
                    
            crunchHit = pygame.sprite.spritecollide(ship, crunchSprites, False)
            if crunchHit:
                ship.sndCrash.play()
                scoreboard.health -= 1
                if scoreboard.health <= 0:
                    paper.sndIntro.stop()
                    keepGoing = False
                for theCrunch in crunchHit:
                    theCrunch.reset()
            
            #launches cyber bullet?
            if squirmy.timer <= 0:
                CyberBullet(lastSquirmy.sprite)
            
            for enemySprites in pygame.sprite.groupcollide(bullets, enemySprites, 1, 1).keys():
                ship.sndCrash.play()
                scoreboard.score += 100
                
            for crunchSprites in pygame.sprite.groupcollide(bullets, crunchSprites, 1, 1).keys():
                ship.sndCrash.play()
                scoreboard.score += 50
                
            for cyberBullet in pygame.sprite.spritecollide(ship, cyberBullets, 1):
                ship.sndCrash.play()
                scoreboard.health -= 1
                                
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
            enemySprites.update()
            crunchSprites.update()
            helpSprites.update()
            scoreSprite.update()
            bullets.update() 
            allSprites.draw(screen)
            enemySprites.draw(screen)
            crunchSprites.draw(screen)
            helpSprites.draw(screen)                       
            scoreSprite.draw(screen)
            bullets.draw(screen)
            
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
