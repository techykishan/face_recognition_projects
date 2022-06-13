from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System ")

        # ****************************variables******************
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()


# first image
        img = Image.open("C:/Users/10 PRO BOOK/Desktop/face recognition system/images/11.jpg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

# second image
        img1 = Image.open(
            "C:/Users/10 PRO BOOK/Desktop/face recognition system/images/22.jpg")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

# third image
        img2 = Image.open(
            "C:/Users/10 PRO BOOK/Desktop/face recognition system/images/33.jpg")
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
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM ", font=(
            "times new roman", 35, "bold"), bg="white", fg="dark green")
        title_lbl.place(x=0, y=0, width=1430, height=40)

# frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=50, width=1600, height=550)

# left side label frame
        Left_frame = LabelFrame(main_frame, bd=4, bg="light blue", relief=RIDGE,
                                text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=660, height=500)

        img_left = Image.open(
            "C:/Users/10 PRO BOOK/Desktop/face recognition system/images/left_img.jpg")
        img_left = img_left.resize((640, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=4, y=0, width=640, height=110)

# current course
        current_course_frame = LabelFrame(Left_frame, bd=4, bg="light blue", relief=RIDGE,
                                          text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=3, y=60, width=640, height=110)

# labels-> Department
        dep_label = Label(current_course_frame, text="Department", font=(
            "times new roman", 10, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=2, pady=10)

# combo_Box
        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=(
            "times new roman", 10, "bold"), state="read only", width=20)
        dep_combo["values"] = ("Select department",
                               "Computer Science", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)


# labels->Course
        course_label = Label(current_course_frame, text="Course", font=(
            "times new roman", 10, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

# combo_Box
        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course,  font=(
            "times new roman", 10, "bold"), state="read only", width=20)
        course_combo["values"] = ("Select Course", "FE", "TE", "CI", "Ml")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)


# labels->Year
        year_label = Label(current_course_frame, text="Year", font=(
            "times new roman", 10, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=2, pady=10, sticky=W)

# combo_Box
        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year,  font=(
            "times new roman", 10, "bold"), state="read only", width=20)
        year_combo["values"] = ("Select Year", "2020-21",
                                "2021-22", "2022-2023", "2023-2024")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)


# labels->Semester
        semester_label = Label(current_course_frame, text="Semester", font=(
            "times new roman", 10, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=2, pady=10, sticky=W)

# combo_Box
        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester,  font=(
            "times new roman", 10, "bold"), state="read only", width=20)
        semester_combo["values"] = (
            "Select semester", "semester-1", "semester-2", "semester-3", "semester-4")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)


# class student information
        class_student_frame = LabelFrame(Left_frame, bd=4, bg="light blue", relief=RIDGE,
                                         text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=3, y=170, width=640, height=300)

# labels->StudentID
        studentid_label = Label(class_student_frame, text="StudentID:", font=(
            "times new roman", 10, "bold"), bg="white")
        studentid_label.grid(row=0, column=0, padx=5, pady=3, sticky=W)

        studentid_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_std_id,  width=20, font=("times new roman", 12, "bold"))
        studentid_entry.grid(row=0, column=1, padx=6, sticky=W)


# labels->student name
        studentName_label = Label(class_student_frame, text="Student Name:", font=(
            "times new roman", 10, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=5, pady=3, sticky=W)

        studentName_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_std_name,  width=20, font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=6, pady=5, sticky=W)


# labels->class division
        classdiv_label = Label(class_student_frame, text="Class Division:", font=(
            "times new roman", 10, "bold"), bg="white")
        classdiv_label.grid(row=1, column=0, padx=5, pady=3, sticky=W)

        # classdiv_entry = ttk.Entry(
        #     class_student_frame,textvariable=self.var_div,  width=20, font=("times new roman", 12, "bold"))
        # classdiv_entry.grid(row=1, column=1, padx=6, pady=5, sticky=W)

        div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div,  font=(
            "times new roman", 10, "bold"), state="read only", width=21)
        div_combo["values"] = (
            "A", "B", "C")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=5, pady=10, sticky=W)


# labels->Roll No
        Rollno_label = Label(class_student_frame, text="Roll No:", font=(
            "times new roman", 10, "bold"), bg="white")
        Rollno_label.grid(row=1, column=2, padx=5, pady=3, sticky=W)

        Rollno_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_roll,  width=20, font=("times new roman", 12, "bold"))
        Rollno_entry.grid(row=1, column=3, padx=6, pady=5, sticky=W)


# labels->Gender
        Gender_label = Label(class_student_frame, text="Gender:", font=(
            "times new roman", 10, "bold"), bg="white")
        Gender_label.grid(row=2, column=0, padx=5, pady=3, sticky=W)

        # Gender_entry = ttk.Entry(
        #     class_student_frame,textvariable=self.var_gender,  width=20, font=("times new roman", 12, "bold"))
        # Gender_entry.grid(row=2, column=1, padx=6, pady=5, sticky=W)

        Gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender,  font=(
            "times new roman", 10, "bold"), state="read only", width=21)
        Gender_combo["values"] = (
            "Male", "Female", "Other")
        Gender_combo.current(0)
        Gender_combo.grid(row=2, column=1, padx=5, pady=5, sticky=W)


# labels->dob
        dob_label = Label(class_student_frame, text="DOB:", font=(
            "times new roman", 10, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=5, pady=3, sticky=W)

        dob_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_dob,  width=20, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=6, pady=5, sticky=W)

 # labels->E mail
        Email_label = Label(class_student_frame, text="Email", font=(
            "times new roman", 10, "bold"), bg="white")
        Email_label.grid(row=3, column=0, padx=5, pady=3, sticky=W)

        Email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email,  width=20, font=(
            "times new roman", 12, "bold"))
        Email_entry.grid(row=3, column=1, padx=6, pady=5, sticky=W)


# labels->Phone no
        Phone_label = Label(class_student_frame, text="Phone No:", font=(
            "times new roman", 10, "bold"), bg="white")
        Phone_label.grid(row=3, column=2, padx=5, pady=3, sticky=W)

        Phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone,  width=20, font=(
            "times new roman", 12, "bold"))
        Phone_entry.grid(row=3, column=3, padx=6, pady=5, sticky=W)


# labels->Addess
        address_label = Label(class_student_frame, text="Address:", font=(
            "times new roman", 10, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=5, pady=3, sticky=W)

        address_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_address, width=20, font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=6, pady=5, sticky=W)

 # labels->Teacher Names
        teacher_label = Label(class_student_frame, text="Teacher Name:", font=(
            "times new roman", 12, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=5, pady=3, sticky=W)

        teacher_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_teacher, width=20, font=("times new roman", 12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=6, pady=5, sticky=W)
    
# radio buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1,
                                text="Take Photo Sample", value="yes")
        radiobtn1.grid(row=6, column=0)

        radiobtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1,
                                text="No Photo Sample", value="No")
        radiobtn2.grid(row=6, column=1)

# button frame
        btn_frame = Frame(class_student_frame, bd=1, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=210, width=600, height=30)

# save button
        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=16, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

# update button
        update_btn = Button(btn_frame, text="Update", command=self.Update_data, width=16, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

 # Delete button
        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=16, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

# Reset button
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=16, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

# button1 frame
        btn_frame1 = Frame(class_student_frame, bd=1, relief=RIDGE, bg="white")
        btn_frame1.place(x=5, y=240, width=600, height=30)


# Take photo button
        take_photo_btn = Button(btn_frame1, command=self.generate_dataset, text="Take Photo Sample", width=33, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=0)


#  update photo button
        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", width=33, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1)


# right side label frame
        Right_frame = LabelFrame(main_frame, bd=4, bg="light blue", relief=RIDGE,
                                 text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=680, y=10, width=660, height=500)

        img_right = Image.open(
            "C:/Users/10 PRO BOOK/Desktop/face recognition system/images/right_img.jpg")
        img_right = img_right.resize((640, 130), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=4, y=0, width=640, height=80)


#       *********Searching System**************


# Search Frame
        search_frame = LabelFrame(Right_frame, bd=4, bg="light blue", relief=RIDGE,
                                  text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=3, y=80, width=640, height=65)

# labels->search label
        search_label = Label(search_frame, text="Serach By:", font=(
            "times new roman", 10, "bold"), bg="red", fg="yellow")
        search_label.grid(row=0, column=0, padx=2, pady=10, sticky=W)


# combo_Box
        search_combo = ttk.Combobox(search_frame, font=(
            "times new roman", 10, "bold"), state="read only", width=15)
        search_combo["values"] = ("Select", "Roll No", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame, width=15, font=(
            "times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=6, pady=5, sticky=W)


# search button
        search_btn = Button(search_frame, text="Search", width=14, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=4)


# showall button
        showAll_btn = Button(search_frame, text="Show All", width=14, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=4)


#       ***************Table frame***************
        table_frame = Frame(Right_frame, bd=4, bg="light blue", relief=RIDGE)
        table_frame.place(x=5, y=150, width=640, height=320)

# scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender",
                                          "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

# header
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

# setting up width of headings
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)
# table pack
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()


# *********************Function Declaration*******************

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id == "":
            messagebox.showerror("Error", "All Fields are required")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", port="3306", password="kishan8283#", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (

                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Student details has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To :{str(es)}", parent=self.root)

    # ********************************************* Fetch Data **********************

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root",
                                       port="3306", password="kishan8283#", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student ")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ****************** get cursor ***********
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14]),

# ************** Update function **********

    def Update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id == "":
            messagebox.showerror("Error", "All Fields are required")
        else:
            try:
                Upadate = messagebox.askyesno(
                    "Update", "Do you want to update this detail", parent=self.root)
                if Upadate > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", port="3306", password="kishan8283#", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("Update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s", (

                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()

                    ))
                else:
                    if not Upadate:
                        return
                messagebox.showinfo(
                    "Success", "Student details Successfully Update completed", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to :{str(es)}", parent=self.root)

    # ************** delete function ************

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete Page", "Do you want to Delete Student data", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", port="3306", password="kishan8283#", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Delete", "Sucessfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to :{str(es)}", parent=self.root)

# ************************ Reaset Function ***************
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_dep.set("Select Department")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

        # ******************** generate dataset  or Take photo samples***********
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id == "":
            messagebox.showerror("Error", "All Fields are required")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", port="3306", password="kishan8283#", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student ")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("Update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s", (

                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get() == id+1
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


# **************************************load predefined data on face frontals from opencv *****************

                face_clssifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml")

                def face_croped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_clssifier.detectMultiScale(gray, 1.3, 5)
                    # 1.3->scaling factor
                    # minimum neighbour=5

                    for(x, y, w, h) in faces:
                        face_croped = img[y:y+h, x:x+w]
                        return face_croped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_croped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_croped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + \
                            str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo(
                    "Result", "Generating Datasets Completed !!!!")
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to :{str(es)}", parent=self.root)








if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
