import cv2
import numpy as np
import matplotlib.pyplot as plt

def fun(A,B,C,D, path):
	
	img=cv2.imread( path ,-1)
	size=img.shape
	rect= np.zeros((4,2), dtype='float32')
	rect[0]= [0,0]
	rect[1]= [size[1],0]
	rect[2]= [size[1],size[0]]
	rect[3]= [0,size[0]]
	
	pts2= np.float32([A,B,C,D])
	
	M= cv2.getPerspectiveTransform(rect,pts2)
	dst=cv2.warpPerspective(img,M,(size[0],size[1]))
	
	plt.subplot(121),plt.imshow(img),plt.title('Input')
	plt.subplot(122),plt.imshow(dst),plt.title('Output')
	plt.show()
		
	return;

		
	
fun([28,387],[389,390],[368,52],[56,65], 'C:/Users/lavi goyal/Desktop/rabbit.jpg')  # parameters (Co-ordinates, path)
	