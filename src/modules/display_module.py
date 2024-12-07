import matplotlib.pyplot as plt
import matplotlib.axes as axes
import numpy as np
import cv2

class DisplayModule:
    def __init__(self, name: str, figsize: tuple[int] = (19, 8)) -> None:
        self.__fig, self.__axs = plt.subplots(3, 4, figsize=figsize)
        self.__figure_setup(name)

    def __figure_setup(self, name) -> None:
        self.__fig.canvas.manager.set_window_title(name)

        self.__fig.set_figwidth(10)
        self.__fig.set_figheight(5)
        

    def load(self, titles: tuple[str] | str, images: tuple[np.ndarray] | np.ndarray, row: int) -> None:
        for i in range(len(images)):
            self.__axs[row-1, i].set_title(titles[i])
            self.__axs[row-1, i].imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
            self.__axs[row-1, i].axis('off')
            

    def show(self) -> None:
        plt.show()
