import cv2
from modules.edge_detection import EdgeDetectionModule
from modules.hough_transform import HoughTransformModule
from modules.display_module import DisplayModule

def run() -> None:
    ed_parameter: dict = {
        "canny": [(50, 120, "line"), (120, 120, "circle")],
        "sobel": [((3, 3), 90, 150, "line"), ((7, 7), 69, 255, "circle")],
        "robert": [((7, 7), 124, 255, "line"), ((5, 5), 30, 255, "circle")],
        "prewitt": [((3, 3), 35, 255), ((9, 9), 45, 255)],
    }  # Parameters for each method

    hl_parameter = {
        "canny": (255, 85, 90, 10), 
        "sobel": (220, 100, 50, 10), 
        "robert": (360, 150, 100, 5), 
        "prewitt": (220, 50, 85, 5)
    }

    for case in [ "circle"]:
        for method_name in dir(EdgeDetectionModule):
            if method_name.startswith("__"): 
                continue

            method = getattr(EdgeDetectionModule, method_name)
            if callable(method):
                display = DisplayModule(f"{method_name.capitalize()} Method")
                for i in range(1, 4):
                    original = cv2.imread(f'./images/{case}/#{i}.jpg', cv2.IMREAD_COLOR)
                    grayscale = cv2.imread(f'./images/{case}/#{i}.jpg', cv2.IMREAD_GRAYSCALE)

                    edge_detector = EdgeDetectionModule(grayscale)
                    
                    parameters = ed_parameter.get(method_name.lower(), [])
                    
                    edges = method(edge_detector, *parameters[0 if case == "line" else 1])

                    hough_transform = HoughTransformModule(edges, original.copy())
                    result_image, count = hough_transform.hough_line(*hl_parameter.get(method_name.lower(), [])) if case == "line" else hough_transform.hough_circle()
                    display.load((
                        "Original Image", 
                        "Grayscale Image", 
                        "Edge Detected Image", 
                        f"Hough {case.capitalize()} Image: {count} {case.capitalize()}s"
                    ), (original, grayscale, edges, result_image), i)

                display.show()

def main() -> None:
    run()

if __name__ == "__main__":
    main()

