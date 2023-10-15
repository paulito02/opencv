import cv2 as cv
import numpy as np

img = cv.imread('pictures/bulbasaur.jpg')
cv.imshow('bulbasaur', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRAY', gray)

#laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('lap_image', lap)

#sobel
sobelx = cv.Sobel(gray,cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray,cv.CV_64F, 0,1)
# combining two sobel using bitwise or
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('sobel X', sobelx)
cv.imshow('sobel Y', sobely)
cv.imshow('combined_sobel', combined_sobel)

#canny
canny = cv.Canny(gray, 150, 150)
cv.imshow('canny_image', canny)

cv.waitKey(0)