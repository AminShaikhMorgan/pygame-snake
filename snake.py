
'''
Snake game.
Authors:
Rushaad Hayward, Emmanuel Cook
'''

import pygame
import random
import sys

# The game grid contains this many cells in the x direction. A piece of food or a segment of the snake takes up one cell.
GRID_WIDTH = 30
# The game grid contains this many cells in the y direction. A piece of food or a segment of the snake takes up one cell.
GRID_HEIGHT = 30
# The height and width of each square cell in pixels.
PIXELS_IN_CELL = 20
# The width of the game grid in pixels.
GRID_WIDTH_PIXELS = PIXELS_IN_CELL * GRID_WIDTH
# The height of the game grid in pixels.
GRID_HEIGHT_PIXELS = PIXELS_IN_CELL * GRID_HEIGHT
# The initial length of the snake. Before eating any food, the snake contains this many segments.
INITIAL_SNAKE_LENGTH = 10

# Each of these directions contains a 2-tuple representing delta-x and delta-y for moving in that direction.
DIRECTION_LEFT = (-1, 0)
DIRECTION_RIGHT = (1, 0)
DIRECTION_UP = (0, -1)
DIRECTION_DOWN = (0, 1)

# Background color of the snake grid.
COLOR_BACKGROUND = (255, 255, 255)  # rgb color for white
# This is the color of the snake's head. 
COLOR_SNAKE_HEAD = (255,254,255)      # rgb color for red
# This is the color of the rest of the snake.
COLOR_SNAKE = (0, 255, 0)           # rgb color for green
# This is the color for the snake's food.
COLOR_FOOD = (255, 200, 0)          # rgb color for orange
# This is the color for the game over text.
COLOR_GAME_OVER_TEXT = (0, 0, 0)    # rgb color for black

def get_direction(previous_direction, event_key):
    """Return the new direction of the snake: one of DIRECTION_{LEFT,RIGHT,UP,DOWN}.
    previous_direction - the previous direction of the snake; one of DIRECTION_{LEFT,RIGHT,UP,DOWN} 
    event_key - the event that the user pressed; one of https://www.pygame.org/docs/ref/key.html
    If event_key does not correspond with any of the arrows keys, return previous_direction.
    """
   if event_key == pygame.K_LEFT:
        return DIRECTION_LEFT
    elif event_key == pygame.K_UP:
        return DIRECTION_UP
    elif event_key == pygame.K_RIGHT:
        return DIRECTION_RIGHT
    elif event_key == pygame.K_DOWN:
        return DIRECTION_DOWN
    return previous_direction
def create_food_position():
    """Returns a random 2-tuple in the grid where the food should be located.
    The first element is the x position. Must be an int between 0 and GRID_WIDTH - 1, inclusively.
    The second element is the y position. Must be an int between 0 and GRID_HEIGHT - 1, inclusively.
    """
    create_food_position = (x_position, y_position)
    y = random.randint(0,GRID_HEIGHT -1)
    x = random.randint(0,GRID_WIDTH -1)
    return (x,y)
    

def snake_ate_food(snake, food):
    """Returns whether food was eaten by the snake.
    snake - list of 2-tuples representing the positions of each snake segment
    food - 2-tuple representing the position in the grid of the food
    This function should return True if the head of the snake is in the same position as food.
    """
     if snake[0] == food:
        return True
    return False

def snake_ran_out_of_bounds(snake):
    """Returns whether the snake has ran off one of the four edges of the grid.
    snake - list of 2-tuples representing the positions of each snake segment
    Note that the grid is GRID_WIDTH cells wide and GRID_HEIGHT cells high.
    """
    return False

def snake_intersected_body(snake):
    """Returns whether the snake has ran into itself.
    snake - list of 2-tuples representing the positions of each snake segment
    The snake ran into itself if the position of the head is the same as the position
    of any of its body segments.
    """
    return False

def get_score(snake):
    """Returns the current score of the game.
    snake - list of 2-tuples representing the positions of each snake segment
    The user earns 10 points for each of the segments in the snake.
    For example, if the snake has 25 segments, the score is 250.
    """
    return 0

def get_game_over_text(score):
    """Returns the text to draw on the screen after the game is over.
    This text should contain 'Game Over' as well as the score.
    score - integer representing the current score of the game.
    """
    return 'Game Over.'

def get_snake_speed(snake):
    """Return the number of cells the snake should travel in one second.
    snake - list of 2-tuples representing the positions of each snake segment
    The speed at the beginning of the game should be 5. Once the snake has eaten 10 pieces of food,
    the speed of the game should increase (by how much is up to you).
    """
    return 5

def move_snake(snake, direction, food):
    """Moves the snake one space in the direction specified and returns whether food was eaten.
    The snake moves by removing the last segment and added a new head to the beginning of the snake list.
    If the snake ate the food, the last segment is not removed, so the snake grows by a single segment.
    Do not edit this function.
    """
    head = snake[0]
    new_head = (head[0] + direction[0], head[1] + direction[1])
    snake.insert(0, new_head)
    ate_food = snake_ate_food(snake, food)
    if not ate_food:
        snake.pop()
    return ate_food

def get_initial_snake():
    """Returns a list of 2-tuples representing the initial positions of the snake segments.
    The snake starts with its head in the middle of the grid, extending to the left.
    Do not edit this function.
    """
    snake = []
    head = (GRID_HEIGHT // 2, GRID_WIDTH // 2)
    snake.append(head)
    for _ in range(INITIAL_SNAKE_LENGTH - 1):
        last_segment = snake[-1]
        next_segment = (last_segment[0] - 1, last_segment[1])
        snake.append(next_segment)
    return snake

def draw_food(screen, food):
    """Draw the food onto the screen.
    Do not edit this function.
    """
    if food == None:
        return
    x = food[0] * PIXELS_IN_CELL
    y = food[1] * PIXELS_IN_CELL
    pygame.draw.ellipse(screen, COLOR_FOOD, (x, y, PIXELS_IN_CELL, PIXELS_IN_CELL))

def draw_snake(screen, snake):
    """Draw the snake onto the screen.
    Do not edit this function.
    """
    color = COLOR_SNAKE_HEAD
    for segment in snake:
        x = segment[0] * PIXELS_IN_CELL
        y = segment[1] * PIXELS_IN_CELL
        pygame.draw.ellipse(screen, color, (x, y, PIXELS_IN_CELL, PIXELS_IN_CELL))
        color = COLOR_SNAKE

def draw_game_over(screen, game_over_text):
    """Draw game_over_text in the middle of the screen.
    Do not edit this function.
    """
    font_size = 50
    sys_font = pygame.font.Font(None, font_size)
    text_surface = sys_font.render(game_over_text, True, COLOR_GAME_OVER_TEXT)
    x = GRID_WIDTH_PIXELS // 2 - text_surface.get_width() // 2
    y = GRID_HEIGHT_PIXELS // 2 - text_surface.get_height() // 2
    # https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit
    screen.blit(text_surface, (x, y))

def draw_screen(screen, snake, food, game_over):
    """Draw the snake, food and maybe the game over message to the screen.
    Do not edit this function.
    """
    # Fill the screen with the background color.
    # https://www.pygame.org/docs/ref/surface.html#pygame.Surface.fill
    screen.fill(COLOR_BACKGROUND)

    # Draw the snake, food, and optionally the game over message to the screen.
    draw_snake(screen, snake)
    draw_food(screen, food)
    if game_over:
        score = get_score(snake)
        game_over_text = get_game_over_text(score)
        draw_game_over(screen, game_over_text)

    # Call flip after we're done drawing this frame. This updates the entire screen.
    # https://www.pygame.org/docs/ref/display.html#pygame.display.flip
    pygame.display.flip()

def process_events(direction, game_over):
    """Returns the new direction and whether the game should reset after processing
    all mouse and keyboard input events.
    Do not edit this function.
    """
    should_reset_game = False
    for event in pygame.event.get():
        # Quit the program when the user presses the x in the corner of the window.
        if event.type == pygame.QUIT:
            sys.exit()
        # Process events when the user presses a key on the keyboard.
        # https://www.pygame.org/docs/ref/key.html
        elif event.type == pygame.KEYDOWN:
            # Update the snake's direction based on which key the user pressed.
            direction = get_direction(direction, event.key)
            if game_over and event.key == pygame.K_SPACE:
                # Reset all game state if the space bar is pressed after the game is over.
                should_reset_game = True
    return (direction, should_reset_game)

def start_game():
    """Starts the snake game. 
    Do not edit this function.
    """
    # Initialize the pygame module.
    pygame.init()
    # Create a screen to display the game.
    screen = pygame.display.set_mode((GRID_WIDTH_PIXELS, GRID_HEIGHT_PIXELS))
    # Set the title of the screen to Snake.
    pygame.display.set_caption('Snake')
    # This clock is used to ensure that the game progresses at the right speed.
    clock = pygame.time.Clock()

    # The snake starts out traveling in the right direction.
    direction = DIRECTION_RIGHT
    # The 2-tuple representing the position of the food in the grid.
    food = create_food_position() 
    # The list of 2-tuples that make up the snake. The first element in the list is the snake's head.
    snake = get_initial_snake()
    # Tracks whether the game is over. When the game is over the user can press the space bar to restart.
    game_over = False

    # Loop forever until the user quits the game.
    while True:
        # Process all of the events the user input after the last loop iteration.
        # (e.g. mouse clicks and keyboard button presses).
        direction, should_reset_game = process_events(direction, game_over)
        if should_reset_game:
            # Reset all game state if the space bar is pressed after the game is over.
            direction = DIRECTION_RIGHT
            food = create_food_position()
            snake = get_initial_snake()
            game_over = False

        # After processing all input events, move the snake and check whether the game is over.
        if not game_over:
            # Move the snake in the current direction.
            ate_food = move_snake(snake, direction, food)
            # Check if the snake moved into a position that should end the game.
            game_over = snake_intersected_body(snake) or snake_ran_out_of_bounds(snake)
            if not game_over and ate_food:
                # Move the food if the snake just ate it.
                food = create_food_position()

        # Draw the snake, food, and optionally game over message to the screen.
        draw_screen(screen, snake, food, game_over)

        # After drawing the frame, pause the game momentarily to make sure the game
        # does not progress too quickly.
        clock.tick(get_snake_speed(snake))

# Start the snake game.
start_game()

