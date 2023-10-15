import cv2 as cv
import numpy as np

#to draw shapes
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('blank', blank)

# to paint a particular shape or portion of the entire shape
blank[200:300, 400:500]=0,0,225
cv.imshow('red', blank)
# drawing rectangle
#drawing a rectangular shape
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('blank', blank)

cv.rectangle(blank, (0,0), (250,250), (0,250,0), thickness=6)
cv.imshow('rectangle', blank)

cv.waitKey(0)