import cv2
import matplotlib.pyplot as plt
# Load the image
image = cv2.imread('cat.jpeg')
# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Calculate the histogram
histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
# Plot the grayscale image
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')
# Plot the histogram
plt.subplot(1, 2, 2)
plt.plot(histogram, color='black')
plt.title('Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
