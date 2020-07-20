from tkinter import *
from tkinter import ttk
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="orange",fg="white")
        title.pack(side=TOP,fill=X)

        ##############MANAGE FRAME=============================
        Manage_Frame= Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=470,height=600)


        m_title=Label(Manage_Frame,text="Manage Students",bg="crimson",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll = Label(Manage_Frame, text="Roll No.", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1, column=0, padx=10,pady=10,sticky="w")

        txt_Roll=Entry(Manage_Frame, font=("times new roman", 15, "bold"),bd=2,relief=GROOVE)
        txt_Roll.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        lbl_name = Label(Manage_Frame, text="Name", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, padx=20, pady=10, sticky="w")

        txt_name = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=2, relief=GROOVE)
        txt_name.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        lbl_Email = Label(Manage_Frame, text="Email", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_Email.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        txt_Email = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=2, relief=GROOVE)
        txt_Email.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        lbl_Gender = Label(Manage_Frame, text="Gender", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_Gender.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        combo_Gender =ttk.Combobox(Manage_Frame,font=("times new roman", 13, "bold"),state='readonly')
        combo_Gender['values']=("male","female","other")
        combo_Gender.grid(row=4, column=1, padx=20, pady=10, sticky="w")

        lbl_Contact = Label(Manage_Frame, text="Contact", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_Contact.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        txt_Contact = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=2, relief=GROOVE)
        txt_Contact.grid(row=5, column=1, padx=20, pady=10, sticky="w")

        lbl_dob = Label(Manage_Frame, text="D.O.B", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_dob.grid(row=6, column=0, padx=10, pady=10, sticky="w")

        txt_dob = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=2, relief=GROOVE)
        txt_dob.grid(row=6, column=1, padx=20, pady=10, sticky="w")

        lbl_address = Label(Manage_Frame, text="Address", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_address.grid(row=7, column=0, padx=10, pady=10, sticky="w")

        txt_address = Text(Manage_Frame,width=20,height=4, font=("times new roman", 15, "bold"), bd=2, relief=GROOVE)
        txt_address.grid(row=7, column=1, padx=20, pady=10, sticky="w")

        #=========================Detail FRAME=============================

        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=500,y=100,width=830,height=600)

root =Tk()
ob=Student(root)
root.mainloop()

