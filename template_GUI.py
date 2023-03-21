import tkinter as tk
from tkinter import ttk

class App():
    def __init__(self):
        #Create GUI
        self.root = tk.Tk()
        self.root.geometry('350x250')
        self.root.title("Test GUI")
        self.mainframe = tk.Frame(self.root, background='white')
        self.mainframe.pack(fill='both', expand=True)
        
        #Create GUI header
        self.text = ttk.Label(self.mainframe, text='Hello World', background='white', font=("Brass Mono", 30))
        self.text.grid(row=0, column=0)
        
        #Set text field for input
        self.set_text_field = ttk.Entry(self.mainframe)
        self.set_text_field.grid(row=1, column=0, pady=10, sticky='NWES')
        set_text_button = ttk.Button(self.mainframe, text='Set Text', command=self.set_text)
        set_text_button.grid(row=1, column=1, pady=10)
        
        #Set text color in GUI
        color_options = ['red', 'blue', 'green', 'grey', 'purple', 'pink', 'black']
        self.set_color_field = ttk.Combobox(self.mainframe, values=color_options)
        self.set_color_field.grid(row=2, column=0, pady=10, sticky='NWES')
        set_color_button = ttk.Button(self.mainframe, text='Set Text', command=self.set_color)
        set_color_button.grid(row=2, column=1, pady=10)
        
        #Reverse text
        self.reverse_text = ttk.Button(self.mainframe, text='Reverse Text', command=self.reverse)
        self.reverse_text.grid(row=3, column=0, pady=10, sticky='NWES')
        
        #Loop code
        self.root.mainloop()
        return
    
    #Set text button in GUI
    def set_text(self):
        newtext = self.set_text_field.get()
        self.text.config(text=newtext)
    
    #Set text color button in GUI
    def set_color(self):
        newcolor = self.set_color_field.get()
        self.text.config(foreground=newcolor)
    
    #Set reverse text button in GUI
    def reverse(self):
        newtext = self.text.cget('text')
        reversed = newtext[::-1]
        self.text.config(text=reversed)

if __name__ == '__main__':
    App()