import pygame
pygame.init() #inicia o mixer
pygame.mixer.music.load('teste21.mp3') #seleciona a musica
pygame.mixer.music.play()
input()
pygame.event.wait()


