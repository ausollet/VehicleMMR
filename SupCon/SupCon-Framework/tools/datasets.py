import torchvision
from PIL import Image
import numpy as np
import random

class SupConDatasetCifar10(torchvision.datasets.CIFAR10):
    def __init__(self, data_dir, train, transform, second_stage):
        super().__init__(root=data_dir, train=train, download=True, transform=transform)

        self.second_stage = second_stage
        self.transform = transform

    def __getitem__(self, idx):
        image, label = self.data[idx], self.targets[idx]

        # leave this part unchanged. The reason for this implementation - in the first stage of training
        # you have TwoCropTransform(actual transforms), so you have to call it by self.transform(img)
        # on the other hard, in the second stage of training there is no wrapper, so it's a regular
        # albumentation trans block, so it's called by self.transform(image=img)['image']
        if self.second_stage:
            image = self.transform(image=image)['image']
        else:
            image = self.transform(image)

        return image, label


class SupConDatasetCifar100(torchvision.datasets.CIFAR100):
    def __init__(self, data_dir, train, transform, second_stage):
        super().__init__(root=data_dir, train=train, download=True, transform=transform)

        self.second_stage = second_stage
        self.transform = transform

    def __getitem__(self, idx):
        image, label = self.data[idx], self.targets[idx]

        # leave this part unchanged. The reason for this implementation - in the first stage of training
        # you have TwoCropTransform(actual transforms), so you have to call it by self.transform(img)
        # on the other hard, in the second stage of training there is no wrapper, so it's a regular
        # albumentation trans block, so it's called by self.transform(image=img)['image']
        if self.second_stage:
            image = self.transform(image=image)['image']
        else:
            image = self.transform(image)

        return image, label

def Pad_Random(img1):
    im1 = Image.open(img1).convert('RGB')
    w, h = im1.size
    big = max(w, h)
    size = (int(big/224)+1)*224
    im2 = Image.new(mode="RGB", size=(size, size))
    # print(w, h, '\t', size, size)
    random_x = random.randint(0, size-w)
    random_y = random.randint(0, size-h)
    im2.paste(im1, (random_x, random_y))
    im1.close()

    return im2

class SupConDatasetCustom(torchvision.datasets.ImageFolder):
    def __init__(self, data_dir, train, transform, second_stage):
        super().__init__(root=data_dir, transform=transform)

        self.second_stage = second_stage
        self.transform = transform

    def __getitem__(self, idx):
        # image, label = np.asarray(Image.open(self.imgs[idx][0]).convert('RGB')), self.imgs[idx][1]
        image, label = np.asarray(Pad_Random(self.imgs[idx][0])), self.imgs[idx][1]
        if self.second_stage:
            image = self.transform(image=image)['image']
        else:
            image = self.transform(image)

        return image, label


DATASETS = {'cifar10': SupConDatasetCifar10,
            'cifar100': SupConDatasetCifar100,
            'Upload_Data': SupConDatasetCustom,
            'Small_Data': SupConDatasetCustom,
            'Toyota_Data': SupConDatasetCustom,
            'Car_Models_train': SupConDatasetCustom,
            'Car_Models_valid': SupConDatasetCustom,
            'Car_Models_GreyScale_train': SupConDatasetCustom,
            'Car_Models_GreyScale_valid': SupConDatasetCustom,
            'Small_Data_New_train': SupConDatasetCustom,
            'Small_Data_New_valid': SupConDatasetCustom,
            'Small_Data_Crop_train': SupConDatasetCustom,
            'Small_Data_Crop_valid': SupConDatasetCustom,
            'Small_Data_Crop_New_train': SupConDatasetCustom,
            'Small_Data_Crop_New_valid': SupConDatasetCustom,
            'Small_Data_Crop_New_2_train': SupConDatasetCustom,
            'Small_Data_Crop_New_2_valid': SupConDatasetCustom,
            'Upload_Data_train': SupConDatasetCustom,
            'Upload_Data_valid': SupConDatasetCustom}

def create_supcon_dataset(dataset_name, data_dir, train, transform, second_stage):#, csv, second_stage):
    try:
        print(dataset_name)
        return DATASETS[dataset_name](data_dir, train, transform, second_stage)#, csv, second_stage)
    except KeyError:
        print(dataset_name)
        Exception('Can\'t find such a dataset. Either use cifar10 or cifar100, or write your own one in tools.datasets')


