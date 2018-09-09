import pygame, sys, math
import serial
import threading
import random

from config import *
from util import *
from status import *
from composition import *
import pygame.gfxdraw
from roundedRect import *
from homescreen import *
from noteClass import *
import keyboardForComp as kb


class CompositionPage():
    
    def __init__(self):
        self.curX = 1024
        self.clock = pygame.time.Clock()
        pygame.font.init()
        self.menufont = pygame.font.SysFont('comicsansms', 25, bold = False)
        self.user = self.menufont.render("User", False, (255,255,255))
        self.home = self.menufont.render("Home", False, (255,255,255))
        self.start = self.menufont.render("Start", False, (255,255,255))
        self.pause = self.menufont.render("Pause", False, (255,255,255))
        self.end = self.menufont.render("End", False, (255,255,255))
        self.composing = True
        self.rec = False
        self.tempo = 60
        self.gameDisplay = pygame.display.set_mode((Config.display_width, Config.display_height))
        self.gameDisplay.fill(Config.black)
        self.userIcon = pygame.image.load('media/ui icons/batman.jpg')
        self.homeIcon = pygame.image.load('media/ui icons/thor.jpg')
        self.userIcon = pygame.transform.scale(self.userIcon,(50,50))
        self.homeIcon = pygame.transform.scale(self.homeIcon,(50,50))
        self.startIcon = pygame.image.load('media/ui icons/start.png')
        self.pauseIcon = pygame.image.load('media/ui icons/pause.png')
        self.endIcon = pygame.image.load('media/ui icons/end.png')
        self.startIcon = pygame.transform.scale(self.startIcon,(50,50))
        self.pauseIcon = pygame.transform.scale(self.pauseIcon,(50,50))
        self.endIcon = pygame.transform.scale(self.endIcon,(50,50))
        self.staff = pygame.image.load("media/staff.png")
        self.staff = pygame.transform.scale(self.staff, (964, 300))
        self.scrollHori = 0
        self.scrollVerti = 0
        self.numLines = 1
        self.colors = [(21,199,208),(241,90,36),(237,28,36),(202,244,239), (73,165,109),(115,99,86)]
        self.notes = []
        self.myKeyboard = kb.Keyboard(60,400)
            
    def drawBar(self, surface, note):
        i = random.randint(0, 5)
        pygame.draw.rect(surface, (254,241,0), (note.x-self.scrollHori, note.y, 50, 36), 0)

        
    def drawKeyboard(self):
        self.myKeyboard.draw(self.gameDisplay)

    def draw(self,surface):
        #draw deviding lines
        #pygame.draw.rect(self.gameDisplay, Config.black, ((0,0,60,60)),0)
        
        
        pygame.draw.line(self.gameDisplay, (225,225,225), (60, 300), (1024, 300), 3)
          
        self.gameDisplay.blit(self.staff, (60-self.scrollHori, 0+self.scrollVerti))
        pygame.draw.line(self.gameDisplay, (254,241,0), (300-self.scrollHori, 265+self.scrollVerti), ((1024*self.numLines+1)-self.scrollHori,265+self.scrollVerti), 3)
        pygame.draw.line(self.gameDisplay, (254,241,0), (300-self.scrollHori, 28+self.scrollVerti), ((1024*self.numLines+1)-self.scrollHori,28+self.scrollVerti), 3)
        pygame.draw.line(self.gameDisplay, (254,241,0), (300-self.scrollHori, 10+self.scrollVerti), ((1024*self.numLines+1)-self.scrollHori,10+self.scrollVerti), 3)
        pygame.draw.line(self.gameDisplay, (254,241,0), (300-self.scrollHori, -8+self.scrollVerti), ((1024*self.numLines+1)-self.scrollHori,-8+self.scrollVerti), 3)
        pygame.draw.line(self.gameDisplay, (254,241,0), (300-self.scrollHori, -26+self.scrollVerti), ((1024*self.numLines+1)-self.scrollHori,-26+self.scrollVerti), 3)
        pygame.draw.line(self.gameDisplay, (254,241,0), (300-self.scrollHori, -44+self.scrollVerti), ((1024*self.numLines+1)-self.scrollHori,-44+self.scrollVerti), 3)
        pygame.draw.line(self.gameDisplay, (254,241,0), (300-self.scrollHori, -62+self.scrollVerti), ((1024*self.numLines+1)-self.scrollHori,-62+self.scrollVerti), 3)
        pygame.draw.line(self.gameDisplay, (254,241,0), (300-self.scrollHori, -80+self.scrollVerti), ((1024*self.numLines+1)-self.scrollHori,-80+self.scrollVerti), 3)
        pygame.draw.line(self.gameDisplay, (254,241,0), (300-self.scrollHori, -98+self.scrollVerti), ((1024*self.numLines+1)-self.scrollHori,-98+self.scrollVerti), 3)
        pygame.draw.rect(self.gameDisplay, Config.black, ((0,0,60,600)),0)
        pygame.draw.line(self.gameDisplay, (225,225,225), (60,0), (60,600), 3)
        pygame.draw.line(self.gameDisplay, (254,241,0), (1024*self.numLines-self.scrollHori, 87), (1024*(self.numLines+1)-self.scrollHori, 87), 3)
        pygame.draw.line(self.gameDisplay, (254,241,0), (1024*self.numLines-self.scrollHori, 123), (1024*(self.numLines+1)-self.scrollHori, 123), 3)
        pygame.draw.line(self.gameDisplay, (254,241,0), (1024*self.numLines-self.scrollHori, 155), (1024*(self.numLines+1)-self.scrollHori, 155), 3)
        pygame.draw.line(self.gameDisplay, (254,241,0), (1024*self.numLines-self.scrollHori, 191), (1024*(self.numLines+1)-self.scrollHori, 191), 3)
        pygame.draw.line(self.gameDisplay, (254,241,0), (1024*self.numLines-self.scrollHori, 228), (1024*(self.numLines+1)-self.scrollHori, 228), 3)
        
        pygame.draw.rect(self.gameDisplay, Config.black, ((60,0,1024,46)),0)
        pygame.draw.rect(self.gameDisplay, Config.black, ((60,264,1024,34)),0)
        #pygame.draw.line(self.gameDisplay, (225,225,225), (0,60), (60, 60), 3)

        #drawImage(gameDisplay, "media/pianoop.png", 80, 270, (140, 60))

        #draw the left menu bar
        self.gameDisplay.blit(self.userIcon, (5, 5))
        self.gameDisplay.blit(self.user, (11, 65))
        self.gameDisplay.blit(self.homeIcon, (5, 90))
        self.gameDisplay.blit(self.home, (9, 150))
        self.gameDisplay.blit(self.startIcon, (5, 175))
        self.gameDisplay.blit(self.start, (10, 235))
        
        self.gameDisplay.blit(self.pauseIcon, (5, 260))
        self.gameDisplay.blit(self.pause, (8, 320))
        self.gameDisplay.blit(self.endIcon, (5, 345))
        self.gameDisplay.blit(self.end, (13, 405))
        if self.rec:
            self.scrollHori += 5 
            self.curX -= self.scrollHori
        if self.curX < 400:
            self.numLines += 1
            self.curX = 1024
        for n in self.notes:
            self.drawBar(self.gameDisplay, n)

        self.drawKeyboard()
            
        
            
        
        
    def handleEvents(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
             #check if home button is clicked
            if pygame.Rect(5,90,50,50).collidepoint(event.pos):
                runHomescreen()
            elif pygame.Rect(5, 175, 50, 50).collidepoint(event.pos):
                self.rec = True
            elif pygame.Rect(5, 260, 50, 50).collidepoint(event.pos):
                self.rec = False
            elif pygame.Rect(5, 345, 50, 50).collidepoint(event.pos):
                pass
            else:
                newNote = Note("c3", 60, 0, 1)
                noteY = newNote.putBars(newNote.note)
                print(newNote.x)
                print(noteY)
                self.notes.append(newNote)
                
                newNote2 = Note("c4", 60, 0 ,1)
                noteY2 = newNote2.putBars(newNote2.note)
                self.notes.append(newNote)
            
                


    def compositionMode(self):
        while self.composing:
            #area for the background is 964 * 566
            for event in pygame.event.get():
                #refresh to home page 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    Status.isQuit = True
                    self.practice = False
                    sys.exit()
                self.handleEvents(event)

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            self.draw(self.gameDisplay)
            
            pygame.display.update()
            self.clock.tick(60)
            
    def midiOut(self, tempo):
        mf = MIDIFile(1)     # only 1 track
        track = 0   # the only track
        
        time = 0    # start at the beginning
        mf.addTrackName(track, time, "midiOut")
        mf.addTempo(track, time, 120)
        
        # add some notes
        channel = 0
        volume = 100
        
        for n in self.notes:
            pitch = n.pitch
            time = n.time
            duration = n.duration
            mf.addNote(track, channel, pitch, time, duration, volume)
        
        with open("output.mid", 'wb') as outf:
            mf.writeFile(outf)
                    

    def runCM(self):
        pygame.init()
        self.compositionMode()


if __name__ == '__main__':
    cp = CompositionPage()
    cp.runCM()
        
        