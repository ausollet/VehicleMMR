import os

os.environ['WANDB_API_KEY'] = ''

# os.chdir('./yolov5')
os.chdir('./yolov7')

with open('./custom_data.yaml', 'w') as f:
    # f.write('path: ../\ntrain: train/images\nval: valid/images\ntest: test/images\n\nnc: 13\nnames: [\'Suzuki\', \'Hyundai\', \'Tata\', \'Kia\', \'Mahindra\', \'Toyota\', \'Renault\', \'Honda\', \'MG Motor\', \'Skoda\', \'Ford\', \'Nissan\', \'Volkswagen\']')
    # f.write('path: ../\ntrain: train/images\nval: valid/images\ntest: test/images\n\nnc: 7\nnames: [\'Suzuki\', \'Hyundai\', \'Tata\', \'Toyota\', \'Honda\', \'Ford\', \'Volkswagen\']')
    f.write('train: ../train/images\nval: ../valid/images\ntest: ../test/images\n\nnc: 7\nnames: [\'Suzuki\', \'Hyundai\', \'Tata\', \'Toyota\', \'Honda\', \'Ford\', \'Volkswagen\']')

# with open('./custom_data_2.yaml', 'w') as f:
    # f.write('path: ../\ntrain: train/images\nval: valid/images\ntest: test/images\n\nnc: 10\nnames: [\'Buick\', \'Chery\', \'Ciroen\', \'Honda\', \'Hyundai\', \'Lexus\', \'Mazda\', \'Peugoet\', \'Toyota\', \'Volkswagen\']')
    # f.write('path: ../\ntrain: train/images\nval: valid/images\ntest: test/images\n\nnc: 4\nnames: [\'Honda\', \'Hyundai\', \'Toyota\', \'Volkswagen\']')

with open('./custom_data_3.yaml', 'w') as f:
    # f.write('path: ../\ntrain: train/images\nval: valid/images\ntest: test/images\n\nnc: 13\nnames: [\'Suzuki\', \'Hyundai\', \'Tata\', \'Kia\', \'Mahindra\', \'Toyota\', \'Renault\', \'Honda\', \'MG Motor\', \'Skoda\', \'Ford\', \'Nissan\', \'Volkswagen\']')
    # f.write('path: ../\ntrain: train2/images\nval: valid2/images\ntest: test2/images\n\nnc: 7\nnames: [\'Suzuki\', \'Hyundai\', \'Tata\', \'Toyota\', \'Honda\', \'Ford\', \'Volkswagen\']')
    f.write('train: ../train2/images\nval: ../valid2/images\ntest: ../test2/images\n\nnc: 7\nnames: [\'Suzuki\', \'Hyundai\', \'Tata\', \'Toyota\', \'Honda\', \'Ford\', \'Volkswagen\']')


# os.system('python train_aux.py --img 640 --batch 16 --device 0 --epochs 100 --data custom_data.yaml --cfg cfg/training/yolov7-w6.yaml --weights yolov7-w6.pt --name run1 --hyp data/hyp.scratch.custom.yaml')
# os.system('python train.py --resume')

# os.system('python train.py --img 640 --batch 4 --epochs 200 --data custom_data_3.yaml --weights runs/train/exp19/weights/best.pt --freeze 10')
os.system('python train_aux.py --img 640 --batch 4 --device 0 --epochs 100 --freeze 47 --data custom_data_3.yaml --cfg cfg/training/yolov7-w6.yaml --weights runs/train/run19/weights/best.pt --name run1 --hyp data/hyp.scratch.custom.yaml')
# os.system('python train.py --img 640 --batch 4 --epochs 200 --data custom_data_3.yaml --weights yolov5m.pt')
os.chdir('../')

