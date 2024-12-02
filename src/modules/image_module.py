class ImageModule:
    
    def __init__(self) -> None:
        self.__byte_image: bytearray = None

    def load(self, image_path: str) -> None:
        with open(image_path, 'rb') as file:
            self.__byte_image = file.read()

    def get_dimensions(self) -> tuple[int, int]:
        byte: bytearray = self.get_byte_image()
        if byte[:8] != b"\x89PNG\r\n\x1a\n":
            raise ValueError("This image is not .PNG file.")
        
        width: int = int.from_bytes(byte[16:20], 'big')
        height: int = int.from_bytes(byte[20:24], 'big')
        return width, height

    def get_byte_image(self) -> bytearray:
        return self.__byte_image
