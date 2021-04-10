import numpy as np
from PIL import Image
import matplotlib.pyplot as plt 
from collections import defaultdict

img = Image.open('path to image') # Path to image
img = img.convert("RGB")

pixdata = img.load()

x_list = []
y_list = []
c = []
for y in range(0,img.size[1]):
    for x in range(0,img.size[0]):
        x_list.append(x)
        y_list.append(y)
        c.append(pixdata[(img.size[0]-x-1), (img.size[1]-y-1)])

z_list = [None] * len(x_list)

d = defaultdict(list)
for i, x in enumerate(c):
    d[x].append(i)

l = list(d.values())

n = 0
for i in l:
    for j in i:
        z_list[j] = n
    n += 1

cl = np.array(c)

fig = plt.figure()
ax = plt.axes(projection ="3d")
ax.scatter3D(x_list,y_list,z_list,c=cl/255)

ax.view_init(azim=0, elev=90)

plt.show()

