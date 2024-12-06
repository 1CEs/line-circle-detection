import cv2
from modules.edge_detection import EdgeDetectionModule
from modules.hough_transform import HoughTransformModule

def main():
    original = cv2.imread('./images/line.jpg', cv2.IMREAD_COLOR)
    grayscale = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

    edge_detector = EdgeDetectionModule(grayscale)
    edges = edge_detector.canny()
    threshold = edge_detector.get_threshold()

    hough_transform = HoughTransformModule(edges, original.copy())
    result_image, line_count = hough_transform.hough_line(threshold)

    cv2.imshow(f"Detected Lines: {line_count}", result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()