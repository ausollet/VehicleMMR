import os

os.environ['WANDB_API_KEY'] = '998acac7a46e43d3f64cc44b2a9c3db8fe240d7c'

os.chdir('./yolov7')

with open('./custom_data.yaml', 'w') as f:
    f.write('path: ../\ntrain: train/images\nval: valid/images\ntest: test/images\n\nnc: 13\nnames: [\'Suzuki\', \'Hyundai\', \'Tata\', \'Kia\', \'Mahindra\', \'Toyota\', \'Renault\', \'Honda\', \'MG Motor\', \'Skoda\', \'Ford\', \'Nissan\', \'Volkswagen\']')

os.system('python train.py --workers 8 --device 0 --batch-size 32 --data ./custom_data.yaml --img 640 640 --cfg cfg/training/yolov7-custom.yaml --weights \'yolov7_training.pt\' --name yolov7-custom --hyp data/hyp.scratch.custom.yaml')

os.chdir('../')

