# Exercises from U01C08
# I have to use pillow because Runestone's 'image' module is apparently its own thing

import image

# Exercise 6
# Write a program to remove all the red from an image.
img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,15)   # setDelay(0) turns off animation, but appears to freeze while processing...

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        new_red = 0
        new_green = p.getGreen()
        new_blue = p.getBlue()

        new_pixel = image.Pixel(new_red, new_green, new_blue)

        img.setPixel(col, row, new_pixel)

img.draw(win)
win.exitonclick()

# Exercise 7
# Write a function to convert the image to grayscale.

import image

img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,15)   # setDelay(0) turns off animation, but appears to freeze while processing...

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        grayscale_avg = (p.getBlue() + p.getGreen() + p.getRed())/3

        new_pixel = image.Pixel(grayscale_avg, grayscale_avg, grayscale_avg)

        img.setPixel(col, row, new_pixel)

img.draw(win)
win.exitonclick()

# Exercise 8 
# Write a function to convert an image to black and white.
import image

img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,15)   # setDelay(0) turns off animation, but appears to freeze while processing...

threshold = int(input("Threshold 0-255:"))

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        grayscale_avg = (p.getBlue() + p.getGreen() + p.getRed())/3
        paint = 0
        if grayscale_avg < threshold:
            paint = 0
        else:
            paint = 255
        new_pixel = image.Pixel(paint, paint, paint)

        img.setPixel(col, row, new_pixel)

img.draw(win)
win.exitonclick()

# Exercise 9
# Sepia Tone images are those brownish colored images
# that may remind you of times past. The formula for 
# creating a sepia tone is as follows:
# new_r = (R × 0.393 + G × 0.769 + B × 0.189)
# new_g = (R × 0.349 + G × 0.686 + B × 0.168)
# new_b = (R × 0.272 + G × 0.534 + B × 0.131)
# Write a function to convert an image to sepia tone. 
# Hint: Remember that RGB values must be integers between 0 and 255.

# Not sure if this implementation is correct. Looks too bright...

import image

img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,15)   # setDelay(0) turns off animation, but appears to freeze while processing...

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)
        
        new_red = (p.getRed() * 0.393 + p.getGreen() * 0.769 + p.getBlue() * 0.189)
        new_green = (p.getRed() * 0.349 + p.getGreen() * 0.686 + p.getBlue() * 0.168)
        new_blue = (p.getRed() * 0.272 + p.getGreen() * 0.534 + p.getBlue() * 0.131)

        new_pixel = image.Pixel(new_red, new_green, new_blue)

        img.setPixel(col, row, new_pixel)

img.draw(win)
win.exitonclick()

# Exercise 10
# Write a function to uniformly enlarge an image by
# a factor of 2 (in other words, make the image twice 
# as wide and twice as tall).

# Exercise 11
# After you have scaled an image too much it looks blocky. One way of 
# reducing the blockiness of the image is to replace each pixel with the 
# average values of the pixels around it. This has the effect of smoothing 
# out the changes in color. Write a function that takes an image as a 
# parameter and smooths the image. Your function should return a new image 
# that is the same as the old one but smoothed.

# Exercise 12
# When you scan in images using a scanner they may have lots of noise due to 
# dust particles on the image itself or the scanner itself, or the images 
# themselves may be damaged. One way of eliminating this noise is to replace 
# each pixel by the median value of the pixels surrounding it. 
# Write a program to do this.




