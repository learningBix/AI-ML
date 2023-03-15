import cv2
import numpy as np
from matplotlib import pyplot as plt
import numpy as np


# Let's load a simple image with 3 black squares
image = cv2.imread('pooja.jfif')
image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

blank = np.zeros(image.shape, dtype="uint8")
cv2.imshow("blank",blank)


plt.imshow(image)
plt.title('Input Image')
cv2.imwrite('input_image.jpg', image)

plt.show()

# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

row, col = 1, 2
fig, axs = plt.subplots(row, col, figsize=(15, 10))
fig.tight_layout()

# Find Canny edges

ret, thresh = cv2.threshold(gray, 100,255,cv2.THRESH_BINARY)
image = cv2.GaussianBlur(thresh, (3,3),cv2.BORDER_DEFAULT)
edged = cv2.Canny(gray, 70, 150)
axs[0].imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))
axs[0].set_title('Canny Edges')
cv2.imshow('canny_edges.jpg', edged)



# cv2.imshow('Thresh',thresh)
# cv2.waitKey(0)



# Finding Contours
# Use a copy of your image e.g. edged.copy(), since findContours alters the image
contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print("Number of Contours found = " + str(len(contours)))

cv2.drawContours(blank, contours, -1,(0,255,0),1)
cv2.imshow('contours drawn', blank)
cv2.waitKey(0)
# Draw all contours
# Use '-1' as the 3rd parameter to draw all
cv2.drawContours(image, contours, -1, (0, 0, 255), 3)
axs[1].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[1].set_title('Contours')
cv2.imwrite('contour_image.jpg', image)

plt.show()