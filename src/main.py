from modules.image_module import ImageModule

def main():
    im = ImageModule()
    im.load('./images/line.jpg')
    w, h = im.get_dimensions()
    print(f"{w} {h}")

if __name__ == "__main__":
    main()