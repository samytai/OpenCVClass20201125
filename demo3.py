import cv2
import matplotlib
from matplotlib import pyplot as plt
matplotlib.rcParams['image.cmap']='gray'
IMAGE1='images/number_zero.jpg'
image1=cv2.imread(IMAGE1, 1)
# print(type(image1),image1.shape)
# plt.imshow(image1)
# plt.show()
# cv2.imshow("from opencv", image1)
# print(image1.dtype)
# print(image1[0,0])
plt.figure(figsize=[14,6])
image1[0,0]=(255,0,0)
image1[1,1]=(0,255,0)
image1[2,2]=(0,0,255)
plt.subplot(1,4,1)
plt.imshow(image1[:,:,0])
plt.title("image1[:,:,0]")
plt.subplot(1,4,2)
plt.imshow(image1[:,:,1])
plt.title("image1[:,:,1]")
plt.subplot(1,4,3)
plt.imshow(image1[:,:,2])
plt.title("image1[:,:,2]")
plt.subplot(1,4,4)
plt.imshow(image1[:,:,::-1])
plt.title("image1[:,:,::-1]")
plt.show()
