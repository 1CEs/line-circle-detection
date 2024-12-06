import cv2
from modules.edge_detection import EdgeDetectionModule

def main():
    img = cv2.imread('./images/line.jpg', cv2.IMREAD_COLOR)

    gs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ed = EdgeDetectionModule(gs)
    ed.robert()

if __name__ == "__main__":
    main()