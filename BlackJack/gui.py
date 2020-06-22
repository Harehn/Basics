import pygame

# IMPORTANT
pygame.init()

# Screen creation
screen = pygame.display.set_mode((800, 600))

# 
pygame.display.set_caption("Blackjack game")

running = True

# a while true may crash
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
