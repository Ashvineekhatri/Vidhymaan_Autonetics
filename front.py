from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import os

def btnclick1():
   os.system("python dataset_capture.py")

def btnclick2():
   os.system("python training_dataSet.py")

def btnclick3():
   os.system("python recognizer.py")
   
def btnclick5():
   messagebox.showinfo("Successfull", "Welcome!!!")
#root =Tk()
#topFrame = Frame(root)
#topFrame.pack()
class Front:
   def __init__(self, root):
      self.root = root
      self.root.title("Vidhymaan Autonetics")
      self.root.wm_iconbitmap("Camera.ico")
      root.geometry("1350x700+0+0")

      # =============All Images==============
      self.bg_icon = ImageTk.PhotoImage(file="bg.PNG")
      self.pic2 = PhotoImage(file="Capture.PNG")
      self.pic1 = PhotoImage(file="Camera.PNG")
      self.pic3 = PhotoImage(file="Recognize.PNG")
      self.pic5 = PhotoImage(file="attend.PNG")
      self.pic6 = PhotoImage(file="Logout.png")
      #========================================
      bg_lbl = Label(self.root, image=self.bg_icon).pack()
      title = Label(self.root, text="Vidhymaan Autonetics", font=("lucida handwriting", 40, "bold"), bg="orange", fg="White", bd=5,
                    relief=RAISED)
      title.place(x=0, y=0, relwidth=1)
      Login_Frame = Frame(self.root, bg="light yellow", bd=5, relief=RAISED)
      Login_Frame.place(x=250, y=100)

      btn_log1 = Button(Login_Frame, image=self.pic1,bd=5,command=btnclick1,relief=GROOVE).grid(row=0,column=0,padx=5,pady=20)

      btn_log2 = Button(Login_Frame, image=self.pic2, bd=5,command=btnclick2,relief=GROOVE).grid(row=0, column=1, padx=5, pady=20)
      btn_log3 = Button(Login_Frame, image=self.pic3, bd=5,command=btnclick3,relief=GROOVE).grid(row=0, column=2, padx=5, pady=20)
      btn_log5 = Button(Login_Frame, image=self.pic5, bd=5,command=btnclick5, relief=GROOVE).grid(row=1, column=0, padx=5, pady = 5)
      btn_log6 = Button(Login_Frame, image=self.pic6, bd=5, command=exit,relief=GROOVE).grid(row=1, column=2, padx=5,pady=5)

root=Tk()
obj=Front(root)
root.mainloop()
