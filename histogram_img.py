import cv2
import numpy as np

# We need to import matplotlib to create our histogram plots
from matplotlib import pyplot as plt

image = cv2.imread('pooja.jfif')
histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

# cv2.imshow("image",image)

# Simply use 'imwrite' specificing the file name and the image to be saved
# cv2.imwrite('histogram.jpg', cv2.merge(image))
# cv2.imwrite('red.png', cv2.merge(image)
plt.hist(image.ravel(), 256, [0, 256]); plt.show()

plt.show()

color = ('b', 'g', 'r')

# We now separate the colors and plot each in the Histogram
for i, col in enumerate(color):
    histogram2 = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(histogram2, color=col)
    plt.xlim([0, 256])

plt.show()

row, col = 1, 2
fig, axs = plt.subplots(row, col, figsize=(15, 10))
fig.tight_layout()

axs[0].imshow(image)
axs[0].set_title('Matplotlib Colors')

axs[1].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[1].set_title('Original RGB Colors')

plt.show()

image_tobago = cv2.imread("image", image)