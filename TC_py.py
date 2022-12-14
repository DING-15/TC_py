import cv2
from PIL import Image
import numpy as np
import sys

RANGE_0=0.8
RANGE_1=30
RANGE_2=70
RANGE_3=100
img = Image.open('C://...//foo.jpg').convert('L')
img.save('C://...//foo.jpg')
ary = np.array(img)
np.set_printoptions(threshold=sys.maxsize)
shape=ary.shape
result=np.zeros(shape)
#j:255=x:100 --> x=100j/255
for i in range(0, shape[0]):
    for j in range(0, shape[1]):
        x=(100*ary[i][j])/255
        result[i][j]=x
shape2=result.shape
#backtorgb = cv2.cvtColor(ary,cv2.COLOR_GRAY2BGRA)
backtorgb = cv2.cvtColor(ary,cv2.COLOR_GRAY2BGR)
color_final=Image.fromarray(backtorgb)
for i in range(0,shape2[0]):
    for j in range(0,shape2[1]):
        if result[i][j] < RANGE_0:
            #color_final.putpixel( (i,j), (135,206,235))
            backtorgb[i][j]=[135,206,235]
        elif result[i][j] < RANGE_1 and result[i][j] > RANGE_0:
            #color_final.putpixel( (i,j), (135,206,235))
            #backtorgb[i][j]=[255, 0, 0, 0.5]
            backtorgb[i][j]=[150,75,0]
        elif result[i][j] < RANGE_2 and result[i][j] > RANGE_1:
            #color_final.putpixel( (i,j), (135,206,235))
            #backtorgb[i][j]=[255, 0, 0, 0.5]
            backtorgb[i][j]=[255,255,0]
        else:
            backtorgb[i][j]=[34,139,34]
            
color_final=Image.fromarray(backtorgb)
color_final.save('C://...//foo.jpg')
print(result)

