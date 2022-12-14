import shutil
import glob
import os
import random

# dataset_name = './Small_Data_Crop'
dataset_name = './Car_Models_GreyScale'

for i in glob.glob(dataset_name+'/*'):
    train_subfolder = dataset_name+'_train/'+i.split('/')[-1]
    valid_subfolder = dataset_name+'_valid/'+i.split('/')[-1]
    os.system('mkdir -p \'' + train_subfolder + '\'')
    os.system('mkdir -p \'' + valid_subfolder + '\'')
    images_list = glob.glob(i+'/*')
    print(len(images_list))
    if  int(0.3*len(images_list))<10:
        print('deleting:', i, '\timages contined:', len(images_list))
        # # os.system('rm -r \'' + i + '\'')
        continue
    valid_images_list = random.choices(images_list, k=int(0.3*len(images_list)))
    train_images_list = list(set(images_list)-set(valid_images_list))

    for j in valid_images_list:
        # print(valid_subfolder, j.split('/')[-1])
        os.system('cp \'' + j + '\' \'' + valid_subfolder + '/' + j.split('/')[-1] + '\'')
    for j in train_images_list:
        # print(train_subfolder, j.split('/')[-1])
        os.system('cp \'' + j + '\' \'' + train_subfolder + '/' + j.split('/')[-1] + '\'')

    print(i)
    os.system('ls \'' + i + '/*\' | wc -l')
    os.system('ls \'' + valid_subfolder + '/*\' | wc -l')
    os.system('ls \'' + train_subfolder + '/*\' | wc -l')
    print('\n')

os.system('find . -type d -empty -print -delete')
os.system('ls \'' + dataset_name + '\' | wc -l')
os.system('ls \'' + dataset_name + '_valid\' | wc -l')
os.system('ls \'' + dataset_name + '_train\' | wc -l')
