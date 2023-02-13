import cv2 as cv
import numpy as np

img = cv.imread('photos/cat.webp')
cv.imshow('cat', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank',blank)

gray =cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur =cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)



# canny = cv.Canny(img,123,150)
# cv.imshow('Canny',canny)


ret, thresh =cv.threshold(gray, 125,255,cv.THRESH_BINARY)
cv.imshow('thresn',thresh)

contours, hierarchies =cv.findContours(thresh, cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} countour(s) found!')



cv.drawCountours(blank, contours, -1, (0,0,255),2)
cv.imshow('Countours Drawn', blank)
cv.waitKey(0)