import cv2
import matplotlib.pyplot as plt

IMAGE1='images/bg1.jpg'
orginalImage=cv2.imread(IMAGE1, -1)
cv2.ellipse(orginalImage,(400,225),(200,80),0,0,360,
            (250,0,0),thickness=3,lineType=cv2.LINE_AA)
cv2.ellipse(orginalImage,(400,225),(80,200),0,90,180,
            (0,250,0),thickness=3,lineType=cv2.LINE_AA)
cv2.ellipse(orginalImage,(400,225),(140,140),0,180,360,
            (0,0,250),thickness=3,lineType=cv2.LINE_AA)
plt.imshow(orginalImage[:,:,::-1])
plt.title("origianl figure")
plt.show()