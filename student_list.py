import tkinter as tk
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import csv
from tkinter import messagebox


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.configure(bg='black')

        title_lbl=Label(self.root,text="STUDENT LIST",font=("times new romen",35,"bold"),bg="black",fg="yellow")
        title_lbl.place(x=0,y=0,width=1530,height=70)

        # Main Frame
        main_frame=LabelFrame(self.root,bd=2,relief=RIDGE,bg="black")
        main_frame.place(x=5,y=70,width=1530,height=720)

        # Search by Label
        search_by=Label(main_frame,text="Search By:",font=("times new romen",20,"bold"),bg="black",fg="white")
        search_by.place(x=30,y=25)

        self.search_by_combo=ttk.Combobox(main_frame,font=("times new romen",15),width=25,state="readonly")
        self.search_by_combo["values"]=("Name","Roll No","Department")
        self.search_by_combo.current(0)
        self.search_by_combo.place(x=200,y=30)

        # Sort By Label
        sort_by=Label(main_frame,text="Sort By:",font=("times new romen",20,"bold"),bg="black",fg="white")
        sort_by.place(x=1050,y=25)

        self.sort_by_combo=ttk.Combobox(main_frame,font=("times new romen",15),width=25,state="readonly")
        self.sort_by_combo["values"]=("Name","Department")
        self.sort_by_combo.current(0)
        self.sort_by_combo.place(x=1185,y=30)

        self.sort_by_combo.bind("<<ComboboxSelected>>",lambda e:self.sort_function())

        # Search Label
        search_label=Label(main_frame,text="Search =>",font=("times new romen",20,"bold"),bg="black",fg="white")
        search_label.place(x=30,y=100)

        self.search_var=tk.StringVar()
        self.search_var.trace_add("write",self.on_search_change)

        self.name_text=ttk.Entry(main_frame,font=("times new romen",15),width=60,textvariable=self.search_var)
        self.name_text.place(x=190,y=105)

        # Search Button
        search_button=Button(self.root,text="SEARCH",command=self.search_function,cursor="hand2",font=("times new romen",15,"bold"),bg="darkblue",fg="white")
        search_button.place(x=880,y=177,width=200,height=30)

        # Update Button
        update_button=Button(self.root,text="UPDATE",cursor="hand2",font=("times new romen",15,"bold"),bg="darkblue",fg="white")
        update_button.place(x=1090,y=177,width=200,height=30)

        # Delete Button
        delete_button=Button(self.root,text="DELETE",command=self.delete_function,cursor="hand2",font=("times new romen",15,"bold"),bg="darkblue",fg="white")
        delete_button.place(x=1300,y=177,width=200,height=30)

        # List Frame
        list_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg="white")
        list_frame.place(x=30,y=170,width=1470,height=530)

        # Scroll Bar
        scroll_x=ttk.Scrollbar(list_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(list_frame,orient=VERTICAL)

        # Loading Datas
        def load_students():
            try:
                with open("jerin.csv","r") as file:
                    reader=csv.reader(file)
                    headers=next(reader,None)
                    for row in reader:
                        self.tree.insert("","end",values=row)
            except FileNotFoundError:
                messagebox.showwarning("No Data","No students registered yet!",parent=self.root)

        # Define Column Headings
        self.column=("Name", "DOB", "Gender", "Phone", "Village", "Taluk", "District", "State", "Pincode", "Roll No", "Department", "Course", "Year", "Semester", "DOJ", "Way of Joining","Photo Sample")

        self.tree=ttk.Treeview(list_frame,columns=self.column,show="headings")

        # Placing Scroll Bar
        scroll_x.config(command=self.tree.xview)
        scroll_y.config(command=self.tree.yview)
        self.tree.config(yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        # Disabling Resizing Columns
        def disable_resize(event):
            if self.tree.identify_region(event.x, event.y) == "separator":
                return "break"
        
        self.tree.bind("<Motion>", disable_resize)

        # Fixing the Tree
        self.tree.pack(expand=True,fill="both")

        # Placing the Columns and Headings
        for col in self.column:
            self.tree.heading(col,text=col)
            self.tree.column(col,width=150,minwidth=150,stretch=False)

        # Giving Style for the Headings
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("times new romen", 12, "bold"))

        self.tree.tag_configure('heading',font=("times new romen", 12, "bold"))

        load_students()

        # Function for Update Button
        def update_function():
            selected_item=self.tree.focus()    # Getting Selected Row
            if not selected_item:
                messagebox.showwarning("Warning","Select one student to update",parent=self.root)
                return
            
            student_data=self.tree.item(selected_item)["values"]

            if len(student_data)!=len(self.column):
                messagebox.showerror("Error","Data Mismatch! Some fields are missing",parent=self.root)
                return

            # Update Window
            window=Toplevel(root)
            window.title("Update Details")
            window.geometry("500x760")

            # Creating New Fields Dynamically
            entry_fields=[]
            for i,column in enumerate(self.column):
                ttk.Label(window,text=column,font=("times new roman", 15, "bold"), width=20).grid(row=i,column=0,padx=10,pady=5,sticky="W")
                entry=ttk.Entry(window,width=40)
                entry.grid(row=i,column=1,padx=10,pady=5,ipady=5)
                if i<len(student_data):
                    entry.insert(0,str(student_data[i]))   # Autofill Data
                entry_fields.append(entry)

            # Function for Saving Updates
            def save_updates():
                updated_data=[entry.get() for entry in entry_fields]

                # Reading Existing Data
                rows=[]
                with open("jerin.csv","r",newline="") as file:
                    reader=csv.reader(file)
                    headers=next(reader)
                    for row in reader:
                        if row and row[0] == student_data[0]:
                            rows.append(updated_data)
                        else:
                            rows.append(row)
            
                # Writing Updated Data Back To CSV
                with open("jerin.csv","w",newline="") as file:
                    writer=csv.writer(file)
                    writer.writerow(headers)
                    writer.writerows(rows)

                messagebox.showinfo("Success","Student details updated succesfully!",parent=self.root)
                window.destroy()
                self.refresh_treeview()

            # Save Button For Updates
            save_btn=tk.Button(window,text="SAVE", font=("times new roman", 15, "bold"), bg="darkblue",fg="white",command=save_updates)
            save_btn.place(x=170,y=715,width=130,height=40)

        update_button.config(command=update_function)

    # Function for Refresh Treeview
    def refresh_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            with open("jerin.csv","r",newline="") as file:
                reader=csv.reader(file)
                next(reader)
                for row in reader:
                    self.tree.insert("","end",values=row)
        except FileNotFoundError:
            messagebox.showwarning("No Data","No students registered yet!",parent=self.root)


        # Function for Delete Button
    def delete_function(self):
        selected_item=self.tree.focus()    # Getting Selected Row
        if not selected_item:
            messagebox.showwarning("Warning","Select one student to delete",parent=self.root)
            return
            
        student_data=self.tree.item(selected_item)["values"]

        if not student_data:
            messagebox.showerror("Error","No student data found!",parent=self.root)
            return
            
        confirm=messagebox.askyesno("Confirm Delete",f"Are you sure to delete {student_data[0]}?",parent=self.root)
        # Read Existing Data
        if confirm:
            rows=[]
            with open("jerin.csv","r",newline="") as file:
                reader=csv.reader(file)
                headers=next(reader)
                for row in reader:
                    if row and row[0]!=student_data[0]:
                        rows.append(row)

            # Write Updated Data Back to CSV
            with open("jerin.csv","w",newline="") as file:
                writer=csv.writer(file)
                writer.writerow(headers)
                writer.writerows(rows)

            # Remove From Treeview
            self.tree.delete(selected_item)

            messagebox.showinfo("Success",f"{student_data[0]}'s record deleted successfully!",parent=self.root)

    # Function for Search Button
    def search_function(self):
        search_by=self.search_by_combo.get()
        search_term=self.name_text.get().strip()

        if not search_term:
            messagebox.showwarning("Warning","Enter a value to search!",parent=self.root)
            return
        
        column_index={"Name":0,"Roll No":9,"Department":10}

        if search_by not in column_index:
            messagebox.showerror("Error","Invalid search criteria!",parent=self.root)
            return
        
        search_index=column_index[search_by]
        
        # Clear Existing Treeview Content
        for item in self.tree.get_children():
            self.tree.delete(item)

        found=False
        with open("jerin.csv","r",newline="") as file:
            reader=csv.reader(file)
            next(reader)
            for row in reader:
                if search_term.lower() in row[search_index].lower():
                    self.tree.insert("","end",values=row)
                    found=True

        if not found:
            messagebox.showinfo("Not Found",f"No records found for {search_term} in {search_by}",parent=self.root)

    # For Search Field
    def on_search_change(self, *args):
        search_term = self.search_var.get().strip()

        # Check if Previous Search had Text
        if hasattr(self, 'previous_search') and self.previous_search and not search_term:
            self.refresh_treeview()

        # Store current search term for next comparison
        self.previous_search = search_term

    # Function for SortBY
    def sort_function(self):
        sort_by=self.sort_by_combo.get()

        column_index={"Name":0,"Roll No":9,"Department":10}

        if sort_by not in column_index:
            messagebox.showerror("Error","Invalid sort criteria!",parent=self.root)
            return
        
        sort_index=column_index[sort_by]

        # Extract Data From Treeview
        student_data=[]
        for child in self.tree.get_children():
            student_data.append(self.tree.item(child)["values"])

        # Sort Data
        student_data.sort(key=lambda x:x[sort_index])

        # Clear Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert Sorted Data Back
        for row in student_data:
            self.tree.insert("","end",values=row)





if __name__=="__main__"  :
    root=Tk()
    obj=Student(root)
    root.mainloop()