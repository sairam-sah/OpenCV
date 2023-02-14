import cv2 as cv
import matplotlib.pyplot as plt
 
img = cv.imread('photos/cat.webp')
cv.imshow('cat', img)


# plt.imshow(img)
# plt.show()


# bgr to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# bgr to HSV(hue saturation value)
hsv =cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# bgr to L*a*b
lab =cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)
 
# bgr to rgb
rgb =cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR', hsv_bgr)


plt.imshow(rgb)
plt.show()



cv.waitKey(0)