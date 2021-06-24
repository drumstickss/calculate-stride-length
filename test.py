import os, json
import pandas as pd
import math as m 


i=0
for root, dirs, files in os.walk('C:/Users/ozanc/OneDrive/Masaüstü/project/jsons/'):
    for folder in dirs :  
        print(folder)
    
        path_to_json = "jsons/" + folder + "/"
        print(path_to_json)
        json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
        #print(json_files)
        diff_ys = []
        diff_xs = []
        for index, js in enumerate(json_files):
            with open(os.path.join(path_to_json, js)) as json_file:
                json_text = json.load(json_file)
                a= json_text['people'][0]["pose_keypoints_2d"]
                x1 = a[33]
                y1 = a[34]
                x2 = a[42]
                y2 = a[43]

                if y1 > y2  :
                    dif_y = y1 - y2
                    diff_ys.append(dif_y)
                elif y2 > y1 :
                    dif_y = y2 - y1
                    diff_ys.append(dif_y)

                if x1 > x2 and x1 != 0 and x2 !=0  :
                    dif_x = x1 - x2
                    diff_xs.append(dif_x)
                elif x2 > x1 and x1 != 0 and x2 !=0:
                    dif_x = x2 - x1
                    diff_xs.append(dif_x)

        #print(diff_ys)
        #print(diff_xs)
        used_diff = min(diff_ys) 
        idx_of_min =diff_ys.index(used_diff)       
        #print(idx_of_min)
        #print(diff_xs[idx_of_min])
        used_xs=diff_xs[idx_of_min]

        pixel_factor = 351 # Shows how many pixels are in 1 meter.

        stride_length = 100 * used_xs / pixel_factor 
        print("....................................for the video" + str(i) +"..............................................")
        result =  m.sqrt(pow((used_xs),2) + pow((used_diff),2))
        lastResult = result * 100 / pixel_factor
        print(stride_length)
        c = max(diff_xs)
        print(c)        
        z = idx_of_x =diff_xs.index(c) 
        print(z)
        print( lastResult)

        
        i+=1

   



   