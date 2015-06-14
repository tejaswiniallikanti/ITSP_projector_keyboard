import numpy as np
import cv2
import time
import os
start_time=time.time()
cap = cv2.VideoCapture(2)
cap2 = cv2.VideoCapture(1)
'''def intial_image(cap,i):
     while time.time()<2:
        imwrite('first_image.jpg',cap)


def back_subtract(cap):'''

def Video_filter(cap,i ):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if(i==2):# bottom camera
        ch = frame.shape
        pts1 = np.float32([[109,199],[638,201],[148,270],[589,273]])
        pts2 = np.float32([[0,0],[484,0],[0,162],[484,162]])
        M = cv2.getPerspectiveTransform(pts1,pts2)
        frame = cv2.warpPerspective(frame,M,(484,162))
    elif(i==1):#t0p camera
        ch = frame.shape
        pts1 = np.float32([[4,201],[634,224],[66,220],[501,233]])
        pts2 = np.float32([[0,0],[484,0],[0,15],[484,15]])
        M = cv2.getPerspectiveTransform(pts1,pts2)
        frame= cv2.warpPerspective(frame,M,(484,15))
        cv2.imwrite('frame.jpg',frame)
        #from PIL import Image
        #frame = Image.open('frame.jpg').transpose(Image.FLIP_LEFT_RIGHT)
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([0, 30, 60])
    upper_blue = np.array([20, 150, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
   
    kernel = np.ones((7,7),np.uint8)
    erosion = cv2.dilate(mask,kernel,iterations = 2)
    dilation = cv2.erode(erosion,kernel,iterations = 2)
    ret3,th3 = cv2.threshold(dilation,100,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #cv2.imshow("masked%d"%i,th3)
    edges = cv2.Canny(th3,150,255)
    cv2.imshow('edge%d'%i,edges)
    cv2.imshow('colour%d'%i,frame)
    return edges

def first_white(img,x_lower,x_upper,y_upper,tf):
    i=x_lower
    j=0
    img[j,i] = 0
    while(j<y_upper):
        i=x_lower
        while(i<x_upper):
            if(img[j,i]<1):
                i=i+1
            else:
                break
        if(img[j,i]<1):
            j=j+1
        else:
            break
    if tf==True:
        return i
    else:
        return j


def touched(img):
    
    if first_white(img,0,483,14,True) >482 :
        return False

    elif first_white(img,0,483,14,True)>-1 :
        return True
    else:
        return False

def touched_x(img):
    if(touched(img)):
        return first_white(img,0,483,14,True)


#instead of using the lines double times we can write a common code for both of them
def keystroke(a,b):
    if a==404 or b==125:
        pass
    else:
        if b<45:
            if a < 44:
                os.system('xte "key Q"')
            elif a>43 and a <83:
                os.system('xte "key W"')
            elif a>82 and a <123:
                os.system('xte "key E"')
            elif a>123 and a <163:
                os.system('xte "key R"')
            elif a>163 and a <203:
                os.system('xte "key T"')
            elif a>203 and a <243:
                os.system('xte "key Y"')
            elif a>243 and a <283:
                os.system('xte "key U"')
            elif a>283 and a <323:
                os.system('xte "key I"')
            elif a>323 and a <363:
                os.system('xte "key O"')
            elif a>363 and a <403:
                os.system('xte "key P"')
            elif a>402:
                os.system('xte "key BackSpace"')
        elif b>44 and b<84:
            if a<53:
                os.system('xte "key A"')
            elif a>54 and a <94:
                os.system('xte "key S"')
            elif a>94 and a <134:
                os.system('xte "key D"')
            elif a>134 and a <174:
                os.system('xte "key F"')
            elif a>174 and a <214:
                os.system('xte "key G"')
            elif a>214 and a <254:
                os.system('xte "key H"')
            elif a>254 and a <294:
                os.system('xte "key J"')
            elif a>294 and a <334:
                os.system('xte "key K"')
            elif a>334 and a <374:
                os.system('xte "key L"')
            elif a>373:
                os.system('xte "key Return"')
        elif b>84 and b<124:
            if a>43 and a <83:
                os.system('xte "key z"')
            elif a>83 and a <123:
                os.system('xte "key X"')
            elif a>123 and a <163:
                os.system('xte "key C"')
            elif a>163 and a <203:
                os.system('xte "key V"')
            elif a>203 and a <243:
                os.system('xte "key B"')
            elif a>243 and a <283:
                os.system('xte "key N"')
            elif a>283 and a <323:
                os.system('xte "key M"')
            elif a> 443:
                os.system('xte "key Up"')
        elif b>124 :
            if a>123 and a <360:
                os.system('xte "key Space"')
            elif a>360 and a <400:
                os.system('xte "key Left"')
            elif a>400 and a <440:
                os.system('xte "key Right"') 
            elif a>440:
                os.system('xte "key Down"')

        else:
            pass

'''def keystroke(a,b):
    #if a=299
    if a==299:
        pass
    elif b==299:
        pass
    else:
        #print a
        #print b
        #print " "
        if b<45:
            if a < 44:
                print "q"
            if a>43 and a <83:
                print 'w'
            if a>82 and a <123:
                print 'e'
            if a>123 and a <163:
                print 'r'
            if a>163 and a <203:
                print 't'
            if a>203 and a <243:
                print 'y'
            if a>243 and a <283:
                print 'u'
            if a>283 and a <323:
                print 'i'
            if a>323 and a <363:
                print 'o'
            if a>363 and a <403:
                print 'p'
        if b>44 and b<84:
            if a<53:
                print "a"
            if a>54 and a <94:
                print 's'
            if a>94 and a <134:
                print 'd'
            if a>134 and a <174:
                print 'f'
            if a>174 and a <214:
                print 'g'
            if a>214 and a <254:
                print 'h'
            if a>254 and a <294:
                print 'j'
            if a>294 and a <334:
                print 'k'
            if a>334 and a <374:
                print 'l'
        elif b>84 and b<124:
            if a>43 and a <83:
                print 'z'
            if a>83 and a <123:
                print 'x'
            if a>123 and a <163:
                print 'c'
            if a>163 and a <203:
                print 'v'
            if a>203 and a <243:
                print 'b'
            if a>243 and a <283:
                print 'n'
            if a>283 and a <323:
                print 'm'
        else:
            pass'''

while(True):
    #touch = False
    edges_bot=Video_filter(cap,1)
    edges_top=Video_filter(cap2,2)
    if touched(edges_bot):
        keystroke(touched_x(edges_bot)+30,first_white(edges_top,0,483,140,False))
    if cv2.waitKey(1) & 0xFF == ord('1'):
        break
    #end_time=time.time()
    #print end_time-start_time
# When everything done, release the Capture
cap.release()
cv2.destroyAllWindows()




