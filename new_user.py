from tkinter import *
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

class user:
    def __init__(self,root):
        self.root=root
        self.root.title("New User Register")
        self.root.geometry("1530x790+0+0")
        self.root.configure(bg="black")

        # Variables
        self.fname=StringVar()
        self.lname=StringVar()
        self.contact=StringVar()
        self.email=StringVar()
        self.securityQ=StringVar()
        self.securityA=StringVar()
        self.password=StringVar()
        self.confpass=StringVar()

        frame=LabelFrame(self.root,bg="black")
        frame.place(x=260,y=230,width=1000,height=400)

        title_lbl=Label(self.root,text="NEW USER REGISTER",font=("times new romen",35,"bold"),bg="black",fg="yellow")
        title_lbl.place(x=460,y=120,width=550,height=50)

        # row 1
        fname_lbl=Label(frame,text="First Name",font=("times new romen",17,"bold"),bg="black",fg="white")
        fname_lbl.place(x=20,y=30)

        self.fname_txt=ttk.Entry(frame,textvariable=self.fname,font=("times new romen",12),width=22)
        self.fname_txt.place(x=250,y=35)

        lname_lbl=Label(frame,text="Last Name",font=("times new romen",17,"bold"),bg="black",fg="white")
        lname_lbl.place(x=510,y=30)

        self.lname_txt=ttk.Entry(frame,textvariable=self.lname,font=("times new romen",12),width=22)
        self.lname_txt.place(x=740,y=35)

        # row 2
        contact_lbl=Label(frame,text="Contact",font=("times new romen",17,"bold"),bg="black",fg="white")
        contact_lbl.place(x=20,y=90)

        self.contact_txt=ttk.Entry(frame,textvariable=self.contact,font=("times new romen",12),width=22)
        self.contact_txt.place(x=250,y=95)

        email_lbl=Label(frame,text="Email",font=("times new romen",17,"bold"),bg="black",fg="white")
        email_lbl.place(x=510,y=90)

        self.email_txt=ttk.Entry(frame,textvariable=self.email,font=("times new romen",12),width=22)
        self.email_txt.place(x=740,y=95)

        # row 3
        securityQ_lbl=Label(frame,text="Sequrity Question",font=("times new romen",17,"bold"),bg="black",fg="white")
        securityQ_lbl.place(x=20,y=150)

        self.securityQ_combo=ttk.Combobox(frame,textvariable=self.securityQ,font=("times new romen",12),state="readonly")
        self.securityQ_combo["values"]=("Select Ouestion","Your favourite place","Your favourite fruit","Your favourite anime","Your favourite game")
        self.securityQ_combo.current(0)
        self.securityQ_combo.place(x=250,y=155)

        securityA_lbl=Label(frame,text="Sequrity Answer",font=("times new romen",17,"bold"),bg="black",fg="white")
        securityA_lbl.place(x=510,y=150)

        self.securityA_txt=ttk.Entry(frame,textvariable=self.securityA,font=("times new romen",12),width=22)
        self.securityA_txt.place(x=740,y=155)

        # row 4
        password_lbl=Label(frame,text="Password",font=("times new romen",17,"bold"),bg="black",fg="white")
        password_lbl.place(x=20,y=210)

        self.password_txt=ttk.Entry(frame,textvariable=self.password,font=("times new romen",12),width=22)
        self.password_txt.place(x=250,y=215)

        confpass_lbl=Label(frame,text="Confirm Password",font=("times new romen",17,"bold"),bg="black",fg="white")
        confpass_lbl.place(x=510,y=210)

        self.confpass_txt=ttk.Entry(frame,textvariable=self.confpass,font=("times new romen",12),width=22)
        self.confpass_txt.place(x=740,y=215)

        # Check Button
        self.check=IntVar()
        self.check_btn=Checkbutton(frame,variable=self.check,text="I agree the terms & conditions",font=("times new romen",14,"bold"),selectcolor="grey",background="black",foreground="white",activebackground="black",activeforeground="white",onvalue=1,offvalue=0)
        self.check_btn.place(x=20,y=260)

        # Register Button
        btn1=Button(frame,cursor="hand2",command=self.register,text="REGISTER",font=("times new romen",17,"bold"),bg="darkblue",fg="white")
        btn1.place(x=420,y=320)

        # Register Function
    def register(self):
        if self.fname.get()=="" or self.email.get()=="" or self.securityQ.get()=="Select Question":
            messagebox.showerror("Error","All fields required",parent=self.root)
        elif self.password.get()!=self.confpass.get():
            messagebox.showerror("Error","Password and Confirm Password must be same",parent=self.root)
        elif self.check==0:
            messagebox.showerror("Error","Please agree all terms and conditions",parent=self.root)
        else:
            messagebox.showinfo("Success","Registered Successfully",parent=self.root)
            self.root.destroy()





if __name__=="__main__":
    root=Tk()
    app=user(root)
    root.mainloop()