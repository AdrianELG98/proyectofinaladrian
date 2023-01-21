import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from flask import Flask
app = Flask(_name_)

@app.route("/")
def main():
    #Aqui va su código


   img = cv.imread('RX.jpg')

   mask = np.zeros(img.shape[:2],np.uint8)
   bgdModel = np.zeros((1,65),np.float64)
   fgdModel = np.zeros((1,65),np.float64)
   rect = (92,84,227,229)
   cv.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv.GC_INIT_WITH_RECT)
   mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
   img = img*mask2[:,:,np.newaxis]
   titles = ['Original Image']
   images = [img]
   for i in range(1):
      plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
      plt.title(titles[i])
      plt.xticks([]),plt.yticks([])

   plt.show()
return img