import cv2 as cv
capture = cv.VideoCapture('video/shaba.mp4')

#while True:
#    isTrue, frame = capture.read()
    # to show each frame of the video
 #   cv.imshow('video', frame)
# to stop the video from playing
#    if cv.waitKey(20) & 0xFF==ord('d'):
#        break

#capture.release()
#cv.destroyAllwindows()

# rescaling the size of the frame of the picture or video
def rescaleFrame(frame, Scale=0.75):
    width = int(frame.shape[1] * Scale)
    height = int(frame.shape[0] * Scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
##setting the resolution of the video (work for only live videos
#def changeResolution(width, height):
   # capture.set(3, width)
    #capture,set(4, height)
# reading a video
capture = cv.VideoCapture('video/shaba.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized= rescaleFrame(frame)
    # to show each frame of the video
    cv.imshow('video', frame)
    cv.imshow('video Resized', frame_resized)
# to stop the video from playing
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllwindows()

