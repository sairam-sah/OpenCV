import cv2 as cv

img = cv.imread('Photos/cat.webp')

cv.imshow('cat', img)

#converting  to grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# # Blur 
# blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)

cv.waitKey(0)
