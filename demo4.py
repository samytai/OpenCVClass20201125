import cv2
import matplotlib.pyplot as plt
IMAGE1='images/transparency1.png'
image1=cv2.imread(IMAGE1,1)
image1=cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
plt.figure(figsize=[14,6])
plt.subplot(1,5,1)
plt.title("original figure")
plt.imshow(image1)

plt.subplot(1,5,2)
plt.title("mage1[:,:,0]")
plt.imshow(image1[:,:,0])

plt.subplot(1,5,3)
plt.title("image1[:,:,1]")
plt.imshow(image1[:,:,1])

plt.subplot(1,5,4)
plt.title("image1[:,:,2]")
plt.imshow(image1[:,:,2])

plt.subplot(1,5,5)
plt.title("image1[:,:,-1]")
plt.imshow(image1[:,:,-1])
plt.show()

# image2=cv2.imread(IMAGE1,0)
# image3=cv2.imread(IMAGE1,1)
# image4=cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
# image5=cv2.cvtColor(image3, cv2.COLOR_BGR2RGB)
# image6=image1[:,:,2]
# image7=image1[:,:,-1]
# print(f"read as -1,shape={image1.shape}")
# print(f"read as 0,shape={image2.shape}")
# print(f"read as 1,shape={image3.shape}")
# print(f"correct with alpha (-1=keep),shape={image3.shape}")
# plt.figure(figsize=[14,6])
# plt.subplot(1,4,1)
# plt.title("read as -1")
# plt.imshow(image1)
#
# plt.subplot(1,4,2)
# plt.title("read as 0")
# plt.imshow(image2)
#
# plt.subplot(1,4,3)
# plt.title("read as 1")
# plt.imshow(image3)
#
# plt.subplot(1,4,4)
# plt.title("image1, cv2.COLOR_BGR2RGB")
# plt.imshow(image4)
# plt.show()
#
# plt.figure(figsize=[14,6])
# plt.subplot(1,4,1)
# plt.title("original figure")
# plt.imshow(image1)
#
# plt.subplot(1,4,2)
# plt.title("(image3, cv2.COLOR_BGR2RGB)")
# plt.imshow(image5)
#
# plt.subplot(1,4,3)
# plt.title("image1[:,:,2]")
# plt.imshow(image6)
#
# plt.subplot(1,4,4)
# plt.title("image1[:,:,-1]")
# plt.imshow(image7)
# plt.show()