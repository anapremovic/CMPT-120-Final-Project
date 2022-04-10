# CMPT 120 Yet Another Image Processer
# Starter code for main.py
# Author(s): Angelica Lim, Ana Premovic
# Date: Nov 23-Dec 3 2021
# Description: The implementation of the filter for the image processor. Creates a menu where the
#              user can upload any image, apply basic and advanced filters, and save the image(s).

# This line has exactly 100 characters (including the period), use it to keep each line under limit.

import cmpt120imageProjHelper
import cmpt120imageManip
import tkinter.filedialog
import pygame
pygame.init()

# list of system options
system = [
            "Q: Quit", "O: Open Image", "S: Save Current Image", "R: Reload Original Image"
         ]

# list of basic operation options
basic = [
          "1: Apply Red Filter", "2: Apply Green Filter", "3: Apply Blue Filter",
          "4: Apply Sepia Filter", "5: Apply Warm Filter", "6: Apply Cold Filter",
          "7: Switch to Advanced Functions"
         ]

# list of advanced operation options
advanced = [
                "1: Rotate Left", "2: Rotate Right", "3: Double Size", "4: Half Size",
                "5: Locate Fish", "6: Switch to Basic Functions"
             ]

# a helper function that generates a list of strings to be displayed in the interface
def generateMenu(state):
    """
    Input:  state - a dictionary containing the state values of the application
    Returns: a list of strings, each element represets a line in the interface
    """
    menuString = ["Welcome to CMPT 120 Image Processer!"]
    menuString.append("") # an empty line
    menuString.append("Choose the following options:")
    menuString.append("") # an empty line
    menuString += system
    menuString.append("") # an empty line

    # build the list differently depending on the mode attribute
    if state["mode"] == "basic":
        menuString.append("--Basic Mode--")
        menuString += basic
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-7)...")
    elif state["mode"] == "advanced":
        menuString.append("--Advanced Mode--")
        menuString += advanced
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-6)...")
    else:
        menuString.append("Error: Unknown mode!")

    return menuString

# a helper function that returns the result image as a result of the operation chosen by the user
# it also updates the state values when necessary
# (e.g, the mode attribute if the user switches mode)
def handleUserInput(state, img):
    """
    Input:  state - a dictionary containing the state values of the application
            img - the 2d array of RGB values to be operated on
    Returns: the 2d array of RGB vales of the result image of an operation chosen by the user
    """
    userInput = state["lastUserInput"].upper()
    # handle the system functionalities
    if userInput.isalpha(): # check if the input is an alphabet
        print("Log: Doing system functionalities " + userInput)
        
        if userInput == "Q": # this case actually won't happen, it's here as an example
            print("Log: Quitting...")
        
        # if the user enters "O" (open image), they can upload an image file from their computer
        elif userInput == "O":
            # upload an image and set it to img
            tkinter.Tk().withdraw()
            openFilename = tkinter.filedialog.askopenfilename()
            img = cmpt120imageProjHelper.getImage(openFilename)

            # get the last part of the path file of the image to be used for the window title
            display_name = openFilename.split("/")[-1]
            # display the image and window title
            cmpt120imageProjHelper.showInterface(img,
                                                 "Open Image " + display_name,
                                                 generateMenu(appStateValues))

            # update dictionary with correct info
            appStateValues["lastOpenFilename"] = display_name
            appStateValues["lastUserInput"] = "O"
           
        # if the user enter "S" (save image), they can save the current image to their computer
        elif userInput == "S":
            # save img
            tkinter.Tk().withdraw()
            saveFilename = tkinter.filedialog.asksaveasfilename()
            cmpt120imageProjHelper.saveImage(img, saveFilename)

            # display the saved image with whichever file name the user chose
            display_name = saveFilename.split("/")[-1]
            cmpt120imageProjHelper.showInterface(img,
                                                 "Save Image " + display_name,
                                                 generateMenu(appStateValues))
            
            appStateValues["lastSaveFilename"] = display_name
            appStateValues["lastUserInput"] = "S"
        
        # if the user enters "R" (reload image), they can reset 
        # the current image to when it had no filters
        elif userInput == "R":
            # if the user has not uploaded an image yet, display a message saying so
            if appStateValues["lastOpenFilename"] == "":
                print("No image has been loaded yet! Please enter 'O' to load an image.")
            # if they have, display the last opened image
            else:
                img = cmpt120imageProjHelper.getImage(appStateValues["lastOpenFilename"])
                cmpt120imageProjHelper.showInterface(img, "Reload Image " +
                                                     appStateValues["lastOpenFilename"],
                                                     generateMenu(appStateValues))

            appStateValues["lastUserInput"] = "R"

    # or handle the manipulation functionalities based on which mode the application is in
    elif userInput.isdigit(): # has to be a digit for manipulation options
        # print whatever the user inputs in the console
        print("Log: Doing manipulation functionalities " + userInput)

        # BASIC FILTER OPTIONS
        if state["mode"] == "basic":
            if int(userInput) < 1 or int(userInput) > 7:
                print("Please enter a valid number.")
            else:
                print("Log: Performing " + basic[int(userInput)-1])

            # if the user enters option 1, apply a red filter and display the new image
            if userInput == "1":
                img = cmpt120imageManip.applyRedFilter(img)
                cmpt120imageProjHelper.showInterface(img, "Apply Red Filter " +
                                                     appStateValues["lastOpenFilename"],
                                                     generateMenu(appStateValues))

                appStateValues["lastUserInput"] = "1"

            # if the user enters option 2, apply a green filter and display the new image
            elif userInput == "2":
                img = cmpt120imageManip.applyGreenFilter(img)
                cmpt120imageProjHelper.showInterface(img, "Apply Green Filter " +
                                                     appStateValues["lastOpenFilename"],
                                                     generateMenu(appStateValues))
                appStateValues["lastUserInput"] = "2"

            # if the user enters option 3, apply a blue filter and display the new image
            elif userInput == "3":
                img = cmpt120imageManip.applyBlueFilter(img)
                cmpt120imageProjHelper.showInterface(img, "Apply Blue Filter " +
                                                     appStateValues["lastOpenFilename"],
                                                     generateMenu(appStateValues))
                appStateValues["lastUserInput"] = "3"

            # if the user enters option 4, apply a sepia filter and display the new image
            elif userInput == "4":
                img = cmpt120imageManip.applySepiaFilter(img)
                cmpt120imageProjHelper.showInterface(img, "Apply Sepia Filter " +
                                                     appStateValues["lastOpenFilename"],
                                                     generateMenu(appStateValues))
                appStateValues["lastUserInput"] = "4"

            # if the user enters option 5, apply a warm filter and display the new image
            elif userInput == "5":
                img = cmpt120imageManip.applyWarmFilter(img)
                cmpt120imageProjHelper.showInterface(img, "Apply Warm Filter " +
                                                     appStateValues["lastOpenFilename"],
                                                     generateMenu(appStateValues))
                appStateValues["lastUserInput"] = "5"

            # if the user enters option 6, apply a cold filter and display the new image
            elif userInput == "6":
                img = cmpt120imageManip.applyColdFilter(img)
                cmpt120imageProjHelper.showInterface(img, "Apply Cold Filter " +
                                                     appStateValues["lastOpenFilename"],
                                                     generateMenu(appStateValues))
                appStateValues["lastUserInput"] = "6"

            # if the user enters option 7, display the advanced filters menu
            elif userInput == "7":
                state["mode"] = "advanced"
                cmpt120imageProjHelper.showInterface(currentImg, "Advanced Settings " +
                                                     appStateValues["lastOpenFilename"],
                                                     generateMenu(appStateValues))

        # ADVANCED FILTER OPTIONS
        elif state["mode"] == "advanced":
            if int(userInput) < 1 or int(userInput) > 6:
                print("Please enter a valid number.")
            else:
                print("Log: Performing " + advanced[int(userInput)-1])

            # if the user enters option 1, rotate the image left and display the new image
            if userInput == "1":
                img = cmpt120imageManip.rotateLeft(img)
                cmpt120imageProjHelper.showInterface(img, "Rotate Left " +
                                                         appStateValues["lastOpenFilename"],
                                                         generateMenu(appStateValues))

            # if the user enters option 2, rotate the image right and display the new image
            elif userInput == "2":
                img = cmpt120imageManip.rotateRight(img)
                cmpt120imageProjHelper.showInterface(img, "Rotate Right " +
                                                         appStateValues["lastOpenFilename"],
                                                         generateMenu(appStateValues))

            # if the user enters option 3, double the image in size and display the new image
            elif userInput == "3":
                img = cmpt120imageManip.doubleSize(img)
                cmpt120imageProjHelper.showInterface(img, "Double Size " +
                                                         appStateValues["lastOpenFilename"],
                                                         generateMenu(appStateValues))

            # if the user enters option 4, half the image in size and display the new image
            elif userInput == "4":
                img = cmpt120imageManip.halfSize(img)
                cmpt120imageProjHelper.showInterface(img, "Half Size " +
                                                         appStateValues["lastOpenFilename"],
                                                         generateMenu(appStateValues))
            
            # if the user enters option 5, locate the fish in the image
            # and draw a green rectangle around it
            # *** ONLY WORKS FOR THE PROVIDED FISH IMAGE
            elif userInput == "5":
                img = cmpt120imageManip.locateFish(img)
                cmpt120imageProjHelper.showInterface(img, "Locate Fish " +
                                                         appStateValues["lastOpenFilename"],
                                                         generateMenu(appStateValues))

            # if the user enters options 6, display the basic filters menu
            elif userInput == "6":
                state["mode"] = "basic"
                cmpt120imageProjHelper.showInterface(currentImg, "Basic Settings " +
                                                     appStateValues["lastOpenFilename"],
                                                     generateMenu(appStateValues))
    
    else: # unrecognized user input
        print("Log: Unrecognized user input: " + userInput)

        

    return img


# This line has exactly 100 characters (including the period), use it to keep each line under limit.

# ***NOTE: some of the lines below are above 100 characters but I am not allowed to change the code

# *** DO NOT change any of the code below this point ***

# use a dictionary to remember several state values of the application
appStateValues = {
                    "mode": "basic",
                    "lastOpenFilename": "",
                    "lastSaveFilename": "",
                    "lastUserInput": ""
                 }

currentImg = cmpt120imageProjHelper.getBlackImage(300, 200) # create a default 300 x 200 black image
cmpt120imageProjHelper.showInterface(currentImg, "No Image", generateMenu(appStateValues)) # note how it is used

# ***this is the event-loop of the application. Keep the remainder of the code unmodified***
keepRunning = True
# a while-loop getting events from pygame
while keepRunning:
    ### use the pygame event handling system ###
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            appStateValues["lastUserInput"] = pygame.key.name(event.key)
            # prepare to quit the loop if user inputs "q" or "Q"
            if appStateValues["lastUserInput"].upper() == "Q":
                keepRunning = False
            # otherwise let the helper function handle the input
            else:
                currentImg = handleUserInput(appStateValues, currentImg)
        elif event.type == pygame.QUIT: #another way to quit the program is to click the close botton
            keepRunning = False

# shutdown everything from the pygame package
pygame.quit()

print("Log: Program Quit")
