import os
import numpy as np
import cv2 
from glob import glob
import json
from pathlib import Path


o=0
for root, dirs, files in os.walk('C:/Users/ozanc/OneDrive/Masaüstü/project/videos/'):
    for file in files:

        print(file)       
        pathss = "videos"+"/"+ file 
        print(pathss)

        cap = cv2.VideoCapture(pathss)

        i=0
        
        path = "C:/Users/ozanc/OneDrive/Masaüstü/project/frames/video" + str(o)+ "/"
        os.makedirs(path)
        print(path)
        
        print(o)
        name = "frames/" + "video" + str(o) + "/"
        
        asd = "frames/video"+ str(o) + "/"
        print(asd)
        while(cap.isOpened()):
            
            
            flag , frame = cap.read()
            if flag== False:
                break
            patha = asd  + file + str(i)+'.jpg'
            cv2.imwrite(patha , frame)
            
            i+=1
        o+=1
        cap.release()
        cv2.destroyAllWindows()


