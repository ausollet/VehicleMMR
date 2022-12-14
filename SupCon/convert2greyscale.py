import glob
from PIL import Image, ImageOps

dataset = './Car_Models_GreyScale'
for i in glob.glob(dataset+'/*/*'):
    img = Image.open(i)
    ImageOps.grayscale(img).save(i)
    img.close()
