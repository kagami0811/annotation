
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import glob
import copy
import pandas as pd
##rectangle　矩形を表示し、クラス名を入力する

img_paths = sorted(glob.glob(os.path.join("./val2017", "*.png")))
from_label_path = "rec-val"
save_path = "./label-val"
def make_label(image_path):
    image = cv2.imread(image_path)
    #simage = cv2.resize(image, (600, 600))
    ind = 0
    filename = "{base}.csv".format(base=os.path.splitext(os.path.basename(image_path))[0])
    rectanglefile = os.path.join(from_label_path, filename)
    label_path = os.path.join(save_path, filename)
    print(filename)
    new_cols = ["class", "x", "y", "w", "h"]
    new_dataframe = pd.DataFrame(columns=new_cols)
    rectangle_dataframe = pd.read_csv(rectanglefile)
    for ind in range(len(rectangle_dataframe)):
        _, x0, y0, x1, y1 = rectangle_dataframe.iloc[ind]
        copyimg = copy.deepcopy(image)
        show_img = cv2.rectangle(copyimg,(x0,y0),(x1, y1),(0,255,0),1)
        show_img = cv2.cvtColor(show_img,cv2.COLOR_BGR2RGB)
        plt.imshow(show_img)
        plt.show()
        class_name = input()
        if class_name == "":
            continue
        record = [class_name, x0, y0, x1-x0 ,y1-y0]  
        new_dataframe.loc[ind] = record
        ind += 1
    new_dataframe.to_csv(label_path)

for img_path in img_paths[:]:
    make_label(image_path=img_path)
