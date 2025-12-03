import pygame

### use class function to make a charater, and another one to make the enviroment
Player_x = 0
Player_y = 0
Player_width = 50
Player_Height = 50
PLAYER_Distance = 5

pygame.init()

window = pygame.display.set_caption("2D Platfomer")
resolution = (800,800)
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

Player_Height = 50
PLAYER_Distance = 5
class Player(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, Player_x, Player_y, Player_width, Player_Height)
player = pygame.Rect(150,150,50,50)


def draw():
    screen.fill((20,18,167))
    pygame.draw.rect(screen,(2,239,238), player)


# initalize & shut down game/ holds all game functions
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y = max(player.y - PLAYER_Distance, 0)
    
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y = min(player.y + PLAYER_Distance, 800 - player.height)
    
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x = max(player.x - PLAYER_Distance, 0)
    
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x = min(player.x + PLAYER_Distance, 800 - Player_width)
    
    draw()
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()