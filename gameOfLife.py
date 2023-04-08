import pygame

# Set up the Pygame window
WINDOW_SIZE = (1000, 1000)
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)

# Define some colors
LIVE = (25, 55, 109)
DEAD = (218, 245, 255)

turningNuumbers = [3]

# Set up the grid
GRID_SIZE_H = 25
GRID_SIZE_W = 25
SQUARE_SIZE = 40
grid = []
for i in range(GRID_SIZE_H):
    row = []
    for j in range(GRID_SIZE_W):
        row.append(DEAD)
    grid.append(row)

x_offset = 5
y_offset = 4

# grid[y_offset][x_offset] = LIVE 
# grid[y_offset][x_offset + 1] = LIVE
# grid[y_offset + 1][x_offset + 1] = LIVE
# grid[y_offset + 2][x_offset + 1] = LIVE
# grid[y_offset + 3][x_offset + 2] = LIVE
# grid[y_offset + 3][x_offset + 3] = LIVE
# grid[y_offset + 2][x_offset + 3] = LIVE

# grid[y_offset + 16][x_offset] = LIVE 
# grid[y_offset + 16][x_offset + 1] = LIVE
# grid[y_offset + 15][x_offset + 1] = LIVE
# grid[y_offset + 14][x_offset + 1] = LIVE
# grid[y_offset + 13][x_offset + 2] = LIVE
# grid[y_offset + 13][x_offset + 3] = LIVE
# grid[y_offset + 14][x_offset + 3] = LIVE


# grid[y_offset][x_offset + 28] = LIVE 
# grid[y_offset][x_offset + 27] = LIVE
# grid[y_offset + 1][x_offset + 27] = LIVE
# grid[y_offset + 2][x_offset + 27] = LIVE
# grid[y_offset + 3][x_offset + 26] = LIVE
# grid[y_offset + 3][x_offset + 25] = LIVE
# grid[y_offset + 2][x_offset + 25] = LIVE

# grid[y_offset + 16][x_offset + 28] = LIVE 
# grid[y_offset + 16][x_offset + 27] = LIVE
# grid[y_offset + 15][x_offset + 27] = LIVE
# grid[y_offset + 14][x_offset + 27] = LIVE
# grid[y_offset + 13][x_offset + 26] = LIVE
# grid[y_offset + 13][x_offset + 25] = LIVE
# grid[y_offset + 14][x_offset + 25] = LIVE

# grid[y_offset + 5][x_offset + 8] = LIVE
# grid[y_offset + 5][x_offset + 9] = LIVE
# grid[y_offset + 6][x_offset + 8] = LIVE
# grid[y_offset + 6][x_offset + 9] = LIVE

# grid[y_offset + 10][x_offset + 8] = LIVE
# grid[y_offset + 10][x_offset + 9] = LIVE
# grid[y_offset + 11][x_offset + 8] = LIVE
# grid[y_offset + 11][x_offset + 9] = LIVE

# grid[y_offset + 6][x_offset + 12] = LIVE
# grid[y_offset + 6][x_offset + 14] = LIVE
# grid[y_offset + 7][x_offset + 13] = LIVE
# grid[y_offset + 5][x_offset + 15] = LIVE
# grid[y_offset + 4][x_offset + 14] = LIVE
# grid[y_offset + 3][x_offset + 13] = LIVE

# grid[y_offset + 10][x_offset + 12] = LIVE
# grid[y_offset + 12][x_offset + 14] = LIVE
# grid[y_offset + 13][x_offset + 13] = LIVE
# grid[y_offset + 11][x_offset + 15] = LIVE
# grid[y_offset + 10][x_offset + 14] = LIVE
# grid[y_offset + 9][x_offset + 13] = LIVE




# Main game loop

timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 100)  # 1000 milliseconds = 1 second

done = False
playing = False

while not done:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            x = mouse_pos[0] // SQUARE_SIZE
            y = mouse_pos[1] // SQUARE_SIZE
            if(grid[y][x] == LIVE):
                grid[y][x] = DEAD
            else:
                grid[y][x] = LIVE

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                playing = not playing
            if event.key == pygame.K_k:
                for i in range(GRID_SIZE_H):
                    for j in range(GRID_SIZE_W):
                        grid[i][j] = DEAD


        if event.type == timer_event:
            if(playing):
                newGrid = []
                for i in range(GRID_SIZE_W):
                    row = []
                    for j in range(GRID_SIZE_H):
                        number = 0
                        if(i>0):
                            if(grid[i-1][j] == LIVE):
                                number += 1
                            if(j>0):
                                if(grid[i-1][j-1] == LIVE):
                                    number += 1
                            if(j<GRID_SIZE_H-1):
                                if(grid[i-1][j+1] == LIVE):
                                    number += 1
                        if(j>0):
                            if(grid[i][j-1] == LIVE):
                                number += 1
                        if(j<GRID_SIZE_H-1):
                            if(grid[i][j+1] == LIVE):
                                number += 1

                        if(i<GRID_SIZE_W-1):
                            if(grid[i+1][j] == LIVE):
                                number += 1
                            if(j<GRID_SIZE_H-1):
                                if(grid[i+1][j+1] == LIVE):
                                    number += 1    
                            if(j>0):    
                                if(grid[i+1][j-1] == LIVE):
                                    number += 1
                        
                        if(grid[i][j] == LIVE):
                            if(number in [2, 3]):
                                row.append(LIVE)
                            else:
                                row.append(DEAD)
                        else:
                            if(number in [3]):
                                row.append(LIVE)
                            else:
                                row.append(DEAD)

                    newGrid.append(row)
                grid = newGrid

            # Draw the grid
            for i in range(GRID_SIZE_W):
                for j in range(GRID_SIZE_H):
                    rect = pygame.Rect(j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                    pygame.draw.rect(screen, grid[i][j], rect)

            pygame.display.flip()



# Quit the game
pygame.quit()
