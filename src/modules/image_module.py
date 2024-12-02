class ImageModule:
    
    def __init__(self) -> None:
        self.byte_image: bytearray = None
        self.image = None

    def load(self, image_path: str) -> None:
        with open(image_path, 'rb') as file:
            self.image = file

