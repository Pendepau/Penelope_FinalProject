import pygame

### use class function to make a charater, and another one to make the enviroment

class Character():
    def _init_(self, pos=(10,10),size = 20):
        self.pos = pos
        self.size = size
        self.color = pygame.Color (255,0,0)
    
    def draw(self, resolution):
        pygame.draw.rect(resolution, self.color, 
                 pygame.Rect(30, 30, 60, 60))


def main():
    # initalize & shut down game/ holds all game functions
    pygame.init()
    pygame.display.set_caption("2D Platfomr")
    resolution = (800,800)
    screen = pygame.display.set_mode(resolution)
    running = True
    while running:
        pygame.display.flip()
        color = pygame.Color (0,55,0)
        screen.fill(color)
        Character.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()


if __name__ == "__main__":
    main()