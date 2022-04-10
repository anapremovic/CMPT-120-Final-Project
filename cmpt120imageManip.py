# CMPT 120 Yet Another Image Processer
# Starter code for cmpt120imageManip.py
# Author(s): Ana Premovic
# Date: Nov 23-Dec 3 2021
# Description: A helper module which has all the filter functions to be used in main.py

# This line has exactly 100 characters (including the period), use it to keep each line under limit.

import cmpt120imageProjHelper
import numpy
import copy

"""
Whenever the parameter is "pixels", this represents the 2D array/image
that the filter will be applied to
"""

# returns a new image, like pixels but with a red filter applied
def applyRedFilter(pixels):
    new_img = copy.deepcopy(pixels)
    
    for row in range(len(pixels)):
        for col in range(len(pixels[0])):
            # set green and blue components to 0
            new_img[row][col][1] = 0
            new_img[row][col][2] = 0

    return new_img

# returns a new image, like pixels but with a green filter applied
def applyGreenFilter(pixels):
    new_img = copy.deepcopy(pixels)
    
    for row in range(len(pixels)):
        for col in range(len(pixels[0])):
            # set red and blue components to 0
            new_img[row][col][0] = 0
            new_img[row][col][2] = 0

    return new_img

# returns a new image, like pixels but with a blue filter applied
def applyBlueFilter(pixels):
    new_img = copy.deepcopy(pixels)
    
    for row in range(len(pixels)):
        for col in range(len(pixels[0])):
            # set red and green components to 0
            new_img[row][col][0] = 0
            new_img[row][col][1] = 0

    return new_img

# returns a new image, like pixels but with a sepia filter applied
def applySepiaFilter(pixels):
    new_img = copy.deepcopy(pixels)

    for row in range(len(pixels)):
        for col in range(len(pixels[0])):
            # red, green, and blue components of the current pixel on pixels
            red = new_img[row][col][0]
            green = new_img[row][col][1]
            blue = new_img[row][col][2]

            # the new rgb components using the sepia formula
            new_red = int(min(red*0.393+green*0.769+blue*0.189, 255))
            new_green = int(min(red*0.349+green*0.686+blue*0.168, 255))
            new_blue = int(min(red*0.272+green*0.534+blue*0.131, 255))

            # set the current pixel's rgb components to their new variants
            new_img[row][col][0] = new_red
            new_img[row][col][1] = new_green
            new_img[row][col][2] = new_blue

    return new_img

# a helper function for applyWarmFilter and applyColdFilter
# value - a number representing a red, green, or blue rgb component
# makes value more noticable compared to the other 2 rgb components
def scaleUp(value):
    if value < 64:
        return int(value/64*80)
    elif value < 128:
        return (value-64)/(128-64) * (160-80) + 80

    return (value-128)/(255-128) * (255-160) + 160

# a helper function for applyWarmFilter and applyColdFilter
# input - a number representing a red, green, or blue rgb component
# makes value less noticable compared to the other 2 rgb components
def scaleDown(value):
    if value < 64:
        return value/64*50
    elif value < 128:
        return (value-64)/(128-64) * (100-50) + 50

    return (value-128)/(255-128) * (255-100) + 100

# returns a new image, like pixels but with a warm filter applied
def applyWarmFilter(pixels):
    new_img = copy.deepcopy(pixels)

    for row in range(len(pixels)):
        for col in range(len(pixels[0])):
            # the current red and blue components of the current pixel on pixels
            red = new_img[row][col][0]
            blue = new_img[row][col][2]

            # scale up the red component and scale down the blue component
            new_img[row][col][0] = scaleUp(red)
            new_img[row][col][2] = scaleDown(blue)

    return new_img

# returns a new image, like pixels but with a cold filter applied
def applyColdFilter(pixels):
    new_img = copy.deepcopy(pixels)

    for row in range(len(pixels)):
        for col in range(len(pixels[0])):
            # the current red and blue components of the current pixel on pixels
            red = new_img[row][col][0]
            blue = new_img[row][col][2]

            # scale up down red component and scale up the blue component
            new_img[row][col][0] = scaleDown(red)
            new_img[row][col][2] = scaleUp(blue)

    return new_img

# returns a new image, like pixels but rotated left
def rotateLeft(pixels):
    # a black image with height = pixels's width and width = pixels's height
    new_img = cmpt120imageProjHelper.getBlackImage(len(pixels), len(pixels[0]))

    for row in range(len(pixels[0])):
        for col in range(len(pixels)):
            new_img[row][col] = pixels[col][len(pixels[0])-1-row]

    return new_img

# returns a new image, like pixels but rotated right
def rotateRight(pixels):
    # a black image with height = pixels's width and width = pixels's height
    new_img = cmpt120imageProjHelper.getBlackImage(len(pixels), len(pixels[0]))

    for row in range(len(pixels[0])):
        for col in range(len(pixels)):
            new_img[row][col] = pixels[len(pixels)-1-col][row]

    return new_img

# returns a new image, like pixels but doubled in size
def doubleSize(pixels):
    # a black image with height = twice pixels's height and width = twice pixels's width
    new_img = cmpt120imageProjHelper.getBlackImage(len(pixels[0])*2, len(pixels)*2)

    # the current row being extracted from pixels
    pixels_row = 0
    
    for row in range(0, len(new_img), 2):
        # the current column being extracted from pixels
        pixels_col = 0
        
        for col in range(0, len(new_img[0]), 2):
            # set the surrounding 4x4 block of the current pixel to the current pixel of pixels
            new_img[row][col] = pixels[pixels_row][pixels_col]
            new_img[row][col+1] = pixels[pixels_row][pixels_col]
            new_img[row+1][col] = pixels[pixels_row][pixels_col]
            new_img[row+1][col+1] = pixels[pixels_row][pixels_col]

            pixels_col += 1

        pixels_row += 1

    return new_img

# returns a new image, like pixels but halfed in size           
def halfSize(pixels):
    # a black image with height = half pixels's height and width = half pixels's width
    new_img = cmpt120imageProjHelper.getBlackImage(len(pixels[0])//2, len(pixels)//2)

    # the current row being extracted from pixels
    pixels_row = 0
    
    for row in range(len(new_img)):
        # the current column being extracted from pixels
        pixels_col = 0
        
        for col in range(len(new_img[0])):
            # 4 pixels/the 2x2 block of pixels whose average will
            # represent the current pixel on new_img
            one = pixels[pixels_row][pixels_col]
            two = pixels[pixels_row][pixels_col+1]
            three = pixels[pixels_row+1][pixels_col]
            four = pixels[pixels_row+1][pixels_col+1]

            # the rgb values of the current pixel on new_img
            # they are an average of the colours of the 2x2 block
            red_avg = min(255, (one[0]+two[0]+three[0]+four[0])/4)
            green_avg = min(255, (one[1]+two[1]+three[1]+four[1])/4)
            blue_avg = min(255, (one[2]+two[2]+three[2]+four[2])/4)

            # set the current pixel to the averages
            new_img[row][col] = [red_avg, green_avg, blue_avg]

            pixels_col += 2

        pixels_row += 2

    return new_img

# a helper function for findOuterYellowCoords
# rgb_list - a list of rgb values (must be length 3) of the form [r, g, b] (represents a pixel)
# returns a Boolean value which says if the pixel represented by rgb_list is yellow
def isYellow(rgb_list):
    # a tuple representing the hsv values of rgb_list
    hsv_tuple = cmpt120imageProjHelper.rgb_to_hsv(rgb_list[0], rgb_list[1], rgb_list[2])

    # requirements for each hsv component so that the pixel represented by rgb_list is yellow
    h = hsv_tuple[0] >= 50 and hsv_tuple[0] <= 65
    s = hsv_tuple[1] >= 50 and hsv_tuple[1] <= 60
    v = hsv_tuple[2] >= 50 and hsv_tuple[2] <= 100

    # the pixel is only yellow if it meets the requirements for h, s, and v
    return h and s and v

"""
a helper function for locateFish

locates the yellow object in pixels (a fish), and determines
the which pixel it starts and ends on

returns a list of the form [x_min, x_max, y_min, y_max]
(x_min, y_min) - the coord of the top left corner of the yellow object
(x_max, y_max) - the coord of the bottom right corner of the yellow object
"""
def findOuterYellowCoords(pixels):
    x_min = len(pixels[0])
    x_max = 0
    y_min = len(pixels)
    y_max = 0

    for row in range(len(pixels)):
        for col in range(len(pixels[0])):
            # the current pixel
            cur = pixels[row][col]

            # if the current pixel is yellow, update the coords if necessary
            if isYellow(cur):
                if col < x_min:
                    x_min = col

                if col > x_max:
                    x_max = col

                if row < y_min:
                    y_min = row

                if row > y_max:
                    y_max = row

    return [x_min, x_max, y_min, y_max]

# *** ONLY WORKS ON THE GIVEN FISH IMAGE
# returns a new image, like pixels but with a green rectangle drawn around the fish
def locateFish(pixels):
    new_img = copy.deepcopy(pixels)

    # get the min and max coords of the fish using the helper function
    x_y_coords = findOuterYellowCoords(pixels)
    x_min = x_y_coords[0]
    x_max = x_y_coords[1]
    y_min = x_y_coords[2]
    y_max = x_y_coords[3]

    # draw the green rectangle
    for row in range(len(pixels)):
        for col in range(len(pixels[0])):
            if row == y_min and col >= x_min and col <= x_max:
                new_img[row][col] = [0, 255, 0]
            elif row == y_max and col >= x_min and col <= x_max:
                new_img[row][col] = [0, 255, 0]

            if col == x_min and row >= y_min and row <= y_max:
                new_img[row][col] = [0, 255, 0]
            elif col == x_max and row >= y_min and row <= y_max:
                new_img[row][col] = [0, 255, 0]

    return new_img
            

    





    
