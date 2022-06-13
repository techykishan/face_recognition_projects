from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition

class Face_recognition_system:
    def __init__(self, root): 
        self.root = root 
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


# first image
        img = Image.open(
            "C:/Users/10 PRO BOOK/Desktop/face recognition system/images/1.jpeg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

# second image
        img1 = Image.open(
            "C:/Users/10 PRO BOOK/Desktop/face recognition system/images/2.png")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)
# third image
        img2 = Image.open(
            "C:/Users/10 PRO BOOK/Desktop/face recognition system/images/3.jpg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=450, height=130)

# bg Image->
        img3 = Image.open(
            "C:/Users/10 PRO BOOK/Desktop/face recognition system/images/bg_img.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

# for Title
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM ", font=(
            "times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1430, height=40)

# Student's Buttons
        img4 = Image.open(
            "C:/Users/10 PRO BOOK/Desktop/face recognition system/images/student.jpg")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,
                    command=self.student_details, cursor="hand2")
        b1.place(x=100, y=70, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="dark blue", fg="white")
        b1_1.place(x=100, y=250, width=220, height=40)

# Detect face Buttons
        img5 = Image.open(
            "C:/Users/10 PRO BOOK/Desktop/face recognition system/images/face_detector.jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.face_data)
        b2.place(x=400, y=70, width=220, height=220)

        b2_2 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data, font=(
            "times new roman", 15, "bold"), bg="dark blue", fg="white")
        b2_2.place(x=400, y=250, width=220, height=40)


# Attendance Buttons
        img6 = Image.open(
            "C:/Users/10 PRO BOOK/Desktop/face recognition system/images/attendance.jpeg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b3.place(x=700, y=70, width=220, height=220)

        b3_3 = Button(bg_img, text="Attendance", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="dark blue", fg="white")
        b3_3.place(x=700, y=250, width=220, height=40)


# Help Desk Buttons
        img7 = Image.open(
            "C:/Users/10 PRO BOOK/Desktop/face recognition system/images/help.jpeg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b5 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b5.place(x=1000, y=70, width=220, height=220)

        b5_5 = Button(bg_img, text="Help Desk", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="dark blue", fg="white")
        b5_5.place(x=1000, y=250, width=220, height=40)


# Train Buttons
        img8 = Image.open(
            "C:/Users/10 PRO BOOK/Desktop/face recognition system/images/train.jpg")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b6 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.train_data)
        b6.place(x=100, y=320, width=220, height=220)

        b6_6 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data, font=(
            "times new roman", 15, "bold"), bg="dark blue", fg="white")
        b6_6.place(x=100, y=500, width=220, height=40)

# Phtos Buttons
        img9 = Image.open(
            "C:/Users/10 PRO BOOK/Desktop/face recognition system/images/photos.jpg")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b7 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b7.place(x=400, y=320, width=220, height=220)

        b7_7 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img, font=(
            "times new roman", 15, "bold"), bg="dark blue", fg="white")
        b7_7.place(x=400, y=500, width=220, height=40)


# Developer Buttons
        img10 = Image.open(
            "C:/Users/10 PRO BOOK/Desktop/face recognition system/images/developer.jpg")
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b8 = Button(bg_img, image=self.photoimg10, cursor="hand2")
        b8.place(x=700, y=320, width=220, height=220)

        b8_8 = Button(bg_img, text="Developer", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="dark blue", fg="white")
        b8_8.place(x=700, y=500, width=220, height=40)

# Exit Buttons
        img11 = Image.open(
            "C:/Users/10 PRO BOOK/Desktop/face recognition system/images/exit.jpg")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b9 = Button(bg_img, image=self.photoimg11, cursor="hand2")
        b9.place(x=1000, y=320, width=220, height=220)

        b9_9 = Button(bg_img, text="Exit", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="dark blue", fg="white")
        b9_9.place(x=1000, y=500, width=220, height=40)


    def open_img(self):
        os.startfile("data")

# ********************* Functions Buttons***************


    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)




if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition_system(root)
    root.mainloop()
