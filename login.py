from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from main import Face_Recognition_System
from new_user import user

class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.root.configure(bg="black")

        frame=LabelFrame(self.root,bd=2,relief=RIDGE,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img=Image.open(r"C:\Users\Jerin\Downloads\logo1.png")
        img=img.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img)
        lable=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lable.place(x=730,y=175,width=100,height=100)

        get_started=Label(frame,text="Get Started",font=("times new romen",20,"bold"),bg="black",fg="white")
        get_started.place(x=95,y=100)

        # Labels
        username=lbl=Label(frame,text="Username",font=("times new romen",15,"bold"),bg="black",fg="white")
        username.place(x=40,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new romen",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new romen",15,"bold"),bg="black",fg="white")
        password.place(x=40,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new romen",15,"bold"),show="*")
        self.txtpass.place(x=40,y=250,width=270)

        btn=Button(frame,text="Login",command=self.login,font=("times new romen",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activebackground="red",activeforeground="white")
        btn.place(x=110,y=300,width=120,height=35)

        btn1=Button(frame,text="New User Register",command=self.new_user,font=("times new romen",10,"bold"),borderwidth=0,fg="white",bg="black",activebackground="black",activeforeground="white")
        btn1.place(x=15,y=350,width=160)

        btn2=Button(frame,text="Forget Password",font=("times new romen",10,"bold"),borderwidth=0,fg="white",bg="black",activebackground="black",activeforeground="white")
        btn2.place(x=10,y=370,width=160)

    def login(self):
        username = self.txtuser.get()
        password = self.txtpass.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields required", parent=self.root)
        elif username == "Jerin@2025" and password == "123456":
            messagebox.showinfo("Success", "Opening Hostel Facial Recognition System", parent=self.root)
            for widget in self.root.winfo_children():
                widget.destroy()
            self.app = Face_Recognition_System(self.root)
        else:
            messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)

    def new_user(self):
        self.window=Toplevel(self.root)
        self.win=user(self.window)




if __name__=="__main__":
    root=Tk()
    app=login_window(root)
    root.mainloop()