import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('subodh.jfif')

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("S",hsv_image)

lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("lab",lab)


cv2.waitKey(0)
row, col = 2, 2
fig, axs = plt.subplots(row, col, figsize=(15, 10))
fig.tight_layout()

axs[0][0].imshow(cv2.cvtColcvcvor(hsv_image, cv2.COLOR_BGR2RGB))
axs[0][0].set_title('HSV image')

axs[0][1].imshow(cv2.cvtColor(hsv_image[:, :, 0], cv2.COLOR_BGR2RGB))
axs[0][1].set_title('Hue channel')

axs[1][0].imshow(cv2.cvtColor(hsv_image[:, :, 1], cv2.COLOR_BGR2RGB))
axs[1][0].set_title('Saturation channel')

axs[1][1].imshow(cv2.cvtColor(hsv_image[:, :, 2], cv2.COLOR_BGR2RGB))
axs[1][1].set_title('Value channel')

plt.show()