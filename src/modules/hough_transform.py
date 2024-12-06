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

    def hough_line(self, t: int) -> tuple[np.ndarray, int]:
        """
        Apply standard Hough Line Transform.
        :param t: Threshold for Hough Transform.
        :return: Image with detected lines drawn.
        """
        lines = cv2.HoughLines(self.__edge, 1, np.pi / 180, t)
        if lines is None:
            print("No lines detected.")
            return self.__image

        for line in lines:
            rho, theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            cv2.line(self.__image, (x1, y1), (x2, y2), (0, 0, 255), 2)
        
        return self.__image, len(lines)

    def hough_line_probabilistic(self, t: int, min_line_length: int, max_line_gap: int) -> np.ndarray:
        """
        Apply Probabilistic Hough Line Transform.
        :param t: Threshold for Hough Transform.
        :param min_line_length: Minimum length of a line to be accepted.
        :param max_line_gap: Maximum allowed gap between line segments to treat them as a single line.
        :return: Image with detected line segments drawn.
        """
        lines = cv2.HoughLinesP(self.__edge, 1, np.pi / 180, t, minLineLength=min_line_length, maxLineGap=max_line_gap)
        if lines is None:
            print("No lines detected.")
            return self.__image

        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(self.__image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        return self.__image
