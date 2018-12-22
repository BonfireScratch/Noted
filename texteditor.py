from tkinter import *
import tkinter.filedialog
from tkinter import messagebox
 
class TextEditor:

    @staticmethod
    def quit_app(event=None):
        root.quit()

    def open_file(self, event=None):
        self.ask_for_save()
        
        txt_file = tkinter.filedialog.askopenfilename(parent=root,initialdir='/Desktop/')
        
        if txt_file:
            with open(txt_file) as _file:
                self.text_area.insert(1.0, _file.read())
                root.update_idletasks()


    def new_file(self, event=None):
        self.ask_for_save()
 
    def save_file(self, event=None):
        file = tkinter.filedialog.asksaveasfile(mode='w')
        if file != None:
            data = self.text_area.get('1.0', END + '-1c')

            file.write(data)
            file.close()
            
    def ask_for_save(self, event=None):
        data = self.text_area.get('1.0', END + '-1c')
        
        if data != None:
            response = messagebox.askyesnocancel('TextEditor', 'Do you want to save changes to this text file?')
            if response != None:
                if response == False:
                    self.text_area.delete(1.0, END)
                else:
                    self.save_file()
                    self.text_area.delete(1.0, END)
        else:
            self.text_area.delete(1.0, END)
      
    def __init__(self, root):
        global pastData
        self.text_to_write = ""
        root.title("Text Editor")
        root.geometry("600x550")
        frame = Frame(root, width=600, height=550)
        scrollbar = Scrollbar(frame)
        self.text_area = Text(frame, width=600, height=550,
                        yscrollcommand=scrollbar.set,
                        padx=10, pady=10)
        scrollbar.config(command=self.text_area.yview)
        scrollbar.pack(side="right", fill="y")
        self.text_area.pack(side="left", fill="both", expand=True)
        frame.pack()
        the_menu = Menu(root)
        file_menu = Menu(the_menu, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit_app)
        the_menu.add_cascade(label="File", menu=file_menu)
        root.config(menu=the_menu)
 
root = Tk()
 
text_editor = TextEditor(root)
 
root.mainloop()
