import cv2
import numpy as np
import glob
import os
import json
from collections import OrderedDict
from PIL import Image
import pandas as pd

def make_images(image_path,image_id):
    file_name = os.path.basename(image_path)
    image = OrderedDict()
    image["id"] = image_id
    img = Image.open(image_path)
    width, height = img.size
    image["width"] = width
    image["height"] = height
    print(width, height)
    image["file_name"] = file_name

    return image

#1つのオブジェクトに対するannotationの辞書を作成
#The COCO bounding box format is [top left x position, top left y position, width, height].
def  create_annotations(image_id,category_id, id, bbox):

    annotation = OrderedDict()
    annotation["segmentation"] = ""
    annotation["area"] = bbox[2] * bbox[3]
    annotation["iscrowd"] = 0
    annotation["image_id"] = image_id
    annotation["bbox"] = bbox
    annotation["category_id"] = category_id
    annotation["id"] = id
    return annotation


def create_categories(obj_dict):
    category = []
    for key, val in obj_dict.items():
        dict = OrderedDict()
        dict['id'] = int(val)
        dict['name'] = key
        category.append(dict)
    return category


if __name__  == "__main__":
    dict = OrderedDict()
    image_id  = 0
    id = 0
    json_dict = OrderedDict()
    annotations = []
    images = []

    obj_dict ={"rrrr":1, "yyyy":2, "bbbb":3, "ryry":4, "byby":5, "brbr":6, "byrr":7, "bbrr":8, "yybb":9, "yyrr":10, "rbyy":11, "yrbb":12}

    train_image_parent_path = "./val2017"
    train_label_parent_path = "./label-val"   

    train_images_path = sorted(glob.glob(os.path.join(train_image_parent_path, "*.png")))
    train_labels_path = sorted(glob.glob(os.path.join(train_label_parent_path, "*.csv")))
    #print(len(train_images_path), len(train_labels_path)) # 43, 43

    for image_path, label_path in zip(train_images_path, train_labels_path):
        image_dict = make_images(image_path, image_id)
        images.append(image_dict)
        df = pd.read_csv(label_path)
        for i in range(len(df)):
            unnamed, class_name, x, y, w, h = df.iloc[i]
            bbox = [int(x), int(y), int(w), int(h)]
            if not class_name in obj_dict.keys():
                print(label_path)
                print(class_name)
                print("ann miss")
                exit()
            category_id = int(obj_dict[class_name])
            annotation_dict = create_annotations(image_id, category_id, id, bbox)
            
            annotations.append(annotation_dict)
            id += 1


        image_id += 1    


    category_list = create_categories(obj_dict)    
    json_dict["images"] = images
    json_dict["annotations"] = annotations
    json_dict ["categories"] = category_list
    print(json_dict)
    #jsonファイル
    filename = os.path.join("./annotations","instances_val.json")
    with open(filename, "w") as f:
        
        json.dump(json_dict, f, ensure_ascii=False)
        

    print(image_id)
    print(id)
