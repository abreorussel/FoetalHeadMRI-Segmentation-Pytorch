import os

from utils.options import *



def train_pipeline(root_path):
    opt , args = parse_options(root_path, is_train=True)
    opt['root_path'] = root_path




if __name__ == '__main__':
    root_path = os.path.abspath(os.path.join(__file__, os.path.pardir, os.path.pardir))
    train_pipeline(root_path)