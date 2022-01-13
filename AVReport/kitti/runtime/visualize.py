import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Rectangle
from PIL import Image as PIL_Image
import requests
from io import StringIO

def visualize_regions(image):
    plt.imshow(img)
    ax = plt.gca()
    ax.add_patch(Rectangle((223.5, 20.5),
    	497,
    	197,
    	fill=False,
    	edgecolor='red',
    	linewidth=3))
    ax.add_patch(Rectangle((217.5, 9.5),
    	127,
    	150,
    	fill=False,
    	edgecolor='blue',
    	linewidth=3))
    ax.add_patch(Rectangle((1.5, 89.5),
    	55,
    	63,
    	fill=False,
    	edgecolor='green',
    	linewidth=3))
    ax.add_patch(Rectangle((1.5, 79),
    	316,
    	138.5,
    	fill=False,
    	edgecolor='yellow',
    	linewidth=3))
    ax.add_patch(Rectangle((249.5, 25.5),
    	63,
    	63,
    	fill=False,
    	edgecolor='black',
    	linewidth=3))
    ax.add_patch(Rectangle((217.5, 41.5),
    	63,
    	63,
    	fill=False,
    	edgecolor='white',
    	linewidth=3))
    ax.add_patch(Rectangle((233.5, 73.5),
    	63,
    	63,
    	fill=False,
    	edgecolor='purple',
    	linewidth=3))
    plt.show()
img = mpimg.imread("umm_000075.png")
visualize_regions(img)
