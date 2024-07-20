from graphics import Canvas
import time
import random

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 550
BASE_WIDTH = 30
TOP_WIDTH = 15
PLAYER_HEIGHT = 40
NUM_ASTEROIDS = 5
NUM_STARS = 50
DELAY = 0.05

ASTEROID_COLORS = ["lightsteelblue", "slategray", "grey"]

def create_player(canvas):
    top_x = WINDOW_WIDTH // 2 - TOP_WIDTH // 2
    top_y = WINDOW_HEIGHT - PLAYER_HEIGHT - 10
    base_x = WINDOW_WIDTH // 2 - BASE_WIDTH // 2
    base_y = top_y + PLAYER_HEIGHT // 2
    
    top = canvas.create_rectangle(top_x, top_y, top_x + TOP_WIDTH, top_y + PLAYER_HEIGHT // 2, "red")
    base = canvas.create_rectangle(base_x, base_y, base_x + BASE_WIDTH, base_y + PLAYER_HEIGHT // 2, "red")
    
    return base, top

def create_asteroid(canvas):
    size = random.randint(20, 40)
    color = random.choice(ASTEROID_COLORS)
    x = random.randint(0, WINDOW_WIDTH - size)
    y = random.randint(-600, -30)
    return canvas.create_oval(x, y, x + size, y + size, color), size

def create_star(canvas):
    x = random.randint(0, WINDOW_WIDTH)
    y = random.randint(-600, WINDOW_HEIGHT)
    return canvas.create_oval(x, y, x + 2, y + 2, "white")

def create_asteroids(canvas, num_asteroids):
    return [create_asteroid(canvas) for _ in range(num_asteroids)]

def create_stars(canvas, num_stars):
    return [create_star(canvas) for _ in range(num_stars)]

def create_world(canvas):
    stars = create_stars(canvas, NUM_STARS)
    player = create_player(canvas)
    asteroids = create_asteroids(canvas, NUM_ASTEROIDS)
    return player, asteroids, stars

def move_player(canvas, player, dx, dy):
    base, top = player
    canvas.move(base, dx, dy)
    canvas.move(top, dx, dy)

def check_boundary_collision(canvas, player):
    base, top = player
    x_base = canvas.get_left_x(base)
    y_base = canvas.get_top_y(base)
    
    if x_base < 0:
        canvas.moveto(base, 0, y_base)
        top_x = (BASE_WIDTH - TOP_WIDTH) // 2
        canvas.moveto(top, top_x, y_base - PLAYER_HEIGHT // 2)
    elif x_base + BASE_WIDTH > WINDOW_WIDTH:
        canvas.moveto(base, WINDOW_WIDTH - BASE_WIDTH, y_base)
        top_x = WINDOW_WIDTH - ((BASE_WIDTH - TOP_WIDTH) // 2 + TOP_WIDTH)
        canvas.moveto(top, top_x, y_base - PLAYER_HEIGHT // 2)

def move_asteroid(canvas, asteroid, size, speed):
    canvas.move(asteroid, 0, speed)
    y = canvas.get_top_y(asteroid)
    if y > WINDOW_HEIGHT:
        reset_asteroid_position(canvas, asteroid, size)

def reset_asteroid_position(canvas, asteroid, size):
    x = random.randint(0, WINDOW_WIDTH - size)
    canvas.moveto(asteroid, x, random.randint(-600, -30))

def move_asteroids(canvas, asteroids, speed):
    for asteroid, size in asteroids:
        move_asteroid(canvas, asteroid, size, speed)

def move_stars(canvas, stars, speed):
    for star in stars:
        canvas.move(star, 0, speed)
        y = canvas.get_top_y(star)
        if y > WINDOW_HEIGHT:
            reset_star_position(canvas, star)

def reset_star_position(canvas, star):
    x = random.randint(0, WINDOW_WIDTH)
    canvas.moveto(star, x, random.randint(-600, -10))

def check_collision(canvas, player, asteroids):
    player_coords = get_player_coords(canvas, player)
    for asteroid, size in asteroids:
        asteroid_coords = get_asteroid_coords(canvas, asteroid, size)
        if is_collision(player_coords, asteroid_coords):
            return True
    return False

def get_player_coords(canvas, player):
    base, top = player
    base_x = canvas.get_left_x(base)
    base_y = canvas.get_top_y(base)
    top_x = canvas.get_left_x(top)
    top_y = canvas.get_top_y(top)
    return [base_x, base_y, base_x + BASE_WIDTH, base_y + PLAYER_HEIGHT // 2, 
            top_x, top_y, top_x + TOP_WIDTH, top_y + PLAYER_HEIGHT // 2]

def get_asteroid_coords(canvas, asteroid, size):
    asteroid_x = canvas.get_left_x(asteroid)
    asteroid_y = canvas.get_top_y(asteroid)
    return [asteroid_x, asteroid_y, asteroid_x + size, asteroid_y + size]

def is_collision(player_coords, asteroid_coords):
    base_x1, base_y1, base_x2, base_y2, top_x1, top_y1, top_x2, top_y2 = player_coords
    a_x1, a_y1, a_x2, a_y2 = asteroid_coords

    return not ((base_x2 < a_x1 or base_x1 > a_x2 or base_y2 < a_y1 or base_y1 > a_y2) and 
                (top_x2 < a_x1 or top_x1 > a_x2 or top_y2 < a_y1 or top_y1 > a_y2))

def game_over(canvas, score):
    canvas.create_text(WINDOW_WIDTH // 6, WINDOW_HEIGHT // 6, f"Game Over! Your score is {score}", "Arial", 20, "red")
    canvas.create_text(WINDOW_WIDTH // 6, WINDOW_HEIGHT // 6 + 30, "Click to restart!", "Arial", 16, "white")
    canvas.wait_for_click()

def handle_key_press(canvas, keys_held):
    key = canvas.get_last_key_press()
    if key == 'ArrowLeft':
        keys_held.add('ArrowLeft')
    elif key == 'ArrowRight':
        keys_held.add('ArrowRight')
    else:
        keys_held.discard('ArrowLeft')
        keys_held.discard('ArrowRight')

def update_player_position(canvas, player, keys_held):
    if 'ArrowRight' in keys_held:
        move_player(canvas, player, BASE_WIDTH // 2, 0)
    elif 'ArrowLeft' in keys_held:
        move_player(canvas, player, -BASE_WIDTH // 2, 0)
    check_boundary_collision(canvas, player)

def main():
    while True:
        canvas = Canvas(WINDOW_WIDTH, WINDOW_HEIGHT)
        canvas.create_rectangle(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, "black")
        player, asteroids, stars = create_world(canvas)
        keys_held = set()
        score = 0
        start_time = time.time()
        
        while True:
            handle_key_press(canvas, keys_held)
            update_player_position(canvas, player, keys_held)
            elapsed_time = time.time() - start_time
            current_speed = min(100, 10 + elapsed_time / 2)
            move_asteroids(canvas, asteroids, current_speed)
            move_stars(canvas, stars, current_speed)
            if check_collision(canvas, player, asteroids):
                game_over(canvas, score)
                break
            score += 1
            time.sleep(DELAY)

if __name__ == "__main__":
    main()
