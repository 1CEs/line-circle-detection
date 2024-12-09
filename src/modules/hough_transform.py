import numpy as np
import cv2

class HoughTransformModule:
    def __init__(self, edge: np.ndarray, original_image: np.ndarray):
        self.__edge = edge
        self.__image = original_image


    def hough_line(self, div: int, threshold: int, minLineLength: int, maxLineGap: int) -> tuple[np.ndarray, int]:
        
        lines = cv2.HoughLinesP(
            self.__edge,
            rho = 1, 
            theta = np.pi/div, 
            threshold=threshold, 
            minLineLength = minLineLength, 
            maxLineGap = maxLineGap
        )
        
        if lines is None:
            print("No lines detected.")
            return self.__image, 0

        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(self.__image, (x1, y1), (x2, y2), (255, 0, 0), 2)
        
        return self.__image, len(lines)
    
    def hough_circle(self) -> tuple[np.ndarray, int]:

        circles = cv2.HoughCircles(
            self.__edge,
            cv2.HOUGH_GRADIENT,
            dp=1.05,
            minDist=20,
            param1=80,
            param2=30,
            minRadius=9,
            maxRadius=70,
        )

        count_circle: int = 0
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for c in circles[0, :]:
                cv2.circle(self.__image, (c[0], c[1]), c[2], (0, 255, 0), 3)
                cv2.circle(self.__image, (c[0], c[1]), 1, (0, 0, 255), 5)
                count_circle += 1
        else:
            print("No circles detected.")

        return self.__image, count_circle
