import cv2 as cv

img = cv.imread('pictures/bulbasaur.jpg ')
cv.imshow('bulbasaur', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#simple threshold
threshold, thresh = cv.threshold(gray,225, 255, cv.THRESH_BINARY)
cv.imshow('simple thresh', thresh)

#inverse
threshold, thresh_inv = cv.threshold(gray,225, 255, cv.THRESH_BINARY_INV)
cv.imshow('simple thresh_inv', thresh_inv )

#adaptives threshold
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11,3)
cv.imshow('adaptive thresholding', adaptive_thresh)

cv.waitKey(0)