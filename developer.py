import tkinter as tk
from tkinter import Label, Frame
from PIL import Image, ImageTk

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080")

        # Background Image
        img_top = Image.open(r".\\images\\bg.jpg")
        img_top = img_top.resize((1920, 1080), Image.BICUBIC)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=0, width=1920, height=1080)

        # Title Label
        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="white", fg="navyblue")
        title_lbl.place(x=0, y=0, width=1920, height=45)

        # Frame for Caca
        caca_frame = Frame(f_lbl, bg="navy")
        caca_frame.place(x=173, y=138, width=691, height=383)

        caca_img = Image.open(r".\\images\\girl.jpg")
        caca_img = caca_img.resize((200, 250), Image.LANCZOS)
        self.photoimg_caca = ImageTk.PhotoImage(caca_img)

        caca_img_lbl = Label(caca_frame, image=self.photoimg_caca)
        caca_img_lbl.place(x=66, y=67, width=200, height=250)

        caca_data_frame = Frame(caca_frame, bg="white")
        caca_data_frame.place(x=276, y=67, width=350, height=250)

        caca_description = Label(caca_data_frame, text="Adinda Salsabila\n2215061035\n@chacasta_staria\nchacastastaria@gmail.com", font=("times new roman", 15), bg="white")
        caca_description.place(x=0, y=0, width=350, height=250)

        # Frame for Ajeng
        ajeng_frame = Frame(f_lbl, bg="navy")
        ajeng_frame.place(x=1068, y=138, width=691, height=383)

        ajeng_img = Image.open(r".\\images\\girl.jpg")
        ajeng_img = ajeng_img.resize((200, 250), Image.LANCZOS)
        self.photoimg_ajeng = ImageTk.PhotoImage(ajeng_img)

        ajeng_img_lbl = Label(ajeng_frame, image=self.photoimg_ajeng)
        ajeng_img_lbl.place(x=66, y=67, width=200, height=250)

        ajeng_data_frame = Frame(ajeng_frame, bg="white")
        ajeng_data_frame.place(x=276, y=67, width=350, height=250)

        ajeng_description = Label(ajeng_data_frame, text="Ajeng Nursyifa\n2215061035\n@ajengnsyy\nemailajeng@gmail.com", font=("times new roman", 15), bg="white")
        ajeng_description.place(x=0, y=0, width=350, height=250)

        # Frame for Pira
        pira_frame = Frame(f_lbl, bg="navy")
        pira_frame.place(x=173, y=610, width=691, height=383)

        pira_img = Image.open(r".\\images\\girl.jpg")
        pira_img = pira_img.resize((200, 250), Image.LANCZOS)
        self.photoimg_pira = ImageTk.PhotoImage(pira_img)

        pira_img_lbl = Label(pira_frame, image=self.photoimg_pira)
        pira_img_lbl.place(x=66, y=67, width=200, height=250)

        pira_data_frame = Frame(pira_frame, bg="white")
        pira_data_frame.place(x=276, y=67, width=350, height=250)

        pira_description = Label(pira_data_frame, text="Ghefira Zahira Sofa\n2215061127\n@ghefirazahira\nghefirazahirasofa@gmail.com", font=("times new roman", 15), bg="white")
        pira_description.place(x=0, y=0, width=350, height=250)

        # Frame for Emy
        emy_frame = Frame(f_lbl, bg="navy")
        emy_frame.place(x=1068, y=610, width=691, height=383)

        emy_img = Image.open(r".\\images\\girl.jpg")
        emy_img = emy_img.resize((200, 250), Image.LANCZOS)
        self.photoimg_emy = ImageTk.PhotoImage(emy_img)

        emy_img_lbl = Label(emy_frame, image=self.photoimg_emy)
        emy_img_lbl.place(x=66, y=67, width=200, height=250)

        emy_data_frame = Frame(emy_frame, bg="white")
        emy_data_frame.place(x=276, y=67, width=350, height=250)

        emy_description = Label(emy_data_frame, text="Nur Emy Ramadhani\n2215061027\n@nuremy\nemyramadhani@gmail.com", font=("times new roman", 15), bg="white")
        emy_description.place(x=0, y=0, width=350, height=250)

if __name__ == "__main__":
    root = tk.Tk()
    app = Developer(root)
    root.mainloop()
