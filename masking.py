import cv2 as cv
import numpy as np


img = cv.imread('pictures/bulbasaur.jpg')
cv.imshow('bulbassaur', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank image', blank)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100,255, -1)
cv.imshow('masked', mask)

masked = cv.bitwise_and(img,img, mask=mask)
cv.imshow('masked_image', masked)


cv.waitKey(0)