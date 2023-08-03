""" 
Tkinter Notes/Prototype 

This is to better understand how to use Tkinter to create the system's GUI.
Additionally, this will be used to create a prototype of the GUI as well.
"""
from tkinter import *
import tkinter.font as tkFont 

# Debug function for buttons
def buttonClicked(response):
    print("You Clicked " + response)

if __name__ == "__main__":
    # Creates the window to use
    window = Tk()
    fontStyleBody = tkFont.Font(family="Arial", size=48)
    # Set up the properties of the window (Name, display size, then color)
    window.title("Prototype Test")

    width = str(window.winfo_screenwidth())
    height = str(window.winfo_screenheight())
    geometryStr = width + "x" + height
    window.geometry(geometryStr)

    window.configure(bg='white')

    # Adding items into Tkinter through frames
    # Create a frame to add to the main window
    # Use grid(row = , column =, and sticky (alignment) = ) to set placement
    tabOptions = Frame(window)
    tabOptions.grid(row = 0, column = 0, sticky = E)


    # Create frames to put into frames (nested frames) by settings first parameter to parent frame
    pmTab = Frame(tabOptions, bg="red", height = int((1 / 6) * float(height)), width = int((1 / 3) * float(width)))
    glTab = Frame(tabOptions, bg="green", height = int((1 / 6) * float(height)), width = int((1 / 3) * float(width)))
    rsTab = Frame(tabOptions, bg="blue", height = int((1 / 6) * float(height)), width = int((1 / 3) * float(width)))
    # Use the grid() to organize how items are placed; grid() refers to the grid system in attached frame/window
    pmTab.grid(row = 0, column = 0, sticky = NSEW);
    glTab.grid(row = 0, column = 1, sticky = NSEW);
    rsTab.grid(row = 0, column = 2, sticky = NSEW);

    # Step-By-Step process for the Pantry Tab
    
    # Disable the frame items from affecting frame size due to their grid placement
    pmTab.grid_propagate(False)
    # Create the text label by specifying the text, background color, and fount
    pmLabel = Label(pmTab, text = "Pantry", bg="red", font = fontStyleBody)
    pmLabel.grid(row = 0, column = 0, columnspan = 2)
    # Create the buttons with Button(<button text>, <function call>, <height>, <width>)
    pmButton1 = Button(pmTab, text = "Storage", command=lambda: buttonClicked("Pm1"), height=1, width=20)
    pmButton2 = Button(pmTab, text = "Data", command=lambda: buttonClicked("Pm2"), height=1, width=20)
    pmButton1.grid(row = 1, column = 0, sticky = W, padx = 30, pady=10)
    pmButton2.grid(row = 1, column = 1, sticky = E, padx = 30, pady=10)

    # Do the same for the grocery list tab
    glTab.grid_propagate(False)
    glLabel = Label(glTab, text = "Grocery List", bg="green", font = fontStyleBody)
    glLabel.grid(row = 0, column = 0, columnspan = 2)
    glButton1 = Button(glTab, text = "Active List", command=lambda: buttonClicked("Gm1"), height=1, width=20)
    glButton2 = Button(glTab, text = "All Lists", command=lambda: buttonClicked("Gm2"), height=1, width=20)
    glButton1.grid(row = 1, column = 0, sticky = W, padx = 30, pady=10)
    glButton2.grid(row = 1, column = 1, sticky = E, padx = 30, pady=10)


    # Then with the Recipe Storage
    rsTab.grid_propagate(False)
    rsLabel = Label(rsTab, text = "Recipes", bg="Blue", font = fontStyleBody)
    rsLabel.grid(row = 0, column = 0, columnspan = 2)
    rsButton1 = Button(rsTab, text = "Active Recipe", command=lambda: buttonClicked("Rs1"), height=1, width=20)
    rsButton2 = Button(rsTab, text = "All Recipe", command=lambda: buttonClicked("Rs2"), height=1, width=20)
    rsButton1.grid(row = 1, column = 0, sticky = W, padx = 30, pady=10)
    rsButton2.grid(row = 1, column = 1, sticky = E, padx = 30, pady=10)

    # Run Tkinter Window
    window.mainloop()
