import matplotlib.pyplot as plt
import matplotlib.axes as axes
import numpy as np
import cv2

class DisplayModule:
    """
    A utility class to display images in a grid layout using Matplotlib.
    Designed to show multiple rows of images with their respective titles.
    """

    def __init__(self, name: str, figsize: tuple[int] = (19, 8)) -> None:
        """
        Initializes the display module.
        - `name`: The name of the window where the images will be displayed.
        - `figsize`: Size of the figure (width, height) in inches.
        - Creates a 3x4 grid of subplots for displaying images.
        """
        self.__fig, self.__axs = plt.subplots(3, 4, figsize=figsize)  # Create a 3x4 grid for displaying images
        self.__figure_setup(name)  # Configure the figure (e.g., window title, dimensions)

    def __figure_setup(self, name: str) -> None:
        """
        Configures the figure setup.
        - Sets the window title of the figure.
        - Adjusts the width and height of the figure.
        """
        self.__fig.canvas.manager.set_window_title(name)  # Set the window title
        self.__fig.set_figwidth(10)  # Set the figure width (adjustable)
        self.__fig.set_figheight(5)  # Set the figure height (adjustable)

    def load(self, titles: tuple[str] | str, images: tuple[np.ndarray] | np.ndarray, row: int) -> None:
        """
        Loads images and their titles into the specified row of the grid.
        - `titles`: A tuple of titles corresponding to the images in the row.
        - `images`: A tuple of images to display in the row.
        - `row`: The row index (1-based) where the images will be placed.
        - Converts images from BGR (OpenCV format) to RGB for display.
        - Removes axes from the subplots for a cleaner look.
        """
        for i in range(len(images)):  # Iterate through the images to display them in the specified row
            self.__axs[row-1, i].set_title(titles[i])  # Set the title for each subplot
            self.__axs[row-1, i].imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))  # Convert BGR to RGB
            self.__axs[row-1, i].axis('off')  # Turn off axes for a cleaner display

    def show(self) -> None:
        """
        Displays the figure with all the loaded images and titles.
        """
        plt.show()  # Show the figure
