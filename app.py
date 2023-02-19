from tkinter import Label
import customtkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import subprocess
import Database as db

def execute_python_file(file_path):
    subprocess.call(['python', file_path])


ash = tk.CTk()


for i in range(3):
    for j in range(3):
        cell = Label(ash, text="", width=10, height=5,bg="#c4cbca")
        cell.grid(row=i, column=j)


ash.geometry("1920x1080")  # Sets Window size
ash.title("Attendance System")

title = Label(text="Attendance System", bg="#AFEDA1",font=("Courgette", 20, "bold"), pady=10)
title.place(relx=0.5, y=0, anchor='n', width=1920)

bottom = Label(text="Malay Vyas | Manan Patel | Jainil Chauhan | Ashish Prajapati", bg="#AFEDA1")
bottom.place(relx=0.5, rely=1.0, anchor='s', width=1920)


def run():
    execute_python_file(r'main.py')



frame = Frame(ash, borderwidth=5, bg="#70ABA0")
frame.grid(row=5, column=0)


frame2 = Frame(ash, borderwidth=5, bg="#70ABA0")
frame2.grid(row=7, column=2)


b1 = Button(frame, fg="black", text="Take Attendance", command=run,width=15)
b1.grid(row=4, column=0)

cell = Label(ash, text="", width=120,bg="#c4cbca")
cell.grid(row=4, column=0)

register_label = Label(ash, text="Register", font=("Courgette", 14, "bold"), bg="#c4cbca")
register_label.grid(row=2, column=1, padx=10, pady=10)

l1 = Label(ash, text="Name",width=10)
l2 = Label(ash, text="Semester",width=10)
l3 = Label(ash, text="Roll No",width=10)
l4 = Label(ash, text="Branch",width=10)

name = StringVar()
sem = IntVar()
rollno = StringVar()
branch = StringVar()

Name = Entry(ash, textvariable=name)
Semester = Entry(ash, textvariable=sem)
Rollno = Entry(ash, textvariable=rollno)
Branch = Entry(ash, textvariable=branch)

l1.grid(row=3, column=1, padx=10, pady=10)
l2.grid(row=4, column=1, padx=10, pady=10)
l3.grid(row=5, column=1, padx=10, pady=10)
l4.grid(row=6, column=1, padx=10, pady=10)

Name.grid(row=3, column=2, padx=10, pady=10)
Semester.grid(row=4, column=2, padx=10, pady=10)
Rollno.grid(row=5, column=2, padx=10, pady=10)
Branch.grid(row=6, column=2, padx=10, pady=10)



def buttonclick():
    db.add(name=name.get(), rollno= rollno.get(), sem= sem.get(), branch=branch.get())
    # print(name.get(), rollno.get(), sem.get(), branch.get())
    # print("Yes")
    name.set("")
    rollno.set("")
    sem.set("")
    branch.set("")


sub = Button(frame2, fg="black", text="Submit", command=buttonclick)
sub.grid(row=7, column=2)

ash.minsize(1080, 720)
ash.config(bg="#c4cbca")
ash.mainloop()
