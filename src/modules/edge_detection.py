import cv2
import numpy as np

class EdgeDetectionModule:
    
    def __init__(self, grayscale: np.ndarray) -> None:
        if len(grayscale.shape) != 2:
            raise ValueError("Input image must be grayscale.")
        
        self.__gs_img = grayscale

    def __len__(self):
        return self.__data

    def sobel(self) -> np.ndarray:
        self.__gs_img = cv2.GaussianBlur(self.__gs_img, (3, 3), 0)
        grad_x = cv2.Sobel(self.__gs_img, cv2.CV_64F, 1, 0, ksize=3)
        grad_y = cv2.Sobel(self.__gs_img, cv2.CV_64F, 0, 1, ksize=3)

        sobel_magnitude = np.sqrt(grad_x ** 2 + grad_y ** 2)
        sobel_magnitude = np.uint8(255 * sobel_magnitude / np.max(sobel_magnitude))

        _, sobel_threshold = cv2.threshold(sobel_magnitude, 90, 150, cv2.THRESH_BINARY)

        return sobel_threshold

    def canny(self) -> np.ndarray:
        self.__gs_img = cv2.GaussianBlur(self.__gs_img, (9, 9), 0)
        return cv2.Canny(self.__gs_img, 50, 120)

    def prewitt(self) -> np.ndarray:
        self.__gs_img = cv2.GaussianBlur(self.__gs_img, (3, 3), 0)
        kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
        kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
        img_prewittx = cv2.filter2D(self.__gs_img, -1, kernelx)
        img_prewitty = cv2.filter2D(self.__gs_img, -1, kernely)
        return img_prewittx + img_prewitty

    def robert(self) -> np.ndarray:
        self.__gs_img = cv2.GaussianBlur(self.__gs_img, (7, 7), 0)
        kernel_x = np.array([[1, 0], [0, -1]])
        kernel_y = np.array([[0, 1], [-1, 0]])

        gradient_x = cv2.filter2D(self.__gs_img, cv2.CV_64F, kernel_x)
        gradient_y = cv2.filter2D(self.__gs_img, cv2.CV_64F, kernel_y)

        edge_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
        edge_magnitude = np.uint8(np.clip(edge_magnitude, 0, 255))
        return edge_magnitude

