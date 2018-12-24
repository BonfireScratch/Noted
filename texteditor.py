from tkinter import *
import tkinter.filedialog
from tkinter import messagebox
import os
 
class TextEditor:

    @staticmethod
    def quit_app(event=None):
        root.quit()

    def open_file(self, event=None):
        global pastData
        global txt_file
        self.ask_for_save()
        
        txt_file = tkinter.filedialog.askopenfilename(parent=root,initialdir='/Desktop/')
        
        if txt_file:
            with open(txt_file) as _file:
                self.text_area.insert(1.0, _file.read())
                pastData = _file.read()
                root.update_idletasks()


    def new_file(self, event=None):
        self.ask_for_save()
 
    def save_file(self, event=None):
        file = tkinter.filedialog.asksaveasfile(mode='w')
        if file != None:
            data = self.text_area.get('1.0', END + '-1c')
            file.write(data)
            file.close
            pastData = data
            
    def ask_for_save(self, event=None):
        data = self.text_area.get('1.0', END + '-1c')
        if pastData == data:
            self.text_area.delete(1.0, END)
        elif data != None:
            response = messagebox.askyesnocancel('Noted', 'Do you want to save changes to this text file?')
            if response != None:
                if response == False:
                    self.text_area.delete(1.0, END)
                else:
                    self.save_file()
                    self.text_area.delete(1.0, END)
      
    def change_color(self, event=None):
        global c
        colors = ["white", "gray", "black", "green", "SpringGreen2", "light sea green", "blue", "navy", "deep sky blue", "cyan3", "aquamarine", "SteelBlue3", "red", "orange red", "orange", "sienna1", "indian red", "violet red"]
        c+=1
        if c == len(colors):
            c = 0
        self.set_color(colors[c])
            
    def set_color(self, color):
        self.text_area.configure(background=color)
        if color == "black":
            self.text_area.configure(foreground = "white")
        elif color == "blue" or color == "navy":
            self.text_area.configure(foreground = "white")
        else:
            self.text_area.configure(foreground = "black")
            
    def change_font(self, event=None):
        global a
        fnt = ["Heveltica", "Times", "verdana", "comic sans ms", "courier new", "fixedsys", "ms sans Serif", "ms Serif", "symbol", "times new roman"]
        siz = ["10", "10", "10", "8", "12", "9", "11", "16", "12", "16"]
        
        a+=1
        if a == len(fnt):
            a = 0
        self.set_font(fnt[a], siz[a])
        
    def set_font(self, fnt, siz):
        self.text_area.configure(font=(fnt, int(siz), ""))
    
    def delete_file(self, event=None):
        self.ask_for_delete()
        
    def ask_for_delete(self, event=None):
        response = messagebox.askyesnocancel('Noted', 'Do you want to delete this file?')
        if response != None:
            if response == False:
                self.text_area.delete(1.0, END)
            else:
                os.remove(self.get_path())
                self.text_area.delete(1.0, END)
                
    def get_path(self):
        return txt_file
    
    def __init__(self, root):
        self.text_to_write = ""
        root.title("Noted")
        root.geometry("600x550")
        frame = Frame(root, width=600, height=550)
        scrollbar = Scrollbar(frame)
        self.text_area = Text(frame, width=600, height=550,
                        yscrollcommand=scrollbar.set,
                        padx=20, pady=20)
        self.text_area.configure(background='white')
        self.text_area.configure(foreground = "black")
        scrollbar.config(command=self.text_area.yview)
        scrollbar.pack(side="right", fill="y")
        self.text_area.pack(side="left", fill="both", expand=True)
        frame.pack()
        the_menu = Menu(root)
        file_menu = Menu(the_menu, tearoff=0)
        settings_menu = Menu(the_menu, tearoff=0)
        settings_menu.add_command(label="Color", command=self.change_color)
        settings_menu.add_command(label="Font", command=self.change_font)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Delete", command=self.delete_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit_app)
        the_menu.add_cascade(label="File", menu=file_menu)
        the_menu.add_cascade(label="Settings", menu=settings_menu)
        root.config(menu=the_menu)

pastData = ""

c = 0 

a = 0
 
root = Tk()
 
text_editor = TextEditor(root)
 
root.mainloop()
