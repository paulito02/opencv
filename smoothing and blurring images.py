import cv2 as cv

img = cv.imread('pictures/bulbasaur.jpg')
cv.imshow('bulbassaur', img)

#averaging
average = cv.blur(img, (3,3))
cv.imshow('average blur', average)

#gaussian blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussain blur', gauss)

#median blur
median = cv.medianBlur(img, 3)
cv.imshow('median blur', median)

#bilateral(most effective)
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('bilateral blur', bilateral)

cv.waitKey(0)