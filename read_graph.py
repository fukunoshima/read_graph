# -*- coding: utf-8 -*-

# ---------------------------------
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
# --------------------------------

# setting ----------------------
filename = "" # filename

xmin = 0      # ranges of graph
xmax = 20
ymin = 0
ymax = 4
# ------------------------------


img    = Image.open(filename)
width  = img.width
height = img.height
tate = 8/width*height

fig = plt.figure(figsize=(8, tate))
fig.patch.set_facecolor=('white')
ax = fig.add_subplot(1,1,1)
ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)
xlim = ax.get_xlim()
ylim = ax.get_ylim()



ax.imshow(img, extent=[*xlim, *ylim], aspect='auto', alpha=0.6)
plt.show()




