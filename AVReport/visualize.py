import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Rectangle
from PIL import Image as PIL_Image
import requests
from io import StringIO

def visualize_regions(image):
    plt.imshow(img)
    ax = plt.gca()
    ax.add_patch(Rectangle((36.5, 175),
    	361,
    	180,
    	fill=False,
    	edgecolor='red',
    	linewidth=3))
    ax.add_patch(Rectangle((57.5, 201.5),
    	127,
    	127,
    	fill=False,
    	edgecolor='blue',
    	linewidth=3))
    ax.add_patch(Rectangle((441.5, 1.5),
    	279,
    	295,
    	fill=False,
    	edgecolor='green',
    	linewidth=3))
    ax.add_patch(Rectangle((303.5, 180.5),
    	417,
    	220,
    	fill=False,
    	edgecolor='yellow',
    	linewidth=3))
    ax.add_patch(Rectangle((249.5, 217.5),
    	127,
    	127,
    	fill=False,
    	edgecolor='black',
    	linewidth=3))
    ax.add_patch(Rectangle((201.5, 169),
    	127,
    	127,
    	fill=False,
    	edgecolor='white',
    	linewidth=3))
    ax.add_patch(Rectangle((1.5, 1.5),
    	625,
    	220,
    	fill=False,
    	edgecolor='purple',
    	linewidth=3))
    ax.add_patch(Rectangle((1.5, 1.5),
    	204,
    	399,
    	fill=False,
    	edgecolor='orange',
    	linewidth=3))
    plt.show()
img = mpimg.imread("cars1.jpg")
visualize_regions(img)
