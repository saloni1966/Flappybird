import pygame 


pygame.init() 
pygame.init()


WIDTH = 800 
HEIGHT = 600 
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 

bg = pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game Dev 2\Flappy bird\bgflap.png') 


class Bird(pygame.sprite.Sprite): 
    def __init__(self,x,y): 
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game Dev 2\Flappy bird\flappy1.png')
        self.rect = self.image.get_rect() 
        self.rect.center = [x,y]
bird = Bird(200,300)
bird_group = pygame.sprite.Group()
bird_group.add(bird) 

class pipe(pygame.sprite.Sprite): 
    def ___init___(self,x,y) : 
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game Dev 2\Flappy bird\flappypipe.png') 
        self.rect = self.image.get_rect()
        self.rect.center = [x,y] 
        


    

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()
    screen.blit(bg,(0,0))
    bird_group.draw(screen)
    pygame.display.update()  
    

