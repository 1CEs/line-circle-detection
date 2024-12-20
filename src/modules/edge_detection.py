import cv2
import numpy as np

class EdgeDetectionModule:
    """
    A class for edge detection in grayscale images using various methods such as Sobel, Canny, Prewitt, and Robert.
    """
    
    def __init__(self, grayscale: np.ndarray) -> None:
        """
        Initializes the module with a grayscale image. 
        Ensures the input is a 2D array, representing a grayscale image.
        """
        if len(grayscale.shape) != 2:
            raise ValueError("Input image must be grayscale.")
        
        self.__gs_img = grayscale

    def sobel(self, ksize: tuple[int], t: int, tmax: int, case: str) -> np.ndarray:
        """
        Applies the Sobel edge detection algorithm.
        - Blurs the image to reduce noise using a Gaussian kernel.
        - Calculates gradients in the x and y directions using the Sobel operator.
        - Computes the edge magnitude (either directly or using `cv2.magnitude`) based on the `case`.
        - Applies a threshold to create a binary image of detected edges.
        """
        self.__gs_img = cv2.GaussianBlur(self.__gs_img, ksize, 0)
        grad_x = cv2.Sobel(self.__gs_img, cv2.CV_64F, 1, 0, ksize=3)
        grad_y = cv2.Sobel(self.__gs_img, cv2.CV_64F, 0, 1, ksize=3)
        
        sobel_magnitude: any = None
        
        if case == "line":
            sobel_magnitude = np.sqrt(grad_x ** 2 + grad_y ** 2)
            sobel_magnitude = np.uint8(255 * sobel_magnitude / np.max(sobel_magnitude))
        else:
            sobel_magnitude = cv2.magnitude(grad_x, grad_y).astype(np.uint8)

        _, sobel_threshold = cv2.threshold(sobel_magnitude, t, tmax, cv2.THRESH_BINARY)

        return sobel_threshold

    def canny(self, t1: int, t2: int, case: str) -> np.ndarray:
        """
        Applies the Canny edge detection algorithm.
        - Blurs the image to reduce noise using a Gaussian kernel.
        - Detects edges using the Canny algorithm, with thresholds `t1` and `t2`.
        - Returns the binary edge-detected image.
        """
        self.__gs_img = cv2.GaussianBlur(self.__gs_img, (9, 9), 0)
        return cv2.Canny(self.__gs_img, t1, t2, apertureSize=3)

    def prewitt(self, ksize: tuple[int], t: int, tmax: int) -> np.ndarray:
        """
        Applies the Prewitt edge detection algorithm.
        - Blurs the image using a Gaussian kernel.
        - Applies the Prewitt kernel in the x and y directions.
        - Calculates the edge magnitude using the gradients.
        - Applies a threshold to produce a binary edge-detected image.
        """
        self.__gs_img = cv2.GaussianBlur(self.__gs_img, ksize, 0)
        kernelx = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
        kernely = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

        img_prewittx = cv2.filter2D(self.__gs_img, -1, kernelx)
        img_prewitty = cv2.filter2D(self.__gs_img, -1, kernely)

        grad_x = np.float32(img_prewittx)
        grad_y = np.float32(img_prewitty)

        edge_magnitude = cv2.magnitude(grad_x, grad_y)

        _, prewitt_threshold = cv2.threshold(edge_magnitude, t, tmax, cv2.THRESH_BINARY)

        return np.uint8(prewitt_threshold)

    def robert(self, ksize: tuple[int], t: int, tmax: int, case: str) -> np.ndarray:
        """
        Applies the Robert Cross edge detection algorithm.
        - Blurs the image using a Gaussian kernel.
        - Applies the Robert Cross operator to calculate gradients in the x and y directions.
        - Computes the edge magnitude (based on the `case`).
        - Adjusts dimensions and scales the output for `circle` case.
        - Applies a threshold to generate a binary image of detected edges.
        """
        self.__gs_img = cv2.GaussianBlur(self.__gs_img, ksize, 0)
        self.__gs_img = np.float32(self.__gs_img) if case == "circle" else self.__gs_img

        kernel_x = np.array([[1, 0], [0, -1]], dtype=np.float32)
        kernel_y = np.array([[0, 1], [-1, 0]], dtype=np.float32)

        gradient_x = cv2.filter2D(self.__gs_img, -1 if case == "line" else cv2.CV_32F, kernel_x)
        gradient_y = cv2.filter2D(self.__gs_img, -1 if case == "line" else cv2.CV_32F, kernel_y)

        edge_magnitude: any = None
        if case == "circle":
            min_rows = min(gradient_x.shape[0], gradient_y.shape[0])
            min_cols = min(gradient_x.shape[1], gradient_y.shape[1])
            gradient_x = gradient_x[:min_rows, :min_cols]
            gradient_y = gradient_y[:min_rows, :min_cols]

            edge_magnitude = cv2.magnitude(gradient_x, gradient_y)
            edge_magnitude = np.uint8(np.clip(edge_magnitude, 0, 255))
        else: 
            edge_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
            edge_magnitude = np.uint8(255 * edge_magnitude / np.max(edge_magnitude))

        _, robert_threshold = cv2.threshold(edge_magnitude, t, tmax, cv2.THRESH_BINARY)

        return robert_threshold
