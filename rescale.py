from logging import captureWarnings
import cv2 as cv

img = cv.imread('photos/cat.webp')

cv.imshow('cat', img)


# def rescaleFrame(frame, scale=0.75):
#     width = int(frame.shape[1] * scale)
#     height = int(frame.shape[0] * scale) 

#     dimensions = (width, height)
    
#     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# resized_image = rescaleFrame(img)
# cv.imshow('Image', resized_image)
# def changeRes(width,height):
    
    #Reading videos
 capture = cv.VideoCapture('videos/baby.mp4')

while True:
     isTrue, frame  =captureWarnings .read()

     frame_resized = rescaleFrame(frame,scale=0.3)

     cv.imshow('videos', frame)
     cv.imshow('video Resized', frame_resized  )

     if cv.waitKey(20) & 0xFF==('d'):
        break

capture.release()
cv.destroyWindow()


cv.waitKey(0)