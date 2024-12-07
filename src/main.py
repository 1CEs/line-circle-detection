import cv2
from modules.edge_detection import EdgeDetectionModule
from modules.hough_transform import HoughTransformModule
from modules.display_module import DisplayModule
import matplotlib.pyplot as plt
import numpy as np

def main():
    original = cv2.imread('./images/line.jpg', cv2.IMREAD_COLOR)
    grayscale = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

    edge_detector = EdgeDetectionModule(grayscale)
    edges = edge_detector.canny()

    hough_transform = HoughTransformModule(edges, original.copy())
    result_image, line_count = hough_transform.hough_line(255, 85)

    display = DisplayModule((
        "Original Image", 
        "Grayscale Image", 
        "Edge Detected Image", 
        f"Hough Line Image: {line_count} Lines"
    ), (original, grayscale, edges, result_image))

    display.show()

if __name__ == "__main__":
    main()