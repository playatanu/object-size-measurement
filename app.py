import os
import cv2
from object_measure import sizeMeasure

folder_path = "images" 
ref_object_size = 2 

files = os.listdir(folder_path)

image_extensions = ['.jpg', '.jpeg', '.png']
image_files = [f for f in files if any(f.lower().endswith(ext) for ext in image_extensions)]

for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    image = cv2.imread(image_path)
    image = cv2.resize(image, (300, 400))
    cv2.imshow(image_file, sizeMeasure(image, ref_object_size))

cv2.waitKey(0)

