import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import Message ,Text
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font

class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Dataset Capture")
        self.root.wm_iconbitmap("Camera.ico")
        root.geometry("530x260+470+250")
        fm = Frame(root, bg="light yellow", bd=5, relief=RAISED)
        fm.place(x=0, y=0)
        user_icon = PhotoImage(file="a.png")
        face_id = Label(fm, text="Enter your id", image=user_icon, compound=LEFT, font=("times new roman", 15, "bold",),
                        bg="white", bd=5, relief=RAISED).grid(row=1, column=0, padx=20, pady=20)
        self.uid = StringVar()
        txtuser = Entry(fm, bd=5, textvariable=self.uid, relief=GROOVE, font=("", 15)).grid(row=1, column=1, padx=25)

        face_id1 = Label(fm, text="Enter your name", image=user_icon, compound=LEFT, font=("times new roman", 15, "bold",),
                        bg="white", bd=5, relief=RAISED).grid(row=2, column=0, padx=20, pady=20)
        self.name = StringVar()
        txtuser1 = Entry(fm, bd=5, textvariable=self.name, relief=GROOVE, font=("", 15)).grid(row=2, column=1, padx=25)
        btn_log= Button(fm, text="OK", width=15, command=self.login, font=("times new roman", 14, "bold"),
                         bg="orange", fg="black").grid(row=3, columnspan=2, pady=10)



    def login(self):
        Id = self.uid.get()
        name = self.name.get()

        def is_number(self, s):
            try:
                float(s)
                return True
            except ValueError:
                pass

            try:
                import unicodedata
                unicodedata.numeric(s)
                return True
            except (TypeError, ValueError):
                pass

            return False
        if (is_number(self,Id) and name.isalpha()):
            def assure_path_exists(path):
                dir = os.path.dirname(path)
                if not os.path.exists(dir):
                    os.makedirs(dir)

                    # Start capturing video

            vid_cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

            # Detect object in video stream using Haarcascade Frontal Face
            face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

            # Initialize sample face image
            count = 0

            assure_path_exists("dataset/")

            # Start looping
            while (True):

                # Capture video frame
                _, image_frame = vid_cam.read()

                # Convert frame to grayscale
                gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

                # Detect frames of different sizes, list of faces rectangles
                faces = face_detector.detectMultiScale(gray, 1.3, 5)

                # Loops for each faces
                for (x, y, w, h) in faces:
                    # Crop the image frame into rectangle
                    cv2.rectangle(image_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                    # Increment sample face image
                    count += 1

                    # Save the captured image into the datasets folder
                    # cv2.imwrite("dataset/User." + str(Id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])
                    # Save the captured image into the datasets folder
                    cv2.imwrite("dataset/User." + str(Id) + '.' + str(name) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])

                    # Display the video frame, with bounded rectangle on the person's face
                    cv2.imshow('frame', image_frame)

                # To stop taking video, press 'q' for at least 100ms
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    break

                # If image taken reach 100, stop taking video
                elif count >= 30:
                    messagebox.showinfo("Done", "Successfully Captured")
                    break
            # Stop video
            vid_cam.release()
            cv2.destroyAllWindows()

            res = "Images Saved for ID : " + Id + " Name : " + name
            row = [Id, name]
            with open('StudentDetails\StudentDetails.csv', 'a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
            csvFile.close()
            messagebox.showinfo("Successfull", res)

        else:
            if (is_number(Id)):
                res = "Enter Alphabetical Name"
                messagebox.showinfo("Error", res)
            if (name.isalpha()):
                res = "Enter Numeric Id"
                messagebox.showinfo("Error", res)




root=Tk()
obj=Login_System(root)
root.mainloop()



