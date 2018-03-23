#!/usr/local/bin/python2
import os
from sys import argv
import numpy as np
import pygame
import time, sys
from pygame import mixer
from pyAudioAnalysis import audioTrainTest 
script, filename = argv
pygame.init()
isSignificant = 0.33 #try different values.
# print argv
# P: list of probabilities
Result, P, classNames = audioTrainTest.fileClassification(filename, "svmSMtemp", "svm")
winner = np.argmax(P) #pick the result with the highest probability value.

print classNames[winner]
# is the highest value found above the isSignificant threshhold? 
if P[winner] > isSignificant :
  	print("File: " +filename + " is in category: " + classNames[winner] + ", with probability: " + str(P[winner]))
  	path="msg/"+classNames[winner]
  	alert_path="msg/"+classNames[winner]+"_tamil.wav"
	pygame.mixer.music.load(alert_path)
	pygame.mixer.music.play()		
  	os.system(' telegram-cli -k server.pub -W -e "send_photo Alert %s" "safe_quit"' %(path+".jpg") )
	# pygame.mixer.music.play()
	os.system(' telegram-cli -k server.pub -W -e "msg Alert WARNING !!!!  %s " "safe_quit" '%(classNames[winner]))
else :
  print("Can't classify sound: " + str(P))

