import cv2
import os
import numpy as np
from tkinter import *
from tkinter import ttk
from time import strftime
from datetime import datetime, timedelta
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        # Dictionary to track last recognized face time
        self.last_recognized_time = {}

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35), bg="white", fg="navy")
        title_lbl.place(x=0, y=0, width=1920, height=45)

        # img_top = Image.open(r"images\\bg.jpg")
        # img_top = img_top.resize((650, 700))
        # self.photoimg_top = ImageTk.PhotoImage(img_top)

        # f_lbl = Label(self.root, image=self.photoimg_top)
        # f_lbl.place(x=0, y=0, width=1920, height=1035)

        img_bottom = Image.open(r"images\\bg.jpg")
        img_bottom = img_bottom.resize((1920, 1035))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=45, width=1920, height=1035)

        # Button to start face recognition
        b1_1 = Button(f_lbl, text="Face Recognition", cursor="hand2", font=("times new roman", 18, "bold"), bg="navyblue", fg="white", command=self.face_recog)
        b1_1.place(x=800, y=620, width=300, height=40)


        #=====functions=====

    def mark_attendance(self, i, r, n, d):
        current_time = datetime.now()
        if i in self.last_recognized_time:
            last_time = self.last_recognized_time[i]
            if current_time - last_time < timedelta(minutes=1): 
                return 

        self.last_recognized_time[i] = current_time

        with open("attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])
            if (i not in name_list and r not in name_list and n not in name_list and d not in name_list):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select name from student where student_id=%s", (str(id),))
                n = my_cursor.fetchone()
                n = "+".join(n) if n else "Unknown"

                my_cursor.execute("select npm from student where student_id=%s", (str(id),))
                r = my_cursor.fetchone()
                r = "+".join(r) if r else "Unknown"

                my_cursor.execute("select Dep from student where student_id=%s", (str(id),))
                d = my_cursor.fetchone()
                d = "+".join(d) if d else "Unknown"

                my_cursor.execute("select npm from student where student_id=%s", (str(id),))
                i = my_cursor.fetchone()
                i = "+".join(i) if i else "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"NPM:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:
                print("Failed to grab frame")
                break
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Point your face to the camera to record attendance", img)
            

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
