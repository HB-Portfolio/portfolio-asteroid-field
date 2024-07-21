# Asteroid Field

I created **Asteroid Field** as my final project for the Code in Place course taught by Stanford. I faced some challenges with using polygons and maintaining accurate collision detection as the speed increased, so I pivoted to using solid shapes to ensure accurate collisions even at max speed.

**Author:** Hendrich Buhrer  
**Certification:** [Stanford Code in Place Certificate](https://codeinplace.stanford.edu/cip4/certificate/e80xil)  
**Deployed Game:** [Asteroid Field](https://codeinplace.stanford.edu/cip4/share/kUXS1Wp8Wc4IMICnSgR1)

## Project Details

This project was developed as part of the **Code in Place** program by Stanford University. You can view the deployed game on the [Stanford Code in Place Website](https://codeinplace.stanford.edu/cip4/share/kUXS1Wp8Wc4IMICnSgR1). 

I earned a certification for completing this course, which you can view [here](https://codeinplace.stanford.edu/cip4/certificate/e80xil).

## Game Overview

Asteroid Field is a game where the player navigates a spaceship through an asteroid field, avoiding collisions with asteroids and collecting stars to score points. The game gets progressively more challenging as the speed of the asteroids increases over time.

### Key Features

- **Custom Graphics Library:** The game uses a custom `graphics.py` library created by Chris Piech, Lisa Yan, and Nick Troccoli, which is a lightweight wrapper around the tkinter library. This makes it easier to create graphical programs for CS106A students.
- **Player and Asteroids:** The player is represented by two rectangles (a base and a top), while the asteroids are ovals of varying sizes and colors.
- **Collision Detection:** Accurate collision detection ensures that the game remains challenging and fair at higher speeds.
- **Dynamic Difficulty:** The game speed increases over time, making it progressively more challenging.

## Code Quality and Structure

All the files are uploaded to the repository. I encourage you to look at the code to see the quality and structure. The main game logic is contained in the following functions:

- **create_player:** Creates the player spaceship.
- **create_asteroid:** Generates a single asteroid.
- **create_star:** Generates a single star.
- **create_world:** Initializes the game world with the player, asteroids, and stars.
- **move_player:** Moves the player based on user input.
- **check_boundary_collision:** Ensures the player stays within the game boundaries.
- **move_asteroid:** Moves an asteroid and resets its position if it goes off-screen.
- **move_asteroids:** Moves all asteroids.
- **move_stars:** Moves the stars to create a scrolling background effect.
- **check_collision:** Checks for collisions between the player and asteroids.
- **game_over:** Displays a game over message and restarts the game.
- **handle_key_press:** Handles player input.
- **update_player_position:** Updates the player's position based on input.
- **main:** The main game loop that ties everything together.

## How to Play

- Use the left and right arrow keys to move the spaceship.
- Avoid colliding with the asteroids.
- Collect stars to increase your score.
- The game speed increases over time, so stay alert!

Feel free to explore the code and see how the game is implemented. If you have any questions or feedback, don't hesitate to reach out. 
