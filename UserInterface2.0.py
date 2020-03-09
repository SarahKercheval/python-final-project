#User interface 2.0
#make the first frame not connected to the second frame
#have the first frame be 'toplevel'?


from tkinter import *
import tkinter as tk

class first_window(tk.Toplevel):
    def __init__(self, root):
        self.root = root
        self.root.title('Recipe Creation and Organization')
        self.window = tk.Frame(root)
        self.window.rowconfigure(3,minsize = 300, weight = '1')
        self.window.columnconfigure(2, minsize = 500, weight = '1')

        self.b1 = tk.Button(text = 'Create new recipe', command = lambda: self.create_new_recipe())
        self.b2 = tk.Button(text = 'Open saved recipe', command = lambda: self.open_saved_recipe(root))
        self.b3 = tk.Button(text = 'Schedule recipes', command = lambda: self.schedule_recipes(root))
        
        self.b1.grid(column = 2, row = 1, padx = 20, pady = 15)
        self.b2.grid(column = 2, row = 2, padx = 20, pady = 15)
        self.b3.grid(column = 2, row = 3, padx = 20, pady = 15)

        self.b2['state'] = DISABLED
        self.b3['state'] = DISABLED

        root.mainloop()

       

    def create_new_recipe(self):
        #close/hide/destroy first window
        root.destroy()
        second_window()
        
'''
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
        #make the second window
        parent = tk.Tk()
        self.parent = parent
        self.parent.title('Create New Recipe')
        self.window2 = tk.Frame(parent)
        
        recipe_name = StringVar
        self.recipe_name = Entry(parent, width = 40, background = 'lightCyan2')
        self.recipe_name.grid(column = 2, row = 2, sticky='w',columnspan=3)
        self.label_recipe_name = Label(parent, text='Recipe name: ').grid(column = 1, row = 2, sticky = 'e')

        self.description = Text(parent, width = 60, height = 10, background = 'lightCyan2')
        self.description.grid(column = 2, row = 3,sticky='sw',columnspan=3)
        self.label2_recipe_name = Label(parent, text='Brief recipe description: ').grid(column = 1, row = 3,sticky = 'e')
        #Scrollbar(parent, self.description)

        self.label3 = Label(parent, text="Please select the Categories in which your recipe falls. \nCan select multiple.")
        self.label3.grid(column = 2, row = 6,sticky ='w', columnspan = 3, pady = 30)

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
        self.otherLabel = Checkbutton(parent, text='Other:').grid(column=1, row = 13,sticky = 'w', pady = 5, padx = 5)

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
        self.otherLabel2 = Checkbutton(parent, text='Other:').grid(column = 3, row = 12, sticky = 'w', pady = 5, padx = 5)

        #button to go to the next window
        self.next = tk.Button(parent, text="Next", command=lambda: self.recipe_specifics(parent))
        self.next.grid(column = 5, row = 15, sticky='se', pady = 10, padx = 30, ipadx = 30)

        #button to quit
        self.quit = tk.Button(parent, text="Quit", command = lambda:quit(parent))
        self.quit.grid(column = 5, row = 1, sticky='ne', pady = 10, padx = 30, ipadx = 30)

        parent.mainloop()

    #method to quit the program using a handy dandy button
    def quit(self, parent):
        self.parent = parent
        parent.destroy()

       
    def recipe_specifics(self, parent):
        self.parent = parent
        parent.destroy()
        newParent = tk.Tk()
        newParent.title(self.recipe_name)




if __name__ == '__main__':
    root = tk.Tk()
    first_window(root)
    