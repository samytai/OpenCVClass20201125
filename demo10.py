import cv2
import matplotlib.pyplot as plt
import math
from PIL import ImageFont, ImageDraw, Image
import numpy as np

IMAGE1 = 'images/bg1.jpg'
orginalImage = cv2.imread(IMAGE1, -1)
image_copy=orginalImage.copy() ###建立複本
#center=[0,0]
#bbox=[0,0]
def drawCircle(action,x,y,flags,userdata):
    global center

    if action==cv2.EVENT_LBUTTONDOWN:
        center = (x, y)
        #pass
        print("left button down at {}, {} ".format(x,y))
        cv2.circle(orginalImage,center,1,(250,0,0),6,cv2.LINE_AA)

    elif action==cv2.EVENT_LBUTTONUP:
        print("left button up at {}, {} ".format(x,y))
        bbox=(x,y)
        radius=math.sqrt(math.pow(center[0]-bbox[0],2)+math.pow(center[1]-bbox[1],2))
        cv2.circle(orginalImage,center,int(radius),(0,250,250),2,cv2.LINE_AA)


myWindow = "main Window"
cv2.namedWindow(myWindow)
cv2.setMouseCallback(myWindow, drawCircle)
FONT_PATH='fonts/NotoSerifCJKtc-Regular.otf'
font=ImageFont.truetype(FONT_PATH, 36)


k = 0  ##keyboard 事件
while k != 27:
    cv2.imshow(myWindow, orginalImage)
    img_pil = Image.fromarray(orginalImage)
    draw = ImageDraw.Draw(img_pil)
    draw.text((10,60),"我是中文.ㄅㄆㄇㄈ①②③④⑤⑥.",font=font, fill=(250,255,255,255))
    orginalImage=np.array(img_pil)
    # cv2.putText(orginalImage, "left click, and drag", (50, 50),
    #             cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
    k = cv2.waitKey(20)
    if k==ord('c'):
        orginalImage=image_copy.copy()
cv2.destroyAllWindows()  ##關閉視窗...
