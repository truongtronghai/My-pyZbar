import pyzbar.pyzbar as zbar
import os,cv2,sys
import numpy as np
import matplotlib.pyplot as plt

os.chdir("C:\\Projects\\python\\imgProcessing")
img = cv2.imread(os.getcwd() +'\\imgs\\code5.jpg')

barcodes = zbar.decode(img)

if len(barcodes) :
    for barcode in barcodes:
        print(barcode.data)
        x1 = barcode.rect.left
        y1 = barcode.rect.top
        x2 = barcode.rect.left + barcode.rect.width
        y2 = barcode.rect.top + barcode.rect.height
        img = cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
else:
    print("No code detected")
    sys.exit()

cv2.imshow("Result",img)
cv2.waitKey(0)
cv2.destroyAllWindows()