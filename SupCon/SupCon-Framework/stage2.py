import os
from MulticoreTSNE import MulticoreTSNE as TSNE
from matplotlib import pyplot as plt
from tools import utils
import torch
import torch.functional as F
import numpy as np

# os.system('python3.6 train.py --config_name configs/train/train_supcon_resnet50_cifar100_stage1.yml')
# os.system('python3.6 swa.py --config_name configs/train/swa_supcon_resnet50_cifar100_stage1.yml')
# os.system('python3.6 train.py --config_name configs/train/train_supcon_resnet50_cifar100_stage2.yml')
# os.system('python3.6 swa.py --config_name configs/train/swa_supcon_resnet50_cifar100_stage2.yml')

scaler = torch.cuda.amp.GradScaler()

ckpt_pretrained = 'weights/supcon_second_stage_cifar100/swa'
# data_dir = '../Toyota_Data'
# data_dir = '../Car_Models'
# data_dir = '../Upload_Data'
data_dir = '../Small_Data_Crop_New'
# num_classes = 266
# num_classes = 36
num_classes = 7
batch_sizes = {
            "train_batch_size": 16,
            'valid_batch_size': 4
                }
num_workers = 16
backbone = 'resnet50'
# stage = 'First'
stage = 'second'

transforms = utils.build_transforms(second_stage=(stage == 'second'))
loaders = utils.build_loaders(data_dir, transforms, batch_sizes, num_workers, second_stage=(stage == 'second'))

print(loaders)

model = utils.build_model(backbone, second_stage=(stage == 'second'), num_classes=num_classes, ckpt_pretrained=ckpt_pretrained).cuda()
# model.use_projection_head(False)
model.use_projection_head(True)
model.eval()

embeddings, labels = utils.compute_embeddings(loaders['valid_loader'], model, scaler)

print('Predictions:', np.argmax(embeddings, axis=-1), '\nGround truth labels:', labels)

count = 0
x = np.argmax(embeddings, axis=-1)
label_count = {}
label_ttl = {}
for i in range(len(labels)):
    if not label_ttl.get(labels[i]):
        label_ttl[labels[i]] = 1
    else:
        label_ttl[labels[i]] += 1
    if x[i]==labels[i]:
        count+=1
        if not label_count.get(labels[i]):
            label_count[labels[i]] = 1
        else:
            label_count[labels[i]] += 1
print(count, len(labels), (count/len(labels))*100)
for i in label_count:
    print(i, (label_count[i]/label_ttl[i])*100)
'''
embeddings_tsne = TSNE(n_jobs=num_workers).fit_transform(embeddings)
vis_x = embeddings_tsne[:, 0]
vis_y = embeddings_tsne[:, 1]
plt.scatter(vis_x, vis_y, c=labels, cmap=plt.cm.get_cmap("jet", num_classes), marker='.')
plt.colorbar(ticks=range(num_classes))
plt.savefig('valid_features.png')
plt.show()
plt.clf()

embeddings, labels = utils.compute_embeddings(loaders['train_features_loader'], model, scaler)
embeddings_tsne = TSNE(n_jobs=num_workers).fit_transform(embeddings)
vis_x = embeddings_tsne[:, 0]
vis_y = embeddings_tsne[:, 1]
plt.scatter(vis_x, vis_y, c=labels, cmap=plt.cm.get_cmap("jet", num_classes), marker='.')
plt.colorbar(ticks=range(num_classes))
plt.savefig('train_features.png')
plt.show()
'''
