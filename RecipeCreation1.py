#Class for making the frames (first window is its own class, second window is another)
#second window will only make the frame, then another class will use it
#set default values for the checkboxes and entry/text boxes
#Recipe Creation v.1

import tkinter as tk
from tkinter import *

class first_window(tk.Toplevel):
    def __init__(self, root):
        root = root
        root.title('Recipe Creation & Organization')
        window = tk.Frame(root)
        root.rowconfigure(3, minsize = 200, weight = 1)
        root.columnconfigure(2, minsize = 400, weight = 1)

        b1 = tk.Button(text = 'Create new recipe', command = lambda: self.create_new_recipe())
        b2 = tk.Button(text = 'Open saved recipe', command = lambda: self.open_saved_recipe(root))
        b3 = tk.Button(text = 'Schedule recipes', command = lambda: self.schedule_recipes(root))
        
        b1.grid(column = 2, row = 1, pady = 60, ipadx = 5, ipady = 5)
        b2.grid(column = 2, row = 2, pady = 10)
        b3.grid(column = 2, row = 3, pady = 10)

        b2['state'] = DISABLED
        b3['state'] = DISABLED

        root.mainloop()

    def create_new_recipe(self):
        #close/hide/destroy first window
        root.destroy()
        second_window()
        
    '''Button calls for later!!!
    def open_saved_recipe(self, root):
        self.root = root
        tk.Toplevel(root, text = 'Function currently not available')
        pass

    def schedule_recipes(self, root):
        tk.Toplevel(root, text = 'Function currently not available')
        pass
    '''

class second_window(tk.Toplevel):
    def __init__(self):
        #making the window and setting up the variables to be edited in future windows
        root = tk.Tk()
        root.title('Recipe Creation')
        win = tk.Frame(root)
        #setting the variables for the checkboxes
        self.breakfast_var = tk.BooleanVar()
        self.lunch_var = tk.BooleanVar()
        self.dinner_var = tk.BooleanVar()
        self.snack_var = tk.BooleanVar()
        self.dessert_var = tk.BooleanVar()
        self.vegan_var = tk.BooleanVar()
        self.gluten_free_var = tk.BooleanVar()
        self.vegetarian_var = tk.BooleanVar()
        self.pescetarian_var = tk.BooleanVar()
        self.otherType_var = tk.BooleanVar()
        self.otherTime_var = tk.BooleanVar()
        #setting variables for entry boxes
        self.recipe_name = tk.StringVar()
        self.other_time_var = tk.StringVar()
        self.other_type_var = tk.StringVar()

        entryName = tk.Entry(root, width = 40, background = 'lightCyan2', textvariable = self.recipe_name)
        entryName.insert(END, 'Name')
        entryName.grid(column = 2, row = 2, sticky='w',columnspan=3)
        label_recipe_name = tk.Label(root, text='Recipe name: ').grid(column = 1, row = 2, sticky = 'e')
        #setting description for recipe
        self.description = tk.Text(root, width = 60, height = 10, background = 'lightCyan2')
        self.description.insert(END, 'Description')
        self.description.grid(column = 2, row = 3,sticky='sw',columnspan=3)
        label2_recipe_name = tk.Label(root, text='Recipe description: ').grid(column = 1, row = 3,sticky = 'e')

        label3 = Label(root, text="Please select the Categories in which your recipe falls. \nCan select multiple.")
        label3.grid(column = 2, row = 6,sticky ='w', columnspan = 3, pady = 30)

        #Layout of the frame
        
        chk1 = tk.Checkbutton(root, text='Breakfast', variable = self.breakfast_var)
        chk1.grid(column = 1, row = 8, sticky='w', pady = 5, padx = 5)
        
        chk2 = tk.Checkbutton(root, text='Lunch', variable = self.lunch_var)
        chk2.grid(column = 1, row = 9, sticky='w', pady = 5, padx = 5)
        
        chk3 = tk.Checkbutton(root, text='Dinner', variable = self.dinner_var)
        chk3.grid(column = 1, row = 10, sticky='w', pady = 5, padx = 5)
        
        chk4 = tk.Checkbutton(root, text='Snack', variable = self.snack_var)
        chk4.grid(column = 1, row = 11, sticky='w', pady = 5, padx = 5)
        
        chk5 = tk.Checkbutton(root, text='Dessert', variable = self.dessert_var)
        chk5.grid(column = 1, row = 12, sticky='w', pady = 5, padx = 5)
        
        entry1 = tk.Entry(root, text='Other', textvariable = self.other_time_var)
        entry1.grid(column = 2, row = 13, sticky='w', pady = 5, padx = 5)
        chkOther= tk.Checkbutton(root, text='Other:', variable = self.otherTime_var).grid(column=1, row = 13,sticky = 'w', pady = 5, padx = 5)
     
        chk6 = tk.Checkbutton(root, text='Vegan', variable = self.vegan_var)
        chk6.grid(column = 3, row = 8, sticky='w', pady = 5, padx = 5)
        
        chk7 = tk.Checkbutton(root, text='Gluten Free', variable = self.gluten_free_var)
        chk7.grid(column = 3, row = 9, sticky='w', pady = 5, padx = 5)
 
        chk8 = tk.Checkbutton(root, text='Vegetarian', variable = self.vegetarian_var)
        chk8.grid(column = 3, row = 10, sticky='w', pady = 5, padx = 5)

        chk9 = tk.Checkbutton(root, text='Pescetarian', variable = self.pescetarian_var)
        chk9.grid(column = 3, row = 11, sticky='w', pady = 5, padx = 5)
        
        entry2 = tk.Entry(root, text='Other', textvariable = self.other_type_var)
        entry2.grid(column = 4, row = 12, sticky='w', pady = 5, padx = 5)
        chkOther2 = tk.Checkbutton(root, text='Other:', variable = self.otherType_var).grid(column = 3, row = 12, sticky = 'w', pady = 5, padx = 5)

        #button to go to the next window
        nextB = tk.Button(root, text="Next", command=lambda: recipe_specifics(self, root))
        nextB.grid(column = 5, row = 15, sticky='se', pady = 10, padx = 30, ipadx = 30)

        #quit button
        quitB = tk.Button(root, text="Quit", command = lambda:quit(root))
        quitB.grid(column = 5, row = 1, sticky='ne', pady = 10, padx = 30, ipadx = 30)

    #method to quit the program using a handy dandy button
    def quit(self, parent):
        self.parent = parent
        parent.destroy()

#method outside of the class so I can use it in other classes
def recipe_specifics(self, root):
        
    #times list
    self.times = []
    self.breakfast = self.breakfast_var.get()
    self.lunch = self.lunch_var.get()
    self.dinner = self.dinner_var.get()
    self.snack = self.snack_var.get()
    self.dessert = self.dessert_var.get()
    self.otherTime = self.otherTime_var.get()
    self.otherTime_entry = self.other_time_var.get()

     #categories list
    self.categories = []
    self.vegan = self.vegan_var.get()
    self.gluten_free = self.gluten_free_var.get()
    self.pescetarian = self.pescetarian_var.get()
    self.otherType = self.otherType_var.get()
    self.otherType_entry = self.other_type_var.get()

    #If loops to populate times list depending on what check button was clicked
    if self.breakfast == True:
        self.times.append('Breakfast')
    if self.lunch == True:
        self.times.append('Lunch')    
    if self.dinner == True:
        self.times.append('Dinner')  
    if self.dessert == True:
        self.times.append('Dessert')  
    if self.snack == True:
        self.times.append('Snack')
    if self.otherTime == True:
        self.times.append(self.otherTime_entry)  
    #if loops to poppulate categories list depending on what check button was clicked
    if self.vegan == True:
        self.categories.append('Vegan')
    if self.gluten_free == True:
        self.categories.append('Gluten Free')
    if self.pescetarian == True:
        self.categories.append('Pescetarian')
    if self.otherType == True:
        self.categories.append(self.otherType_entry)

    #destroying the window that gets the input for all these settings, (second window)
    root.destroy()

    recipe_editor(self.times, self.categories)

        
class recipe_editor():
    def __init__(self, times, categories):

        #setting up the times and categories lists to transfer over to this class
        self.times = times
        self.categories = categories
        #calling function to make window for editable recipe
        self.recipe_editor_window(times, categories)

    def recipe_editor_window(self, times, categories):
        #print(self.times, self.categories)
        #make window to edit recipe
        editor_window = tk.Tk()
        editor_window.title('Recipe Editor')
        editor_window.rowconfigure(3, minsize = 800, weight = 1)
        editor_window.columnconfigure(2, minsize = 800, weight = 1)

        frame = tk.Frame(editor_window)
        #text = tk.Text(editor_window, height = 40, width = 20)
        #text.grid(row = 1, column = 1)



        #button to quit
        b_quit = tk.Button(editor_window, text = 'Quit', command = lambda: quit_editor(self, editor_window))
        b_quit.grid(row = 5, column = 5, padx = 10, pady = 10, ipadx = 5, ipady = 5)

        #method to quit and make sure that the user wants to quit before actually quitting
        def quit_editor(self, parent):
            new_root = tk.Tk()
            new_root.title('Recipe Creator')
            quit_q = tk.Frame(new_root)
            quit_q.rowconfigure(0, minsize = 300, weight = 1)
            quit_q.columnconfigure(0, minsize = 200, weight = 1)
            msg = tk.Label(new_root, text = 'Are you sure you would like to quit?')

            def quit_application(self, parent):
                parent.destroy()
                new_root.destroy()

            b1 = tk.Button(new_root, text = 'Yes (Quit)', command = lambda: quit_application(self, parent))
            b2 = tk.Button(new_root, text = 'No (Do not quit)', command = lambda: new_root.destroy())

            b1.grid(row = 2, column = 1, padx = 10, pady = 20)
            b2.grid(row = 2, column = 2, padx = 10, pady = 20)
            msg.grid(row = 1, column = 1, columnspan = 2, padx = 20, pady = 20)

    
        

        #radiobutton for menu?
        #need save and potentially open button
        #back button?
        #ingredients list to choose from on left side of window
        #'other' option for other ingredients
        #Need to draw up templates, maybe 3. 
            #want to have a window pop up that displays the potential options for templates
            #then user can choose which template
            #GOAL is to have one template by end of quarter

        #templates will probably have the 'times' and 'categories' lists displayed somewhere
            #as well as The recipe name, and notes, and description in a particular place.
            #need to have recipe name and description editable

        

        

    
        



       
           


if __name__ == '__main__':
    
    root = tk.Tk()
    first_window(root)

    '''
    references for getting variables from tkinter

        print(self.description.get('1.0', END))

        if self.varB.get() == 0:
            print('Not breakfast time')
        else:
            print('breakfast time')

        print(self.otherTime.get())

        #print(tk.grid_slaves(row = 11, column = 1))

        #print(self.varB.get()) 
        '''
