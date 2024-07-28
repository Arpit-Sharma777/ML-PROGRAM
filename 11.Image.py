image url : https://drive.google.com/file/d/1Hzd2zMxsAdebdaODShZwNN-KocznJNnA/view?usp=sharing

#11Image(any image)
import cv2
import numpy as np
from google.colab.patches import cv2_imshow



# Load the image (make sure to specify the correct path)
img = cv2.imread('Lap.jpg')

# Resizing the image
resized_img = cv2.resize(img, (300, 300))

# Blurring the image
ksize = (10, 10)  # Define the kernel size
blurred_img = cv2.blur(img, ksize)

# Grayscaling the image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Scaling the image
scaled_img = cv2.resize(img, (400, 400))

# Rotating the image
rotated_img = cv2.rotate(img, cv2.ROTATE_180)

# Edge detection
edges = cv2.Canny(img, 100, 200)

# Segmentation using thresholding
ret, thresh = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)

# Morphological operations
kernel = np.ones((5, 5), np.uint8)
eroded_img = cv2.erode(img, kernel, iterations=1)
dilated_img = cv2.dilate(img, kernel, iterations=1)

# Display the images using cv2_imshow
cv2_imshow(img)
cv2_imshow(resized_img)
cv2_imshow(blurred_img)
cv2_imshow(gray_img)
cv2_imshow(scaled_img)
cv2_imshow(rotated_img)
cv2_imshow(edges)
cv2_imshow(thresh)
cv2_imshow(eroded_img)
cv2_imshow(dilated_img)

# Note: No need for cv2.waitKey(0) and cv2.destroyAllWindows() in Colab
