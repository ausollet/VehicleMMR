import torch
from yolov5.models import yolo
from yolov5.utils import general
import numpy as np

from torch._C import device
from models import *
from utils import *

import os, sys, time, datetime, random
import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from facenet_pytorch import MTCNN, InceptionResnetV1
from torch.autograd import Variable

from PIL import Image
import cv2
# from sort import *
import json
import time

import pickle as pkl
import glob

# In[3]:


repo_path = './yolov5'
model_path='yolov5m'
weights_path='./yolov5/runs/train/exp16/weights/best.pt'
nc = 7
# class_dict = {0: 'Buick', 1: 'Chery', 2: 'Citroen', 3: 'Honda', 4: 'Hyundai', 5: 'Lexus', 6: 'Mazda', 7: 'Peugeot', 8: 'Toyota', 9: 'Volkwagen'}
# class_dict = {0: 'Honda', 1: 'Hyundai', 2: 'Toyota', 3: 'Volkwagen'}
# Top_Car_Brands = {0: 'Suzuki', 1: 'Hyundai', 2: 'Tata', 3: 'Kia', 4: 'Mahindra', 5: 'Toyota', 6: 'Renault', 7: 'Honda', 8: 'MG Motor', 9: 'Skoda', 10: 'Ford', 11: 'Nissan', 12: 'Volkswagen'}
img_size = 640
conf_thres = 0.4
nms_thres = 0.45

model = yolo.Model(cfg='./yolov5/models/yolov5m.yaml', nc=nc)
model.load_state_dict(torch.load(weights_path)['model'].state_dict())

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

model = model.to(device)
model.eval()

# model = torch.hub.load(repo_path, model_path, classes=nc, pretrained=False, autoshape=False, source='local')
# model.load_state_dict(torch.load(weights_path)['model'].state_dict())

# model.conf = conf_thres
# model.iou = nms_thres


# In[4]:


Tensor = torch.cuda.FloatTensor


def detect_image(img, device):
    # scale and pad image
    #     ratio = min(img_size/img.size[0], img_size/img.size[1])
    imw = img_size
    imh = img_size
    img_transforms = transforms.Compose([ transforms.Resize((imh, imw)),
    transforms.Pad((max(int((imh-imw)/2),0), max(int((imw-imh)/2),0), max(int((imh-imw)/2),0), max(int((imw-imh)/2),0)),
        (128,128,128)),
        transforms.ToTensor(),
    ])
    # convert image to Tensor
    image_tensor = img_transforms(img).to(device).float()
    image_tensor = image_tensor.unsqueeze_(0)
    input_img = Variable(image_tensor.type(Tensor))
    # run inference on the model and get detections
    with torch.no_grad():
        pred = model(image_tensor)
        output = general.non_max_suppression(pred[0], conf_thres, nms_thres)
    del  image_tensor, input_img
    return output

model.eval()

img_folder_path = './test/images/'
# img_folder_path = './valid/images/'
# img_folder_path = '../cctv/vehicle_crop/'
# img_folder_path = './data/*/*/'
# img_folder_path = './TrainingData/TrainingData/*/'

for i in glob.glob(img_folder_path+'*.*')[:10]:
    print(i)
    img = Image.open(i, mode='r').convert('RGB')
    # img.show()
    output = detect_image(img, device=device)
    print(output)
