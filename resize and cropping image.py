import cv2 as cv

img = cv.imread('pictures/bulbasaur.jpg')
resize = cv.resize(img, (150,150))
cv.imshow('resized', resize)


#cropping
cropped = img[50:100, 200:400]
cv.imshow('cropped', cropped)
cv.waitKey(0)