'''
Chuong trinh nay chay khong dung. Can xem lai
'''
import pyzbar.pyzbar as zbar
import os,cv2,sys
import numpy as np
import matplotlib.pyplot as plt

os.chdir("C:\\Projects\\python\\imgProcessing")
img = cv2.imread(os.getcwd() +'\\imgs\\code3.jpg')
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gradX = cv2.Sobel(gray_img,ddepth=cv2.CV_64F,dx=1,dy=0,ksize=-1)
#cv2.imshow("gradX",gradX)
gradY = cv2.Sobel(gray_img,ddepth=cv2.CV_64F,dx=0,dy=1,ksize=-1)
#cv2.imshow("gradY",gradY)
# The function subtract calculates: Difference between two arrays, when both input arrays have the same size and the same number of channels:
grad = cv2.subtract(gradY,gradX,dtype=-1)
#cv2.imshow('Subtract',grad)
grad = cv2.convertScaleAbs(grad)
#cv2.imshow('Convert',grad)
grad = cv2.blur(grad,(9,9))
#cv2.imshow('Blurred',grad)
ret, thresh = cv2.threshold(grad,127,255,cv2.THRESH_BINARY)
#cv2.imshow('Threshold',thresh)

kernelSize = np.ones((15,15),np.uint8)

erosion = cv2.erode(thresh,kernelSize)
#cv2.imshow('erosion',erosion)
dilation = cv2.dilate(erosion,kernelSize)
#cv2.imshow('dilation',dilation)

# finding contours of those shapes
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# with each contour, I will check and decide which one is barcode and draw a rectangle for it
i=0
for cnt in contours:
    
    x,y,w,h = cv2.boundingRect(cnt)
        
    roi = img[y:y+h,x:x+w] # region of image, warning the postion of Y and X
    #img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    #cv2.imshow('roi'+str(i),roi)
    #print(roi)
    i += 1
    barcodes = zbar.decode(roi)
    for barcode in barcodes:
        print(i)
        
    '''
    if(len(res)):
        print(res[0].data)
        x1 = res[0].rect.left
        y1 = res[0].rect.top
        x2 = res[0].rect.left + res[0].rect.width
        y2 = res[0].rect.top + res[0].rect.height
        img = cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
    '''

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()