from itertools import count
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import glob
import copy
import pandas as pd

os.makedirs("./label-train", exist_ok=True)
os.makedirs("./label-val", exist_ok=True)

parent_path = "./train2017"
images_path = sorted(glob.glob(os.path.join(parent_path, "*.png")))



def make_counters(image, bgrLower, bgrUpper, area_th = 2000):
    img_mask = cv2.inRange(image, bgrLower, bgrUpper)
    img_mask = 255 - img_mask #反転
    #process_image = cv2.bitwise_and(image, image, mask=img_mask)
    #show_image = cv2.cvtColor(process_image, cv2.COLOR_BGR2RGB) 
    counters, hierachy = cv2.findContours(img_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    counters = list(filter(lambda x: cv2.contourArea(x) > area_th, counters))

    return counters


def crip(image_path, counters):
    image = cv2.imread(image_path)
    filename = "{base}.csv".format(base=os.path.splitext(os.path.basename(image_path))[0])
    print(filename)
    label_path = os.path.join("./label-train", filename)
    print(label_path)
    cols = ["class", "x", "y", "w", "h"]
    dataframe = pd.DataFrame(columns=cols)
    ind = 0
    for cnt in counters:
        x,y,w,h = cv2.boundingRect(cnt)
        process_image = copy.deepcopy(image)
        img = cv2.rectangle(process_image,(x,y),(x+w,y+h),(0,255,0),5)
        show_image = cv2.cvtColor(img ,cv2.COLOR_BGR2RGB)
        plt.imshow(show_image)
        plt.show()
        class_name = input()
        if class_name == "":
            continue
        else:  
            record = [class_name, x, y, w ,h]  
            dataframe.loc[ind] = record
            ind += 1
    dataframe.to_csv(label_path)        
      

for image_path in images_path:
    image = cv2.imread(image_path)
    counters = make_counters(image, bgrLower=np.array([90,90 ,90]), bgrUpper=np.array([255, 255, 255]))    
    crip(image_path, counters=counters)



