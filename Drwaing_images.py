import cv2
import numpy as np
from matplotlib import pyplot as plt

image = np.zeros((512, 512, 3), np.uint8)

# Can we make this in black and white?
image_bw = np.zeros((512, 512), np.uint8)

row, col = 1, 2
fig, axs = plt.subplots(row, col, figsize=(15, 10))
fig.tight_layout()

axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0].set_title('Original RGB Colors')

axs[1].imshow(cv2.cvtColor(image_bw, cv2.COLOR_BGR2RGB))
axs[1].set_title('Original RGB Colors')

image = np.zeros((512, 512, 3), np.uint8)
cv2.line(image, (0, 0), (511, 511), (255, 127, 0), 100)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Bule Linear line')
plt.show()

image = np.zeros((512,512,3), np.uint8)

cv2.rectangle(image, (100,100), (300,300), (127,50,127), 5)
cv2.putText(image, 'I love Computer vision', (80,350),
            cv2.FONT_HERSHEY_COMPLEX, 1, (100,170,0), 2)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.title('Rectangle')

plt.show()
plt.show()

plt.show()