import sys
import pygame
import pygame.camera
import pygame.image

pygame.init()

pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
cam.start()
img = cam.get_image()
pygame.image.save(img,"tesfile.png")
pygame.camera.quit()

