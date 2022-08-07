
import cv2
import matplotlib.pyplot as plt
import os
import glob
import numpy as np
import copy
save_train_path = "./train2017"
save_val_path = "./val2017"
os.makedirs("./train2017", exist_ok=True)
os.makedirs("./val2017", exist_ok=True)
#movie_parent_path = './movie_paper'
#movie_file_path = sorted(glob.glob(os.path.join(movie_parent_path, "*.MP4")))

movie_path = sorted(glob.glob("./movie/*.MP4"))

for path in movie_path:
    cap = cv2.VideoCapture(path)
    i = 0
    train_cnt = 0
    val_cnt = 0
    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        if i % 48 == 0:
            filename = "{base}_{number:05}_val.png".format(base=os.path.splitext(os.path.basename(path))[0], number=val_cnt)
            frame = cv2.resize(frame, (640, 640))
            cv2.imwrite(os.path.join(save_val_path, filename), frame)
            val_cnt += 1
            print(i)
            i += 1
            continue
        if i % 18 == 0:
            filename = "{base}_{number:05}_train.png".format(base=os.path.splitext(os.path.basename(path))[0], number=train_cnt)
            frame = cv2.resize(frame, (640, 640))
            cv2.imwrite(os.path.join(save_train_path, filename), frame)
            train_cnt += 1
        i += 1    
        
        
    cap.release()