from PIL import Image
im = Image.open('Luther.jpg')
print(im.format, im.size, im.mode)
# im.show()

box = (50, 50, 200, 200)
region = im.crop(box)
region = region.transpose(Image.ROTATE_180)
im.paste(region, box)
im.show()

# r, g, b = im.split()
# im = Image.merge("RGB", (g, b, r))
# im.show()