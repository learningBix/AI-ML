import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('')
plt.imshow("image",cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Bule Linear line')

plt.show()

row, col = 1, 3
fig, axs = plt.subplots(row, col, figsize=(15, 10))
fig.tight_layout()

axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0].set_title('0 - Original Image')
cv2.imwrite('original_rgb.jpg', image)

# Create a black image with same dimensions as our loaded image
blank_image = np.zeros((image.shape[0], image.shape[1], 3))
# Create a copy of our original image
orginal_image = image
# Grayscale our image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Find Canny edges
edged = cv2.Canny(gray, 50, 200)
axs[1].imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))
axs[1].set_title('1 - Canny Edges')
cv2.imwrite('original_rgb.jpg', edged)

# Find contours and print how many were found
contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print("Number of contours found = ", len(contours))

# Draw all contours over blank image
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
axs[2].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[2].set_title('3 - All Contours')
cv2.imwrite('original_rgb.jpg', image)

plt.show()

def get_contour_areas(contours):
    # returns the areas of all contours as list
    all_areas = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        all_areas.append(area)
    return all_areas

# Let's print the areas of the contours before sorting
print("Contor Areas before sorting",)
print(get_contour_areas(contours))

# Sort contours large to small
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)
#sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)[:3]
print("Contor Areas after sorting")
print(get_contour_areas(sorted_contours))

for c in sorted_contours:
    plt.imshow(cv2.cvtColor(orginal_image, cv2.COLOR_BGR2RGB))
    plt.title('Contours by area'); plt.show()
    cv2.drawContours(orginal_image, [c], -1, (255,0,0), 3)
plt.imshow(cv2.cvtColor(orginal_image, cv2.COLOR_BGR2RGB))
plt.title('Contours by area'); plt.show()