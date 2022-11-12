import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
from cgpa import sgpa
import mysql.connector

global sub1_entry,sub2_entry,sub3_entry,sub4_entry,sub5_entry,sub6_entry,sub7_entry,sub8_entry,sub9_entry
global username_entry, password_entry,mycursor

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="toor",
    database="bytecoders"
    )

mycursor = mydb.cursor()


def temp_text(e):
   username_entry.delete(0,"end")

def temp_pass(e):
   password_entry.delete(0,"end")

def calculate():
    sub1 = int(sub1_entry.get())
    sub2 = int(sub2_entry.get())
    sub3 = int(sub3_entry.get())
    sub4 = int(sub4_entry.get())
    sub5 = int(sub5_entry.get())
    sub6 = int(sub6_entry.get())
    sub7 = int(sub7_entry.get())
    sub8 = int(sub8_entry.get())
    sub9 = int(sub9_entry.get())
    res = sgpa([sub1,sub2,sub3,sub4,sub5,sub6,sub7,sub8,sub9])

    sub1_entry.delete(0,tk.END)
    sub2_entry.delete(0,tk.END)
    sub3_entry.delete(0,tk.END)
    sub4_entry.delete(0,tk.END)
    sub5_entry.delete(0,tk.END)
    sub6_entry.delete(0,tk.END)
    sub7_entry.delete(0,tk.END)
    sub8_entry.delete(0,tk.END)
    sub9_entry.delete(0,tk.END)

    showinfo("SGPA Calculated Successfully",f"Your SGPA is {res} / 10")


def check_if_member(username,password):
    mycursor.execute("select * from members")
    all_members = mycursor.fetchall()
    if (username,password) in  all_members:
        return True
    else:
        return False

def allow_entry():
    pass


def login():
    try:
        username = username_entry.get()
        password = password_entry.get()
        if check_if_member(username,password):
            allow_entry()
        else:
            showerror("Invalid Credentials","You have entered a Wrong Username or Password / Don't have an account")

    except:
        showerror("Something Went Wrong","We are sorry, Please try again later")

def register_user(username,password):
    try:
        query = f'insert into members(username,password) values("{username}","{password}");'
        mycursor.execute(query)
        mydb.commit()
        showinfo("Account Made","Your Account is successfully made! Please Login!")
    except:
        mydb.rollback()
        showerror("Something Went Wrong","We are sorry, Please try again later")



def register():
    try:
        username = username_entry.get()
        password = password_entry.get()
        if check_if_member(username,password):
            showerror("You already have an account","You already have an account, please login!")
        else:
           register_user(username,password)         

    except:
        showerror("Something Went Wrong","We are sorry, Please try again later")


def user_profile():
    global username_entry, password_entry

    root.geometry("600x370+100+100")
    screen2 = tk.Toplevel()
    screen2.title("User Profile")
    screen2.geometry('350x500+610+200')
    screen2.resizable(0, 0)
    screen2.iconbitmap('ic.ico')
    screen2.config(bg='#1F1F1F')

    logo_img_2 = tk.PhotoImage(file='./buttons/logo_2.png')
    logo_img_label= tk.Label(screen2,image=logo_img_2)
    logo_img_label.place(x=75,y=20)


    user_icon = tk.PhotoImage(file="./buttons/user_2.png")
    password_icon = tk.PhotoImage(file="./buttons/password.png")

    title_member = tk.Label(screen2,text = "MEMBERS LOGIN",bg="#1F1F1F",fg='#FFFFFF',font=('Copperplate Gothic Light',20))
    title_member.pack(pady=115)

    user_icon_label = tk.Label(screen2, image=user_icon,bg="#1F1F1F")
    user_icon_label.place(x=40, y=180)
    username_entry = tk.Entry(screen2,bg="#121212",fg='#E0D9D9',font=('Helvetica',15),borderwidth=0)
    username_entry.insert(0,"   username")
    username_entry.place(x=91,y=181,width=220,height=49)
    username_entry.bind("<FocusIn>", temp_text)

    pass_icon_label = tk.Label(screen2, image=password_icon,bg="#1F1F1F")
    pass_icon_label.place(x=40, y=240)
    password_entry = tk.Entry(screen2,bg="#121212",fg='#E0D9D9',font=('Helvetica',15),borderwidth=0)
    password_entry.insert(0,"   password")
    password_entry.place(x=91,y=241,width=220,height=49)
    password_entry.bind("<FocusIn>", temp_pass)

    login_btn_img = tk.PhotoImage(file='./buttons/login_button.png')
    login_button = tk.Button(screen2,image=login_btn_img,bg='#1F1F1F',command=login,borderwidth=0)
    login_button.place(x=61,y=330)

    register_btn_img = tk.PhotoImage(file='./buttons/register_button.png')
    register_button = tk.Button(screen2,image=register_btn_img,bg='#1F1F1F',command=register,borderwidth=0)
    register_button.place(x=61,y=380)

    screen2.mainloop()

def first_year():
    global sub1_entry,sub2_entry,sub3_entry,sub4_entry,sub5_entry,sub6_entry,sub7_entry,sub8_entry,sub9_entry
    root.geometry("600x370+170+100")
    score_screen = tk.Toplevel(root)
    score_screen.title("Calculate First Year SGPA")
    score_screen.geometry("800x570+370+150")
    score_screen.config(bg="#121212")
    score_screen.iconbitmap('ic.ico')

    title_marks = tk.Label(score_screen,text = "Please Enter Your Marks",bg="#121212",fg='#BB86FC',font=('copperplate gothic bold',35))
    title_marks.pack(pady=25)

    theory_subject_label = tk.LabelFrame(score_screen,text="     Theory Subjects     ",width=682,height=130,bg="#1F1F1F",fg='#FFFFFF',font=('Helvetica',15))
    theory_subject_label.place(x=60,y=103)

    ''' Making Labels and entry for theory subjects '''
    sub1_label = tk.Label(theory_subject_label,text="Math Marks -",bg="#1F1F1F",fg='#BB86FC',font=('Helvetica',15))
    sub1_label.place(x=18,y=12)
    sub1_entry = tk.Entry(theory_subject_label,bg="#E0E5EC",fg='#1F1F1F',width=5,font=('Helvetica',15))
    sub1_entry.place(x=145,y=12)

    sub2_label = tk.Label(theory_subject_label,text="Phys/Chem  -",bg="#1F1F1F",fg='#BB86FC',font=('Helvetica',15))
    sub2_label.place(x=18,y=60)
    sub2_entry = tk.Entry(theory_subject_label,bg="#E0E5EC",fg='#1F1F1F',width=5,font=('Helvetica',15))
    sub2_entry.place(x=145,y=60)

    sub3_label = tk.Label(theory_subject_label,text="ELE/PSP -",bg="#1F1F1F",fg='#BB86FC',font=('Helvetica',15))
    sub3_label.place(x=260,y=12)
    sub3_entry = tk.Entry(theory_subject_label,bg="#E0E5EC",fg='#1F1F1F',width=5,font=('Helvetica',15))
    sub3_entry.place(x=370,y=12)

    sub4_label = tk.Label(theory_subject_label,text="CIV/ELN  -",bg="#1F1F1F",fg='#BB86FC',font=('Helvetica',15))
    sub4_label.place(x=260,y=60)
    sub4_entry = tk.Entry(theory_subject_label,bg="#E0E5EC",fg='#1F1F1F',width=5,font=('Helvetica',15))
    sub4_entry.place(x=370,y=60)

    sub5_label = tk.Label(theory_subject_label,text="EVNL/EME -",bg="#1F1F1F",fg='#BB86FC',font=('Helvetica',15))
    sub5_label.place(x=475,y=12)
    sub5_entry = tk.Entry(theory_subject_label,bg="#E0E5EC",fg='#1F1F1F',width=5,font=('Helvetica',15))
    sub5_entry.place(x=595,y=12)



    lab_subject_label = tk.LabelFrame(score_screen,text="     Lab Subjects     ",width=682,height=100,bg="#1F1F1F",fg='#FFFFFF',font=('Helvetica',15))
    lab_subject_label.place(x=60,y=265)

    ''' Making Labels and entry for lab subjects '''
    sub6_label = tk.Label(lab_subject_label,text="PHYL/CHEL -",bg="#1F1F1F",fg='#BB86FC',font=('Helvetica',15))
    sub6_label.place(x=60,y=18)
    sub6_entry = tk.Entry(lab_subject_label,bg="#E0E5EC",fg='#1F1F1F',width=5,font=('Helvetica',15))
    sub6_entry.place(x=205,y=18)

    sub7_label = tk.Label(lab_subject_label,text="ELEL/CPL  -",bg="#1F1F1F",fg='#BB86FC',font=('Helvetica',15))
    sub7_label.place(x=355,y=18)
    sub7_entry = tk.Entry(lab_subject_label,bg="#E0E5EC",fg='#1F1F1F',width=5,font=('Helvetica',15))
    sub7_entry.place(x=480,y=18)

    extra_subject_label = tk.LabelFrame(score_screen,text="     Extra Subjects     ",width=682,height=80,bg="#1F1F1F",fg='#FFFFFF',font=('Helvetica',15))
    extra_subject_label.place(x=60,y=395)

    ''' Making Labels and entry for extra subjects '''
    sub8_label = tk.Label(extra_subject_label,text="English marks -",bg="#1F1F1F",fg='#BB86FC',font=('Helvetica',15))
    sub8_label.place(x=60,y=13)
    sub8_entry = tk.Entry(extra_subject_label,bg="#E0E5EC",fg='#1F1F1F',width=5,font=('Helvetica',15))
    sub8_entry.place(x=205,y=13)

    sub9_label = tk.Label(extra_subject_label,text="IDT/SFH -",bg="#1F1F1F",fg='#BB86FC',font=('Helvetica',15))
    sub9_label.place(x=355,y=13)
    sub9_entry = tk.Entry(extra_subject_label,bg="#E0E5EC",fg='#1F1F1F',width=5,font=('Helvetica',15))
    sub9_entry.place(x=480,y=13)

    calculate_btn_img = tk.PhotoImage(file='./buttons/calculate_button.png')
    calculate_button = tk.Button(score_screen,image=calculate_btn_img,bg='#BB86FC',command=calculate,borderwidth=0)
    calculate_button.place(x=335,y=490)

    score_screen.mainloop() 


root = tk.Tk()
root.title("SGPA Calculator")
root.geometry("600x370+470+200")
root.config(bg='#000000')
root.iconbitmap('ic.ico')
root.resizable(0,0)

bg_picture = tk.PhotoImage(file='bg.png')
bg = tk.Label(root,image=bg_picture)
bg.pack()

sgpa_btn_img = tk.PhotoImage(file='./buttons/sgpa_button.png')
user_btn_img = tk.PhotoImage(file='./buttons/sign_in_button_2.png')
logo_img = tk.PhotoImage(file='logo.png')
logo_img_label= tk.Label(image=logo_img)
logo_img_label.place(x=200,y=50)

sgpa_button = tk.Button(root,image=sgpa_btn_img,bg='#000000',command= first_year,borderwidth=0)
sgpa_button.place(x=65,y=225)

user_profile_button = tk.Button(root,image=user_btn_img,bg='#000000',command= user_profile,borderwidth=0)
user_profile_button.place(x=360,y=225)
# sgpa_button = tk.Button(root,text='Calculate SGPA',command=first_year,width=15,font=('Helvetica',20),bg='#bb86fc',fg='#000000',relief=tk.FLAT)
# sgpa_button.place(x=81,y=275)

root.mainloop()
