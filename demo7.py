import cv2
import matplotlib.pyplot as plt

IMAGE1='images/bg1.jpg'
orginalImage=cv2.imread(IMAGE1, -1)
text1="original image"
text2="我是中文"
cv2.putText(orginalImage,text1,(50,50),cv2.FONT_HERSHEY_SIMPLEX,
            2, (250,0,0), thickness=2, lineType=cv2.LINE_AA)
cv2.putText(orginalImage,text2,(50,200),cv2.FONT_HERSHEY_SIMPLEX,
            2, (0,250,0), thickness=2, lineType=cv2.LINE_AA)
plt.imshow(orginalImage[:,:,::-1])
plt.title("origianl figure")
plt.show()