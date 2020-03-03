#finalProject User interface code
#Sarah Kercheval
#!/usr/bin/env python
#implementing tkinter and creating an user interface

import tkinter as tk
from tkinter import *

class first_window(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(parent)
        parent.title('Recipe Creator and Organizer')
        parent.rowconfigure(3, minsize=300,weight = '1')
        parent.columnconfigure(2, minsize=300,weight='1')
        label = tk.Label(parent, text='Please select an option').grid(column = 2, row = 1, pady = 20)
        #create buttons
        b1 = tk.Button(parent, text="Create new recipe", background='green', command=lambda: second_window(parent))
        b2 = tk.Button(parent, text='Open saved recipe')
        b3 = tk.Button(parent, text='Schedule recipes')
        #disable button 2 and 3 cause not using them rn
        b2['state'] = DISABLED
        b3['state'] = DISABLED
        #setting up the buttons where they need to be
        b1.grid(column = 2, row = 2)#, padx=10, pady=10)
        b2.grid(column = 2, row = 3, padx=10, pady=10)
        #b3.grid(column = 2, row = 4, sticky='n', padx=10, pady=10)
        
        #run the program
        parent.mainloop()

    def destroy(self):
        self.destroy()
        
        
class second_window(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.geometry('800x700')
        self.parent = parent
        parent.title('Categories')
        tk.Label(parent, text='Please fill out the following; ').grid(column = 2, row = 1)
        self.recipe_name = Entry(parent, width = 40)
        self.recipe_name.grid(column = 2, row = 2, sticky='w',columnspan=3)
        self.description = Entry(parent, width = 40)
        self.description.grid(column = 2, row = 3,sticky='w',columnspan=3, ipady = 20)
        tk.Scrollbar(self.description)
        tk.Label(text='Recipe name: ').grid(column = 1, row = 2, sticky = 'e')
        tk.Label(text='Brief recipe description: ').grid(column = 1, row = 3,sticky = 'e')
        tk.Label(text="Please select the Categories in which your recipe falls. \nCan select multiple.").grid(column = 2, row = 6,sticky ='w', columnspan = 3, pady = 30)
        #categories
        self.breakfast = Checkbutton(parent, text='Breakfast')
        self.breakfast.grid(column = 1, row = 8, sticky='w', pady = 5, padx = 5)
        self.lunch = Checkbutton(parent, text='Lunch')
        self.lunch.grid(column = 1, row = 9, sticky='w', pady = 5, padx = 5)
        self.dinner = Checkbutton(parent, text='Dinner')
        self.dinner.grid(column = 1, row = 10, sticky='w', pady = 5, padx = 5)
        self.snack = Checkbutton(parent, text='Snack')
        self.snack.grid(column = 1, row = 11, sticky='w', pady = 5, padx = 5)
        self.dessert = Checkbutton(parent, text='Dessert')
        self.dessert.grid(column = 1, row = 12, sticky='w', pady = 5, padx = 5)
        self.otherTime = Entry(parent, text='Other')
        self.otherTime.grid(column = 2, row = 13, sticky='w', pady = 5, padx = 5)
        tk.Checkbutton(text='Other:').grid(column=1, row = 13,sticky = 'w', pady = 5, padx = 5)

        self.vegan = Checkbutton(parent, text='Vegan')
        self.vegan.grid(column = 3, row = 8, sticky='w', pady = 5, padx = 5)
        self.gluten_free = Checkbutton(parent, text='Gluten Free')
        self.gluten_free.grid(column = 3, row = 9, sticky='w', pady = 5, padx = 5)
        self.vegetarian = Checkbutton(parent, text='Vegetarian')
        self.vegetarian.grid(column = 3, row = 10, sticky='w', pady = 5, padx = 5)
        self.pescetarian = Checkbutton(parent, text='Pescetarian')
        self.pescetarian.grid(column = 3, row = 11, sticky='w', pady = 5, padx = 5)
        self.otherType = Entry(parent, text='Other')
        self.otherType.grid(column = 4, row = 12, sticky='w', pady = 5, padx = 5)
        tk.Checkbutton(text='Other:').grid(column = 3, row = 12, sticky = 'w', pady = 5, padx = 5)

        #button to go to the next window
        self.next = tk.Button(parent, text="Next", command=lambda: recipe_specifics())
        self.next.grid(column = 5, row = 15, sticky='se', pady = 10, padx = 30, ipadx = 30)
        #button to quit
        self.quit = tk.Button(parent, text="Quit", command = lambda:quit(parent))
        self.quit.grid(column = 5, row = 1, sticky='ne', pady = 10, padx = 30, ipadx = 30)
        #back button



        parent.mainloop()
    #method to quit the program using a handy dandy button
    def quit(parent):
        self.parent = parent
        parent.destroy()


class recipe_specifics(tk.Frame):
    def __init__(self):
        

        pass
    

if __name__ == '__main__':
    root = tk.Tk()
    first_window(root)#passing in root as the top level 'parent'

    #root.mainloop()









def comments():
    '''
    from tkinter import *
    from tkinter import ttk

    fields = 'Recipe Name', 'Description', 'Author Name'
    def openFile():
        print("open file plz")
        pass

    def categories(mainframe):
        mainframe.withdraw()
        print('categories')
        pass

    def schedule():
        pass

    root = Tk()
    mainframe = ttk.Frame(root, background = 'grey', padx = 5, pady = 5, borderwidth = 3, relief = 'sunken')
    mainframe.title(text= 'Recipe Creation and Organizer')


    root = Tk()
    root.title('Recipe Creation and Organizer')
    #directions for tkinter to know what to do if the window expands, how it fills up the white space
    root.columnconfigure(0, weight = 1)
    root.rowconfigure(0, weight = 1)

    firstframe = ttk.Frame(root, padding = "12 12", borderwidth=3, relief = 'raised')
    #grid for firstframe. WIll be used to put widgets into places
    firstframe.grid(column=5, row=5, sticky=(N,S,E,W))

    #making a label
    ttk.Label(firstframe, text='Please select an option').grid(column = 2, row = 1, sticky = N)

    b1 = ttk.Button(firstframe, text= 'Create new recipe',command = categories())
    b2 = ttk.Button(firstframe, text='Open saved recipe', command = openFile)
    #disabling the button until later on in development of the program
    b2.state(['disabled'])
    b3 = ttk.Button(firstframe, text='Schedule recipes', command = schedule)
    #disabling the button until later on in development of the program
    b3.state(['disabled'])

    ttk.Label(firstframe, text="Button still in beta testing, please try again later").grid(column=2, row=5, sticky=E)
    ttk.Label(firstframe, text="Button still in beta testing, please try again later").grid(column=2, row=7, sticky=E)

    #assigning the locations of the buttons inside the firstframe
    b1.grid(column=2, row=2, sticky = N)
    b2.grid(column=2, row=4, sticky = N)
    b3.grid(column=2, row=6, sticky = S)

    #button color
    #b1.tk_setPalette(highlightColor='Green')

    for child in firstframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()


    from tkinter import *
    from tkinter import ttk

    root = ttk.Tk()

    def foobar(input):
        pass

    def create_window():
        return ttk.TopLevel(root)

    if __name__ == '__main__':
        #assigning root to the gui, then setting the title of the window 
        
        root.title("Recipe Creation and Organization")

        #creating the main frame of the window
        #setting padding, border, and type of border
        mainframe = ttk.Frame(root, padding="12 12", borderwidth=3, relief= 'sunken')


        #creating a grid in order to let tkinter know where to put the smaller 'widgets'
        #providing directions also helps place the widgets
        mainframe.grid(column=5, row=5, sticky=(N, S, E, W)) 

        #telling the frame to expand into place if it's expanded
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        #making buttons!
        #command=create.grid(column=2, row=2, sticky=N)
        #command=openSaved.grid(column=2, row=3, sticky=N)
        #comaand=schedule.grid(column=2, row=4, sticky=S)
        button1 = ttk.Button(mainframe, text="Create new recipe", command=create_window)
        button1.grid(column=2, row=2, sticky=N)

        button2 = ttk.Button(mainframe, text="Open saved recipe")
        button2.grid(column=2, row=3, sticky=N)
        button2.state(['disabled'])

        button3 = ttk.Button(mainframe, text="Schedule recipes")
        button3.grid(column=2, row=5, sticky=S)
        button3.state(['disabled'])

        #buttonOne.state(['disabled'])

        #label
        ttk.Label(mainframe, text="Please select an option").grid(column=2, row=1, sticky=N)

        #labeling the buttons that don't work
        ttk.Label(mainframe, text="Button still in beta testing, please try again later").grid(column=2, row=4, sticky=E)
        ttk.Label(mainframe, text="Button still in beta testing, please try again later").grid(column=2, row=6, sticky=E)

        #setting up the widgets to look nice and not too close together
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
            
        #telling tk to enter its event loop, to make it run
        root.mainloop()
    '''
    '''
    import tkinter as tk


    def new_window(Win_class):
        global win2
        try:
            if win2.state() == "normal": win2.focus()
        except:
            win2 = tk.Toplevel(win)
            Win_class(win2)

    class Win2:
        def __init__(self, root):
            self.root = root
            self.root.geometry("300x300+500+200")
            self.root["bg"] = "red"


    win = tk.Tk()
    win.title('Recipe Creation and Organization')
    win.geometry("200x200+200+100")
    button = tk.Button(win, text="Open new Window")
    button['command'] = lambda: new_window(Win2)
    button.pack()
    text = tk.Text(win, bg='red')
    text.pack()
    win.mainloop()
    '''

