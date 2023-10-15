import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('pictures/bulbasaur.jpg')

cv.imshow('bulbasaur', img)

# BGR to grayScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)


# BGR to HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

#BGR to LAB
LAB = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', LAB)

cv.waitKey(0)

plt.imshow(img)
plt.show()