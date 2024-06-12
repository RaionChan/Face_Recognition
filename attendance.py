from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import csv
import os
from tkinter import filedialog

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        global mydata
        mydata = []

        # ===============Variables================
        self.var_atten_id = StringVar()
        self.var_npm = StringVar()
        self.var_name = StringVar()
        self.var_dep = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attendance = StringVar()

        # # First image
        # img = Image.open(r".\\images\\girl.jpg")
        # img = img.resize((800, 130), Image.Resampling.LANCZOS)
        # self.photoimg = ImageTk.PhotoImage(img)

        # f_lbl = Label(self.root, image=self.photoimg)
        # f_lbl.place(x=0, y=0, width=800, height=130)

        # Second image
        # img1 = Image.open(r".\\images\\student.jpg")
        # img1 = img1.resize((800, 200), Image.Resampling.LANCZOS)
        # self.photoimg1 = ImageTk.PhotoImage(img1)

        # f_lbl = Label(self.root, image=self.photoimg1)
        # f_lbl.place(x=800, y=0, width=800, height=200)

        # Background image
        img3 = Image.open(r".\\images\\bg.jpg")
        img3 = img3.resize((1920, 1080), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1920, height=1080)

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white")
        title_lbl.place(x=0, y=0, width=1920, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=50, y=100, width=1800, height=800)

        # Left label frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 13, "bold"))
        left_frame.place(x=35, y=10, width=850, height=750)

        img_left = Image.open(r".\\images\\bg.jpg")
        img_left = img_left.resize((830, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=10, y=0, width=830, height=130)

        left_inside_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=15, y=145, width=820, height=550)

        # Labels entry
        # Attendance ID
        attendanceID_label = Label(left_inside_frame, text="Attendance ID:", font=("times new roman", 13, "bold"), bg="white")
        attendanceID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceID_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_id ,font=("times new roman", 13, "bold"))
        attendanceID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # npm
        npmLabel = Label(left_inside_frame, text="NPM:", bg="white", font="comicsansns 11 bold")
        npmLabel.grid(row=0, column=2, padx=4, pady=8)

        atten_npm = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_npm, font="comicsansns 11 bold")
        atten_npm.grid(row=0, column=3, pady=8)

        # Name
        nameLabel = Label(left_inside_frame, text="Name:", bg="white", font="comicsansns 11 bold")
        nameLabel.grid(row=1, column=0)

        atten_name = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_name, font="comicsansns 11 bold")
        atten_name.grid(row=1, column=1, pady=8)

        # Department
        deptLabel = Label(left_inside_frame, text="Department:", bg="white", font="comicsansns 11 bold")
        deptLabel.grid(row=1, column=2)

        atten_dep = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_dep, font="comicsansns 11 bold")
        atten_dep.grid(row=1, column=3, pady=8)

        # Time
        timeLabel = Label(left_inside_frame, text="Time:", bg="white", font="comicsansns 11 bold")
        timeLabel.grid(row=2, column=0)

        atten_time = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_time, font="comicsansns 11 bold")
        atten_time.grid(row=2, column=1, pady=8)

        # Date
        dateLabel = Label(left_inside_frame, text="Date:", bg="white", font="comicsansns 11 bold")
        dateLabel.grid(row=2, column=2)

        atten_date = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_date, font="comicsansns 11 bold")
        atten_date.grid(row=2, column=3, pady=8)

        # Attendance Status
        attendanceLabel = Label(left_inside_frame, text="Attendance Status:", bg="white", font="comicsansns 11 bold")
        attendanceLabel.grid(row=3, column=0)

        self.atten_status = ttk.Combobox(left_inside_frame, width=20, textvariable=self.var_attendance, font="comicsansns 11 bold", state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)

        # Button frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=810, height=35)

        save_btn = Button(btn_frame, text="Import CSV", command=self.importCsv, width=15, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        export_btn = Button(btn_frame, text="Export CSV", command=self.exportCsv, width=15, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        export_btn.grid(row=0, column=1)

        update_btn = Button(btn_frame, text="Update", width=15, command=self.update_data, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=14, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        img_left2 = Image.open(r".\\images\\bg.jpg")
        img_left2 = img_left2.resize((830, 130), Image.Resampling.LANCZOS)
        self.photoimg_left2 = ImageTk.PhotoImage(img_left2)

        f_lbl = Label(left_frame, image=self.photoimg_left2)
        f_lbl.place(x=10, y=550, width=830, height=130)




        # Right label frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 13, "bold"))
        right_frame.place(x=920, y=10, width=840, height=750)

        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=15, y=15, width=800, height=690)

        # Scrollbar table
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, columns=("id", "npm", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("npm", text="NPM")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id", width=120)
        self.AttendanceReportTable.column("npm", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

        #================fetch data================
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", "end", values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No data found to export", parent=self.root)
                return False

            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your data exported to " + os.path.basename(fln) + " successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)


    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content["values"]
        self.var_atten_id.set(rows[0])
        self.var_npm.set(rows[1])
        self.var_name.set(rows[2])
        self.var_dep.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_name.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("")

    def update_data(self):
        try:
            if self.var_atten_id.get() == "":
                messagebox.showerror("Error", "Attendance ID must be required", parent=self.root)
            else:
                for i in range(len(mydata)):
                    if mydata[i][0] == self.var_atten_id.get():
                        mydata[i] = (self.var_atten_id.get(), self.var_npm.get(), self.var_name.get(), self.var_dep.get(), self.var_time.get(), self.var_date.get(), self.var_attendance.get())
                        messagebox.showinfo("Success", "Record successfully updated", parent=self.root)
                        self.fetchData(mydata)
                        self.reset_data()
                        break

        except Exception as es:
            messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)

        
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
