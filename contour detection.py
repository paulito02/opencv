import cv2 as cv
import numpy as np


img = cv.imread('pictures/bulbasaur.jpg')
cv.imshow('bulbassaur', img)

blank= np.zeros((500,500,3), dtype='uint8')
cv.imshow('blanked', blank)

#to convert the img color first
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#blurring the img reduce the amount of contour found
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blurred img', blur)

#to get the edges in the image
canny = cv.Canny(blur, 125, 175)
cv.imshow('canny edges', canny)

#to determine the contours
contours, hierachies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found')

cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow('contours Drawn', blank)

cv.imshow('contours drawn', blank)


cv.waitKey(0)