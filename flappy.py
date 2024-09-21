import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
gravity = 0.5
jump_strength = -10
bg = pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game Dev 2\Flappy bird\bgflap.png')

score = 0


font = pygame.font.SysFont('Arial', 36)

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game Dev 2\Flappy bird\flappy1.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.movement = 0

    def update(self):
        self.movement += gravity
        self.rect.y += self.movement

    
        if self.rect.bottom > HEIGHT or self.rect.top < 0:
            self.rect.bottom = HEIGHT / 2

    def jump(self):
        self.movement = jump_strength

bird = Bird(200, 300)
bird_group = pygame.sprite.Group()
bird_group.add(bird)

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game Dev 2\Flappy bird\flappypipe.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]


def display_score(score):
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (WIDTH - 200, 20))


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()

    # Clear screen and draw background
    screen.blit(bg, (0, 0))

    # Update and draw bird
    bird_group.update()
    bird_group.draw(screen)

    # Display the score
    display_score(score)

    # Update display
    pygame.display.update()

pygame.quit()
    

