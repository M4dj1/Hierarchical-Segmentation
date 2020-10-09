import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def fusion(image, iters):
    for greyscale in range(255):
        distance_matrix = abs(image - greyscale)
        i = 0
        distance_range = 1
        while i < iters:
            if distance_range in distance_matrix :
                index = np.argmin(np.ma.masked_where(distance_matrix < distance_range, distance_matrix))
                nearest_pixel = image.item(index)
                image[image == nearest_pixel] = min(greyscale, nearest_pixel)
                distance_range += 1
            i += 1

iteration = int(input("How many fusions ? : "))

img = Image.open('bird.jpg').convert('L')
imageMat = np.array(img)


fusion(imageMat, iteration)


plt.subplot(1, 2, 1)
plt.title('1')
plt.imshow(img, cmap='gray')
plt.subplot(1, 2, 2)
plt.title('2')
plt.imshow(Image.fromarray(imageMat), cmap='gray')

plt.show()