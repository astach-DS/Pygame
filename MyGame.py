# Import modules
from os import pipe
import sys
import pygame
from pygame import surface
import pygame.draw
import pygame.image
import pygame.mouse
import pygame.display
import pygame.transform
import pygame.time
import pygame.event
import random
# Inicialize PyGame instance
pygame.init()

############################## Functions ########################################
def draw_floor():
    # Floor_surface movement
    screen.blit(floor_surface,(floor_x_position,864))
    # Second floor movement
    screen.blit(floor_surface,(floor_x_position+576,864))

def create_pipe():
    pipe_random_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(600,pipe_random_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(600,pipe_random_pos - 300))
    return top_pipe, bottom_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -=2
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface,pipe)


############################## Develop ##########################################
# Set the screen display size
screen = pygame.display.set_mode((576,1024))

# Load and upscale back surface
back_surface = pygame.image.load('assets/background-night.png').convert()
back_surface = pygame.transform.scale2x(back_surface)

# Load and upscale floor surface
floor_surface = pygame.image.load('assets/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
# Set floor initial x position
floor_x_position = 0

# Load bird surface
bird_surface = pygame.image.load('assets/redbird-midflap.png').convert()
bird_surface = pygame.transform.scale2x(bird_surface)
# Place bird rectangle for colisions
bird_rect = bird_surface.get_rect(center=(250,500))

# Load pipe surface
pipe_surface = pygame.image.load('assets/pipe-green.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
# Make pipe list to add pipes
pipe_list = []
# Every 1200ms SPAWNPIPE event is trigered
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)
# Set heights for pipes
pipe_height = [400,600,800]

# Set gravity aceleration and bird velocity
gravity = 0.1
bird_velocity = 0

# Set the clock for refresh rate
clock = pygame.time.Clock()

# Game loop
while True:
    # Pygame looks for all event ocuring (moving mouse or key press)
    for event in pygame.event.get():
        # If event is quiting the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # If event is pressing down K_UP, then birds moves up
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:   
                bird_velocity = 0
                bird_velocity -= 5
        # If event is SPAWNPIPE, then create a pipe
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
            
    
    # 'back surface' drawing
    screen.blit(back_surface,(0,0))
    
    
    
    # Bird drawing
    bird_velocity += gravity
    bird_rect.centery += bird_velocity
    screen.blit(bird_surface,bird_rect)
    
    # Pipe moving and drawing
    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list) 
    
    # Floor drawing
    floor_x_position -= 2
    draw_floor()
    if floor_x_position == -576:
        floor_x_position =0
   
    # Refresh the screen
    pygame.display.update()
    # Set Refresh Rate
    clock.tick(165)


