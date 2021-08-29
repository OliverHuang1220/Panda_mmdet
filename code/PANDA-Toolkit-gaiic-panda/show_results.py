import cv2 as cv
import os
import matplotlib.pyplot as plt
import json
test_image = '/home1/huangqiangHD/dataset/PANDA/image_test/'
test_annos='person_bbox_test_A.json'
test_results='3_13_det_results.json'

# image = cv.imread(test_image_path)
# left_top = (19134, 5670)
# right_bottom = (19134+349, 5670+891)
# cv.rectangle(image, left_top, right_bottom, (0, 255, 0), 3)

with open(test_annos) as f:
    test_annos = json.load(f)

img_paths = []
img_ids = []
for root, dirs, files in os.walk(test_image):
    for f in files:
        img_path = os.path.join(root, f)
        img_paths.append(img_path)
        img_key = '{}/{}'.format(img_path.split('/')[-2], img_path.split('/')[-1])
        #print(img_key)
        if img_key not in test_annos:
             print('img key error')
             raise InterruptedError
        img_id = test_annos[img_key]['image id']
        img_ids.append(img_id)

count=0
img=cv.imread(img_paths[0])
for results in test_results:
    if results["image_id"] == img_ids[0] :
        count+=1
print(count)