<<<<<<< HEAD
import cv2 as cv

img =cv.imread('photos/cat.webp')
cv.imshow('cat', img)

# Averaging
average = cv.blur(img,(7,7))
cv.imshow('Average Blur', average)

# Gaussian Blur(more natural blur)
gauss = cv.GaussianBlur(img,(7,7),0)
cv.imshow('Gaussian Blur', gauss)

# Median bluring(effective in noise reduc)
median = cv.medianBlur(img,3)
cv.imshow('Median Blur', median)

# Bilateral
bilateral =cv.bilateralFilter(img, 5,15,15)
cv.imshow('Bilateral',bilateral)



=======
import cv2 as cv

img =cv.imread('photos/cat.webp')
cv.imshow('cat', img)

# Averaging
average = cv.blur(img,(7,7))
cv.imshow('Average Blur', average)

# Gaussian Blur(more natural blur)
gauss = cv.GaussianBlur(img,(7,7),0)
cv.imshow('Gaussian Blur', gauss)

# Median bluring(effective in noise reduc)
median = cv.medianBlur(img,3)
cv.imshow('Median Blur', median)

# Bilateral
bilateral =cv.bilateralFilter(img, 5,15,15)
cv.imshow('Bilateral',bilateral)



>>>>>>> 9ab2db15c57917c987b2559b4751b47ba8bc2691
cv.waitKey(0)