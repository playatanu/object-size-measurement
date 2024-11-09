import cv2
import numpy as np

def distance(p1, p2):
    return np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def getScaleRatio(object_countours, object_width):
    rect = cv2.minAreaRect(object_countours)
    
    bbox = np.int32(cv2.boxPoints(rect))
    
    p1, p2, p3, p4 = bbox

    width_in_pixel = distance(p3, p2)
    
    scale = width_in_pixel / object_width
    
    return scale