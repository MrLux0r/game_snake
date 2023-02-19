import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение размеров экрана
screen_width = 500
screen_height = 500

# Создание окна игры
screen = pygame.display.set_mode((screen_width, screen_height))

# Заголовок игры
pygame.display.set_caption("Snake Game")

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Размер блока и скорость змейки
block_size = 10
snake_speed = 15

# Шрифт для отображения счета
font_style = pygame.font.SysFont(None, 30)


def message(msg, color):
    """
    Функция для отображения сообщений на экране
    """
    if msg == "Game Over":
        restart_msg = font_style.render("Game Over", True, red)
        restart_msg_rect = restart_msg.get_rect()
        restart_msg_rect.center = (screen_width / 2, screen_height / 2)
        screen.blit(restart_msg, restart_msg_rect)
    elif msg == "Press Q-Quit or R-Restart":
        restart_msg = font_style.render("Press Q-Quit or R-Restart", True, black)
        restart_msg_rect = restart_msg.get_rect()
        restart_msg_rect.center = (screen_width / 3, screen_height / 3)
        screen.blit(restart_msg, restart_msg_rect)


def snake(snake_list, color):
    """
    Функция для отображения змейки на экране
    """
    for x in snake_list:
        pygame.draw.rect(screen, color, [x[0], x[1], block_size, block_size])


def gameLoop():
    # Начальное положение змейки
    x1 = screen_width / 2
    y1 = screen_height / 2

    # Изменение положения змейки
    x1_change = 0
    y1_change = 0

    # Создание еды
    foodx = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0

    # Создание списка для хранения координат змейки
    snake_List = []
    Length_of_snake = 1

    # Флаг для перезапуска игры
    game_close = False

    # Главный игровой цикл
    while not game_close:

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Изменение координат змейки
        x1 += x1_change
        y1 += y1_change

        # Отрисовка змейки и еды
        screen.fill(white)
        pygame.draw.rect(screen, green, [foodx, foody, block_size, block_size])
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

            # Отображение змейки на экране
        snake(snake_List, black)

        # Проверка на столкновение головы змейки с телом или стенкой окна
        for segment in snake_List[:-1]:
            if segment == snake_Head:
                game_close = True
        if x1 >= screen_width:
            x1 = 0
        elif x1 < 0:
            x1 = screen_width - block_size
        if y1 >= screen_height:
            y1 = 0
        elif y1 < 0:
            y1 = screen_height - block_size

        # Если змейка съела еду, то добавляем длину змейки и создаем новую еду
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0
            Length_of_snake += 1

        # Отображение счета на экране
        score = Length_of_snake - 1
        score_font = font_style.render("Score: " + str(score), True, black)
        screen.blit(score_font, [0, 0])

        # Обновление экрана
        pygame.display.update()

        # Установка скорости змейки
        clock = pygame.time.Clock()
        clock.tick(snake_speed)

    # Показать сообщение Game Over и кнопку Restart
    while True:
        screen.fill(white)
        message("Game Over", red)
        message("Press Q-Quit or R-Restart", black)
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_r:
                    gameLoop()
        # Обновление экрана
        pygame.display.update()


# Запуск игры
gameLoop()
