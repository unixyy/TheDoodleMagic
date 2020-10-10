#!/usr/bin/env python3
import pygame
from pygame.locals import *
import sys
import random

class DoodleJump(object):
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load("assets/Nyan Cat [original].mp3")
        pygame.mixer.music.play(50)
        self.screen_width=1360
        self.screen_height=750
        self.screen=pygame.display.set_mode([self.screen_width,self.screen_height], FULLSCREEN)
        self.playerRight_1 = pygame.image.load("assets/nyancatR.png").convert_alpha()
        self.playerRight = pygame.image.load("assets/nyancatR.png").convert_alpha()
        self.playerLeft = pygame.image.load("assets/nyancatL.png").convert_alpha()
        self.playerLeft_1 = pygame.image.load("assets/nyancatL.png").convert_alpha()
        self.cameray = 0
        self.playerx = 400
        self.playery = 400
        self.xmovement = 0
        self.jump = 0
        self.direction = 0
        self.gravity = 0
        self.green = pygame.image.load("assets/ARC EN CIEL.png").convert_alpha()
        self.platforms = [[400, 500]]
        self.spaceship = 0
        self.trumpmode = 0
        self.nyanmode = 1
        self.ougandamode = 0
        pygame.font.init()
        self.col_red = 1
        self.col_green = 125
        self.col_blue = 255
        self.wtf = 0
        self.txtend = 0
        self.accordmove = 1
        self.accordmusic = 1
        self.toucherestart = 0
        self.juifmode = 0
        self.plateformerandom = 0
        self.vie = 5
        self.generateplateformerandom = 0
        self.pausemenu = 0
        self.musicdefin = 0
        self.score = 0
        self.scorefinal = 0
        self.highscore = 0
        self.nazimode = 0
        self.kim_jong_un_mode = 0

    def run(self):
        clock = pygame.time.Clock()
        self.generatePlatforms()
        while True:
            self.screen.fill((self.col_red, self.col_green, self.col_blue))
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
            if self.playery - self.cameray > 700:
                self.cameray = 0
                self.platforms = [[400, 500]]
                self.generatePlatforms()
                self.playerx = 400
                self.playery = 300
                self.vie -= 1
            self.drawPlatforms()
            self.updatePlatforms()
            self.updatePlayer()
            pygame.display.flip()
            self.score = int(((self.playery - 700) * -1)/10)

            if self.wtf == 1:
                self.updateColors()
            if int(self.vie) <= 0:
                self.end()


    def end(self):
        self.txtend = 1

    def updatePlayer(self):
        if self.musicdefin == 1:
            pygame.mixer.music.load("assets/undertale.mp3")
            pygame.mixer.music.play(50)


        if self.playerx > 1360:
            self.playerx = -50
        elif self.playerx < -50:
            self.playerx = 1300
        self.playerx += self.xmovement
        if self.playery - self.cameray <= 200:
            self.cameray -= 10
        if not self.direction:
            if self.jump:
                self.screen.blit(self.playerRight_1, (self.playerx, self.playery - self.cameray))
            else:
                self.screen.blit(self.playerRight, (self.playerx, self.playery - self.cameray))
        else:
            if self.jump:
                self.screen.blit(self.playerLeft_1, (self.playerx, self.playery - self.cameray))
            else:
                self.screen.blit(self.playerLeft, (self.playerx, self.playery - self.cameray))
        key = pygame.key.get_pressed()
        if key[K_RIGHT]:
            if self.accordmove == 1:
                if self.xmovement < 10:
                    self.xmovement += 1
                    self.direction = 0

        elif key[K_LEFT]:
            if self.accordmove == 1:
                if self.xmovement > -10:
                    self.xmovement -= 1
                    self.direction = 1

        else:
            if self.xmovement > 0:
                self.xmovement -= 1
            elif self.xmovement < 0:
                self.xmovement += 1
        if not self.jump:
            self.playery += self.gravity
            self.gravity += 1
        elif self.jump:
            self.playery -= self.jump
            self.jump -= 1

        if key[K_t]:
            self.nyanmode = 0
            self.trumpmode = 1
            self.juifmode = 0
            self.nazimode = 0
            self.ougandamode = 0
            self.playerRight_1 = pygame.image.load("assets/MexicanoL.png").convert_alpha()
            self.playerRight = pygame.image.load("assets/MexicanoL.png").convert_alpha()
            self.playerLeft = pygame.image.load("assets/MexicanoR.png").convert_alpha()
            self.playerLeft_1 = pygame.image.load("assets/MexicanoR.png").convert_alpha()
            self.green = pygame.image.load("assets/wall.png").convert_alpha()
            if self.accordmusic == 1:
                pygame.mixer.music.load("assets/hymne-national-des-etats-unis-national-anthem-of-usa-enfr-paroles.mp3")
                pygame.mixer.music.play(50)


        if not key[K_s] and self.spaceship:
            self.spaceship = 0
            if self.nyanmode == 1:
                self.playerRight_1 = pygame.image.load("assets/nyancatR.png").convert_alpha()
                self.playerRight = pygame.image.load("assets/nyancatR.png").convert_alpha()
                self.playerLeft = pygame.image.load("assets/nyancatL.png").convert_alpha()
                self.playerLeft_1 = pygame.image.load("assets/nyancatL.png").convert_alpha()
            elif self.ougandamode == 1:
                self.playerRight_1 = pygame.image.load("assets/UgandaJump.png").convert_alpha()
                self.playerRight = pygame.image.load("assets/UGANDA.png").convert_alpha()
                self.playerLeft = pygame.image.load("assets/UgandaJump2.png").convert_alpha()
                self.playerLeft_1 = pygame.image.load("assets/UGANDA1.png").convert_alpha()
            elif self.juifmode == 1:
                self.playerRight_1 = pygame.image.load("assets/juif.png").convert_alpha()
                self.playerRight = pygame.image.load("assets/juif.png").convert_alpha()
                self.playerLeft = pygame.image.load("assets/juif.png").convert_alpha()
                self.playerLeft_1 = pygame.image.load("assets/juif.png").convert_alpha()
            elif self.nazimode == 1:
                self.playerRight_1 = pygame.image.load("assets/doodhitler1.png").convert_alpha()
                self.playerRight = pygame.image.load("assets/doodhitler1.png").convert_alpha()
                self.playerLeft = pygame.image.load("assets/doodhitler.png").convert_alpha()
                self.playerLeft_1 = pygame.image.load("assets/doodhitler.png").convert_alpha()
            else:
                self.playerRight_1 = pygame.image.load("assets/MexicanoL.png").convert_alpha()
                self.playerRight = pygame.image.load("assets/MexicanoL.png").convert_alpha()
                self.playerLeft = pygame.image.load("assets/MexicanoR.png").convert_alpha()
                self.playerLeft_1 = pygame.image.load("assets/MexicanoR.png").convert_alpha()
        if key[K_j]:
            if self.accordmusic == 1:
                pygame.mixer.music.load("assets/deutschland-1945-musik.mp3")
                pygame.mixer.music.play(50)
            self.playerRight_1 = pygame.image.load("assets/juif.png").convert_alpha()
            self.playerRight = pygame.image.load("assets/juif.png").convert_alpha()
            self.playerLeft = pygame.image.load("assets/juif.png").convert_alpha()
            self.playerLeft_1 = pygame.image.load("assets/juif.png").convert_alpha()
            self.green = pygame.image.load("assets/nazi.png").convert_alpha()
            self.juifmode = 1
            self.nyanmode = 0
            self.ougandamode = 0
            self.trumpmode = 0
        if key[K_k]:
            self.juifmode = 0
            self.nyanmode = 0
            self.ougandamode = 0
            self.trumpmode = 0
            self.kim_jong_un_mode = 1
            self.playerRight_1 = pygame.image.load("assets/kim jong un.png").convert_alpha()
            self.playerRight = pygame.image.load("assets/kim jong un.png").convert_alpha()
            self.playerLeft = pygame.image.load("assets/kim jong un.png").convert_alpha()
            self.playerLeft_1 = pygame.image.load("assets/kim jong un.png").convert_alpha()
            self.green = pygame.image.load("assets/donald trump.png").convert_alpha()

        if key[K_s]:
            self.playery -= 20
            self.cameray -= 25
            self.jump = 15
            self.playerRight_1 = pygame.image.load("assets/spaceship.png").convert_alpha()
            self.playerRight = pygame.image.load("assets/spaceship.png").convert_alpha()
            self.playerLeft = pygame.image.load("assets/spaceship.png").convert_alpha()
            self.playerLeft_1 = pygame.image.load("assets/spaceship.png").convert_alpha()
            self.spaceship = 1
        if key[K_u]:
            self.ougandamode = 1
            self.juifmode = 0
            self.trumpmode = 0
            self.nyanmode = 0
            self.playerRight_1 = pygame.image.load("assets/UgandaJump.png").convert_alpha()
            self.playerRight = pygame.image.load("assets/UGANDA.png").convert_alpha()
            self.playerLeft = pygame.image.load("assets/UgandaJump2.png").convert_alpha()
            self.playerLeft_1 = pygame.image.load("assets/UGANDA1.png").convert_alpha()
            self.green = pygame.image.load("assets/left_1.png").convert_alpha()
            if self.accordmusic == 1:
                pygame.mixer.music.load("assets/Running in the 90's.mp3")
                pygame.mixer.music.play(50)
            self.wtf = 1
        if key[K_ESCAPE]:
            sys.exit()
        if self.toucherestart == 1:
            if key[K_SPACE]:
                DoodleJump().run()

        if key[K_n]:
            self.ougandamode = 0
            self.nyanmode = 0
            self.trumpmode = 0
            self.nazimode = 1
            self.juifmode = 0
            pygame.mixer.music.load("assets/je-suis-un-bon-nazi-paroles.mp3")
            pygame.mixer.music.play(50)
            self.playerRight_1 = pygame.image.load("assets/doodhitler1.png").convert_alpha()
            self.playerRight = pygame.image.load("assets/doodhitler1.png").convert_alpha()
            self.playerLeft = pygame.image.load("assets/doodhitler.png").convert_alpha()
            self.playerLeft_1 = pygame.image.load("assets/doodhitler.png").convert_alpha()
            self.green = pygame.image.load("assets/croix gamme.png").convert_alpha()
        if key[K_h]:
            self.screen.fill((0,0,0))
            myfont = pygame.font.SysFont('Comic Sans MS', 30)
            textsurface = myfont.render('le score le plus haut est :' + str(self.highscore), False, (255, 255, 255))
            self.screen.blit(textsurface,(150, 100))

    def drawPlatforms(self):
        for plat in self.platforms:
            regenerate = self.platforms[1][1] - self.cameray
            if regenerate > 600:
                self.platforms.append((random.randint(0, 1360), self.platforms[-1][1] - 50))
                self.platforms.pop(0)
            self.screen.blit(self.green, (plat[0], plat[1] - self.cameray))
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render('PRESS S TO WIN', False, (0, 0, 0))
        self.screen.blit(textsurface,(random.randint(0, 800),random.randint(-100, 500)))
        textsurface = myfont.render('PRESS T TO BECOME LEGENDARY', False, (255, 0, 255))
        self.screen.blit(textsurface,(random.randint(0, 800),random.randint(-100, 500)))
        textsurface = myfont.render('PRESS U TO FIND DA WAE', False, (0, 255, 0))
        self.screen.blit(textsurface,(random.randint(0, 800),random.randint(-100, 500)))
        textsurface = myfont.render('PRESS J TO BECOME A JEW', False, (0, 255, 0))
        self.screen.blit(textsurface,(random.randint(0, 800),random.randint(-100, 500)))
        textsurface = myfont.render('PRESS N TO BECOME A NAZI', False, (0, 255, 0))
        self.screen.blit(textsurface,(random.randint(0, 800),random.randint(-100, 500)))
        self.score = "score:" + str(self.score)
        textsurface = myfont.render(self.score, False, (0, 0, 0))
        self.screen.blit(textsurface,(random.randint(0, 0),random.randint(0, 0)))
        self.scorevie = "vie :"+str(self.vie)
        textsurface = myfont.render(self.scorevie, False, (0, 0, 0))
        self.screen.blit(textsurface,(random.randint(0, 0),random.randint(30, 30)))
        if self.txtend == 1:
            #int(self.scorefinal) += int(self.score)
            textsurface = myfont.render('Dommage, reessaye plus tard.', False, (255, 255, 255))
            self.accordmove = 0
            self.accordmusic = 0
            self.screen.fill((0,0,0))
            self.screen.blit(textsurface,(200,250))
            textsurface = myfont.render('Pour recommencer presse espace ', False, (255, 255, 255))
            self.screen.blit(textsurface,(200,300))
            self.toucherestart = 1
            self.musicdefin += 1
            textsurface = myfont.render('Votre score est : ' + str(self.scorefinal), False, (255, 255, 255))
            self.screen.blit(textsurface,(200,350))
            if self.scorefinal > self.highscore:
                self.scorefinal = self.highscore



        if self.pausemenu == 1:
            myfont = pygame.font.SysFont('Comic Sans MS', 30)
            textsurface = myfont.render('PRESS S TO WIN', False, (0, 0, 0))
            self.screen.blit(textsurface,(random.randint(0, 800),random.randint(-100, 500)))



    def generatePlatforms(self):
        y = 700
        while y >= -100:
            x = random.randint(0, 1360)
            self.platforms.append((x, y))
            y -= 10

    def updatePlatforms(self):
        for p in self.platforms:
            rect = pygame.Rect(p[0], p[1], self.green.get_width() - 10, self.green.get_height())
            player = pygame.Rect(self.playerx, self.playery, self.playerRight.get_width() - 10, self.playerRight.get_height())
            if rect.colliderect(player) and self.gravity and self.playery < (p[1] - self.cameray) and self.spaceship == 0:
                self.jump = 15
                self.gravity = 0

    def updateColors(self):
        self.col_red = random.randint(0, 255)
        self.col_green = random.randint(0, 255)
        self.col_blue = random.randint(0, 255)
        self.plateformerandom = random.randint(0,4)
        if self.plateformerandom == 1:
            self.green = pygame.image.load("assets/ARC EN CIEL.png").convert_alpha()
        elif self.plateformerandom == 2:
            self.green = pygame.image.load("assets/wall.png").convert_alpha()
        elif self.plateformerandom == 3:
            self.green = pygame.image.load("assets/nazi.png").convert_alpha()
        else:
            self.green = pygame.image.load("assets/left_1.png").convert_alpha()

class Commencement(object):
    def __init__(self):
        self.doodle = 0
        self.screen = pygame.display.set_mode((800, 600))
        pygame.font.init()

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
            pygame.display.flip()
            self.Ecriture()

    def Ecriture(self):
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render('Pour commencer appuyez sur espace', False, (255, 255, 255))
        self.screen.blit(textsurface,(150, 250))
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render('Pour voir le meilleur score de la partie appuyez sur H', False, (255, 255, 255))
        self.screen.blit(textsurface,(30, 300))
        key = pygame.key.get_pressed()
        if key[K_SPACE]:
            DoodleJump().run()


Commencement().run()
