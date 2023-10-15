import cv2 as cv

img = cv.imread('pictures/bulbasaur.jpg')
cv.imshow('bulbasaur', img)
def rescaleFrame(frame, Scale=0.75):
    width = int(frame.shape[1] * Scale)
    height = int(frame.shape[0] * Scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
# reading a image
resized_image = rescaleFrame(img)
cv.imshow('image', resized_image)

# video
cv.waitKey(0)