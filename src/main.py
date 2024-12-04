from modules.image_module import ImageModule

def main():
    img = ImageModule('./images/line.jpg')
    img.load()
    img.save('./images/output/line.jpg')
    

if __name__ == "__main__":
    main()