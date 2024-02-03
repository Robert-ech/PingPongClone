import pygame
import sys

pygame.init()

HEIGHT, WIDTH = 900,900
screen = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption("P1ng P0ng")

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)
TEAL = (21,243,176)
BLUE = (0,66,251)
BROWN = (91,80,55)



PADDLE_WIDTH, PADDLE_HEIGHT = 20,120
PADDLE_SPEED = 10

BALL_SIZE = 20
BALL_SPEED_X, BALL_SPEED_Y = 6, 0
## Set positions 
L_PADDLE = pygame.Rect(20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
R_PADDLE = pygame.Rect(WIDTH - 40, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2 , HEIGHT // - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)


##Functions
def move_paddles():
    keys =pygame.key.get_pressed()
    if keys[pygame.K_w] and L_PADDLE.top > 0:
        L_PADDLE.y -= PADDLE_SPEED
    if keys[pygame.K_s] and L_PADDLE.top < HEIGHT:
        L_PADDLE.y += PADDLE_SPEED
    if keys[pygame.K_UP] and L_PADDLE.top > 0:
        R_PADDLE.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and L_PADDLE.top < HEIGHT:
        R_PADDLE.y += PADDLE_SPEED

def move_ball():
    global BALL_SPEED_X, BALL_SPEED_Y
    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        BALL_SPEED_Y *= -1
    if ball.left <= 0 or ball.right >= WIDTH:
        ball.x = WIDTH //2 - BALL_SIZE //2
        ball.y = HEIGHT //2 - BALL_SIZE //2
    if ball.colliderect(L_PADDLE) or ball.colliderect(R_PADDLE):
        BALL_SPEED_X *= -1

running = True
while running:
    screen.fill(BLACK)

    pygame.draw.rect(screen,BLUE, L_PADDLE)
    pygame.draw.rect(screen,BLUE, R_PADDLE)
    pygame.draw.ellipse(screen,WHITE, ball)
    pygame.draw.aaline(screen,TEAL,(WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    pygame.draw.circle(screen, TEAL, (HEIGHT//2,WIDTH//2), HEIGHT//6 ,3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    move_paddles()
    move_ball()

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
