from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import os
class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.wm_iconbitmap("Camera.ico")
        root.geometry("1350x700+0+0")

        #=============All Images==============
        self.bg_icon = ImageTk.PhotoImage(file="bg.PNG")
        self.user_icon = PhotoImage(file="a.png")
        self.pass_icon = PhotoImage(file="bb.PNG")
        self.logo_icon = PhotoImage(file="log.PNG")
        #===============variable==============
        self.uname=StringVar()
        self.pass_=StringVar()
        bg_lbl = Label(self.root, image=self.bg_icon).pack()
        title=Label(self.root,text="Login System",font=("lucida handwriting",40,"bold"), bg="orange",fg="white",bd=5,relief=RAISED)
        title.place(x=0,y=0,relwidth=1)

        Login_Frame=Frame(self.root,bg="light yellow",bd=5,relief=RAISED)
        Login_Frame.place(x=400,y=150)
        logolbl = Label(Login_Frame,image=self.logo_icon,bd=5,relief=RAISED).grid(row=0,columnspan=2,pady=20)

        lbluser = Label(Login_Frame , text="Username", image=self.user_icon, compound=LEFT,
                        font=("times new roman", 15, "bold", ), bg="white", bd=5,relief=RAISED).grid(row=1, column=0, padx=20, pady=20)

        txtuser = Entry(Login_Frame,bd=5, textvariable=self.uname, relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=25)

        lblpass = Label(Login_Frame, text="Password", image=self.pass_icon, compound=LEFT,
                        font=("times new roman", 15, "bold"), bg="white", bd=5,relief=RAISED).grid(row=2, column=0, padx=20, pady=20)
        txtpass = Entry(Login_Frame, bd=5, textvariable=self.pass_, relief=GROOVE, font=("", 15)).grid(row=2, column=1, padx=25)

        btn_log=Button(Login_Frame,text="Login",width=15,command=self.login,font=("times new roman", 14, "bold"), bg="orange", fg="black").grid(row=3, columnspan=2, pady=10)

    def login(self):
        if self.uname.get() == "" or self.pass_.get() == "":
            messagebox.showerror("Error", "All fields are Required")
        elif self.uname.get() == "Ashvinee" and self.pass_.get() == "root":
            messagebox.showinfo("Successfull", f"Welcome!!! {self.uname.get()}")
            os.system("python front.py")
        else:
            messagebox.showerror("Error", "Invalid Username or password")

root=Tk()
obj=Login_System(root)
root.mainloop()