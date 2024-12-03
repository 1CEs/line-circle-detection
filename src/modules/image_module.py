import struct
class ImageModule:
    
    def __init__(self) -> None:
        self.__byte_image: bytearray = None
        self.__width: int = None
        self.__height: int = None

    def load(self, image_path: str) -> None:
        with open(image_path, 'rb') as f:
            self.__byte_image = f.read(24)
            data = self.get_byte_image()
            
            if data[:2] == b'\xff\xd8':
                f.seek(2)
                while True:
                    header = f.read(4)
                    if len(header) < 4:
                        break
                    marker, size = struct.unpack('>HH', header)
                    
                    if marker == 0xFFC0:
                        frame_data = f.read(5) 
                        if len(frame_data) != 5:
                            raise ValueError("Incomplete SOF frame data")
                        
                        precision, height, width = struct.unpack('>BHH', frame_data)
                        self.__width = width
                        self.__height = height
                        return
                    
                    if size < 2:
                        raise ValueError(f"Invalid segment size: {size}")
                    
                    f.seek(size - 2, 1)
                
            elif data[:8] == b'\x89PNG\r\n\x1a\n':
                if len(data) >= 24:
                    width, height = struct.unpack('>II', data[16:24])
                    self.__width = width
                    self.__height = height
                else:
                    raise ValueError("Incomplete PNG header data")
            else:
                raise ValueError("Unsupported or invalid image format")



    def save(self, byte: bytearray, output_path: str):
        if not byte:
            raise ValueError('No byte image to save.')
        
        with open(output_path, 'wb') as file:
            file.write(byte)


    def transform(self) -> None:
        pass

    def get_dimensions(self) -> tuple[int, int]:
        return self.__width, self.__height

    def get_byte_image(self) -> bytearray:
        return self.__byte_image

    def __rgb_to_byte(self, rgb_img: list) -> bytearray:
        pass


    def __byte_to_rgb(self) -> list:
        byte: bytearray = self.get_byte_image()
        w, h = self.get_dimensions()

        

    def __rgb_to_grayscale(self) -> None:
        pass

    
