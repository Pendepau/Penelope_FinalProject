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

class Hazard(pygame.Rect):
    def __init__(self,x,y):
        pygame.Rect.__init__(self,x,y, Tile_size, Tile_size)
        self.image = (255,0,0)

def create_map():
    for i in range(20):
        tile = Tile(0 + i*Tile_size, player.y + Tile_size*3)
        tiles.append(tile)

    for h in range(1):
        hazard = Hazard(Tile_size*3, (h+12)*Tile_size)
        hazards.append(hazard)

def check_tile_collision():
    for tile in tiles:
        if player.colliderect(tile):
            return tile
    return None

def check_hazard_collision():
    for hazard in hazards:
        if player.colliderect(hazard):
            return hazard
    return None

def hazard_death():
    hazard = check_hazard_collision()
    if hazard is not None:
        player.x = 0
        player.y = 0

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

def move_player_x(velocity_x):
    move_map_x(velocity_x)

def move_map_x(velocity_x):
    for tile in tiles:
        tile.x += velocity_x
    
    for hazard in hazards:
        hazard.x += velocity_x

    #for (item) in class etc.

def move():
    check_tile_collisions_x()

    player.velocity_y += Gravity
    player.y += player.velocity_y

    check_tile_collisions_y()

    hazard_death()

def draw():
    screen.fill((20,18,167))
    pygame.draw.rect(screen,(2,239,238), player)

    for tile in tiles:
        pygame.draw.rect(screen, (0,128,0), tile)
    
    for hazard in hazards:
        pygame.draw.rect(screen, (255,0,0), hazard)

player = Player()
tiles = []
hazards = []
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
        move_player_x(Player_Velocity_x)
        player.direction = "left"
    
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        move_player_x(-Player_Velocity_x)
        player.direction = "right"
    
    move()
    draw()
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()