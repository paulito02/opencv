import cv2 as cv
import numpy as np
# writting a text on a blank shape
blank = np.zeros((500,500,3), dtype='uint8')
cv.putText(blank,'hello how are you?',(50,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255, 0), 2 )
cv.imshow('text', blank)

cv.waitKey(0)