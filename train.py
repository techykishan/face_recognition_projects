from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System ")

# for Title
        title_lbl = Label(self.root, text="Train Dataset", font=(
            "times new roman", 35, "bold"), bg="white", fg="Red")
        title_lbl.place(x=0, y=0, width=1430, height=40) 

        
        img_top = Image.open(
            "C:/Users/10 PRO BOOK/Desktop/face recognition system/images/img_top.png")
        img_top = img_top.resize((1530, 325), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)

#button
        b7_7 = Button(self.root, text="TRAIN DATA", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="blue", fg="white")
        b7_7.place(x=0, y=380, width=1530, height=60)

        
        img_bottom = Image.open(
            "C:/Users/10 PRO BOOK/Desktop/face recognition system/images/img_bottom.png")
        img_bottom = img_bottom.resize((1530, 325), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1530, height=300)
    



if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
