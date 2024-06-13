from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox as mb
import os 
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System:
        def __init__(self, root):
                self.root = root
                self.root.geometry("1920x1080+0+0")
                self.root.title("Face Recognition System")


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
                img4=img4.resize((1920, 1080))
                self.photoimg4=ImageTk.PhotoImage(img4)

                bg_img = Label(self.root, image=self.photoimg4)
                bg_img.place(x=0, y=130, width=1920, height=1080)
                

                title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 30, "bold"), bg="white", fg="blue")
                title_lbl.place(x=0, y=0, width=1920, height=45)


                #student button
                img5=Image.open(r".\\images\\student.jpg")
                img5=img5.resize((220,220))
                self.photoimg5=ImageTk.PhotoImage(img5)

                b1 = Button(bg_img, image=self.photoimg5, command=self.student_details, cursor="hand2")
                b1.place(x=267, y=150, width=220, height=220)

                b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
                b1_1.place(x=267, y=350, width=220, height=40)



                #Detect face button
                img6=Image.open(r".\\images\\boy.jpg")
                img6=img6.resize((220,220))
                self.photoimg6=ImageTk.PhotoImage(img6)

                b2 = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.face_data)
                b2.place(x=651, y=150, width=220, height=220)

                b2_2 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
                b2_2.place(x=651, y=350, width=220, height=40)



                #Attendance button
                img7=Image.open(r".\\images\\attendance.jpg")
                img7=img7.resize((220,220))
                self.photoimg7=ImageTk.PhotoImage(img7)

                b3 = Button(bg_img, image=self.photoimg7, cursor="hand2", command=self.attendance_data)
                b3.place(x=1047, y=150, width=220, height=220)
                b3_3 = Button(bg_img, text="Attendance", cursor="hand2", command=self.attendance_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
                b3_3.place(x=1047, y=350, width=220, height=40)



                #Help button
                img8=Image.open(r".\\images\\help.jpg")
                img8=img8.resize((220,220))
                self.photoimg8=ImageTk.PhotoImage(img8)

                b4 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.help_data)
                b4.place(x=1420, y=150, width=220, height=220)

                b4_4 = Button(bg_img, text="Help Desk", cursor="hand2",command=self.help_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
                b4_4.place(x=1420, y=350, width=220, height=40)



                #Train button
                img9=Image.open(r".\\images\\traindata.jpeg")
                img9=img9.resize((220,220))
                self.photoimg9=ImageTk.PhotoImage(img9)

                b5 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.train_data)
                b5.place(x=267, y=380+100, width=220, height=220)

                b5_5 = Button(bg_img, text="Train Data", cursor="hand2", command=self.train_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
                b5_5.place(x=267, y=580+100, width=220, height=40)



                #Photos button
                img10=Image.open(r".\\images\\photos.jpg")
                img10=img10.resize((220,220))
                self.photoimg10=ImageTk.PhotoImage(img10)

                b6 = Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.open_img)
                b6.place(x=651, y=380+100, width=220, height=220)

                b6_6 = Button(bg_img, text="Photos", cursor="hand2", command=self.open_img, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
                b6_6.place(x=651, y=580+100, width=220, height=40)


                #Developer button
                img11=Image.open(r".\\images\\developer.jpg")
                img11=img11.resize((220,220))
                self.photoimg11=ImageTk.PhotoImage(img11)

                b7 = Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.developer_data)
                b7.place(x=1047, y=380+100, width=220, height=220)
                
                b7_7 = Button(bg_img, text="Developer", cursor="hand2", command=self.developer_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
                b7_7.place(x=1047, y=580+100, width=220, height=40)



                #, command=self.iExit button
                img12=Image.open(r".\\images\\exit.jpg")
                img12=img12.resize((220,220))
                self.photoimg12=ImageTk.PhotoImage(img12)


                b8 = Button(bg_img, image=self.photoimg12, cursor="hand2", command=self.iExit)
                b8.place(x=1420, y=380+100, width=220, height=220)

                b8_8 = Button(bg_img, text="Exit", cursor="hand2", command=self.iExit, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
                b8_8.place(x=1420, y=680, width=220, height=40)









        #=================Function======================

        def student_details(self):
                self.new_window = Toplevel(self.root)
                self.app = Student(self.new_window)




#BAGIAN PIRA

        def open_img(self):
                os.startfile("data")
        
        def iExit(self):
                self.iExit=mb.askyesno("Face Recognition","Are you sure you want to exit this project?", parent=self.root)
                if self.iExit>0:
                        self.root.destroy()
                else:
                        return

        
        def train_data(self):
                self.new_window = Toplevel(self.root)
                self.app = Train(self.new_window)

        def face_data(self):
                self.new_window = Toplevel(self.root)
                self.app = Face_Recognition(self.new_window)

        def attendance_data(self):
                self.new_window = Toplevel(self.root)
                self.app = Attendance(self.new_window)

        def developer_data(self):
                self.new_window = Toplevel(self.root)
                self.app = Developer(self.new_window)

        def help_data(self):
                self.new_window = Toplevel(self.root)
                self.app = Help(self.new_window)













if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()

