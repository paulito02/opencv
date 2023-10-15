import cv2 as cv
import numpy as np

img = cv.imread('pictures/bulbasaur.jpg')

cv.imshow('bulbasaur', img)

#translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    #1 signifies the width and 0 signifies the height
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

#-x ---> left
#-y --> up
# x --> right
# y --> down
translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

cv.waitKey(0)

           #rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 90)
cv.imshow('rotated_image', rotated)


# flipping
flip= cv.flip(img, 1)
cv.imshow('flipped img', flip)

# crooping
cropped = img[200:400,300:400]
cv.imshow('croopped img', cropped)

cv.waitKey(0)