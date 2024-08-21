#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install pygame


# In[9]:


import pygame

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1200, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("How on ~Earth~ Space?")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MOON_GRAY = (169, 169, 169)
EARTH_BLUE = (135, 206, 235)
MARS_RED = (205, 92, 92)

# Object properties
object_radius = 20

# Gravity for different celestial bodies
gravity = {
    "Moon": 1.62 / 9.81 * 0.5,  # Simulated Moon gravity
    "Earth": 9.81 / 9.81 * 0.5,  # Simulated Earth gravity
    "Mars": 3.71 / 9.81 * 0.5    # Simulated Mars gravity
}

# Planet and combined modes
planets = ["Earth", "Moon", "Mars"]
planet_colors = {"Earth": EARTH_BLUE, "Moon": MOON_GRAY, "Mars": MARS_RED}
object_positions = {}

# Setup for object positions and speed
def reset_object_positions():
    for planet in planets:
        object_positions[planet] = {"x": WIDTH // 2, "y": object_radius, "speed_y": 0}

# Ground position
ground_y = HEIGHT - 100

# Fonts
font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 24)

# Modes
current_mode = "Earth"  # Default mode

# Text rendering function
def render_text(text, font, color, position):
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, position)

# Reset the object positions
reset_object_positions()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit the loop on quit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Reset simulation on pressing 'R'
                reset_object_positions()
            elif event.key == pygame.K_m:  # Switch to Moon view
                current_mode = "Moon"
                reset_object_positions()
            elif event.key == pygame.K_e:  # Switch to Earth view
                current_mode = "Earth"
                reset_object_positions()
            elif event.key == pygame.K_a:  # Switch to Mars view
                current_mode = "Mars"
                reset_object_positions()
            elif event.key == pygame.K_c:  # Switch to Combined view
                current_mode = "Combined"
                reset_object_positions()

    # Clear the screen
    screen.fill(WHITE)

    if current_mode == "Combined":
        # Combined view: Display all planets side by side
        panel_width = WIDTH // len(planets)
        for i, planet in enumerate(planets):
            panel_x = i * panel_width

            # Apply gravity for each planet's object
            if object_positions[planet]["y"] + object_radius < ground_y:
                object_positions[planet]["speed_y"] += gravity[planet]
                object_positions[planet]["y"] += object_positions[planet]["speed_y"]
            else:
                object_positions[planet]["speed_y"] = 0  # Object has hit the ground

            # Draw each panel's background
            pygame.draw.rect(screen, planet_colors[planet], (panel_x, 0, panel_width, HEIGHT))

            # Draw the object (e.g., a coin) for each planet
            pygame.draw.circle(screen, BLACK, (panel_x + panel_width // 2, int(object_positions[planet]["y"])), object_radius)

            # Draw the ground
            pygame.draw.rect(screen, WHITE, (panel_x, ground_y, panel_width, HEIGHT - ground_y))

            # Display the planet's name
            render_text(planet, font, BLACK, (panel_x + 20, 20))

    else:
        # Individual planet view
        planet = current_mode

        # Apply gravity for the current planet's object
        if object_positions[planet]["y"] + object_radius < ground_y:
            object_positions[planet]["speed_y"] += gravity[planet]
            object_positions[planet]["y"] += object_positions[planet]["speed_y"]
        else:
            object_positions[planet]["speed_y"] = 0  # Object has hit the ground

        # Draw the background for the current planet
        screen.fill(planet_colors[planet])

        # Draw the object (e.g., a coin)
        pygame.draw.circle(screen, BLACK, (WIDTH // 2, int(object_positions[planet]["y"])), object_radius)

        # Draw the ground
        pygame.draw.rect(screen, WHITE, (0, ground_y, WIDTH, HEIGHT - ground_y))

        # Display the planet's name
        render_text(f"{planet} view", font, BLACK, (20, 20))

    # Display instructions
    render_text("Press 'R' to reset, 'M' for Moon, 'E' for Earth, 'A' for Mars, 'C' for Combined view", small_font, BLACK, (20, HEIGHT - 40))

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)

# Clean up and close pygame
pygame.quit()


# In[ ]:




