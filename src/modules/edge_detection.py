import cv2
import numpy as np

class EdgeDetectionModule:
    
    def __init__(self, grayscale: np.ndarray) -> None:
        if len(grayscale.shape) != 2:
            raise ValueError("Input image must be grayscale.")
        
        self.__gs_img = cv2.GaussianBlur(grayscale, (3, 3), 0)
        self.__threshold, _ = cv2.threshold(self.__gs_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    def sobel(self) -> np.ndarray:
        grad_x = cv2.Sobel(self.__gs_img, cv2.CV_64F, 1, 0, ksize=3)
        grad_y = cv2.Sobel(self.__gs_img, cv2.CV_64F, 0, 1, ksize=3)

        abs_grad_x = cv2.convertScaleAbs(grad_x)
        abs_grad_y = cv2.convertScaleAbs(grad_y)

        grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
        return grad

    def canny(self) -> np.ndarray:
        return cv2.Canny(self.__gs_img, 0, 255)

    def prewitt(self) -> np.ndarray:
        kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
        kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
        img_prewittx = cv2.filter2D(self.__gs_img, -1, kernelx)
        img_prewitty = cv2.filter2D(self.__gs_img, -1, kernely)
        return img_prewittx + img_prewitty

    def robert(self) -> np.ndarray:
        kernel_x = np.array([[1, 0], [0, -1]])
        kernel_y = np.array([[0, 1], [-1, 0]])

        gradient_x = cv2.filter2D(self.__gs_img, cv2.CV_64F, kernel_x)
        gradient_y = cv2.filter2D(self.__gs_img, cv2.CV_64F, kernel_y)

        edge_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
        edge_magnitude = np.uint8(np.clip(edge_magnitude, 0, 255))
        return edge_magnitude

    def get_threshold(self) -> int:
        return int(self.__threshold)
