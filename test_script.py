import sys
import pygame
import pygame.camera
import pygame.image
import numpy as np
import serial


pygame.init()

pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[1])
cam.start()
img = cam.get_image()
pygame.image.save(img,"yellow.png")
pygame.camera.quit()
imgdata=pygame.surfarray.array3d(img)
arr=np.array(imgdata)
arr=np.mean(np.mean(arr,axis=0),axis=0)
print(arr)
