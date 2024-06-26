import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1000,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Set up the grid
GRID_SIZE = 20
grid = np.zeros((WIDTH//GRID_SIZE, HEIGHT//GRID_SIZE))
# print(grid.shape)
# Define the update rule
def update_grid(grid):
    new_grid = np.copy(grid)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            count = grid[i-1,j-1] + grid[i,j-1] + grid[i-1,j] 
            if i==grid.shape[0]-1 or j==grid.shape[1]-1:
                if i==grid.shape[0]-1 and j==grid.shape[1]-1:
                    count = count + grid[0,j] + grid[0,j-1] + grid[i,0] + grid[i-1,0] + grid[0,0]
                else:
                    if i==grid.shape[0]-1:
                        count = count + grid[0,j] + grid[0,j-1] + grid[0,j+1] + grid[i,j+1] + grid[i-1,j+1]
                    else:
                        count = count + grid[i+1,j] + grid[i+1,j-1] + grid[i,0] + grid[i-1,0] + grid[i+1,0]
            else:
                count = count + grid[i+1,j] + grid[i+1,j-1] + grid[i,j+1] + grid[i+1,j+1] + grid[i-1,j+1]
            if grid[i, j] == 1:
                if count < 2 or count > 3:
                    new_grid[i, j] = 0
            else:
                if count == 3:
                    new_grid[i, j] = 1
    return new_grid

# Main loop
running = True
coord=set()
start=False
FPS=17
while running:
    for event in pygame.event.get():
        if (
                event.type == pygame.QUIT
                or event.type == pygame.KEYDOWN
                and event.key == pygame.K_ESCAPE
            ):
            exit()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
            start = not start
            # print(start)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_j:
            if FPS < 3:
                FPS = 1
            else:
                FPS-=3
        if event.type == pygame.KEYDOWN and event.key == pygame.K_k:
            if FPS > 22:
                FPS = 20
            else:
                FPS+=3

        if event.type == pygame.MOUSEBUTTONDOWN:
            coordinates = pygame.mouse.get_pos()
            grid[coordinates[0]//20,coordinates[1]//20]=not grid[coordinates[0]//20,coordinates[1]//20]


    # Update the grid
    if start:
        grid = update_grid(grid)
    # Clear the screen
    screen.fill((255, 255, 255))

    for i in range(grid.shape[0]):
            # print(i)
            pygame.draw.line(screen,(200,200,200,),(0,int(i)*20),(WIDTH,int(i)*20),width=1)
            pygame.draw.line(screen,(200,200,200,),(int(i)*20,0),(int(i)*20,HEIGHT),width=1)
    # Draw the grid
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 1:
                pygame.draw.rect(screen, (0, 0, 0), (i*GRID_SIZE, j*GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Update the display
    pygame.display.update()
    
    #time
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
