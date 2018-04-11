import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

import timeit

from PIL import Image

image = input("file name (no extension): ")



img_src = Image.open(image +'.jpg').convert('L')
# img_src.thumbnail((1000, 1000))
im = np.array(img_src)
print (im.shape)

data = im[500,:]
# fig = plt.hist(data)
plt.imshow(img_src)
plt.show()


# im = np.uint8(im * 255)
# data = im(:500)
# im = Image.fromarray(im)
# im.show('test_hot.jpg')
