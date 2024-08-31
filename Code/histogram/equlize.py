import cv2
import matplotlib.pyplot as plt
# Load the image
image = cv2.imread('cat.jpeg')
# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Calculate the histogram before equalization
hist_before = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
# Perform histogram equalization
equalized_image = cv2.equalizeHist(gray_image)
# Calculate the histogram after equalization
hist_after = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])
# Plot the grayscale image and histogram before equalization
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image (Before Equalization)')
plt.axis('off')
plt.subplot(2, 2, 2)
plt.plot(hist_before, color='black')
plt.title('Histogram (Before Equalization)')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
# Plot the grayscale image and histogram after equalization
plt.subplot(2, 2, 3)
plt.imshow(equalized_image, cmap='gray')
plt.title('Grayscale Image (After Equalization)')
plt.axis('off')
plt.subplot(2, 2, 4)
plt.plot(hist_after, color='black')
plt.title('Histogram (After Equalization)')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
