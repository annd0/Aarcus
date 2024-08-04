import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 32

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("80s RPG Style Game")

# Load tile images
grass_tile = pygame.image.load('Cartoon_green_texture_grass.jpg')
water_tile = pygame.image.load('OR6IKU0.jpg')

# Adjust size of background tiles
grass_tile = pygame.transform.scale(grass_tile, (TILE_SIZE, TILE_SIZE))
water_tile = pygame.transform.scale(water_tile, (TILE_SIZE, TILE_SIZE))

# Create a simple tile map
tile_map = [
    ['grass', 'grass', 'grass', 'water', 'water'],
    ['grass', 'grass', 'grass', 'water', 'water'],
    ['grass', 'grass', 'grass', 'grass', 'grass'],
    ['grass', 'grass', 'grass', 'grass', 'grass'],
    ['water', 'water', 'grass', 'grass', 'grass']
]

# Player settings
player_image = pygame.image.load('player.png')
player_image = pygame.transform.scale(player_image, (TILE_SIZE, TILE_SIZE))
player_pos = [1, 1]

# Draw the tile map
def draw_tile_map():
    for row in range(len(tile_map)):
        for col in range(len(tile_map[row])):
            tile_type = tile_map[row][col]
            x = col * TILE_SIZE
            y = row * TILE_SIZE
            if tile_type == 'grass':
                screen.blit(grass_tile, (x, y))
            elif tile_type == 'water':
                screen.blit(water_tile, (x, y))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= 1
    if keys[pygame.K_RIGHT] and player_pos[0] < len(tile_map[0]) - 1:
        player_pos[0] += 1
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= 1
    if keys[pygame.K_DOWN] and player_pos[1] < len(tile_map) - 1:
        player_pos[1] += 1

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the tile map
    draw_tile_map()

    # Draw the player
    player_x = player_pos[0] * TILE_SIZE
    player_y = player_pos[1] * TILE_SIZE
    screen.blit(player_image, (player_x, player_y))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)
