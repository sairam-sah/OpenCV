<<<<<<< HEAD
import cv2 as cv
import numpy as np


img = cv.imread('photos/cat.webp')
cv.imshow('cat',img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image',blank)

# Rectangle
mask= cv.rectangle(blank,(img.shape[1]//2,img.shape[0]//2),(img.shape[1]//2 +100,img.shape[0]//2 +100),255,-1)
cv.imshow('Mask',mask)

# Circle
mask= cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow('Mask',mask)


masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked',masked)




=======
import cv2 as cv
import numpy as np


img = cv.imread('photos/cat.webp')
cv.imshow('cat',img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image',blank)

# Rectangle
mask= cv.rectangle(blank,(img.shape[1]//2,img.shape[0]//2),(img.shape[1]//2 +100,img.shape[0]//2 +100),255,-1)
cv.imshow('Mask',mask)

# Circle
mask= cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow('Mask',mask)


masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked',masked)




>>>>>>> 0cc531a28dd0a342e7733d0ab87797f6fb84b6da
cv.waitKey(0)