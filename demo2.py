import cv2
import matplotlib
from matplotlib import pyplot as plt

matplotlib.rcParams['image.cmap']='gray'
IMAGE1='images/bg1.jpg'
image1=cv2.imread(IMAGE1)
# print(f"iamge dim={image1.shape}")
# plt.title("default, but wrong rgb channel")
# plt.imshow(image1)
# plt.show()
#
# image2=image1[::-1,:,::-1]
# plt.title("Using [::-1,:,::-1]")
# plt.imshow(image2)
# plt.show()
#
# image3=image1[:,::-1,::-1]
# plt.title("Using [:,::-1,::-1]")
# plt.imshow(image3)
# plt.show()
#
# plt.figure(figsize=[20,9])
# plt.subplot(131)
# plt.title("Blue channel")
# plt.imshow(image1[:,:,0])
# plt.subplot(132)
# plt.title("Green channel")
# plt.imshow(image1[:,:,1])
# plt.subplot(133)
# plt.title("Red channel")
# plt.imshow(image1[:,:,2])
# plt.show()
#
# b,g,r=cv2.split(image1)
# plt.figure(figsize=[20,9])
# plt.subplot(131)
# plt.title("Blue channel")
# plt.imshow(b)
# plt.subplot(132)
# plt.title("Green channel")
# plt.imshow(g)
# plt.subplot(133)
# plt.title("Red channel")
# plt.imshow(r)
# plt.show()


result=cv2.split(image1)
plt.imshow(result[0])
plt.show()