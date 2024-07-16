from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
import os

# given an image, get its pixels
def get_pixels(img):
    with Image.open(img) as im:
        im_rgb = im.convert(mode='RGB')
        pixels = list(im_rgb.getdata())
        # print(pixels)
        width, height = im_rgb.size
        print("width = {}, height = {}".format(width, height))
        return pixels

# returns all the dark coords in an image
def get_dark_coords(img):

    # TODO get and store the image's pixels
    
    # TODO get indicies of dark pixels

    # TODO convert from a 1D array of indicies to 2D array of coords

    # TODO return your array of coords


    return None

# calculates distance between 2 coords each with position x, y
def dist(e1, e2):
    # TODO return distance b/t 2 coords
    return None

# creates an ordering of coordinates for the turtle to follow
def ord_coords(coords):

    # TODO given an array of all the dark coordinates in an image
    # create an array of coordinates as a path for the turtle to follow

    # TODO return ordered coordinates
    return None

def main():
    img = "/home/student8/class_ws/src/drawingbot/images/square.png"
    # folder = "../images/"
    plotting = 1

    get_pixels(img)
    
    # # change to false if testing ord_coords
    # test_get_coords = True

    # # get dark coordinates from an image
    # coords = get_dark_coords(img, folder)

    # # order coordinates based on distance
    # ordered = ord_coords(coords)
    # # plot trajectory
    # if plotting:
    #     if test_get_coords:
    #          ordered = coords
    #     ord_np = np.array(ordered)
    #     x = ord_np[0:, 0]
    #     y = ord_np[0:, 1]

    #     fig, ax = plt.subplots()
    #     ax.scatter(x,y,color='blue')
        
    #     if not test_get_coords:
    #         ax.plot(x,y,color='blue')
    #     ax.scatter(x[0], y[0], color = 'green', marker = "*", s=200, zorder=5)

    #     ax.invert_yaxis()
    #     ax.set_aspect('equal')
    #     plt.show()

if __name__ == '__main__':
	main()
