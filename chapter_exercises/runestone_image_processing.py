import image
import sys
import random

img = image.Image("luther.jpg")
new_img = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin(img.getWidth(), img.getHeight())

for i in range(1, img.getWidth() - 1):
    for j in range(1, img.getHeight() - 1):
        # TODO: Randomly choose the coordinates of a neighboring pixel
        # rand x, rand y. Each 0-2
        random_x = random.randrange(0,2)
        random_y = random.randrange(0,2)
        # take the pos of the current pixel (x-1, y-1), add rand x & rand y
        picked_pixel = img.getPixel(i+random_x, j+random_y)
        # that's the pixel to paint from. 
        
        # TODO: in the new image, set this pixel's color to the neighbor's color
        # apply the picked pixel to the new_img.pixel(i,j)
        new_img.setPixel(i, j, picked_pixel)
        
new_img.draw(win)
win.exitonclick()
