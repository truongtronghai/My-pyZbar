import pyzbar.pyzbar as zbar
import cv2,sys
import matplotlib.pyplot as plt
import requests,time,winsound

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    sys.exit("Coudl not open the webcam.")

'''
Formating text for showing code on window
'''
# font
font = cv2.FONT_HERSHEY_SIMPLEX
# org
org = (50, 50) # initialize
# fontScale
fontScale = 0.8
# Blue color in BGR
color = (255, 0, 0)
# Line thickness of 2 px
thickness = 2
# text
txt_code = ""
old_txt_code = ""

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame. Exiting ...")
        break

    try:
        gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        barcodes = zbar.decode(gray_frame)

        for barcode in barcodes:
            
            x1 = barcode.rect.left
            y1 = barcode.rect.top
            x2 = barcode.rect.left + barcode.rect.width
            y2 = barcode.rect.top + barcode.rect.height

            org = (x1, y1)
            txt_code = str(barcode.data).split("'")[1] # remove hyphen and redundant characters in result string

            if txt_code == old_txt_code : # xet xem code vua doc co bi trung lan doc truoc hay khong
                continue
            else:
                old_txt_code = txt_code

            frame = cv2.putText(frame, txt_code, org, font, fontScale, color, thickness, cv2.LINE_AA)
            frame = cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)

            print(barcode.data)
            '''
            calling restapi to post data
            
            data = {"name":"barcode","alias":txt_code}
            url = "http://127.0.0.1:9000/restapi/heroes/" # phai co dau / o cuoi dia chi thi moi goi dang POST duoc
            resp = requests.post(url,data)

            if(resp.status_code == 200 or resp.status_code == 201):
                winsound.Beep(440, 500)
                time.sleep(1) # delay 1 second for user change object to detect new code
                break
            '''
        cv2.imshow("Barcode reader (Press Esc to quit program)",frame)

    finally:
        pass

    k = cv2.waitKey(5) & 0xFF
    if k==27:
        cv2.destroyAllWindows()
        break
