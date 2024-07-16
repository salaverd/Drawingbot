from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
import os
import math

# given an image, get its pixels
def get_pixels(img):
    with Image.open(img) as im:
        im_rgb = im.convert(mode='RGB')
        pixels = list(im_rgb.getdata())
        width, height = im_rgb.size
        # print("width = {}, height = {}".format(width, height))

        # pixels_2d = np.array(pixels).reshape((height, width, 3))
        # print(pixels_2d)
        return pixels, width, height

# returns all the dark coords in an image
def get_dark_coords(img):

    # TODO get and store the image's pixels
    
    # TODO get indicies of dark pixels

    # TODO convert from a 1D array of indicies to 2D array of coords

    # TODO return your array of coords

    pixels, width, height = get_pixels(img)
    
    dark_cords = []
    threshold = 1
    i = 0
    # j = 0
    # k = 0

    # matrix = [width][height]
    # print(pixels)
    for i, pixels in enumerate(pixels):
        # if (sum(pixels) < threshold):
        if (sum(pixels) != 765):
            # print("i = {}".format(i // width))
            # print("j = {}".format(i % width))
            r = i // width
            c = i % width
            dark_cords.append((r, c))
            # print("heeeerrrrreeee")
    # print(dark_cords)

    return dark_cords

# calculates distance between 2 coords each with position x, y
def dist(e1, e2):
    # TODO return distance b/t 2 coords
    return math.sqrt((e1[0] - e2[0]) ** 2 + (e1[1] - e2[1]) ** 2)

# creates an ordering of coordinates for the turtle to follow
def ord_coords(dark_coords):

    # TODO given an array of all the dark coordinates in an image
    # create an array of coordinates as a path for the turtle to follow

    # TODO return ordered coordinates

    ordered_coords = [dark_coords[0]]  # Start with the first dark coordinate
    dark_coords = dark_coords[1:]  # Remaining coordinates

    while dark_coords:
        last = ordered_coords[-1]
        nearest = min(dark_coords, key=lambda p: dist(last, p))
        ordered_coords.append(nearest)
        dark_coords.remove(nearest)

    return ordered_coords

def main():
    # img = "/home/student8/class_ws/src/drawingbot/images/square.png"
    # img = "/home/student8/class_ws/src/drawingbot/images/num1.jpg"
    img = "/home/student8/class_ws/src/drawingbot/images/triangle.png"
    # folder = "../images/"
    plotting = 1

    # get_pixels(img)
    # coords = get_dark_coords(img)
    # ordered_coords = ord_coords(coords)

    # print(ordered_coords)

    # change to false if testing ord_coords
    test_get_coords = True

    # get dark coordinates from an image
    coords = get_dark_coords(img)

    # order coordinates based on distance
    ordered = ord_coords(coords)
    # plot trajectory
    if plotting:
        if test_get_coords:
             ordered = coords
        ord_np = np.array(ordered)
        x = ord_np[0:, 0]
        y = ord_np[0:, 1]

        fig, ax = plt.subplots()
        ax.scatter(x,y,color='blue')
        
        if not test_get_coords:
            ax.plot(x,y,color='blue')
        ax.scatter(x[0], y[0], color = 'green', marker = "*", s=200, zorder=5)

        ax.invert_yaxis()
        ax.set_aspect('equal')
        plt.show()

if __name__ == '__main__':
	main()
