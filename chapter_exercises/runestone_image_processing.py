# Runestone, not statndard Python
import image, sys, random

img = image.Image("luther.jpg")
new_img = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin(img.getWidth(), img.getHeight())

for i in range(1, img.getWidth() - 1):
    for j in range(1, img.getHeight() - 1):
        random_x = random.randrange(0,2)
        random_y = random.randrange(0,2)
        picked_pixel = img.getPixel(i+random_x, j+random_y)
        new_img.setPixel(i, j, picked_pixel)
        
new_img.draw(win)
win.exitonclick()
