import cv2 as cv
import pickle

#green=(0,255,0)
#red=(255,0,0)
w,h=107,48
try:
    with open("CarparkPos","rb")as f:
        poslist=pickle.load(f)
except:
    poslist=[]
poslist=[]

def mouseClick(event,x,y,flags,params):
    if event==cv.EVENT_LBUTTONDOWN:
        poslist.append((x,y))
    if event==cv.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(poslist):
            x1,y1=pos
            if x1<x<x1+w and y1<y<y1+h:
                poslist.pop(i)
    with open("CarparkPos","wb")as f:
        pickle.dump(poslist,f)

while True:   
    img=cv.imread("carimage.png")
    for pos in poslist:
        cv.rectangle(img,pos,(pos[0]+w,pos[1]+h),(0,255,0),2)

    cv.imshow("Image",img)
    cv.setMouseCallback("Image",mouseClick)
    cv.waitKey(1)
