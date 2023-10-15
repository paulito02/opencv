import cv2 as cv

img = cv.imread('pictures/bulbasaur.jpg')
cv.imshow('bulbassaur', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# to blur image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

#edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('canny', canny)
#dillating image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('dilated image', dilated)

#eroding
eroded = cv.erode(dilated, (7,7), iterations=1)
cv.imshow('eroded', eroded)



cv.waitKey(0)