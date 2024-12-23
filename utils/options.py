import argparse
import yaml
import random
from pprint import pprint

from utils.helper import *


def parse_options(path , is_train = True):
    parser = argparse.ArgumentParser() 
    parser.add_argument('-opt', type=str, help='Path to the YAML file')
    args = parser.parse_args()

    # converting the yaml file to dictionary
    with open(args.opt, mode='r') as file:
        opt = yaml.load(file, Loader=yaml.FullLoader)
        pprint(opt)

    seed = opt.get('manual_seed')
    if seed is None:
        seed = random.randint(1, 10000)
        opt['manual_seed'] = seed
    set_random_seed(seed)

    opt['is_train'] = is_train

    