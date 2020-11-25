import cv2
import matplotlib.pyplot as plt

IMAGE1 = 'images/bg1.jpg'
orginalImage = cv2.imread(IMAGE1, -1)
# plt.imshow(orginalImage[:,:,::-1])
# plt.title("origianl figure")
# plt.show()
# for i in range(0, 20):
#     cv2.line(orginalImage, (200, 80 + 20 * i), (480, 80 + 10 * i),
#              (255-10*i, 0+10*i, 0), thickness=5, lineType=cv2.LINE_AA)
# plt.imshow(orginalImage[:, :, ::-1])
# plt.title("image with annotate")
# plt.show()

cv2.circle(orginalImage,(250,250),100,(0,255,0),
           thickness=10, lineType=cv2.LINE_AA)
cv2.circle(orginalImage,(250,250),20,(0,0,255),
           thickness=-1, lineType=None)
plt.imshow(orginalImage[:,:,::-1])
plt.title("Circle try")
plt.show()
