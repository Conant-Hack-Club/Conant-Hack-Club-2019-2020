import cv2
import numpy as np

#READ IMAGE

img = cv2.imread('cougar.jpg')
#plotting the image
cv2.imshow("cougar", img)
cv2.waitKey(0)

#WRITE IMAGE

cv2.imwrite('savedimage.jpg',img)

#GRAYSCALE

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
cv2.waitKey(0)

#RESIZE

resized = cv2.resize(img,(100,70))
cv2.imshow("resized", resized)
cv2.waitKey(0)

#ROTATE

rows,cols = img.shape[:2]
#(col/2,rows/2) is the center of rotation for the image
# M is the cordinates of the center
M = cv2.getRotationMatrix2D((cols/2,rows/2),180,1)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow("rotated", dst)
cv2.waitKey(0)


#THRESHOLD


ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
cv2.imshow("threshold", thresh)
cv2.waitKey(0)

#EDGE DETECTION

edges = cv2.Canny(img,100,200)
cv2.imshow("edges", edges)
cv2.waitKey(0)

#PORTION

portion = img[0:300, 0:300]

cv2.imshow("portion", portion)
cv2.waitKey(0)

#OBJECT TRACKING

# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(img,img, mask= mask)

cv2.imshow("OBJECT TRACKING", res)
cv2.waitKey(0)

#face detection

#load the classifiers downloaded
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
#read the image and convert to grayscale format
img = cv2.imread('brady.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#calculate coordinates
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    #draw bounding boxes around detected features
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
#plot the image
cv2.imshow("facial detection", img)
cv2.waitKey(0)
