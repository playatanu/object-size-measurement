import cv2
import numpy as np
from object_detector import HomogeneousBgDetector

from utils import distance, getScaleRatio

ORANGE_COLOR = (0, 100, 255)
BLUE_COLOR = (255, 0, 0)
RED_COLOR = (0, 0, 255)
GREEN_COLOR = (0, 255, 0)
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

detector = HomogeneousBgDetector()

def sizeMeasure(image,ref_object_size):
    contours = detector.detect_objects(image)

    # Ref Object Distance to Scale Ratio
    ref_object = contours[0]
    rect = cv2.minAreaRect(ref_object)

    (x, y), (w, h), angle = rect

    bbox = np.int32(cv2.boxPoints(rect))

    scale = getScaleRatio(ref_object, ref_object_size)

    cv2.polylines(image, [bbox], True, BLACK_COLOR, 2)
    cv2.putText(image, 'ref 2x2' , (int(x-15), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.45, WHITE_COLOR, 1)

    for c in contours[1:]:
        
            rect = cv2.minAreaRect(c)
            bbox = np.int32(cv2.boxPoints(rect))
            
            (x, y), (w, h), angle = rect
            p1, p2, p3, p4 = bbox
            
            cv2.circle(image, (int(x), int(y)), 8, WHITE_COLOR, -1)
            
            cv2.circle(image, (int(x), int(y)), 3, BLUE_COLOR, -1)
            
            for p in bbox:
                cv2.circle(image, (p), 5, BLUE_COLOR, -1)

            cv2.polylines(image, [bbox], True, WHITE_COLOR, 2)



            width = distance(p3, p2)/scale
            height = distance(p1, p2)/scale

            text = f'{width:.2f} x {height :.2f} cm'
            
            x1, y1 = p1

            cv2.putText(image, text , (x1 + 10, y1 - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.45, BLACK_COLOR, 2)
            
    return image