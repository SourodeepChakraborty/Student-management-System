from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import mysql.connector
from tkinter import messagebox

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Sudarsanpur Dwarika Prosad Uchcha VidyaChakra")

        #Variables
        self.var_class = StringVar()
        self.var_sec = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_roll = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()

        #1st Image
        img = Image.open(r"logo.png")
        img = img.resize((500,210),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        self.button1 = Button(self.root,image = self.photoimg,cursor = "hand2")
        self.button1.place(x = 510, y = 0, width = 500,height = 220)

        #2nd Image
        img1 = Image.open(r"tour.png")
        img1 = img1.resize((500,210),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        self.button2 = Button(self.root,image = self.photoimg1,cursor = "hand2")
        self.button2.place(x = 0,y = 0, width = 500,height = 220)

        # 3rd Image
        img3 = Image.open(r"teacher.png")
        img3 = img3.resize((480, 210), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img3)

        self.button3 = Button(self.root, image=self.photoimg2, cursor="hand2")
        self.button3.place(x=1020, y=0, width=520, height=220)

        #background image
        img2 = Image.open(r"lib.jpg")
        img2 = img2.resize((1530, 700), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img2)

        bg_lbl = Label(self.root, image=self.photoimg3,bd = 2 ,relief = RIDGE)
        bg_lbl.place(x=0, y=220, width=1530, height=700)

        #title
        lbl_title = Label(bg_lbl,text = "SUDARSANPUR DWARIKA PROSAD UCHCHA VIDYACHAKRA",font =("algerian",37,"bold"),fg = "blue", bg = "white")
        lbl_title.place(x=0, y=0, width = 1530, height = 50)

        #Manage Frame
        Manage_frame = Frame(bg_lbl, bd = 2,relief = RIDGE,bg = "white")
        Manage_frame.place(x = 25,y = 50, width = 1470, height = 525)

        #Data Left Frame
        dataleft = LabelFrame(Manage_frame,bd = 4, relief = RIDGE, padx = 2, text = "STUDENT INFORMATION",font =("times new roman",15,"bold"),fg = "red", bg = "white")
        dataleft.place(x = 20, y = 10, width = 660, height= 500)

        #image into the left frame
        img4 = Image.open(r"index.png")
        img4 = img4.resize((650,120),Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        my_img = Label(dataleft, image = self.photoimg4,bd = 2, relief = RIDGE)
        my_img.place(x = 0,y = 0, width = 650, height = 120)

        #current class Label frame information
        std_lbl_info_frame = LabelFrame(dataleft,bd = 4, relief = RIDGE, padx = 2, text = "CURRENT COURSE INFORMATION",font =("arial",15,"bold"),fg = "blue", bg = "white")
        std_lbl_info_frame.place(x = 9, y = 120, width = 620, height = 85)

        #Lables and combo box
        #standard selection
        lbl_dep = Label(std_lbl_info_frame,text = "STANDARD",font =("times new roman",13,"bold"),fg = "red", bg = "white")
        lbl_dep.grid(row = 0, column = 0, padx = 2, sticky = W)
        #class dropdown
        combo_class = ttk.Combobox(std_lbl_info_frame,textvariable = self.var_class,state = "readonly",font =("times new roman",12,"bold"),width = 20)
        combo_class["value"] = ("SELECT STANDARD","CLASS 5","CLASS 6","CLASS 7","CLASS 8","CLASS 9","CLASS 10","CLASS 11","CLASS 12")
        combo_class.current(0)
        combo_class.grid(row = 0, column = 1, padx = 2, pady = 10, sticky = W)

        #section selection
        lbl_sec = Label(std_lbl_info_frame,text = "     SECTION",font =("times new roman",13,"bold"),fg = "blue", bg = "white")
        lbl_sec.grid(row = 0, column = 9, padx = 2,sticky = W)
        #section dropdown
        combo_sec = ttk.Combobox(std_lbl_info_frame,textvariable = self.var_sec,state = "readonly",font = ("times new roman",12,"bold"),width = 20)
        combo_sec["value"] = ("SELECT SECTION","SECTION A","SECTION B","SECTION C","SECTION D","SCIENCE","HUMANITIES","COMMERCE")
        combo_sec.current(0)
        combo_sec.grid(row = 0, column = 11, padx = 2, pady = 10,sticky = W)

        #Student class Label frame
        std_lbl_class_frame = LabelFrame(dataleft, bd = 4,relief = RIDGE, padx = 2, text = "STUDENT CLASS INFORMATION",font =("arial",15,"bold"),fg = "green", bg = "white")
        std_lbl_class_frame.place(x = 9, y = 210, width = 620, height =255)
        #student id
        lbl_id = Label(std_lbl_class_frame,font =("times new roman",13,"bold"),text = "STUDENT ID:",bg = "white")
        lbl_id.grid(row = 0, column = 0, sticky = W, padx = 2, pady = 7)
        #student id textbox
        id_entry = ttk.Entry(std_lbl_class_frame,textvariable = self.var_id,font =("times new roman",13,"bold"),width = 22)
        id_entry.grid(row = 0, column = 1, padx = 2, pady = 7, sticky = W)

        #student name
        lbl_name = Label(std_lbl_class_frame,font =("times new roman",13,"bold"),text = "STUDENT NAME:", bg = "white")
        lbl_name.grid(row = 1, column = 0, sticky = W, padx = 2, pady = 7)
        #student name textbox
        name_entry = ttk.Entry(std_lbl_class_frame,textvariable = self.var_name,font =("times new roman",13,"bold"),width = 30)
        name_entry.grid(row = 1, column = 1,padx = 2, pady = 7,sticky = W)

        #Student Roll number
        lbl_roll = Label(std_lbl_class_frame,font =("times new roman",13,"bold"),text = "STUDENT ROLL NUMBER: ", bg = "white")
        lbl_roll.grid(row = 2, column = 0, sticky = W, padx = 2, pady = 7)
        #Student Roll textbox
        roll_entry = ttk.Entry(std_lbl_class_frame,textvariable = self.var_roll,font =("times new roman",13,"bold"),width = 10)
        roll_entry.grid(row = 2,column = 1, padx = 2, pady = 7, sticky = W)

        #Student phone number
        lbl_call = Label(std_lbl_class_frame,font =("times new roman",13,"bold"),text = "PHONE NUMBER:", bg = "white")
        lbl_call.grid(row = 3, column = 0, sticky = W, padx = 2, pady = 7)
        #student phone number textbox
        call_entry = ttk.Entry(std_lbl_class_frame,textvariable = self.var_phone,font =("times new roman",13,"bold"),width = 15)
        call_entry.grid(row = 3, column = 1, padx = 2, pady = 7, sticky = W)

        #Student Address
        lbl_address = Label(std_lbl_class_frame,font =("times new roman",13,"bold"),text = "ADDRESS:", bg = "white")
        lbl_address.grid(row = 4, column = 0, sticky = W, padx = 2, pady = 7)
        #student Address textbox
        address_entry = ttk.Entry(std_lbl_class_frame,textvariable = self.var_address,font=("times new roman",13,"bold"),width = 40)
        address_entry.grid(row = 4, column = 1, padx = 2, pady = 7,sticky =W)

        #Button Frame
        btn_frame = Frame(dataleft, bd = 2, relief = RIDGE, bg = "white")
        btn_frame.place(x = 13, y = 430,width = 615,height = 35)
        #add button
        btn_add = Button(btn_frame,text = "SAVE",command = self.add_data,font =("times new roman",11,"bold"),width = 16,fg = "white", bg = "blue")
        btn_add.grid(row = 0, column = 0, padx = 1)

        # update button
        btn_add = Button(btn_frame, text="UPDATE",command = self.update_data,font=("times new roman", 11, "bold"), width=16, fg="white", bg="blue")
        btn_add.grid(row=0, column=1, padx=1)

        # Delete button
        btn_add = Button(btn_frame, text="DELETE",command = self.delete_data, font=("times new roman", 11, "bold"), width=16, fg="white", bg="blue")
        btn_add.grid(row=0, column=2, padx=1)

        # reset button
        btn_add = Button(btn_frame, text="RESET",command = self.reset_data,font=("times new roman", 11, "bold"), width=16, fg="white", bg="blue")
        btn_add.grid(row=0, column=3, padx=1)

        # Data Right Frame
        dataright = LabelFrame(Manage_frame, bd=4, relief=RIDGE, padx=2, text="STUDENT INFORMATION",font=("arial", 15, "bold"), fg="green", bg="white")
        dataright.place(x=690, y=10, width=755, height=500)


        #Image into right Frame
        img5 = Image.open(r"sudarsanpur-dwarika-prasad-uchcha-vidyachakra-sudarshanpur-raiganj-schools.png")
        img5 = img5.resize((770,200),Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        my_image = Label(dataright, image = self.photoimg5, bd = 2, relief = RIDGE)
        my_image.place(x = 0, y = 0, width = 745, height = 200)

        #Search Frame
        search_frame = LabelFrame(dataright, bd = 4, relief = RIDGE, padx = 2, text = "SEARCH STUDENT INFORMATION",font=("times new roman", 15, "bold"), width=16, fg="red", bg="white")
        search_frame.place(x = 0, y = 200, width = 742, height = 70)

        #search By frame
        search_by = Label(search_frame, font=("arial", 11, "bold"), text = "SEARCH BY:", fg="blue", bg="white")
        search_by.grid(row = 0, column = 0, padx = 2, pady = 7,sticky = W)

        #search
        self.var_com_search = StringVar()
        #search by dropdown
        com_txt_search = ttk.Combobox(search_frame,textvariable = self.var_com_search ,state = "readonly", font=("arial", 12, "bold"), width=18)
        com_txt_search["value"] = ("SELECT OPTION","PHONE","STUDENT ID","STUDENT NAME")
        com_txt_search.current(0)
        com_txt_search.grid(row = 0, column = 1, padx = 2, pady = 7, sticky = W)

        #text search by
        self.var_search = StringVar()
        txt_search = ttk.Entry(search_frame,textvariable = self.var_search,width = 22, font = ("arial",11,"bold"))
        txt_search.grid(row = 0, column = 2, padx = 5)

        #Search Button
        btn_search = Button(search_frame,text = "SEARCH",command = self.search_data,font = ("arial",12,"bold"),width = 10, bg = "blue", fg = "white")
        btn_search.grid(row = 0, column = 3, padx = 5)

        #Show all Button
        btn_show = Button(search_frame,text = "SHOW ALL",command = self.fetch_data, font = ("arial",12,"bold"),width = 10, bg = "blue", fg = "white")
        btn_show.grid(row = 0, column = 4, padx = 5)


        '''STUDENT TABLE AND SCROLL BAR'''
        #table frame
        table_frame = Frame(dataright,bd = 4, relief = RIDGE)
        table_frame.place(x = 0, y = 270, width = 744, height = 201)

        #scroll bar
        scroll_x = ttk.Scrollbar(table_frame,orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient = VERTICAL)
        self.student_table = ttk.Treeview(table_frame,column = ("STUDENT ID","STUDENT NAME","ROLL","STANDARD","PHONE NUMBER"),xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)

        scroll_x.pack(side = BOTTOM,fill = X)
        scroll_y.pack(side = RIGHT,fill = Y)

        scroll_x.config(command = self.student_table.xview)
        scroll_y.config(command = self.student_table.yview)

        self.student_table.heading("STUDENT ID", text = "STUDENT ID")
        self.student_table.heading("STUDENT NAME", text = "STUDENT NAME")
        self.student_table.heading("ROLL", text = "ROLL")
        self.student_table.heading("STANDARD", text = "STANDARD")
        self.student_table.heading("PHONE NUMBER", text = "PHONE NUMBER")

        self.student_table["show"] = "headings"

        self.student_table.column("STUDENT ID",width = 125)
        self.student_table.column("STUDENT NAME", width = 250)
        self.student_table.column("ROLL", width = 75)
        self.student_table.column("STANDARD", width = 100)
        self.student_table.column("PHONE NUMBER", width=150)

        self.student_table.pack(fill = BOTH, expand = 1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #ADD data
    def add_data(self):
        if(self.var_class.get()== "" or self.var_sec.get()=="" or self.var_id.get()=="" ):
            messagebox.showerror("ERROR","ALL FIELDS ARE REQUIRED")
        else:
            try:
                conn = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "Library_Management_System")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(self.var_id.get(),self.var_name.get(),self.var_class.get(),self.var_sec.get(),self.var_roll.get(),self.var_phone.get(),self.var_address.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("SUCCESS","STUDENT HAS BEEN ADDED!",parent = self.root)
            except Exception as e:
                messagebox.showerror("ERROR",f"DUE TO:{str(e)}",parent = self.root)

    #DATA FETCHING
    def fetch_data(self):
        conn = mysql.connector.connect(host = "localhost",user = "root", password = "", database = "Library_Management_System")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        if len(data)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values = i)
            conn.commit()
        conn.close()

    #GET CURSOR
    def get_cursor(self,event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        data = content["values"]

        self.var_id.set(data[0])
        self.var_name.set(data[1])
        self.var_class.set(data[2])
        self.var_sec.set(data[3])
        self.var_roll.set(data[4])
        self.var_phone.set(data[5])
        self.var_address.set(data[6])

    #UPDATE data
    def update_data(self):
        if (self.var_class.get() == "" or self.var_sec.get() == "" or self.var_id.get() == ""):
            messagebox.showerror("ERROR", "ALL FIELDS ARE REQUIRED")
        else:
            try:
                update = messagebox.askyesno("UPDATE","ARE YOU SURE TO UPDATE THE STUDENTS DATA",parent = self.root)
                if update > 0:
                    conn = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "Library_Management_System")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set student_name = %s, standard = %s, section = %s, roll = %s, phone_number = %s, address = %s where student_id = %s",(self.var_name.get(),self.var_class.get(),self.var_sec.get(),self.var_roll.get(),self.var_phone.get(),self.var_address.get(),self.var_id.get()))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("SUCCESS","STUDENT SUCCESSFULLY UPDATED",parent = self.root)
            except Exception as e:
                messagebox.showerror("ERROR",f"DUE TO:{str(e)}",parent = self.root)

    #DELETE data
    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror("ERROR","ALL FIELDS ARE REQUIRED")
        else:
            try:
                Delete = messagebox.askyesno("DELETE","ARE YOU SURE DELETE THIS SYUDENT")
                if Delete > 0:
                    conn = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "Library_Management_System")
                    my_cursor = conn.cursor()
                    sql = "delete from student where student_id = %s"
                    value = (self.var_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("DELETE","YOUR STUDENT HAS BEEN DELETED",parent = self.root)
            except Exception as e:
                messagebox.showerror("ERROR", f"DUE TO:{str(e)}", parent=self.root)

    #RESET data
    def reset_data(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_class.set("SELECT STANDARD")
        self.var_sec.set("SELECT SECTION")
        self.var_roll.set("")
        self.var_phone.set("")
        self.var_address.set("")

    #SEARCH data
    def search_data(self):
        if self.var_com_search.get() == "" or self.var_search.get() == "":
            messagebox.showerror("ERROR","PLEASE SELECT OPTION")
        else:
            try:
                conn = mysql.connector.connect(host = "localhost", user = "root", password = "",database = "Library_Management_System")
                my_cursor = conn.cursor()
                #my_cursor.execute("select * from student where " + str(self.var_com_search.get())+ " Like %"+ str(self.var_search.get())+"%")
                my_cursor.execute("select * from student where " + str(self.var_com_search.get()) + " = '"+str(self.var_search.get())+"'")
                data = my_cursor.fetchall()
                if len(data) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values = i)
                    conn.commit()
                conn.close()
            except Exception as e:
                messagebox.showerror("ERROR", f"DUE TO:{str(e)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()