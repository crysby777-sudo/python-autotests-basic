import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Меню игры тест")
clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

font = pygame.font.Font(None, 36)

def draw_button(text, x, y, width, height, color, hover=False):
    mouse = pygame.mouse.get_pos()
    rect = pygame.Rect(x, y, width, height)
    if rect.collidepoint(mouse):
        pygame.draw.rect(screen, GRAY, rect)
    else:
        pygame.draw.rect(screen, color, rect)
    text_surf = font.render(text, True, BLACK)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)
    return rect

def main_menu():
    while True:
        screen.fill(WHITE)
        button_new = draw_button("Новая игра", 300, 200, 200, 50, (0, 200, 0))
        button_load = draw_button("Загрузить", 300, 300, 200, 50, (0, 200, 0))
        button_quit = draw_button("Выход", 300, 400, 200, 50, (200, 0, 0))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_new.collidepoint(event.pos):
                    # Запуск игры
                    print("Новая игра")
                elif button_load.collidepoint(event.pos):
                    print("Загрузка")
                elif button_quit.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        clock.tick(60)

if __name__ == "__main__":
    main_menu()