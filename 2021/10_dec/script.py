from PIL import Image, ImageChops

img1 = Image.open('img1.png').convert('1') # Open Image and convert to B&W
img2 = Image.open('img2.png').convert('1') # Open Image and convert to B&W
res = ImageChops.logical_xor(img1, img2) # XOR Images
res.show() # Open Image

print('Please scan this code!')