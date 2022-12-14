import os
import glob
import shutil

for i in glob.glob('Small_Data_New/*/*/*'):
    os.system('mkdir -p Small_Data_New/'+'\\ '.join(i.split('/')[-2].split(' ')))
    shutil.move(i, 'Small_Data_New/'+'/'.join(i.split('/')[2:]))
