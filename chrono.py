import RPi.GPIO as GPIO
import pygame, sys
import time
from pygame.locals import *

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# GPIO d'ecoute entre le GND et le pin 26 soit les deux plus proche du jack (qui est jaune :))
# en principe n'importe quel type de contact peut basculer le port en ON/OFF, penser a proteger 
# le raspberry avec une resistance de 330 Ohm
switch = 7 
GPIO.setup(switch,GPIO.IN, pull_up_down=GPIO.PUD_UP)

# text color on pygame window
txtColor = pygame.Color(102,153,255)
# background color on pygame window
bgColor = pygame.Color(255,255,255)
# init pygame
pygame.init()
width = 580
height = 100
windowSurfaceObj = pygame.display.set_mode((width,height),1,24)
windowSurfaceObj.fill(bgColor)
pygame.display.set_caption('Tempt d\'application')
fontObj = pygame.font.Font('freesansbold.ttf',100)
# default timer entry
msg = "00:00:00:000"
msgSurfaceObj = fontObj.render(msg, False,txtColor)
msgRectobj = msgSurfaceObj.get_rect()
msgRectobj.topleft =(2,0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
windowSurfaceObj.blit(msgSurfaceObj, msgRectobj)
pygame.display.update()

# infinite loop
try:
   while GPIO.input(switch)==1: 
      down = 0
   print "  Ready"
   down = 0
   
   while True :
      # start or restart timer if pushed
      if GPIO.input(switch)==0:
         if down == 0:
            start = time.time()
         # current time since started
         now = time.time() - start
         m,s = divmod(now,60)
         h,m = divmod(m,60)
         msg= "%02d:%02d:%02d" % (h,m,s)
         psec = str(now-int(now))
         pstr = psec[1:5]
         msg = msg + str(pstr)
         pygame.draw.rect(windowSurfaceObj,bgColor,Rect(0,0,width,height))
         msgSurfaceObj = fontObj.render(msg, False,txtColor)
         msgRectobj = msgSurfaceObj.get_rect()
         msgRectobj.topleft =(2,0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
         windowSurfaceObj.blit(msgSurfaceObj, msgRectobj)
         pygame.display.update()
         down = 1
      # release button - stop timer         
      if GPIO.input(switch)==1:
         down = 0
      for event in pygame.event.get():
         if event.type == QUIT:
            pygame.quit()
            sys.exit()

# exit Exception
except KeyboardInterrupt:
  GPIO.cleanup()  
