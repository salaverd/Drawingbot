# from matplotlib import pyplot as plt
# from PIL import Image
# import numpy as np
# import os
# import math

# # given an image, get its pixels
# def get_pixels(img):
#     with Image.open(img) as im:
#         im_rgb = im.convert(mode='RGB')
#         pixels = list(im_rgb.getdata())
#         width, height = im_rgb.size
#         # print("width = {}, height = {}".format(width, height))

#         # pixels_2d = np.array(pixels).reshape((height, width, 3))
#         # print(pixels_2d)
#         return pixels, width, height

# # returns all the dark coords in an image
# def get_dark_coords(img):

#     # TODO get and store the image's pixels
    
#     # TODO get indicies of dark pixels

#     # TODO convert from a 1D array of indicies to 2D array of coords

#     # TODO return your array of coords

#     pixels, width, height = get_pixels(img)
    
#     dark_cords = []
#     threshold = 1
#     i = 0
#     # j = 0
#     # k = 0

#     # matrix = [width][height]
#     # print(pixels)
#     for i, pixels in enumerate(pixels):
#         # if (sum(pixels) < threshold):
#         if (sum(pixels) != 765):
#             # print("i = {}".format(i // width))
#             # print("j = {}".format(i % width))
#             r = i // width
#             c = i % width
#             dark_cords.append((r, c))
#             # print("heeeerrrrreeee")
#     # print(dark_cords)

#     return dark_cords, width, height

# # calculates distance between 2 coords each with position x, y
# def dist(e1, e2):
#     # TODO return distance b/t 2 coords
#     return math.sqrt((e1[0] - e2[0]) ** 2 + (e1[1] - e2[1]) ** 2)

# # creates an ordering of coordinates for the turtle to follow
# def ord_coords(dark_coords):

#     # TODO given an array of all the dark coordinates in an image
#     # create an array of coordinates as a path for the turtle to follow

#     # TODO return ordered coordinates

#     ordered_coords = [dark_coords[0]]  # Start with the first dark coordinate
#     dark_coords = dark_coords[1:]  # Remaining coordinates

#     while dark_coords:
#         last = ordered_coords[-1]
#         nearest = min(dark_coords, key=lambda p: dist(last, p))
#         ordered_coords.append(nearest)
#         dark_coords.remove(nearest)

#     return ordered_coords

# def plot_trajectory(trajectory, width, height):
#     x_coords, y_coords = zip(*trajectory)
    
#     plt.figure(figsize=(10, 10))
#     plt.imshow([[255]*width]*height, cmap='gray', extent=[0, width, height, 0])
#     plt.scatter(x_coords, y_coords, c='black', s=1)
#     plt.title('Trajectory from Black Pixels')
#     plt.xlabel('X Coordinate')
#     plt.ylabel('Y Coordinate')
#     plt.gca().invert_yaxis()
#     plt.show()

# def main():
#     # img = "/home/student8/class_ws/src/drawingbot/images/square.png"
#     # img = "/home/student8/class_ws/src/drawingbot/images/num1.jpg"
#     img = "/Users/simaalaverdyan/Documents/Drawingbot/src/drawingbot/images/num1.jpg"
#     # folder = "../images/"
#     plotting = 1

#     # get_pixels(img)
#     # coords = get_dark_coords(img)
#     # ordered_coords = ord_coords(coords)

#     # print(ordered_coords)

#     # change to false if testing ord_coords
#     test_get_coords = True

#     # get dark coordinates from an image
#     coords, width, height = get_dark_coords(img)

#     # order coordinates based on distance
#     ordered = ord_coords(coords)

#     # plot_trajectory(ordered, width, height)
#     # plot trajectory
#     if plotting:
#         if test_get_coords:
#              ordered = coords
#         ord_np = np.array(ordered)
#         x = ord_np[0:, 0]
#         y = ord_np[0:, 1]

#         fig, ax = plt.subplots()
#         ax.scatter(x,y,color='blue')
        
#         if not test_get_coords:
#             ax.plot(x,y,color='blue')
#         ax.scatter(x[0], y[0], color = 'green', marker = "*", s=200, zorder=5)

#         ax.invert_yaxis()
#         ax.set_aspect('equal')
#         plt.show()

# if __name__ == '__main__':
# 	main()


from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os
import math

def get_pixels(img):
    with Image.open(img) as im:
        im_rgb = im.convert(mode='RGB')
        pixels = list(im_rgb.getdata())
        width, height = im_rgb.size
        return pixels, width, height

def scale_image(img, max_size=(500, 500)):
    with Image.open(img) as im:
        im.thumbnail(max_size, Image.Resampling.LANCZOS)
        im.save('scaled_image.png')
        return 'scaled_image.png'
    
def get_pixels(img):
    with Image.open(img) as im:
        im_rgb = im.convert(mode='RGB')
        pixels = list(im_rgb.getdata())
        width, height = im_rgb.size
        # print("width = {}, height = {}".format(width, height))

        # pixels_2d = np.array(pixels).reshape((height, width, 3))
        # print(pixels_2d)
        return pixels, width, height

def get_black_pixels(pixels, width, height):
    black_pixels = []
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[y * width + x]
            if r == 0 and g == 0 and b == 0:  # Check for black pixel
                black_pixels.append((x, y))
    return black_pixels

def simplify_trajectory(black_pixels, tolerance=2):
    simplified = []
    black_pixels.sort()

    for i in range(len(black_pixels) - 1):
        x1, y1 = black_pixels[i]
        x2, y2 = black_pixels[i + 1]

        if abs(x1 - x2) <= tolerance and abs(y1 - y2) <= tolerance:
            continue

        simplified.append((x1, y1))

    if black_pixels:
        simplified.append(black_pixels[-1])

    return simplified

def get_dark_coords(img):
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

    return dark_cords, width, height

def plot_trajectory(trajectory, width, height):
    x_coords, y_coords = zip(*trajectory)
    
    plt.figure(figsize=(10, 10))
    plt.imshow([[255]*width]*height, cmap='gray', extent=[0, width, height, 0])
    plt.scatter(x_coords, y_coords, c='black', s=1)
    plt.title('Trajectory from Black Pixels')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.gca().invert_yaxis()
    plt.show()

def main():
    img = "/Users/simaalaverdyan/Documents/Drawingbot/src/drawingbot/images/cat.jpg"
    plotting = 1

    test_get_coords = True

    coords, width, height = get_dark_coords(img)

    ordered = simplify_trajectory(coords)
    print("Simplified trajectory coordinates:", ordered)
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