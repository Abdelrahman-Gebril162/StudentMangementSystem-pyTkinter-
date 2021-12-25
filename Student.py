
from tkinter import *
from tkinter import messagebox
from tkinter import ttk, Tk, StringVar
import sqlite3


class Student:
    # name_var = None
    def __init__(self, root):
        self.root = root
        self.root.title("Student Mangement System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("time new roman",40,"bold"),bg="gray",fg="white" )
        title.pack(side=TOP,fill=X)


        # ========All Variables==========
        self.id_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.gpa_var = StringVar()
        self.session_var = StringVar()
        self.course_var = StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()

        #==========================manage_Frame============================================

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="gray")
        Manage_Frame.place(x=10,y=90,width=400,height=600)

        m_title=Label(Manage_Frame,text=" Manage Student ",font=("time new roman",25,"bold"),fg='white',bg="gray")
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_id=Label(Manage_Frame,text="National ID",font=("time new roman",15,"bold"),fg='black',bg="gray")
        lbl_id.grid(row=1,column=0,pady=5,padx=0,sticky='w')

        txt_id = Entry(Manage_Frame,textvariable=self.id_var,font=("time new roman",15,"bold",),bd=5,relief=GROOVE)
        txt_id.grid(row=1,column=1,pady=10,padx=20,sticky='w')

        lbl_name = Label(Manage_Frame, text="Name", font=("time new roman", 15, "bold"), fg='black', bg="gray")
        lbl_name.grid(row=2, column=0, pady=5, padx=0, sticky='w')

        txt_name = Entry(Manage_Frame,textvariable=self.name_var, font=("time new roman", 15, "bold",), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky='w')

        lbl_email = Label(Manage_Frame, text="E-mail", font=("time new roman", 15, "bold"), fg='black', bg="gray")
        lbl_email.grid(row=3, column=0, pady=5, padx=0, sticky='w')

        txt_email = Entry(Manage_Frame,textvariable=self.email_var, font=("time new roman", 15, "bold",), bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky='w')

        lbl_gender = Label(Manage_Frame, text="Gender", font=("time new roman", 15, "bold"), fg='black', bg="gray")
        lbl_gender.grid(row=4, column=0, pady=5, padx=0, sticky='w')

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("time new roman", 13, "bold"),state='readonly')
        combo_gender['values']=('male','female')
        combo_gender.grid(row=4, column=1, pady=5, padx=35, sticky='w')

        lbl_contact = Label(Manage_Frame, text="Contact", font=("time new roman", 15, "bold"), fg='black', bg="gray")
        lbl_contact.grid(row=5, column=0, pady=5, padx=0, sticky='w')

        txt_contact = Entry(Manage_Frame,textvariable=self.contact_var, font=("time new roman", 15, "bold",), bd=5, relief=GROOVE)
        txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky='w')

        lbl_gpa = Label(Manage_Frame, text="GPA", font=("time new roman", 15, "bold"), fg='black', bg="gray")
        lbl_gpa.grid(row=6, column=0, pady=5, padx=0, sticky='w')

        txt_gpa = Entry(Manage_Frame,textvariable=self.gpa_var, font=("time new roman", 15, "bold",), bd=5, relief=GROOVE)
        txt_gpa.grid(row=6, column=1, pady=10, padx=20, sticky='w')

        lbl_session = Label(Manage_Frame, text="Sesssion", font=("time new roman", 15, "bold"), fg='black', bg="gray")
        lbl_session.grid(row=7, column=0, pady=5, padx=0, sticky='w')

        combo_session = ttk.Combobox(Manage_Frame,textvariable=self.session_var, font=("time new roman", 13, "bold"), state='readonly')
        combo_session['values'] = ('1', '2','3','4')
        combo_session.grid(row=7, column=1, pady=5, padx=35, sticky='w')

        lbl_course = Label(Manage_Frame, text="Course", font=("time new roman", 15, "bold"), fg='black', bg="gray")
        lbl_course.grid(row=9, column=0, pady=5, padx=0, sticky='w')

        combo_course=ttk.Combobox(Manage_Frame,textvariable=self.course_var,font=("time new roman", 13, "bold"), state='readonly')
        combo_course['values']=('General','IS','SE','CS','IT')
        combo_course.grid(row=9, column=1, pady=5, padx=35, sticky='w')

        #===========================manage============================================
        # ==========================bun_Frame===========

        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="black")
        btn_Frame.place(x=0,y=530,width=393)

        Add_btn=Button(btn_Frame,text='ADD',width=10,command=self.validation).grid(row=0,column=0,padx=8,pady=10)
        delete_btn=Button(btn_Frame,text='DELETE',width=10,command=self.delet_data).grid(row=0,column=2,padx=8,pady=10)
        update_btn=Button(btn_Frame,command=self.update_data,text='Update',width=10).grid(row=0,column=3,padx=8,pady=10)
        clear_btn=Button(btn_Frame,text='CLEAR',width=10,command=self.clear).grid(row=0,column=4,padx=8,pady=10)
        #===========================Detail_Frame============================================

        Detail_Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="gray")
        Detail_Manage_Frame.place(x=460, y=90, width=850, height=600)

        lbl_search = Label(Detail_Manage_Frame, text="search", font=("time new roman", 15, "bold"), fg='white', bg="gray")
        lbl_search.grid(row=0, column=0, pady=10, padx=10, sticky='w')

        combo_search = ttk.Combobox(Detail_Manage_Frame,textvariable=self.search_by,width=10, font=("time new roman", 13, "bold"), state='readonly')
        combo_search['values'] = ("id", "NAME", "contact","gender","course","session")
        combo_search.grid(row=0, column=1, pady=10, padx=20, sticky='w')

        txt_search = Entry(Detail_Manage_Frame,width=30,textvariable=self.search_txt, font=("time new roman", 15, "bold",), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky='w')

        btn_search=Button(Detail_Manage_Frame,text='Search',width=5,command=self.search_data,font=('times new roman',15,'bold'),bd=5,relief=GROOVE).grid(row=0,column=3,pady=10,padx=20)
        btn_showAll=Button(Detail_Manage_Frame,text='showAll',width=5,command=self.fetch_data,font=('times new roman',15,'bold'),bd=5,relief=GROOVE).grid(row=0,column=4,pady=10,padx=20)


    #==========================TableFrame=======
        Table_Frame=Frame(Detail_Manage_Frame, bd=4, relief=RIDGE, bg="gray")
        Table_Frame.place(x=40, y=70, width=750, height=500)
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_tabel=ttk.Treeview(Table_Frame,column=('ID','Name','E-mail','Gender','contact','GPA','session','Course'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_tabel.xview)
        scroll_y.config(command=self.Student_tabel.yview)
        self.Student_tabel.heading('ID',text='ID')
        self.Student_tabel.heading('Name',text='Name')
        self.Student_tabel.heading('E-mail',text='E-mail')
        self.Student_tabel.heading('Gender',text='Gender')
        self.Student_tabel.heading('contact',text='contact')
        self.Student_tabel.heading('GPA',text='GPA')
        self.Student_tabel.heading('session',text='Year')
        self.Student_tabel.heading('Course',text='Course')
        self.Student_tabel['show']='headings'
        self.Student_tabel.column('ID',width=90)
        self.Student_tabel.column('Name', width=90)
        self.Student_tabel.column('E-mail', width=90)
        self.Student_tabel.column('Gender', width=90)
        self.Student_tabel.column('contact', width=90)
        self.Student_tabel.column('GPA', width=90)
        self.Student_tabel.column('session', width=90)
        self.Student_tabel.column('Course', width=90)
        self.Student_tabel.pack(fill=BOTH,expand=1)
        self.Student_tabel.bind("<ButtonRelease-1>",self.get_record)
        self.fetch_data()

    #==========================Detail============================================
    def validation(self):
        if len(self.id_var.get())==14 and len(self.contact_var.get()) ==11 and\
                self.name_var.get() !="" and self.gender_var.get() !="" and self.gpa_var.get() !=""\
                and self.session_var.get() !="" and self.course_var.get() !="" :
            if '@' in self.email_var.get() and '.com' in self.email_var.get():
                messagebox.showinfo("SUCCESS", "RECORD HAS BEEN INSERTED  *_*")
                self.add_student()
        else:
            messagebox.showwarning("WARNING", "PLEASE FILL ALL CORRECTRLY!!!!!!")

    def createDb(self):
        conn = sqlite3.connect('student.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS students (
            id TEXT,
            name TEXT,
            email TEXT,
            gender TEXT,
            contact TEXT,
            gpa TEXT,
            session TEXT,
            course TEXT)""")
        conn.commit()
        conn.close()

    def add_student(self):
        con = sqlite3.connect("student.db")
        cur = con.cursor()
        cur.execute("insert into students values(?, ?, ?, ?, ?, ?, ?, ?)", (
            self.id_var.get(),
            self.name_var.get(),
            self.email_var.get(),
            self.gender_var.get(),
            self.contact_var.get(),
            self.gpa_var.get(),
            self.session_var.get(),
            self.course_var.get(),

        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def fetch_data(self):
        con = sqlite3.connect("student.db")
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_tabel.delete(*self.Student_tabel.get_children())
            for row in rows:
                self.Student_tabel.insert('', END, values=row)
                con.commit()
            con.close()
        else:
            messagebox.showwarning("warining","NO DATA TO SHOW")


    def clear(self):
        self.id_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.course_var.set("")
        self.gpa_var.set("")
        self.contact_var.set("")
        self.session_var.set("")
    def get_record(self,ev):
        cursor_record=self.Student_tabel.focus()
        content=self.Student_tabel.item(cursor_record)
        record=content['values']
        self.id_var.set(record[0])
        self.name_var.set(record[1])
        self.email_var.set(record[2])
        self.gender_var.set(record[3])
        self.contact_var.set(record[4])
        self.gpa_var.set(record[5])
        self.session_var.set(record[6])
        self.course_var.set(record[7])
    def update_data(self):
        con = sqlite3.connect("student.db")
        cur = con.cursor()
        cur.execute("update students set name=?, email=?,gender=?, contact=?, gpa=?,session=?, course=? where id=? ", (

            self.name_var.get(),
            self.email_var.get(),
            self.gender_var.get(),
            self.contact_var.get(),
            self.gpa_var.get(),
            self.session_var.get(),
            self.course_var.get(),
            self.id_var.get()

        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
    def delet_data(self):
        con = sqlite3.connect("student.db")
        cur = con.cursor()
        cur.execute("delete from students where  id=? ", [
            self.id_var.get()
        ])
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def search_data(self):
        con = sqlite3.connect("student.db")
        cur = con.cursor()

        cur.execute(f"select * from students where  {str(self.search_by.get())} = '{str(self.search_txt.get())}' or {str(self.search_by.get())} like '{str(self.search_txt.get())}%'")

        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_tabel.delete(*self.Student_tabel.get_children())
            for row in rows:
                self.Student_tabel.insert('', END, values=row)
                con.commit()
        con.close()


root = Tk()
ob = Student(root)
ob.createDb()
root.mainloop()
