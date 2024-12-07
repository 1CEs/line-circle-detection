import cv2
from modules.edge_detection import EdgeDetectionModule
from modules.hough_transform import HoughTransformModule
from modules.display_module import DisplayModule

def main() -> None:
    display = DisplayModule()
    for i in range(1, 4):
        original = cv2.imread(f'./images/line/#{i}.jpg', cv2.IMREAD_COLOR)
        grayscale = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

        edge_detector = EdgeDetectionModule(grayscale)
        edges = edge_detector.canny()

        hough_transform = HoughTransformModule(edges, original.copy())
        result_image, line_count = hough_transform.hough_line(255, 85)

        display.load((
            "Original Image", 
            "Grayscale Image", 
            "Edge Detected Image", 
            f"Hough Line Image: {line_count} Lines"
        ), (original, grayscale, edges, result_image), i)

    display.show()

if __name__ == "__main__":
    main()