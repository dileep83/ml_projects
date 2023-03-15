import cv2
import numpy as np

def process_image(image_file, filter_type):
    # Read the image file
    image_bytes = np.frombuffer(image_file.read(), np.uint8)
    image = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)

    # Apply filters to the image
    if filter_type == 'grayscale':
        filtered_image = apply_grayscale(image)
    elif filter_type == 'blur':
        filtered_image = apply_blur(image)
    elif filter_type == 'edge_detection':
        filtered_image = apply_edge_detection(image)

    # Return the filtered image
    return filtered_image

def apply_grayscale(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Add some text to the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(gray, 'Grayscale Filter', (50, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # Return the filtered image
    return gray

def apply_blur(image):
    # Apply Gaussian blur to the image
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # Add some text to the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(blurred, 'Blur Filter', (50, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # Return the filtered image
    return blurred

def apply_edge_detection(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply edge detection to the image
    edges = cv2.Canny(gray, 100, 200)

    # Add some text to the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(edges, 'Edge Detection Filter', (50, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # Return the filtered image
    return edges
