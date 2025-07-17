from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from new_register import New_Register
from student_list import Student
from face_detector import recognize_face
from tkinter import messagebox


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.configure(bg='black')
        

        title_lbl=Label(text="HOSTEL FACIAL RECOGNITION SYSTEM",font=("times new romen",35,"bold"),bg="black",fg="yellow")
        title_lbl.place(x=0,y=0,width=1530,height=300)

        # New register button
        img1=Image.open(r"C:\Users\Jerin\OneDrive\Pictures\register.jpg")
        img1=img1.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        b1=Button(image=self.photoimg1,command=self.register,cursor="hand2")
        b1.place(x=200,y=300,width=220,height=220)

        b1_1=Button(text="NEW REGISTER",command=self.register,cursor="hand2",font=("times new romen",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=500,width=220,height=40)

         # Face Recognition button
        img2=Image.open(r"C:\Users\Jerin\OneDrive\Pictures\recognice.jpg")
        img2=img2.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b2=Button(image=self.photoimg2,command=self.detect_face,cursor="hand2")
        b2.place(x=650,y=300,width=220,height=220)

        b2_2=Button(text="FACE DETECTOR",command=self.detect_face,cursor="hand2",font=("times new romen",15,"bold"),bg="darkblue",fg="white")
        b2_2.place(x=650,y=500,width=220,height=40)

         # Student List button
        img3=Image.open(r"C:\Users\Jerin\OneDrive\Pictures\list.jpg")
        img3=img3.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b3=Button(image=self.photoimg3,command=self.list,cursor="hand2")
        b3.place(x=1100,y=300,width=220,height=220)

        b3_3=Button(text="STUDENT LIST",command=self.list,cursor="hand2",font=("times new romen",15,"bold"),bg="darkblue",fg="white")
        b3_3.place(x=1100,y=500,width=220,height=40)

        # Exit button
        b4=Button(text="EXIT",command=self.exit_func,cursor="hand2",font=("times new romen",15,"bold"),bg="darkblue",fg="white")
        b4.place(x=1160,y=700,width=100,height=40)

    # Function Decleration

    def register(self):
        self.new_window=Toplevel(self.root)
        self.app=New_Register(self.new_window)

    def list(self):
        self.newly=Toplevel(self.root)
        self.appli=Student(self.newly)

    def detect_face(self):
        recognize_face()

    def exit_func(self):
        confirm=messagebox.askyesno("Exit","Are you sure you want to exit?")
        if confirm:
            self.root.destroy()



if __name__=="__main__"  :
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()