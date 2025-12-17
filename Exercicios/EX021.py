#Abrir e reproduzir arquivo mp3
import pygame
pygame.init()
pygame.mixer.music.load('EX021.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
'''input()
pygame.event.wait()'''
