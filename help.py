from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="navyblue")
        title_lbl.place(x=0,y=0,width=1920,height=45)
        
        img_top=Image.open(r".\\images\\bg.jpg")
        img_top=img_top.resize((1920,1080),Image.BICUBIC)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1920, height=1080)

        dev_label=Label(f_lbl,text="Email:chacastastaria@gmail.com",font=("times new roman",20,"bold"),bg="white",fg="navyblue")
        dev_label.place(x=720,y=220)






if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
