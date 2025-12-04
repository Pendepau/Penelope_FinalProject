import pygame

### use class function to make a charater, and another one to make the enviroment
Game_width = 800
Game_height = 800

Player_x = Game_width/2
Player_y = Game_height/2
Player_width = 50
Player_Height = 50
PLAYER_Distance = 5

Gravity = 0.5
Friction = 0.4
Player_Velocity_x = 5
Player_Velocity_y = -10

Floor_y = Game_height * 3/4
Tile_size = 32

pygame.init()

window = pygame.display.set_caption("2D Platfomer")
resolution = (Game_height,Game_width)
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()


class Player(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, Player_x, Player_y, Player_width, Player_Height)
        self.velocity_x = 0
        self.velocity_y = 0
        self.direction = "right"
        self.jumping = False

class Tile(pygame.Rect):
    def __init__(self, x, y):
        pygame.Rect.__init__(self, x, y, Tile_size, Tile_size)
        self.image = (0,128,0)

def create_map():
    for i in range(10):
        tile = Tile(player.x + i*Tile_size, player.y + Tile_size*3)
        tiles.append(tile)

    for h in range(1):
        hazard = Tile

def check_tile_collision():
    for tile in tiles:
        if player.colliderect(tile):
            return tile
    return None

def check_tile_collisions_x():
    tile = check_tile_collision()
    if tile is not None:
        if player.velocity_x < 0:
            player.x = tile.x + tile.width
        elif player.velocity_x > 0:
            player.x = tile.x - player.width
        player.velocity_x

def check_tile_collisions_y():
    tile = check_tile_collision()
    if tile is not None:
        if player.velocity_y < 0:
            player.y = tile.Y + tile.height
        elif player.velocity_y > 0:
            player.y = tile.y - player.height
            player.jumping = False
        player.velocity_y = 0

def move():
    if player.direction == "left" and player.velocity_x < 0:
        player.velocity_x += Friction
    elif player.direction == "right" and player.velocity_x > 0:
        player.velocity_x -= Friction
    else:
        player.velocity_x = 0

    player.x += player.velocity_x
    if player.x < 0:
        player.x = 0
    elif player.x + player.width > Game_width:
        player.x = Game_width - Player_width

    check_tile_collisions_x()

    player.velocity_y += Gravity
    player.y += player.velocity_y

    check_tile_collisions_y()

    if player.y + player.height > Floor_y:
        player.y = Floor_y - player.height
        player.jumping = False


def draw():
    screen.fill((20,18,167))
    pygame.draw.rect(screen,(2,239,238), player)

    for tile in tiles:
        pygame.draw.rect(screen, (0,128,0), tile)

player = Player()
tiles = []
hazard = []
create_map()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and not player.jumping:
        player.velocity_y = Player_Velocity_y
        player.jumping = True
    
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.velocity_x = - Player_Velocity_x
        player.direction = "left"
    
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.velocity_x =  Player_Velocity_x
        player.direction = "right"
    
    move()
    draw()
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()