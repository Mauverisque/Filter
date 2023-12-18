import cv2
import numpy as np
import os

pic_names = ['maxwell', 'monalisa', 'colorful']

curdir = os.getcwd()

for pic in pic_names:
    image = cv2.imread('in/' + pic + '.jpg')
    
    kernel = np.array([[0, 0, 0, 1, 0, 0, 0],
                       [0, 0, 0, -2, 0, 0, 0],
                       [0, 0, 0, 2, 0, 0, 0],
                       [1, -2, 2, -3, 2, -2, 1],
                       [0, 0, 0, 2, 0, 0, 0],
                       [0, 0, 0, -2, 0, 0, 0],
                       [0, 0, 0, 1, 0, 0, 0]])

    img_filtered = cv2.filter2D(src = image, ddepth = -1, kernel = kernel)

    os.chdir('out') 

    cv2.imwrite(pic + '.jpg', img_filtered)