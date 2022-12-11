#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
#feito pelo prof°

print('*' * 51)

import pygame
pygame.init()
pygame.mixer.music.load('021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

