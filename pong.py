import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
BALL_RADIUS = 10
PAD_WIDTH, PAD_HEIGHT = 8, 80
HALF_PAD_WIDTH = PAD_WIDTH // 2
HALF_PAD_HEIGHT = PAD_HEIGHT // 2
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Initialize the ball and paddles
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_vel = [0, 0]
paddle1_pos, paddle2_pos = HEIGHT // 2, HEIGHT // 2
paddle1_vel, paddle2_vel = 0, 0
score1, score2 = 0, 0

def spawn_ball(direction):
    global ball_pos, ball_vel
    ball_pos = [WIDTH // 2, HEIGHT // 2]
    ball_vel[0] = random.randrange(120, 240) // 60 * (1 if direction == "RIGHT" else -1)
    ball_vel[1] = -random.randrange(60, 180) // 60

def new_game():
    global paddle1_pos, paddle2_pos, score1, score2
    paddle1_pos, paddle2_pos = HEIGHT // 2, HEIGHT // 2
    score1, score2 = 0, 0
    spawn_ball("LEFT" if random.random() < 0.5 else "RIGHT")

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    # Draw mid line and gutters
    pygame.draw.line(canvas, WHITE, [WIDTH // 2, 0], [WIDTH // 2, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1)
    
    # Update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Collision detection on top and bottom walls
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]

    # Draw ball
    pygame.draw.circle(canvas, WHITE, ball_pos, BALL_RADIUS)

    # Update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    paddle1_pos = max(HALF_PAD_HEIGHT, min(HEIGHT - HALF_PAD_HEIGHT, paddle1_pos))
    paddle2_pos = max(HALF_PAD_HEIGHT, min(HEIGHT - HALF_PAD_HEIGHT, paddle2_pos))

    # Draw paddles
    pygame.draw.rect(canvas, WHITE, [0, paddle1_pos - HALF_PAD_HEIGHT, PAD_WIDTH, PAD_HEIGHT])
    pygame.draw.rect(canvas, WHITE, [WIDTH - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT, PAD_WIDTH, PAD_HEIGHT])

    # Ball collides with gutters or paddles
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        if paddle1_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0] * 1.1
        else:
            score2 += 1
            spawn_ball("RIGHT")
    elif ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        if paddle2_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0] * 1.1
        else:
            score1 += 1
            spawn_ball("LEFT")

    # Draw scores
    score_text = f"{score1}  {score2}"
    label = pygame.font.Font(None, 36).render(score_text, 1, WHITE)
    canvas.blit(label, (WIDTH // 2 - label.get_width() // 2, 20))

# Main game loop
def main():
    running = True
    clock = pygame.time.Clock()
    new_game()

    while running:
        draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    paddle1_vel = -6
                elif event.key == pygame.K_s:
                    paddle1_vel = 6
                elif event.key == pygame.K_UP:
                    paddle2_vel = -6
                elif event.key == pygame.K_DOWN:
                    paddle2_vel = 6
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_w, pygame.K_s):
                    paddle1_vel = 0
                elif event.key in (pygame.K_UP, pygame.K_DOWN):
                    paddle2_vel = 0

        screen.fill(BLACK)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
