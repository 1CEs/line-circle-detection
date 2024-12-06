import cv2
import numpy as np

class EdgeDetectionModule:
    def __init__(self, grayscale) -> None:
        self.__gs_img = cv2.GaussianBlur(grayscale, (3, 3), 0)

    def sobel(self) -> None:
        grad_x = cv2.Sobel(self.__gs_img, cv2.CV_64F, 1, 0, ksize= 3)
        grad_y = cv2.Sobel(self.__gs_img, cv2.CV_64F, 0, 1, ksize= 3)

        abs_grad_x = cv2.convertScaleAbs(grad_x)
        abs_grad_y = cv2.convertScaleAbs(grad_y)

        grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

        cv2.imshow('Sobel Image', grad)
        cv2.waitKey()

    def canny(self) -> None:
        canny = cv2.Canny(self.__gs_img, 0, 255)
        cv2.imshow('Canny Image', canny)
        cv2.waitKey()

    def prewitt(self) -> None:
        kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
        kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
        img_prewittx = cv2.filter2D(self.__gs_img, -1, kernelx)
        img_prewitty = cv2.filter2D(self.__gs_img, -1, kernely)
        cv2.imshow('Prewitt Image', img_prewittx + img_prewitty)
        cv2.waitKey()

    def robert(self) -> None:
        kernel_x = np.array([[1, 0],
                            [0, -1]])
        kernel_y = np.array([[0, 1],
                            [-1, 0]])

        gradient_x = cv2.filter2D(self.__gs_img, cv2.CV_64F, kernel_x)
        gradient_y = cv2.filter2D(self.__gs_img, cv2.CV_64F, kernel_y)

        edge_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
        edge_magnitude = np.uint8(np.clip(edge_magnitude, 0, 255))
        cv2.imshow('Robert Image', edge_magnitude)
        cv2.waitKey()
