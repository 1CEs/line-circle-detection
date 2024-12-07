import numpy as np
import cv2

class HoughTransformModule:
    def __init__(self, edge: np.ndarray, original_image: np.ndarray):
        if edge is None or original_image is None:
            raise ValueError("Edge-detected image and original image cannot be None.")
        if edge.shape != original_image.shape[:2]:
            raise ValueError("Edge image and original image dimensions must match.")
        
        self.__edge = edge
        self.__image = original_image

    def hough_line(self, div: int, threshold: int) -> tuple[np.ndarray, int]:

        lines = cv2.HoughLinesP(self.__edge, rho = 1, theta = 1*np.pi/div, threshold=threshold, minLineLength = 50, maxLineGap = 10)
        
        if lines is None:
            print("No lines detected.")
            return self.__image, 0

        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(self.__image, (x1, y1), (x2, y2), (255, 0, 0), 2)
        
        return self.__image, len(lines)
