from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow
from tkinter import messagebox
class Register:
  def __init__(self,root):
    self.root=root
    self.root.title("Register")
    self.root.geometry("1600x900+0+0")
    
    self.bg=ImageTk.PhotoImage(file="")
    
if __name__=="__main__":
  root=Tk()
  app=Register(root)
  root.mainloop()