import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import glob
import copy
import pandas as pd

#　矩形をマウスにより描画する
ind = 0
path = sorted(glob.glob(os.path.join("./val2017", "*.png")))
#img_path = "GX010100_00000.jpg"
def make_label(img_path):
    
    drawing = False
    ix,iy = -1,-1
    cols = ["x0", "y0", "x1", "y1"]
    dataframe = pd.DataFrame(columns=cols)

    def draw_rectangle(event,x,y,flags,param):
        global ix,iy,drawing, ind
        
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            ix,iy = x,y


        #elif event == cv2.EVENT_MOUSEMOVE:
            #if drawing == True:
                #cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),2)

        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            
            record = []
            record.append(ix)
            record.append(iy)
            record.append(x)
            record.append(y)
            dataframe.loc[ind] = record
            ind += 1
            
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),1)
            # cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)


    img = cv2.imread(img_path)
    #img = cv2.resize(img, dsize=(600,600))

    
    cv2.namedWindow('my_drawing',cv2.WINDOW_NORMAL )
    cv2.setMouseCallback('my_drawing',draw_rectangle, ind)
    while True: 
        cv2.imshow('my_drawing',img)
        if cv2.waitKey(1) & 0xff == ord("q"):
            break
    cv2.destroyAllWindows()
    return dataframe



for img_path in path:
    labelname = os.path.basename(img_path).split(".")[0] + ".csv"
    print(labelname)
    dataframe = make_label(img_path)
    file_path = os.path.join("./rec-val", labelname)
    dataframe.to_csv(file_path)
    
    ind = 0
    


