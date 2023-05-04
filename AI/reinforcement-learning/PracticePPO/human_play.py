import gym
import pygame
from pygame.locals import *

# Initialize the CartPole environment
env = gym.make('CartPole-v0')

# Initialize PyGame
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Human Play - CartPole')

# Define action mapping
action_mapping = {
    K_LEFT: 0,
    K_RIGHT: 1
}

# Game loop
running = True
while running:
    # Reset the environment
    state = env.reset()
    done = False

    # Render the environment
    env.render(mode='human')

    # Loop until the episode is done
    while not done:
        # PyGame event handling
        action = None
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                running = False
                break

            if event.type == KEYDOWN and event.key in action_mapping:
                action = action_mapping[event.key]

        # Perform action
        if action is not None:
            state, reward, done, _ = env.step(action)

        # Render the environment
        env.render(mode='human')

# Cleanup
pygame.quit()
env.close()
