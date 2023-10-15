import cv2 as cv

img = cv.imread('pictures/paul2.jpg')
cv.imshow('paul', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray person', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
print(f'Number of faces found = {len(faces_rect)}')
for (x,y,w,h) in faces_rect:
   cv.rectangle(img, (x,y), (x+w,Y+h), (0, 255,0), thickness=2)

cv.imshow('detected face',faces_rect)

cv.waitKey(0)
