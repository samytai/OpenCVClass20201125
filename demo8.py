import cv2
capture=cv2.VideoCapture(0)
while True:
    returnValue,frame=capture.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("this is me", gray)
    if cv2.waitKey(1) & 0xFF==ord('q'): ##為了怕型態換轉問題...
        break
    pass
capture.release()