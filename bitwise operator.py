import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')
rectangle= cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(),  (200,200), 200, 255, -1)
cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)


# bitwise_and :  it places two images on each other and returns the interception back
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('btwise_and', bitwise_and)

#bitwise_or: combine two images placed them on each other and returns both the interception and non interception parts
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('bitwise_or', bitwise_or)

#bitwise xor: finds the non intercepting region
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('bitwise_xor', bitwise_xor)

#bitwise_not: inverts the color
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('bitwise_not', bitwise_not)


cv.waitKey(0)