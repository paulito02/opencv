import  cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img = cv.imread('pictures/bulbasaur.jpg')
cv.imshow('bulbassaur', img)


blank= np.zeros((img.shape[:2]), dtype='uint8')


#to convert the img color first
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

circle = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100,255, -1)
#cv.imshow("circle", circle)

mask = cv.bitwise_and(img, img, mask=circle)
cv.imshow('mask', mask)
#GRay scale Histogram
#gray_hist = cv.calcHist([gray],[0], mask , [255], [0,246])

#plt.figure()
#plt.title('Grayscale histogram')
#plt.xlabel('Bins')
#plt.ylabel('# of pixels')
#plt.plot(gray_hist)
#plt.xlim([0,256])
#plt.show()

#color hist
plt.figure()
plt.title('colors histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

colors =('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])


plt.show()


cv.waitKey(0)