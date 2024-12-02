class ImageModule:
    
    def __init__(self) -> None:
        self.__byte_image: bytearray = None

    def load(self, image_path: str) -> None:
        with open(image_path, 'rb') as file:
            self.__byte_image = file.read()

    def transform(self) -> None:
        rgb_img: list = self.__to_rgb()
        print(rgb_img)
        pass

    def __to_rgb(self) -> list:
        byte: bytearray = self.get_byte_image()
        width, height = self.get_dimensions()
        
        pixels: list = []
        actual_data_length = len(byte)
        
        for y in range(height):
            row: list = []
            for x in range(width):
                idx = y * width * 3 + x * 3
                
                # Add boundary checks
                if idx + 2 < actual_data_length:
                    r = byte[idx] if idx < actual_data_length else 0
                    g = byte[idx + 1] if idx + 1 < actual_data_length else 0
                    b = byte[idx + 2] if idx + 2 < actual_data_length else 0
                    
                    row.append((r, g, b))
                else:
                    break
            
            # Only append non-empty rows
            if row:
                pixels.append(row)
        
        return pixels

    def __to_grayscale(self) -> None:
        pass

    def get_dimensions(self) -> tuple[int, int]:
        byte: bytearray = self.get_byte_image()
        if byte[:2] != b'\xFF\xD8':
            raise ValueError("Not a valid JPEG file.")

        i = 2
        while i < len(byte):
            if byte[i] != 0xFF:
                raise ValueError("Invalid marker found in JPEG.")
            
            marker = byte[i + 1]
            length = int.from_bytes(byte[i + 2:i + 4], 'big')
            if 0xC0 <= marker <= 0xC3:
                height = int.from_bytes(byte[i + 5:i + 7], 'big')
                width = int.from_bytes(byte[i + 7:i + 9], 'big')
                return width, height
            
            i += 2 + length

        raise ValueError("SOF0 marker not found. Invalid or corrupted JPEG.")

    def get_byte_image(self) -> bytearray:
        return self.__byte_image
