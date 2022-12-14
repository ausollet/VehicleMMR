from PIL import Image
import glob
import random
import tqdm
import os
import shutil

def Paste_Random_n(img1, bgi_list, class_label, n=3, save_spot_image='./train/images', save_spot_label='./train/labels', count=''):
    name_1 = img1.split('/')[-1].split('.')[0]
    im1 = Image.open(img1).convert('RGB')
    # size = random.randint(64, 129)
    # im1 = im1.resize((size, size))
    bgi_list_select = random.sample(bgi_list, n)
                            
    for i in bgi_list_select:
        im2 = Image.open(i).convert('RGB')
        name_2 = i.split('/')[-1].split('.')[0]
        w, h = im2.size
        size = random.randint(int(h/6), int(h/5))

        if size>w:
            print(w, h, size, i)

        im1 = im1.resize((size, size))
        random_x = random.randint(0, w-size)
        random_y = random.randint(0, h-size)
        im2.paste(im1, (random_x, random_y))
        im2.save(save_spot_image+'/'+class_label+'_'+count+name_1+'_'+name_2+'.jpg')

        with open(save_spot_label+'/'+class_label+'_'+count+name_1+'_'+name_2+'.txt', 'w') as f:
            f.write(str(class_label)+' '+str((random_x+int(size/2))/w)+' '+str((random_y+int(size/2))/h)+' '+str(size/w)+' '+str(size/h)+'\n')

os.system('mkdir -p ./train/images')
os.system('mkdir -p ./train/labels')
os.system('mkdir -p ./valid/images')
os.system('mkdir -p ./valid/labels')
os.system('mkdir -p ./test/images')

os.system('mkdir -p ./train2/images')
os.system('mkdir -p ./train2/labels')
os.system('mkdir -p ./valid2/images')
os.system('mkdir -p ./valid2/labels')
os.system('mkdir -p ./test2/images')

# os.chdir('./test/images')
# os.system('wget https://www.globalsuzuki.com/automobile/home/img/car_dzire.jpg')
# os.system('wget https://www.carpages.co.uk/images/hyundai/i10/hyundai-i10-[@master]-[001-012010].jpg')
# os.system('wget https://www.team-bhp.com/?q=sites/default/files/styles/check_extra_large_for_review/public/tata-nexon_8.jpg')
# os.system('wget https://carwindscreenlondon.london/wp-content/uploads/2021/02/ford.jpg')
# os.system('wget https://www.topgear.com/sites/default/files/cars-car/image/2021/04/large-29336-thearteonshootingbrakeelegance.jpg')
# os.chdir('../..')

# Top_Car_Brands = {'Suzuki': 0, 'Hyundai': 1, 'Tata': 2, 'Kia': 3, 'Mahindra': 4, 'Toyota': 5, 'Renault': 6, 'Honda': 7, 'MG Motor': 8, 'Skoda': 9, 'Ford': 10, 'Nissan': 11, 'Volkswagen': 12}
# Top_Car_Brands = {'Buick': 0, 'Chery': 1, 'Citroen': 2, 'Honda': 3, 'Hyundai': 4, 'Lexus': 5, 'Mazda': 6, 'Peugeot': 7, 'Toyota': 8, 'Volkswagen': 9}
# Top_Car_Brands = {'Honda': 0, 'Hyundai': 1, 'Toyota': 2, 'Volkswagen': 3}
Top_Car_Brands = {'Suzuki': 0, 'Hyundai': 1, 'Tata': 2, 'Toyota': 3, 'Honda': 4, 'Ford': 5, 'Volkswagen': 6}

Top_Car_Brands_2 = {'Suzuki': 0, 'Hyundai': 1, 'Tata': 2, 'Toyota': 3, 'Honda': 4, 'Ford': 5, 'Volkswagen': 6}

VCI_List = glob.glob('../cctv/vehicle_crop/*.jpg')
# VCI_List = glob.glob('./Vehicle_Crop_Downloaded/*.jpeg')
New_VCI_List = []
for i in tqdm.tqdm(VCI_List):
    w, h = Image.open(i).size
    if w >= h/5 and h >= w/2:
        New_VCI_List.append(i)

print('***', len(New_VCI_List), '***')

for i in tqdm.tqdm(Top_Car_Brands.keys()):
    img_count = 0
    img_list = glob.glob('./data'+'/'+i+'/*/*.*')
    # img_list = glob.glob('./TrainingData/TrainingData'+'/'+i+'/*.*')
    n = int(len(img_list)*0.7)
    train_img_list = img_list[:n]
    valid_img_list = img_list[n:]

    for j in tqdm.tqdm(train_img_list):
        img_count+=1
        Paste_Random_n(j, New_VCI_List, str(Top_Car_Brands[i]), count=str(img_count))
    for j in tqdm.tqdm(valid_img_list):
        img_count+=1
        Paste_Random_n(j, New_VCI_List, str(Top_Car_Brands[i]), save_spot_image='./valid/images', save_spot_label='./valid/labels', count=str(img_count))

for i in tqdm.tqdm(Top_Car_Brands_2.keys()):
    img_count = 0
    img_list = glob.glob('./New_Data/'+i+'/*.jpg')
    n = int(len(img_list)*0.8)
    train_img_list = img_list[:n]
    valid_img_list = img_list[n:]

    for j in tqdm.tqdm(train_img_list):
        img_count+=1
        shutil.copy(j, './train2/images/'+i+'_'+j.split('/')[-1])

        f = open(j[:-3]+'txt', 'r')
        lines = f.readlines()
        for k in range(len(lines)):
            lines[k]= str(Top_Car_Brands_2[i]) + lines[k][1:]
        f.close()

        f = open('./train2/labels/'+i+'_'+j.split('/')[-1][:-3]+'txt', 'w')
        f.writelines(lines)
        f.close()

    for j in tqdm.tqdm(valid_img_list):
        img_count+=1
        shutil.copy(j, './valid2/images/'+i+'_'+j.split('/')[-1])

        f = open(j[:-3]+'txt', 'r')
        lines = f.readlines()
        for k in range(len(lines)):
            lines[k]= str(Top_Car_Brands_2[i]) + lines[k][1:]
        f.close()

        f = open('./valid2/labels/'+i+'_'+j.split('/')[-1][:-3]+'txt', 'w')
        f.writelines(lines)
        f.close()
