import cv2 as cv


img = cv.imread('photos/cat.webp')
cv.imshow('cat',img)


gray =cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Simple Thresholding
threshold, thres = cv.threshold(gray, 150, 255,cv.THRESH_BINARY)
cv.imshoW('Simple threshold',thres)

cv.waitkey(0)