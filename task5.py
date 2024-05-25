import cv2
import numpy as np
import requests
from io import BytesIO
from matplotlib import pyplot as plt

def detect_cracks(image_url):
    
    response = requests.get(image_url)
    if response.status_code != 200:
        raise ValueError("Error downloading the image. Check the URL.")
    
    image = np.asarray(bytearray(response.content), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    
    if image is None:
        raise ValueError("Couldn't load image from the URL.")

    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    edges = cv2.Canny(blurred, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    
    min_contour_length = 100 
    filtered_contours = [contour for contour in contours if cv2.arcLength(contour, False) > min_contour_length]

    
    cv2.drawContours(image, filtered_contours, -1, (0, 0, 255), 2)

    
    plt.figure(figsize=(10, 10))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Detected Cracks')
    plt.axis('off')
    plt.show()

image_url = 'https://D:\bridge_imagee.jpg"'  
detect_cracks(image_url)
