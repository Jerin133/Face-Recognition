import tkinter as tk
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkcalendar import DateEntry
import datetime
import csv
from tkinter import messagebox
import cv2
import os


class New_Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.configure(bg='black')

        title_lbl=Label(self.root,text="REGISTER NEW STUDENTS",font=("times new romen",35,"bold"),bg="black",fg="yellow")
        title_lbl.place(x=0,y=0,width=1530,height=70)

        # Frame1
        frame_1=LabelFrame(self.root,bd=2,relief=RIDGE,text="STUDENT DETAILS",font=("times new romen",25,"bold"),bg="black",fg="yellow")
        frame_1.place(x=5,y=70,width=730,height=720)

        # Name label
        name_label=Label(frame_1,text="Student Name",font=("times new romen",20,"bold"),bg="black",fg="white")
        name_label.grid(row=0,column=0,padx=40,pady=20,sticky="W")

        self.name_text=ttk.Entry(frame_1,font=("times new romen",12),width=23)
        self.name_text.grid(row=0,column=1,padx=20,pady=15)

        # Date of Birth Label
        dob_label=Label(frame_1,text="Date of Birth",font=("times new romen",20,"bold"),bg="black",fg="white")
        dob_label.grid(row=1,column=0,padx=40,pady=20,sticky="W")

        today=datetime.date.today()
        dob_picker = DateEntry(frame_1,date_pattern="dd-mm-yyyy",font=("times new romen",12),width=21,maxdate=today,state="readonly")
        dob_picker.grid(row=1,column=1,padx=20,pady=15)

        # Gender Label
        gender_label=Label(frame_1,text="Gender",font=("times new romen",20,"bold"),bg="black",fg="white")
        gender_label.grid(row=2,column=0,padx=40,pady=20,sticky="W")

        gender_combo=ttk.Combobox(frame_1,font=("times new romen",12),width=21,state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=20,pady=15)

        # Phone no. label
        phone_label=Label(frame_1,text="Phone Number",font=("times new romen",20,"bold"),bg="black",fg="white")
        phone_label.grid(row=3,column=0,padx=40,pady=20,sticky="W")

        def validate_reg_number(P):
            return P.isdigit() and len(P)<=10 or P==""

        phone_text=ttk.Entry(frame_1,font=("times new romen",12),width=23,validate="key",validatecommand=(frame_1.register(validate_reg_number),"%P"))
        phone_text.grid(row=3,column=1,padx=20,pady=15)

        # Address Frame
        add_frame_1=LabelFrame(frame_1,bd=2,relief=RIDGE,text="ADDRESS DETAILS",font=("times new romen",18,"bold"),bg="black",fg="yellow")
        add_frame_1.place(x=5,y=315,width=715,height=360)

        # Address Label
        village_label=Label(add_frame_1,text="Village Name",font=("times new romen",20,"bold"),bg="black",fg="white")
        village_label.grid(row=0,column=0,padx=40,pady=15,sticky="W")

        village_text=ttk.Entry(add_frame_1,font=("times new romen",12),width=23)
        village_text.grid(row=0,column=1,padx=50,pady=15)


        taluk_label=Label(add_frame_1,text="Taluk Name",font=("times new romen",20,"bold"),bg="black",fg="white")
        taluk_label.grid(row=1,column=0,padx=40,pady=15,sticky="W")

        taluk_text=ttk.Entry(add_frame_1,font=("times new romen",12),width=23)
        taluk_text.grid(row=1,column=1,padx=50,pady=15)


        district_label=Label(add_frame_1,text="District Name",font=("times new romen",20,"bold"),bg="black",fg="white")
        district_label.grid(row=2,column=0,padx=40,pady=15,sticky="W")

        district_text=ttk.Entry(add_frame_1,font=("times new romen",12),width=23)
        district_text.grid(row=2,column=1,padx=50,pady=15)


        state_label=Label(add_frame_1,text="State Name",font=("times new romen",20,"bold"),bg="black",fg="white")
        state_label.grid(row=3,column=0,padx=40,pady=15,sticky="W")

        state_text=ttk.Entry(add_frame_1,font=("times new romen",12),width=23)
        state_text.grid(row=3,column=1,padx=50,pady=15)


        pin_label=Label(add_frame_1,text="Pincode",font=("times new romen",20,"bold"),bg="black",fg="white")
        pin_label.grid(row=4,column=0,padx=40,pady=15,sticky="W")

        def validate_pin_number(P):
            return P.isdigit() and len(P)<=6 or P==""

        pin_text=ttk.Entry(add_frame_1,font=("times new romen",12),width=23,validate="key",validatecommand=(add_frame_1.register(validate_pin_number),"%P"))
        pin_text.grid(row=4,column=1,padx=50,pady=15)


        # Frame2
        frame_2=LabelFrame(self.root,bd=2,relief=RIDGE,text="COURSE DETAILS",font=("times new romen",25,"bold"),bg="black",fg="yellow")
        frame_2.place(x=750,y=70,width=775,height=720)

        # Roll no. label
        roll_label=Label(frame_2,text="Roll Number",font=("times new romen",20,"bold"),bg="black",fg="white")
        roll_label.grid(row=0,column=0,padx=40,pady=20,sticky="W")

        self.roll_text=ttk.Entry(frame_2,font=("times new romen",12),width=22)
        self.roll_text.grid(row=0,column=1,padx=20,pady=15)

        # Department label
        dep_label=Label(frame_2,text="Department",font=("times new romen",20,"bold"),bg="black",fg="white")
        dep_label.grid(row=2,column=0,padx=40,pady=20,sticky="W")

        dep_combo=ttk.Combobox(frame_2,font=("times new romen",12),width=21,state="readonly")
        dep_combo["values"]=("Select Department","Computer Science","Civil","Mechanical","Electrical Communication","Electrical and Electronics")
        dep_combo.current(0)
        dep_combo.grid(row=2,column=1,padx=20,pady=15)

        # Course Label
        course_label=Label(frame_2,text="Course",font=("times new romen",20,"bold"),bg="black",fg="white")
        course_label.grid(row=1,column=0,padx=40,pady=20,sticky="W")

        course_combo=ttk.Combobox(frame_2,font=("times new romen",12),width=21,state="readonly")
        course_combo["values"]=("Select Course","BE","ME","FE","Bachelors")
        course_combo.current(0)
        course_combo.grid(row=1,column=1,padx=20,pady=15)

        # Year Label
        Year_label=Label(frame_2,text="Year",font=("times new romen",20,"bold"),bg="black",fg="white")
        Year_label.grid(row=3,column=0,padx=40,pady=20,sticky="W")

        current_year = datetime.datetime.now().year
        year_range = [f"{year}-{year+4}" for year in range(current_year - 5,current_year + 1)]
        year_combo = ttk.Combobox(frame_2,values=year_range,state="readonly",font=("times new romen",12),width=21)
        year_combo.set(f"{current_year}-{current_year+4}") 
        year_combo.grid(row=3,column=1,padx=20,pady=15)

        # Sem Label
        sem_label=Label(frame_2,text="Semester",font=("times new romen",20,"bold"),bg="black",fg="white")
        sem_label.grid(row=4,column=0,padx=40,pady=20,sticky="W")

        sem_combo=ttk.Combobox(frame_2,font=("times new romen",12),width=21,state="readonly")
        sem_combo["values"]=("Select Sem","1","2","3","4","5","6","7","8")
        sem_combo.current(0)
        sem_combo.grid(row=4,column=1,padx=20,pady=15)

        # Date of Joining Label
        doj_label=Label(frame_2,text="Date of Joining",font=("times new romen",20,"bold"),bg="black",fg="white")
        doj_label.grid(row=5,column=0,padx=40,pady=20,sticky="W")

        today=datetime.date.today()
        doj_picker = DateEntry(frame_2,date_pattern="dd-mm-yyyy",font=("times new romen",12),width=21,maxdate=today,state="readonly")
        doj_picker.grid(row=5,column=1,padx=20,pady=15)

        # Way Of Joining Label
        woj_label=Label(frame_2,text="Way of Joining",font=("times new romen",20,"bold"),bg="black",fg="white")
        woj_label.grid(row=6,column=0,padx=40,pady=20,sticky="W")

        woj_combo=ttk.Combobox(frame_2,font=("times new romen",12),width=21,state="readonly")
        woj_combo["values"]=("Select Way","General","7.5 Reservation","Special Reservation")
        woj_combo.current(0)
        woj_combo.grid(row=6,column=1,padx=20,pady=15)

        #Radio Button
        style=ttk.Style()
        style.configure("Custom.TRadiobutton",background="black",foreground="white",font=("times new romen",13,"bold"))
        select=tk.StringVar(value="None")

        radio1=ttk.Radiobutton(frame_2,text="Taken Photo Sample",width=20,style="Custom.TRadiobutton",variable=select,value="Taken Photo Sample")
        radio1.grid(row=7,column=0)

        radio2=ttk.Radiobutton(frame_2,text="Not Taken Photo Sample",width=25,style="Custom.TRadiobutton",variable=select,value="Not Taken Photo Sample")
        radio2.grid(row=7,column=1,padx=30)

        # Buttons
        save_button=Button(frame_2,text="Save",font=("times new romen",18,"bold"),bg="darkblue",fg="white",width=12)
        save_button.place(x=50,y=600)

        take_photo_button=Button(frame_2,text="Take Photo",font=("times new romen",18,"bold"),bg="darkblue",fg="white",width=12)
        take_photo_button.place(x=280,y=600)
        take_photo_button.config(command=self.take_photo)

        update_photo_button=Button(frame_2,text="Update Photo",command=self.update_photo,font=("times new romen",18,"bold"),bg="darkblue",fg="white",width=12)
        update_photo_button.place(x=510,y=600)

        # Function of Save Button
        def save_student():
            name = self.name_text.get().strip()
            dob = dob_picker.get()
            gender = gender_combo.get()
            phone = phone_text.get()
            village = village_text.get()
            taluk = taluk_text.get()
            district = district_text.get()
            state = state_text.get()
            pincode = pin_text.get()
            roll_no = self.roll_text.get()
            department = dep_combo.get()
            course = course_combo.get()
            year = year_combo.get()
            semester = sem_combo.get()
            doj = doj_picker.get()
            way_of_joining = woj_combo.get()
            photo_status=select.get()

            if not name or gender == "Select Gender" or department == "Select Department" or course == "Select Course":
                messagebox.showwarning("Warning", "Please fill all required fields!" ,parent=self.root)
                return
            
            student_data = [name, dob, gender, phone, village, taluk, district, state, pincode, roll_no, department, course, year, semester, doj, way_of_joining,photo_status]

            # Save student data to CSV file
            file_exists=False
            try:
                with open("jerin.csv", "r") as file:
                    file_exists = True
            except FileNotFoundError:
                pass

            with open("jerin.csv", "a", newline="") as file:
                writer = csv.writer(file)
                if not file_exists:
                    writer.writerow(["Name", "DOB", "Gender", "Phone", "Village", "Taluk", "District", "State", "Pincode", "Roll No", "Department", "Course", "Year", "Semester", "DOJ", "Way of Joining","Photo Sample"])
                writer.writerow(student_data)

            messagebox.showinfo("Success", f"Student '{name}' registered successfully!",parent=self.root)

            # Clear fields after saving
            self.name_text.delete(0, "end")
            phone_text.delete(0, "end")
            village_text.delete(0, "end")
            taluk_text.delete(0, "end")
            district_text.delete(0, "end")
            state_text.delete(0, "end")
            pin_text.delete(0, "end")
            self.roll_text.delete(0, "end")
            select.set("None")
            
        # Link function to "Save" button
        save_button.config(command=save_student) 

    # Function for Take Photo Sample
    def take_photo(self):
        roll_no = self.roll_text.get().strip()
        name=self.name_text.get().strip()

        if not roll_no and not name:
            messagebox.showerror("Error", "Please enter the Name and Roll Number before taking a photo.", parent=self.root)
            return

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            messagebox.showerror("Error", "Could not open the camera.", parent=self.root)
            return

        messagebox.showinfo("Info", "Press 'SPACE' to capture the photo and 'ESC' to exit.", parent=self.root)

        # Get the absolute path of the photos directory
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of the script
        photo_dir = os.path.join(script_dir, "photos")
        os.makedirs(photo_dir, exist_ok=True)  # Ensure the folder is created

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                continue

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(100, 100))

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.imshow("Capture Photo", frame)

            key = cv2.waitKey(1)
            if key == 32:  # Space bar to capture
                photo_path = os.path.join(photo_dir, f"{roll_no}_{name}.jpg")

                # Save the image and print the full path
                cv2.imwrite(photo_path, frame)
                messagebox.showinfo("Success", f"Photo saved at {photo_path}", parent=self.root)
                break

            elif key == 27:  # ESC to exit
                break

        cap.release()
        cv2.destroyAllWindows()

    # Add this method inside your New_Register class
    def update_photo(self):
        # Get roll number from entry field
        roll_no = self.roll_text.get().strip()
    
        if not roll_no:
            messagebox.showerror("Error", "Please enter Roll Number first!", parent=self.root)
            return

        # Validate roll number exists in CSV
        try:
            with open("jerin.csv", "r") as file:
                reader = csv.DictReader(file)
                student_exists = False
                student_name = ""
                for row in reader:
                    if row["Roll No"] == roll_no:
                        student_exists = True
                        student_name = row["Name"]
                        break
            
                if not student_exists:
                    messagebox.showerror("Error", "Student not found in database!", parent=self.root)
                    return
        except FileNotFoundError:
            messagebox.showerror("Error", "Database file not found!", parent=self.root)
            return

        # Delete existing photos
        photos_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "photos")
        deleted = False
        if os.path.exists(photos_dir):
            # Find all photos for this student
            existing_photos = [f for f in os.listdir(photos_dir) if f.startswith(f"{roll_no}_")]
        
            # Delete existing photos
            for photo in existing_photos:
                os.remove(os.path.join(photos_dir, photo))
                deleted = True
        
        if not deleted:
            messagebox.showinfo("Info", "No existing photos found for this student", parent=self.root)
            return

        # Capture new photo
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(0)
    
        if not cap.isOpened():
            messagebox.showerror("Error", "Could not open camera!", parent=self.root)
            return

        messagebox.showinfo("Instructions", "Press SPACE to capture photo\nESC to cancel", parent=self.root)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(100, 100))

            # Draw rectangle around faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            cv2.imshow("Update Student Photo", frame)

            # Capture photo on SPACE, exit on ESC
            k = cv2.waitKey(1)
            if k % 256 == 32:  # SPACE pressed
                # Ensure photos directory exists
                os.makedirs(photos_dir, exist_ok=True)
            
                # Save image
                img_name = f"{roll_no}_{student_name}.jpg"
                img_path = os.path.join(photos_dir, img_name)
                cv2.imwrite(img_path, frame)
                messagebox.showinfo("Success", f"Photo updated successfully!\n{img_path}", parent=self.root)
                break
            elif k % 256 == 27:  # ESC pressed
                messagebox.showinfo("Info", "Photo update cancelled", parent=self.root)
                break

        cap.release()
        cv2.destroyAllWindows()

        # Update photo status in CSV
        try:
            # Read all data
            with open("jerin.csv", "r") as file:
                rows = list(csv.DictReader(file))
                fieldnames = rows[0].keys() if rows else []

            # Update matching record
            for row in rows:
                if row["Roll No"] == roll_no:
                    row["Photo Sample"] = "Updated"

            # Write back to file
            with open("jerin.csv", "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)

        except Exception as e:
            messagebox.showerror("Error", f"Error updating record: {str(e)}", parent=self.root)
        



if __name__=="__main__"  :
    root=Tk()
    obj=New_Register(root)
    root.mainloop()