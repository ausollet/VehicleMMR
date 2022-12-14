import numpy as np
import cv2
 
import glob
  
files = glob.glob('./Car_Models_GreyScale_valid/*/*.jpg')
# files = glob.glob('./Small_Data_Crop_New_2_train/*/*.jpg')
   
len(files)
    
mean = np.array([0.,0.,0.])
stdTemp = np.array([0.,0.,0.])
std = np.array([0.,0.,0.])
     
numSamples = len(files)
print(numSamples)
      
for i in range(numSamples):
    im = cv2.imread(str(files[i]))
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    im = im.astype(float) / 255.0
    for j in range(3):
        mean[j] += np.mean(im[:,:,j])      
mean = (mean/numSamples)                                            
print(mean)

for i in range(numSamples):
    im = cv2.imread(str(files[i]))
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    im = im.astype(float) / 255.
    for j in range(3):
        stdTemp[j] += ((im[:,:,j] - mean[j])**2).sum()/(im.shape[0]*im.shape[1])                                 
std = np.sqrt(stdTemp/numSamples)
print(std)
