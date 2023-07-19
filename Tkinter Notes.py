""" 
Tkinter Notes/Prototype 

This is to better understand how to use Tkinter to create the system's GUI.
Additionally, this will be used to create a prototype of the GUI as well.
"""
from tkinter import *
import tkinter.font as tkFont 

def buttonClicked(response):
    print("You Clicked " + response)

if __name__ == "__main__":
    # Creates the window to use
    window = Tk()
    fontStyleBody = tkFont.Font(family="Arial", size=36)

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
    tabOptions.grid(row = 0, sticky = N)

    # Setting to turn allow items to display even if exceed frame size
    #window.grid_propagate(False)

    # Create frames to put into frames by settings first parameter to parent frame
    pmTab = Frame(tabOptions, bg="red")
    glTab = Frame(tabOptions, bg="blue")
    rsTab = Frame(tabOptions, bg ="green")
    pmTab.grid(row = 0, column = 0, sticky = E);
    glTab.grid(row = 0, column = 1, sticky = E);
    rsTab.grid(row = 0, column = 2, sticky = E);


    # Create Text Entry with Label()
    pmLabel = Label(pmTab, text = "Pantry", font = fontStyleBody)
    glLabel = Label(glTab, text = "Groceries", font = fontStyleBody)
    rsLabel = Label(rsTab, text = "Recipes", font = fontStyleBody)
    pmLabel.grid(row = 0, column = 0, sticky = W);
    glLabel.grid(row = 0, column = 0, sticky = W);
    rsLabel.grid(row = 0, column = 0, sticky = W);

    # Create Buttons
    pmButton1 = Button(pmTab, text = "Storage", command=lambda: buttonClicked("Pm1"))
    pmButton2 = Button(pmTab, text = "Data", command=lambda: buttonClicked("Pm2"))
    pmButton1.grid(row = 1, column = 0, sticky = W)
    pmButton2.grid(row = 1, column = 1, sticky = W)

    glButton1 = Button(glTab, text = "Active List", command=lambda: buttonClicked("Gl1"))
    glButton2 = Button(glTab, text = "All Grocery Lists", command=lambda: buttonClicked("Gl2"))
    glButton1.grid(row = 1, column = 0, sticky = W)
    glButton2.grid(row = 1, column = 1, sticky = W)

    rsButton1 = Button(rsTab, text = "Recipes", command=lambda: buttonClicked("Rs1"))
    rsButton2 = Button(rsTab, text = "All Recipes", command=lambda: buttonClicked("Rs2"))
    rsButton1.grid(row = 1, column = 0, sticky = W)
    rsButton2.grid(row = 1, column = 1, sticky = W)




    
    # Run Tkinter Window
    window.mainloop()
