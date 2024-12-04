from PIL import Image
from PIL.Image import Image as ImageType

class ImageModule:
    save_filename: str = ''

    def __init__(self, image_path: str) -> None:
        self.__image_path: str = image_path
        self.__instance_image: ImageType = None

        self.save_filename = image_path

    def load(self) -> None:
        self.__instance_image: ImageType = Image.open(self.__image_path).convert('L')

    def show(self) -> None:
        self.__instance_image.show(self.__image_path)    
        
    def save(self, output_path: str = f"./dist/{save_filename}") -> None:
        self.__instance_image.save(output_path)
