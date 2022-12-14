import os
from MulticoreTSNE import MulticoreTSNE as TSNE
from matplotlib import pyplot as plt
from tools import utils
import torch
import torch.functional as F
import numpy as np

# os.system('python3.6 train.py --config_name configs/train/train_supcon_resnet50_cifar100_stage1.yml')
os.system('python3.6 swa.py --config_name configs/train/swa_supcon_resnet50_cifar100_stage1.yml')
# os.system('python3.6 train.py --config_name configs/train/train_supcon_resnet50_cifar100_stage2.yml')
# os.system('python3.6 swa.py --config_name configs/train/swa_supcon_resnet50_cifar100_stage2.yml')
