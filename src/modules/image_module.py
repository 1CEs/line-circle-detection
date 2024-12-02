class ImageModule:
    
    def __init__(self) -> None:
        self.__byte_image: bytearray = None

    def load(self, image_path: str) -> None:
        with open(image_path, 'rb') as file:
            self.__byte_image = file.read()

    def get_byte_image(self) -> bytearray:
        return self.__byte_image
