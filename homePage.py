from tkinter import *
from tkinter import messagebox
from tkinter import ttk, Tk, StringVar
import Student

class home_page:
    def __init__(self,page):
        self.home=page
        self.home.geometry("1350x700+0+0")
        self.home.title("HOME ")
        title=Label(self.home,text="WELCOME",bd=10,font=("time new roman",60,"bold"),fg="black").pack(side=TOP,fill=X)
        choose_label = Label(self.home, text="GO TO ADMIN PANEL", bd=10, relief=RIDGE, font=("time new roman", 60, "bold"), fg="black").pack(side=BOTTOM,fill=X)

    #================= choose entry frame===============
        btn_frame = Frame(self.home, bd=20, relief=RIDGE, bg="gray")
        btn_frame.place(x=170, y=150, width=1000, height=400)

        admin_btn=Button(btn_frame,text='ADMIN',width=100,height=20,command=self.admin,fg="blue").grid(row=0,column=0,padx=60,pady=10)

    def admin(self):
        Student.admin()

home=Tk()
ob=home_page(home)
home.mainloop()

# admin=Tk()
# ob2=home_page.admin(admin)
# admin.mainloop()
