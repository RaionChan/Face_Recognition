from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

#"C:\Python312\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml" 


class Student:
        def __init__(self,root):
                self.root = root
                self.root.geometry("1920x1080+0+0")
                self.root.title("Face Recognition System")

                # Variables
                self.var_std_id = StringVar()
                self.var_dep = StringVar()
                self.var_course = StringVar()
                self.var_year = StringVar()
                self.var_semester = StringVar()
                self.var_std_name = StringVar()
                self.var_div = StringVar()
                self.var_npm = StringVar()
                self.var_gender = StringVar()
                self.var_dob = StringVar()
                self.var_email = StringVar()
                self.var_phone = StringVar()
                self.var_address = StringVar()
                self.var_teacher = StringVar()







       #image 1
                img=Image.open(r".\\images\\pink.jpeg")
                img1=img.resize((640,150), Image.LANCZOS)
                self.photoimg1=ImageTk.PhotoImage(img1)

                f_lbl = Label(self.root, image=self.photoimg1)
                f_lbl.place(x=0, y=0, width=640, height=130)

        #image 2
                img2=Image.open(r".\\images\\girl.jpg")
                img2=img2.resize((640,130), Image.BICUBIC)
                self.photoimg2=ImageTk.PhotoImage(img2)

                f_lbl2 = Label(self.root, image=self.photoimg2)
                f_lbl2.place(x=640, y=0, width=640, height=130)

        #image 3
                img3=Image.open(r".\\images\\pink.jpeg")
                img3=img3.resize((640,130), Image.LANCZOS)
                self.photoimg3=ImageTk.PhotoImage(img3)

                f_lbl3 = Label(self.root, image=self.photoimg3)
                f_lbl3.place(x=1280, y=0, width=640, height=130)

        #bg
                img4=Image.open(r".\\images\\bg.jpg")
                img4=img4.resize((1920,1080))
                self.photoimg4=ImageTk.PhotoImage(img4)

                bg_img = Label(self.root, image=self.photoimg4)
                bg_img.place(x=0, y=130, width=1920, height=1080)
                

                title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 30, "bold"), bg="white", fg="navy")
                title_lbl.place(x=0, y=0, width=1920, height=45)

                main_frame = Frame(bg_img, bd=2, bg="white", relief=RIDGE)
                main_frame.place(x=10, y=55, width=1890, height=780)




                #left label frame
                Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
                Left_frame.place(x=10, y=10, width=920, height=750)

                img_left = Image.open(r".\\images\\pink.jpeg")
                img_left = img_left.resize((960,130))
                self.photoimg_left = ImageTk.PhotoImage(img_left)


                #current course information
                current_course_frame = LabelFrame(Left_frame, bd=2, bg="#b3cde0", relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
                current_course_frame.place(x=10, y=15, width=890, height=150)

                #Department
                dep_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
                dep_label.grid(row=0, column=0, padx=10, sticky=W)

                dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"), state="readonly")
                dep_combo["values"] = ("Select Department", "Informatics", "Electrical", "Civil", "Mechanical")
                dep_combo.current(0)
                dep_combo.grid(row=0, column=1, padx=20, pady=10, sticky=W)

                #Course
                course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
                course_label.grid(row=0, column=2, padx=10, sticky=W)

                course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("times new roman", 12, "bold"), state="readonly")
                course_combo["values"] = ("Select Course", "OOP", "AI", "Calculus", "Web Development")
                course_combo.current(0)

                course_combo.grid(row=0, column=3, padx=20, pady=10, sticky=W)

                #Year
                year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
                year_label.grid(row=1, column=0, padx=10, sticky=W)

                year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("times new roman", 12, "bold"), state="readonly")
                year_combo["values"] = ("Select Year", "2018", "2019", "2020", "2021", "2022", "2023")
                year_combo.current(0)
                year_combo.grid(row=1, column=1, padx=20, pady=10, sticky=W)

                #Semester
                semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
                semester_label.grid(row=1, column=2, padx=10, sticky=W)

                semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("times new roman", 12, "bold"), state="readonly")
                semester_combo["values"] = ("Select Semester", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14")
                semester_combo.current(0)
                semester_combo.grid(row=1, column=3, padx=20, pady=10, sticky=W)


                #Class Student Information
                class_student_frame = LabelFrame(Left_frame, bd=2, bg="#b3cde0", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
                class_student_frame.place(x=10, y=200, width=890, height=335)

                #Student id

                studentID_label = Label(class_student_frame, text="ID:", font=("times new roman", 12, "bold"), bg="white")
                studentID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

                studentID_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=20, font=("times new roman", 12, "bold"))
                studentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

                #Student Name

                studentName_label = Label(class_student_frame, text="Student Name:", font=("times new roman", 12, "bold"), bg="white")
                studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

                studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=20, font=("times new roman", 12, "bold"))
                studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

                #Class Division

                class_div_label = Label(class_student_frame, text="Class Division:", font=("times new roman", 12, "bold"), bg="white")
                class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

                class_div_entry = ttk.Entry(class_student_frame, textvariable=self.var_div, width=20, font=("times new roman", 12, "bold"))
                class_div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

                #NPM

                npm_label = Label(class_student_frame, text="NPM:", font=("times new roman", 12, "bold"), bg="white")
                npm_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

                npm_entry = ttk.Entry(class_student_frame, textvariable=self.var_npm, width=20, font=("times new roman", 12, "bold "))
                npm_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

                #Gender

                gender_label = Label(class_student_frame, text="Gender:", font=("times new roman", 12, "bold"), bg="white")
                gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

                gender_entry = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("times new roman", 12, "bold"), state="readonly", width=18)
                gender_entry["values"] = ("Select gender", "Male", "Female")
                gender_entry.current(0)
                gender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)


                #DOB

                dob_label = Label(class_student_frame, text="DOB:", font=("times new roman", 12, "bold"), bg="white")
                dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

                dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob, width=20, font=("times new roman", 12, "bold"))
                dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

                #Email

                email_label = Label(class_student_frame, text="Email:", font=("times new roman", 12, "bold"), bg="white")
                email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

                email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=("times new roman", 12, "bold"))
                email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

                #Phone No

                phone_label = Label(class_student_frame, text="Phone No:", font=("times new roman", 12, "bold"), bg="white")
                phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

                phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=("times new roman", 12, "bold"))
                phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

                #Address

                address_label = Label(class_student_frame, text="Address:", font=("times new roman", 12, "bold"), bg="white")
                address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

                address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address,width=20, font=("times new roman", 12, "bold"))
                address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

                #Teacher Name2

                teacher_label = Label(class_student_frame, text="Teacher Name:", font=("times new roman", 12, "bold"), bg="white")
                teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

                teacher_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher, width=20, font=("times new roman", 12, "bold"))
                teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)








                # #Radio Buttons

                # self.var_radio1 = StringVar()
                # radiobtn1 = ttk.Radiobutton(class_student_frame, text="Take Photo Sample", value="Yes")
                # radiobtn1.grid(row=6, column=0)

                # self.var_radio2 = StringVar()
                # radiobtn2 = ttk.Radiobutton(class_student_frame, textvariable=self.var_radio1, text="No Photo Sample", value="No")
                # radiobtn2.grid(row=6, column=1)



                photo_frame = LabelFrame(Left_frame, bd=2, bg="#b3cde0", relief=RIDGE, text="Button", font=("times new roman", 12, "bold"))
                photo_frame.place(x=15, y=565, width=880, height=75)

                take_photo_btn = Button(photo_frame, command=self.generate_dataset, text="Take Photo Sample", font=("times new roman", 12, "bold"), bg="navy", fg="white", width=36)
                take_photo_btn.grid(row=0, column=0)

                update_photo_btn = Button(photo_frame, command=self.generate_dataset, text="Update Photo Sample", font=("times new roman", 12, "bold"), bg="navy", fg="white", width=36)
                update_photo_btn.grid(row=0, column=2)


                #Frame Button
                btn_frame = LabelFrame(Left_frame, bd=2, bg="#b3cde0", relief=RIDGE, font=("times new roman", 12, "bold"))
                btn_frame.place(x=15, y=640, width=880, height=65)

                save_btn = Button(btn_frame, command=self.add_data, text="Save",  font=("times new roman", 12, "bold"), bg="blue", fg="white", width=18)
                save_btn.grid(row=1, column=0)

                update_btn = Button(btn_frame, command=self.update_data, text="Update", font=("times new roman", 12, "bold"), bg="blue", fg="white", width=18)
                update_btn.grid(row=1, column=1)

                delete_btn = Button(btn_frame, command=self.delete_data, text="Delete", font=("times new roman", 12, "bold"), bg="blue", fg="white", width=18)
                delete_btn.grid(row=1, column=2)

                reset_btn = Button(btn_frame, command=self.reset_data, text="Reset", font=("times new roman", 12, "bold"), bg="blue", fg="white", width=18)
                reset_btn.grid(row=1, column=3)















                #Right label frame
                Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="List of Students", font=("times new roman", 12, "bold"))
                Right_frame.place(x=950, y=10, width=920, height=750)

                # x=10, y=10, width=920, height=750

                img_right = Image.open(r".\\images\\bg.jpg")
                img_right = img_right.resize((960,130))
                self.photoimg_right = ImageTk.PhotoImage(img_right)

                f_lbl = Label(Right_frame, image=self.photoimg_right)
                f_lbl.place(x=10, y=0, width=890, height=130)

                #Search System

                search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
                search_frame.place(x=10, y=135, width=890, height=80)

                search_label = Label(search_frame, text="Search By:", font=("times new roman", 12, "bold"), bg="grey")
                search_label.grid(row=0, column=0, padx=10, sticky=W)

                search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), state="readonly")
                search_combo["values"] = ("Select", "Roll No", "Phone No")
                search_combo.current(0)
                search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

                search_entry = ttk.Entry(search_frame, width=15, font=("times new roman", 12, "bold"))
                search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

                search_btn = Button(search_frame, text="Search", font=("times new roman", 12, "bold"), bg="blue", fg="white", width=10)
                search_btn.grid(row=0, column=3, padx=4)

                showAll_btn = Button(search_frame, text="Show All", font=("times new roman", 12, "bold"), bg="blue", fg="white", width=10)
                showAll_btn.grid(row=0, column=4, padx=4)





                #Table Frame
                
                table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
                table_frame.place(x=10, y=210, width=890, height=490)

                scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
                scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

                self.student_table = ttk.Treeview(table_frame, column=("student id", "dep", "course", "year", "sem", "name", "div", "npm", "gender", "dob", "email", "phone", "address", "teacher"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

                scroll_x.pack(side=BOTTOM, fill=X)
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_x.config(command=self.student_table.xview)
                scroll_y.config(command=self.student_table.yview)

                self.student_table.heading("student id", text="Student ID")
                self.student_table.heading("dep", text="Department")
                self.student_table.heading("course", text="Course")
                self.student_table.heading("year", text="Year")
                self.student_table.heading("sem", text="Semester")
                # self.student_table.heading("id", text="Student ID")
                self.student_table.heading("name", text="Student Name")
                self.student_table.heading("div", text="Division")
                self.student_table.heading("npm", text="NPM")
                self.student_table.heading("gender", text="Gender")
                self.student_table.heading("dob", text="DOB")
                self.student_table.heading("email", text="Email")
                self.student_table.heading("phone", text="Phone No")
                self.student_table.heading("address", text="Address")
                self.student_table.heading("teacher", text="Teacher")
                self.student_table["show"] = "headings"

                self.student_table.column("student id", width=100)
                self.student_table.column("dep", width=100)
                self.student_table.column("course", width=100)
                self.student_table.column("year", width=100)
                self.student_table.column("sem", width=100)
                # self.student_table.column("id", width=100)
                self.student_table.column("name", width=100)
                self.student_table.column("div", width=100)
                self.student_table.column("npm", width=100)
                self.student_table.column("gender", width=100)
                self.student_table.column("dob", width=100)
                self.student_table.column("email", width=100)
                self.student_table.column("phone", width=100)
                self.student_table.column("address", width=100)
                self.student_table.column("teacher", width=100)
                
                self.student_table.pack(fill=BOTH, expand=1)
                self.student_table.bind("<ButtonRelease>", self.get_cursor)
                self.fetch_data()
                


        #===================Function declaration====================

        def add_data(self):
                if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
                        messagebox.showerror("Error", "All fields are required", parent=self.root)
                else:
                        try:
                            conn=mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
                            my_cursor = conn.cursor()
                            my_cursor.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                                    self.var_std_id.get(),
                                    self.var_dep.get(),
                                    self.var_course.get(),
                                    self.var_year.get(),
                                    self.var_semester.get(),
                                    self.var_std_name.get(),
                                    self.var_div.get(),
                                    self.var_npm.get(),
                                    self.var_gender.get(),
                                    self.var_dob.get(),
                                    self.var_email.get(),
                                    self.var_phone.get(),
                                    self.var_address.get(),
                                    self.var_teacher.get(),
                                #   self.var_radio1.get()

                            ))


                            conn.commit()
                            self.fetch_data()
                            conn.close()
                            messagebox.showinfo("Success", "Student details has been added successfully", parent=self.root)
                        except Exception as es:
                            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)



        #====================Fetch Data===================
        def fetch_data(self):   
                conn=mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                data = my_cursor.fetchall()

                if len(data) != 0:
                        self.student_table.delete(*self.student_table.get_children())
                        for i in data:
                                self.student_table.insert("", END, values=i)
                
                conn.commit()
                conn.close()

        #====================get cursor===================
        # def get_cursor(self, event=""):
        #         cursor_focus = self.student_table.focus()
        #         content = self.student_table.item(cursor_focus)
        #         data = content["values"]

        #         self.var_std_id.set(data[0])
        #         self.var_dep.set(data[1])
        #         self.var_course.set(data[2])
        #         self.var_year.set(data[3])
        #         self.var_semester.set(data[4])
        #         self.var_std_name.set(data[5])
        #         self.var_div.set(data[6])
        #         self.var_npm.set(data[7])
        #         self.var_gender.set(data[8])
        #         self.var_dob.set(data[9])
        #         self.var_email.set(data[10])
        #         self.var_phone.set(data[11])
        #         self.var_address.set(data[12])
        #         self.var_teacher.set(data[13])
        #         # self.var_radio1.set(data[14])
        
        def get_cursor(self, event=""):
                cursor_focus = self.student_table.focus()
                content = self.student_table.item(cursor_focus)
                data = content["values"]

                if len(data) == 0:
                        messagebox.showwarning("Warning", "No data found in the selected row", parent=self.root)
                        return

                try:
                        self.var_std_id.set(data[0])
                        self.var_dep.set(data[1])
                        self.var_course.set(data[2])
                        self.var_year.set(data[3])
                        self.var_semester.set(data[4])
                        self.var_std_name.set(data[5])
                        self.var_div.set(data[6])
                        self.var_npm.set(data[7])
                        self.var_gender.set(data[8])
                        self.var_dob.set(data[9])
                        self.var_email.set(data[10])
                        self.var_phone.set(data[11])
                        self.var_address.set(data[12])
                        self.var_teacher.set(data[13])
                        
                except IndexError as e:
                        messagebox.showerror("Error", f"Data access error: {str(e)}", parent=self.root)


        

        #====================Update Function===================
        def update_data(self):
                if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
                        messagebox.showerror("Error", "All fields are required", parent=self.root)
                else:
                        try:
                                update = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
                                if update > 0:
                                        conn=mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
                                        my_cursor = conn.cursor()

                                        # Check if the student ID exists
                                        my_cursor.execute("SELECT * FROM student WHERE Student_id=%s", (self.var_std_id.get(),))
                                        record = my_cursor.fetchone()
                                        if record is None:
                                                messagebox.showerror("Error", "Student ID not found. Update failed.", parent=self.root)
                                                return

                                        my_cursor.execute("update student set Student_id=%s, dep=%s, course=%s, year=%s, semester=%s,  name=%s, division=%s, npm=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s where Student_id=%s", (
                                                self.var_std_id.get(), self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(),  
                                                self.var_std_name.get(), self.var_div.get(), self.var_npm.get(), self.var_gender.get(), self.var_dob.get(), 
                                                self.var_email.get(), self.var_phone.get(), self.var_address.get(), self.var_teacher.get(), self.var_std_id.get()
                                                ))
                                        
                                        if my_cursor.rowcount == 0:
                                                messagebox.showerror("Error", "No changes found", parent=self.root)
                                        else:
                                                messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)

                                                
                                        
                                        
                                        


                                else:
                                        if not update:
                                                return
                                        
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                        
                        except Exception as es:
                                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

        
        def delete_data(self):
                if self.var_std_id.get() == "":
                        messagebox.showerror("Error", "Student id must be required", parent=self.root)

                else:
                        try:
                                print(f"Attempting to delete record with Student_id: {self.var_std_id.get()}")
                                delete=messagebox.askyesno("Student Delete Page", "Do you want to delete this student?", parent=self.root)
                                if delete > 0:
                                        conn=mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
                                        my_cursor = conn.cursor()
                                        val = (self.var_std_id.get(),)
                                        sql = "delete from student where Student_id=%s"
                                        my_cursor.execute(sql, val)

                                else:
                                        if not delete:
                                                return
                                        
                                conn.commit()
                                self.fetch_data()
                                conn.close()

                        except Exception as es:
                                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


        #====================Reset Function===================
        def reset_data(self):
                self.var_std_id.set("")
                self.var_dep.set("Select Department")
                self.var_course.set("Select Course")
                self.var_year.set("Select Year")
                self.var_semester.set("Select Semester")
                self.var_std_name.set("")
                self.var_div.set("")
                self.var_npm.set("")
                self.var_gender.set("Select Gender")
                self.var_dob.set("")
                self.var_email.set("")
                self.var_phone.set("")
                self.var_address.set("")
                self.var_teacher.set("")




        #===================Generate Dataset of ====================

        def generate_dataset(self):
                if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or not self.var_std_id.get():
                        messagebox.showerror("Error", "All Fields are required", parent=self.root)
                else:
                        try:
                                conn=mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
                                my_cursor=conn.cursor()
                                my_cursor.execute("select * from student")
                                myresult=my_cursor.fetchall()
                                id=0
                                for x in myresult:
                                        id+=1

                                        my_cursor.execute("update student set Student_id=%s, Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Npm=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s where Student_id=%s", (
                                                self.var_std_id.get(),
                                                self.var_dep.get(),
                                                self.var_course.get(),
                                                self.var_year.get(),
                                                self.var_semester.get(),
                                                self.var_std_name.get(),
                                                self.var_div.get(),
                                                self.var_npm.get(),
                                                self.var_gender.get(),
                                                self.var_dob.get(),
                                                self.var_email.get(),
                                                self.var_phone.get(),
                                                self.var_address.get(),
                                                self.var_teacher.get(),
                                                self.var_std_id.get()
                                        ))
                                conn.commit()
                                self.fetch_data()
                                self.reset_data()
                                conn.close()






                #============== Load predifiend data on face frontals from opencv =========
                                face_classifier=cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
                                
                                def face_cropped(img):
                                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                                        faces= face_classifier.detectMultiScale(gray, 1.3, 5)
                                        # scaling factor=1.3
                                        # Minimum Neighbor=5

                                        for (x, y, w, h) in faces:
                                                face_cropped = img[y:y+h, x:x+w]
                                                return face_cropped

                                cap = cv2.VideoCapture(0)
                                img_id = 0
                                while True:
                                        ret, my_frame = cap.read()
                                        if face_cropped(my_frame) is not None:
                                                img_id += 1
                                                face = cv2.resize(face_cropped(my_frame), (450, 450))
                                                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                                                file_name_path = "./data/user."+str(id)+"."+str(img_id)+".jpg"
                                                cv2.imwrite(file_name_path, face)
                                                cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                                                cv2.imshow("Cropped Face", face)

                                        if cv2.waitKey(1) == 13 or int(img_id) == 100:
                                                break
                                        
                                cap.release()
                                cv2.destroyAllWindows()
                                messagebox.showinfo("Result", "Generating data sets completed!!!!")
                        
                        except Exception as es:
                                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)




        




if __name__ == "__main__":
        root = Tk()
        obj = Student(root)
        root.mainloop()
