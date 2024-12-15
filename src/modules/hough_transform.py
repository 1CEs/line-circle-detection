import numpy as np
import cv2

class HoughTransformModule:
    """
    A module for applying Hough Transform algorithms (lines and circles) 
    on an edge-detected image and overlaying the results on the original image.
    """

    def __init__(self, edge: np.ndarray, original_image: np.ndarray):
        """
        Initializes the module with:
        - `edge`: a binary edge-detected image (e.g., from Canny or another edge detector).
        - `original_image`: the original image on which detected shapes will be overlaid.
        """
        self.__edge = edge
        self.__image = original_image

    def hough_line(self, div: int, threshold: int, minLineLength: int, maxLineGap: int) -> tuple[np.ndarray, int]:
        """
        Applies the Hough Line Transform to detect straight lines in the edge-detected image.
        - `div`: the angular resolution of the accumulator in degrees (converted to radians as `np.pi/div`).
        - `threshold`: the minimum number of votes required to consider a line.
        - `minLineLength`: the minimum length of a line to be accepted.
        - `maxLineGap`: the maximum gap between line segments to treat them as a single line.
        - Returns:
            - The original image with detected lines overlaid in red.
            - The count of detected lines.
        """
        # Perform the Hough Line Transform
        lines = cv2.HoughLinesP(
            self.__edge,
            rho=1,  # Distance resolution of the accumulator in pixels
            theta=np.pi / div,  # Angular resolution in radians
            threshold=threshold,  # Number of votes required for a line
            minLineLength=minLineLength,  # Minimum line length to accept
            maxLineGap=maxLineGap  # Maximum gap between segments to link them
        )
        
        # Check if any lines were detected
        if lines is None:
            print("No lines detected.")
            return self.__image, 0

        # Draw each detected line on the original image
        for line in lines:
            x1, y1, x2, y2 = line[0]  # Line endpoints
            cv2.line(self.__image, (x1, y1), (x2, y2), (0, 0, 255), 2)  # Red lines with 2px thickness
        
        return self.__image, len(lines)

    def hough_circle(self) -> tuple[np.ndarray, int]:
        """
        Applies the Hough Circle Transform to detect circles in the edge-detected image.
        - Uses the HOUGH_GRADIENT method for circle detection.
        - Parameters:
            - `dp`: Inverse ratio of the accumulator resolution to the image resolution.
            - `minDist`: Minimum distance between the centers of detected circles.
            - `param1`: Higher threshold for the Canny edge detector.
            - `param2`: Threshold for the center detection in the Hough Circle algorithm.
            - `minRadius`: Minimum circle radius to detect.
            - `maxRadius`: Maximum circle radius to detect.
        - Returns:
            - The original image with detected circles overlaid in red.
            - The count of detected circles.
        """
        # Perform the Hough Circle Transform
        circles = cv2.HoughCircles(
            self.__edge,
            cv2.HOUGH_GRADIENT,  # Detection method
            dp=1.05,  # Accumulator resolution relative to image resolution
            minDist=20,  # Minimum distance between circle centers
            param1=80,  # Higher threshold for Canny edge detection
            param2=30,  # Accumulator threshold for circle detection
            minRadius=9,  # Minimum radius of detected circles
            maxRadius=70,  # Maximum radius of detected circles
        )

        count_circle: int = 0  # Circle counter

        # Check if any circles were detected
        if circles is not None:
            circles = np.uint16(np.around(circles))  # Round circle parameters to integers
            for c in circles[0, :]:
                cv2.circle(self.__image, (c[0], c[1]), c[2], (0, 0, 255), 3)  # Draw the outer circle
                cv2.circle(self.__image, (c[0], c[1]), 1, (0, 0, 255), 5)  # Draw the center
                count_circle += 1
        else:
            print("No circles detected.")

        return self.__image, count_circle
