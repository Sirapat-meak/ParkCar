import cv2 as cv
import pickle
import cvzone
import numpy as np

cap=cv.VideoCapture("carPark.mp4")

with open("example_image.png","rb")as f:
        poslist=pickle.load(f)

w,h=107,48

def checkParkingSpace(imgPro):
    for pos in poslist:
        x,y=pos
        
        imgcrop=imgPro[y:y+h,x:x+w]
        #cv.imshow(str(x*y),imgcrop)
        count=cv.countNonZero(imgcrop)
        cvzone.putTextRect(img,str(count),(x,y+h-3),scale=1,thickness=2,offset=0,colorR=(0,0,255))
        if count<900:
             color=(0,255,0)
             tickness=5
        else:
             color=(0,0,255)
             tickness=2
while True:
    if cap.get(cv.CAP_PROP_POS_FRAMES)==cap.get(cv.CAP_PROP_FRAME_COUNT):
        cap.set(cv.CAP_PROP_POS_FRAMES,0)

    success,img=cap.read()
    imgGray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    imgBlur=cv.GaussianBlur(imgGray,(3,3),1)
    imgTh=cv.adaptiveThreshold(imgBlur,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,25,16)

    imgMedian=cv.medianBlur(imgTh,5)
    kernel=np.ones((3,3),np.uint8)
    imgDi=cv.dilate(imgMedian,kernel,iterations=1)

    checkParkingSpace(imgDi)
    
    cv.imshow("Image",img)
    cv.waitKey(1)