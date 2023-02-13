import cv2 as cv

img = cv.imread('Photos/cat.webp')

cv.imshow('cat', img)

#converting  to grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

 # Blur 
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

# Edge cascade
canny = cv.Canny( img, 125,175)
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('dilated', dilated)

# Erroding
eroded = cv.erode(dilated, (3,3),iterations=1)
cv.imshow('eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)


# crapping
cropped = img[50:200,100:200]
cv.imshow('Cropped', cropped)
cv.waitKey(0)
