import cv2
from modules.edge_detection import EdgeDetectionModule
from modules.hough_transform import HoughTransformModule
from modules.display_module import DisplayModule

def main() -> None:
    
    for method_name in dir(EdgeDetectionModule):

        if method_name.startswith("__"): continue

        method = getattr(EdgeDetectionModule, method_name)

        if callable(method):
            display = DisplayModule(f"{method_name.capitalize()} Method")
            for i in range(1, 4):
                original = cv2.imread(f'./images/circle/#{i}.jpg', cv2.IMREAD_COLOR)
                grayscale = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

                edge_detector = EdgeDetectionModule(grayscale)
                edges = method(edge_detector)

                hough_transform = HoughTransformModule(edges, original.copy())
                result_image = hough_transform.hough_circle()

                display.load((
                    "Original Image", 
                    "Grayscale Image", 
                    "Edge Detected Image", 
                    f"Hough Circle Image"
                ), (original, grayscale, edges, result_image), i)

            display.show()

if __name__ == "__main__":
    main()
