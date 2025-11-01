import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load the music file
pygame.mixer.music.load('Starting.mp3')

# Play the music
pygame.mixer.music.play()


pygame.mixer.music.play(-1)
# Keep the program running to allow music to play
input("Press Enter to stop music...")

pygame.quit()
