import shutil
import glob
import os
import random

dataset_name = './Upload_Data'
car_brands = ['Honda', 'Hyundai', 'Maruti', 'Tata', 'Toyota']

for m in car_brands:
    images_list = []
    for i in glob.glob(dataset_name+'/'+m+'*'):
        train_subfolder = dataset_name+'_train/'+i.split('/')[-1]
        valid_subfolder = dataset_name+'_valid/'+i.split('/')[-1]
        print(train_subfolder, valid_subfolder)
        os.system('mkdir -p \'' + train_subfolder + '\'')
        os.system('mkdir -p \'' + valid_subfolder + '\'')
        images_list += glob.glob(i+'/*')

    # print(int(0.24*len(images_list)))
    valid_images_list = random.choices(images_list, k=60)
    print(len(valid_images_list))
    train_images_list = list(set(images_list)-set(valid_images_list))

    for j in valid_images_list:
        # print(valid_subfolder, j.split('/')[-1])
        valid_subfolder = j.split('/')[-2]
        os.system('cp \'' + j + '\' \'' + dataset_name + '_valid/' + valid_subfolder + '/' + j.split('/')[-1] + '\'')
    for j in train_images_list:
        # print(train_subfolder, j.split('/')[-1])
        train_subfolder = j.split('/')[-2]
        os.system('cp \'' + j + '\' \'' + dataset_name + '_train/' + train_subfolder + '/' + j.split('/')[-1] + '\'')

    print(m, len(images_list), len(valid_images_list), len(train_images_list))
    print('\n')

# os.system('find . -type d -empty -print -delete')
os.system('ls \'' + dataset_name + '\' | wc -l')
os.system('ls \'' + dataset_name + '_valid\' | wc -l')
os.system('ls \'' + dataset_name + '_train\' | wc -l')
