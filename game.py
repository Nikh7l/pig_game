import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)
FPS = 30

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dice Game")

# Initialize game variables
numberPlayers = 2
max_score = 50
player_scores = [0 for _ in range(numberPlayers)]
current_player = 0
rolling = False

# Function to roll the dice
def roll():
    return random.randint(1, 6)

# Function to update the game state
def update_game():
    global current_player, rolling

    if not rolling:
        return

    score = roll()
    if score == 1:
        player_scores[current_player] = 0
    else:
        player_scores[current_player] += score

    if player_scores[current_player] >= max_score:
        rolling = False
        winner_text = FONT.render(f"Player {current_player + 1} wins!", True, BLACK)
        screen.blit(winner_text, (WIDTH // 2 - 100, HEIGHT // 2 - 20))
        pygame.display.flip()
        pygame.time.wait(2000)
        reset_game()

    current_player = (current_player + 1) % numberPlayers

# Function to reset the game
def reset_game():
    global player_scores, current_player
    player_scores = [0 for _ in range(numberPlayers)]
    current_player = 0

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                rolling = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rolling:
                continue
            if event.button == 1:  # Left mouse button
                rolling = True

    screen.fill(WHITE)
    update_game()

    # Display player scores
    for i, score in enumerate(player_scores):
        text = FONT.render(f"Player {i + 1}: {score}", True, BLACK)
        screen.blit(text, (10, 10 + i * 40))

    if rolling:
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(170, 200, 60, 60))
    else:
        pygame.draw.rect(screen, (0, 128, 0), pygame.Rect(170, 200, 60, 60))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
