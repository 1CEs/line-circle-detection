import matplotlib.pyplot as plt
import numpy as np
import cv2

class DisplayModule:
    def __init__(self, titles: tuple[str] | str, images: tuple[np.ndarray] | np.ndarray) -> None:
        plt.figure(figsize=(15, 8))
        self.__titles = titles
        self.__images = images

    def __preparing(self, pos: int, title: str, img: np.ndarray) -> None:
        plt.subplot(1, len(self.__images), pos)
        plt.title(title)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    def show(self) -> None:
        for i in range(len(self.__images)):
            self.__preparing(i + 1, self.__titles[i], self.__images[i])

        plt.show()
