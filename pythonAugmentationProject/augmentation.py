import cv2


class Augmentation:
    def __init__(self, image, annotations, labels):
        self.image = image
        self.annotations = annotations
        self.labels = labels

    def yolobbox2bbox(self, x, y, w, h, c):
        x1, y1 = x - w / 2, y - h / 2
        x2, y2 = x + w / 2, y + h / 2
        return [x1, y1, x2, y2, c]

    def xywh2xyxy(self, annotations):
        print("convert xywh to xyxy")
        new_coords = []
        for d in annotations:
            x = d[1]
            y = d[2]
            w = d[3]
            h = d[4]
            c = d[0]
            print(x, y, w, h, c)
            results = self.yolobbox2bbox(x, y, w, h, c)
            print(results)
            new_coords.append(results)

        return new_coords

    def putText(self, labels):
        y0, dy = 50, 24
        for i, line in enumerate(labels.split('\n')):
            y = y0 + i * dy
            cv2.putText(self.im, line, (50, y), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 12, 144), 2)

    def getFrame(self):
        return self.image



