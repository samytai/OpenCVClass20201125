import cv2, matplotlib.pyplot as plt, matplotlib
IMAGE_PATH1='images/number_zero.jpg'
image1=cv2.imread(IMAGE_PATH1,0)
#print(image1)
print(type(image1))
print(image1.dtype)
print(image1[0][0])
print(image1[0][0],type(image1[0][0]))
print(image1.shape) ##先算直再算橫的...
image1[0][0]=255
image1[0][1]=255
image1[1][0]=255
image1[1][1]=255
#cv2.imshow("This is the image",image1)
# plt.imshow(image1)
# plt.show()
image1[0:6, 0:4]=128
matplotlib.rcParams['figure.figsize']=(6.0,6.0)
#matplotlib.rcParams['image.cmap']='gray'
plt.imshow(image1)
plt.colorbar()
plt.show()