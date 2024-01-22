import cv2
import numpy as np
from sklearn.cluster import KMeans

def dominant_color(image, k=3):
    # Reshape the image to a 2D array of pixels
    pixels = image.reshape((-1, 3))

    # Apply K-Means clustering
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(pixels)

    # Get the dominant color
    dominant_color = kmeans.cluster_centers_.astype(int)[0]

    return dominant_color

def get_center_rectangle(image, width=100, height=100):
    # Get the center coordinates of the image
    center_x, center_y = image.shape[1] // 2, image.shape[0] // 2

    # Define rectangle coordinates
    x1 = center_x - width // 2
    y1 = center_y - height // 2
    x2 = center_x + width // 2
    y2 = center_y + height // 2

    # Extract the central rectangle
    rectangle = image[y1:y2, x1:x2]

    return rectangle

def change_brightness(image, factor):
    # Convert the image to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Adjust the brightness (value channel)
    hsv[:, :, 2] = np.clip(hsv[:, :, 2] * factor, 0, 255)

    # Convert back to BGR
    result = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    return result

# Capture video feed (replace '0' with the appropriate camera index)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video feed
    ret, frame = cap.read()

    # Get the central rectangle
    central_rectangle = get_center_rectangle(frame)

    # Get the dominant color before brightness change
    original_dominant_color = dominant_color(central_rectangle)

    # Change brightness of surroundings
    brightened_frame = change_brightness(frame, 1.5)

    # Get the central rectangle after brightness change
    brightened_rectangle = get_center_rectangle(brightened_frame)

    # Get the dominant color after brightness change
    brightened_dominant_color = dominant_color(brightened_rectangle)

    # Display the results
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Brightened Frame', brightened_frame)

    print(f'Original Dominant Color: {original_dominant_color}')
    print(f'Brightened Dominant Color: {brightened_dominant_color}')

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()