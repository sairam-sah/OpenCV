import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank',blank)

# img = cv.imread('photos/cat.webp')
# cv.imshow('cat', img)

#1. point the image a certain color
# blank[200:250,300:400] =0,255,0
# cv.imshow('Green', blank)

 #2.draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[1]//2),(0,0,255),thickness=cv.FILLED)
cv.imshow('Rectangle',blank)

# 3.draw a circle
cv.circle(blank, (blank.shape[1]//2,blank.shape[1]//2),30, (0,255,0),thickness=3)
cv .imshow('Circle',blank)
# 4.draw line

cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[1]//2), (255,255,255),thickness=3)
cv.imshow('line',blank)

#5. text on image
cv.puttext(blank,'Hello',(255,255),cv.FRONT_HERSHEY_TRIPLEX, 1.0,(0,255,0), 2 )
cv.imshow('Text',blank)
cv.waitKey(0)