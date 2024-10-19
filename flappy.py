import pygame 
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
gravity = 0.5
jump_strength = -10
bg = pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game Dev 2\Flappy bird\bgflap.png') 
ground = pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game Dev 2\Flappy bird\ground.png') 
retry = pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game Dev 2\Flappy bird\retry.png')
clock = pygame.time.Clock()
score = 0 
pipe_gap = random.randint(125,200)  # Increased gap
scroll_speed = 5  
x = 0 
game_over = False
bird_fly = False
pipe_frq = 1500
last_pipe = pygame.time.get_ticks() - pipe_frq 
pass_pipe = False

font = pygame.font.SysFont('Arial', 36)

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game Dev 2\Flappy bird\flappy1.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.movement = 0

    def update(self):
        if bird_fly == True:
            self.movement += gravity
            #self.rect.y += self.movement 
            if self.movement>3: 
                self.movement = 3 
            if self.rect.bottom < 600: 
                self.rect.y += self.movement

  

    #def jump(self):
        self.movement = jump_strength

bird = Bird(200, 300) 
bird_group = pygame.sprite.Group()
bird_group.add(bird)

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game Dev 2\Flappy bird\pipe.png')
        self.rect = self.image.get_rect()
        if position == 1:  # Top pipe
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - (pipe_gap // 2)] 
        elif position == -1:  # Bottom pipe
            self.rect.topleft = [x, y + (pipe_gap // 2)]  
    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()
class Button(): 
    def __init__ (self,x,y):  
        self.image = pygame.image.load(r'C:\Users\aruni\OneDrive\Documents\Game Dev 2\Flappy bird\retry.png') 
        self.rect = self.image.get_rect() 
        self.rect.topleft = [x,y]   
    def draw(self):   
        restart = False   
        pos = pygame.mouse.get_pos() 
        if self.rect.collidepoint(pos): 
            if pygame.mouse.get_pressed()[0] == 1: 
                restart = True  
        screen.blit(self.image, (self.rect.x,self.rect.y))
        return restart
#making object for button 
button = Button(300,400)


        
        

        


pipe_group = pygame.sprite.Group()

def display_score(score):
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (WIDTH - 200, 20))
def reset(): 
    bird.rect.x = 100 
    bird.rect.y = 100 
    pipe_group.empty() 
    
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #if event.type == pygame.KEYDOWN:
            #if event.key == pygame.MOUSEBUTTONDOWN and game_over == False :
                #bird_fly = True
                #bird.jump() 
        if event.type == pygame.MOUSEBUTTONDOWN and game_over == False and bird_fly == False: 
            bird_fly = True  
            

    
    if not game_over and bird_fly:
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frq:
            pipe_height = random.randint(200,300)
            btm_pipe = Pipe(WIDTH, pipe_height, -1)  # Bottom pipe
            top_pipe = Pipe(WIDTH, pipe_height, 1)   # Top pipe (flipped)
            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now  
    
    
    
    # Clear screen and draw background
    screen.blit(bg, (0, 0))

    #blitting the restart button 
    #screen.blit(retry, (400,300))
    
    # Draw ground
    screen.blit(ground, (x, 500))
    x -= scroll_speed
    if x <= -25:
        x = 0 

    if len(pipe_group) > 0: 
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right and pass_pipe == False: 
                pass_pipe = True 
        if pass_pipe == True:
            if bird_group.sprites()[0].rect.right > pipe_group.sprites()[0].rect.right:
                 score += 1  
                 pass_pipe = False 

    if pygame.sprite.groupcollide(bird_group,pipe_group,False,False): 
        game_over = True    
        bird_fly = False 
        scroll_speed = 0 
    
 
    if game_over == True: 
        if button.draw() == True: 
            game_over = False 
            score = 0   
            reset()

        #screen.blit(retry, (400,300))


                 
    # Update and draw pipes and bird 

    pipe_group.update()
    pipe_group.draw(screen)
    bird_group.update()
    bird_group.draw(screen)

    # Display the score
    display_score(score) 

    # Update display
    pygame.display.update() 



pygame.quit()
