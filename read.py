import cv2 as cv

img = cv.imread('pictures/bulbasaur.jpg')

cv.imshow('bulbassaur', img)

cv.waitKey(0)