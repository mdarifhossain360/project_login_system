def configure_user(event):
	user_entry.config(state=NORMAL)
	user_entry.delete(0,END)

def configure_pass(event):
	pass_entry.config(state=NORMAL)
	pass_entry.delete(0,END)
	pass_entry.configure(show="*")
	

def logged():
	if user_var.get()=="" or pass_var.get()=="":
		messagebox.showerror("Error","All fields are required")
	elif user_var.get()!="mdarif" and pass_var.get()!="hossain":
		messagebox.showerror("Invalid","Username and password are Invalid")
	else:
		messagebox.showinfo("Welcome",f"Your Username is : {user_var.get()}\n and your password is : {pass_var.get()}")


import tkinter
from tkinter import*
from tkinter.ttk import*
from tkinter import messagebox
from PIL import ImageTk,Image
window=Tk()
window.title("Login System                                                              Developed by MD Arif Hossain (Desktop Application Develper)")
window.geometry("904x604+200+60")
user_var=StringVar()
pass_var=StringVar()
my_pic=Image.open("images/login_pic.jpg")
re=my_pic.resize((900,600),Image.ANTIALIAS)
my_pic=ImageTk.PhotoImage(re)
pic_label=Label(window,image=my_pic)
pic_label.place(x=0,y=0)


frame=tkinter.Frame(window,width=500,height=350,bg="#FEFAEC")
frame.place(x=200,y=170)

man_icon=ImageTk.PhotoImage(file="images/login_man.png")
man_icon_label=tkinter.Label(frame,image=man_icon,bd=0)
man_icon_label.place(x=210,y=0)

login_label=tkinter.Label(frame,text="Login",font=("times new roman",30,"bold"),bg="white")
login_label.place(x=105,y=0)

system_label=tkinter.Label(frame,text="System",font=("times new roman",30,"bold"),bg="white")
system_label.place(x=308,y=0)


user_icon=ImageTk.PhotoImage(file="images/user.png")
user_icon_label=tkinter.Label(frame,image=user_icon,bg="white",bd=0)
user_icon_label.place(x=60,y=120)

user_entry=Entry(frame,font=("time new roman",20),width=21,textvariable=user_var)
user_entry.insert(END,"Username")
user_entry.config(state=DISABLED)
user_entry.place(x=120,y=125)
user_entry.bind("<Button-1>",configure_user)

pass_icon=ImageTk.PhotoImage(file="images/password.png")
pass_icon_label=tkinter.Label(frame,image=pass_icon,bg="white")
pass_icon_label.place(x=60,y=200)

pass_entry=Entry(frame,font=("time new roman",20),width=21,textvariable=pass_var)
pass_entry.insert(0,"Password")
pass_entry.config(state=DISABLED)
pass_entry.place(x=120,y=200)
pass_entry.bind("<Button-1>",configure_pass)

fotget_button=tkinter.Button(frame,text="Forget password ?",font=("time new roman",15),fg="red",bd=0,bg="white")
fotget_button.place(x=120,y=250)
def configure_user_event(event):
	button_login.config(
		bg="#344955"
	)
def configure_pass_event(event):
	button_login.config(
		bg="#232F34"
	)

button_login=tkinter.Button(window,text="Login",font=("time new roman",20,"bold"),command=logged,activebackground="#EEB462")
button_login.place(x=400,y=500)
button_login.bind("<Enter>",configure_user_event)
button_login.bind("<Leave>",configure_pass_event)

window.mainloop()