import os

from yolox.exp.yolox_base import Exp as MyExp


class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 0.33
        self.width = 0.50
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]

        # Define yourself dataset path
        self.data_dir = "datasets/tongari"
        self.train_ann = "instances_train.json"
        self.val_ann = "instances_val.json"
        

        self.num_classes = 1
        
        #self.multiscale_range = 0
        self.max_epoch = 500
        self.data_num_workers = 2
        self.eval_interval = 10
        self.print_interval=10
        
        



