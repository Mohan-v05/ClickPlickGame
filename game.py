import pgzrun
import random

# Game settings
WIDTH = 800
HEIGHT = 600
lives = 3
image_x = -100  # Start off-screen
image_speed = 1  # Speed of image moving to the right
score = 0
Player = "Mahi"

# Load your image using Actor
image = Actor("mahi") # The image should be in the same folder as your game script or specify its path

# Function to handle the game logic
def update():
    global image_x, image_speed, lives, score  # Added image_speed here as global
    # Move the image to the right
    image_x += image_speed
      # Increase speed for next update
    
    # If the image goes off the screen, reset its position and lose a life
    if image_x > WIDTH:
        image_x = -100  # Reset image to the left of the screen
        lives -= 1  # Decrease lives if image goes off-screen

        if lives == 0:
            print("Game Over!")
            quit()

    if score == 10:
        print("Excellent!")
        image_speed += 0.1
    # Update image position
    image.x = image_x


# Function to handle mouse click
def on_mouse_down(pos):
    global image_x, score
    # Check if the click was on the image
    if image_x <= pos[0] <= image_x + 100 and 100 <= pos[1] <= 200:
        score += 1  # Increase score
        
        image_x = -100  # Reset image to the left
        print(f"Score: {score}")

# Function to draw the image and game elements
def draw():
    screen.clear()  # screen is available automatically in pgzrun
    screen.draw.text(f"Lives: {lives}", (10, 10), fontsize=30, color="red")
    screen.draw.text(f"Score: {score}", (WIDTH - 120, 10), fontsize=30, color="green")
    screen.draw.text(f"Player: {Player}", (50, 10), fontsize=30, color="blue")
    
    if  score == 10:
        screen.draw.text("Welcome to round to {player}", (50, 50), fontsize=30, color="blue")
    # Draw the moving image using Actor
    image.draw()  # This will automatically use image.x and image.y

# Start the game
pgzrun.go()
