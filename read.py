import cv2 as cv

from rescale import rescaleFrame

img = cv.imread('videos/baby.mp4')

cv.imshow('baby', img)




   #Reading videos
capture = cv. VideoCapture('videos/baby.mp4')

while True:
     isTrue, frame  =capture .read()

     frame_resized = rescaleFrame(frame)

     cv.imshow('videos', frame)
     cv.imshow('Video Resized', frame_resized)

     if cv.waitKey(20) & 0xFF==('d'):
        break

capture.release()
cv.destroyWindow()
cv.waitKey(0)




