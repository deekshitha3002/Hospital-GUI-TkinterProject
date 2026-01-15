import tkinter as tk
from tkinter import messagebox, ttk
import datetime
appointments = []
details=[]
class HospitalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome to Prathima Hospital")
        self.root.geometry("1400x1400")
        self.first_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def first_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Welcome to Prathima Hospital", font=("Times New Roman",50)).pack(pady=20)
        tk.Label(self.root,text="If you are a new client to the hospital, \n please register and then login else login",font=("Times New Roman",25),bg="light blue").pack(pady=150)
        bt=tk.Button(self.root,text="REGISTER NOW",font="bold",command=self.register_screen,bg="yellow")
        bt.place(x=250,y=500,height=50,width=200)
        bt=tk.Button(self.root,text="LOGIN NOW",font="bold",bg="yellow",command=self.login_screen)
        bt.place(x=950,y=500,height=50,width=200)
        lb=tk.Label(self.root,text="Phone Number:040-5960 3636",font=("bold"),bg="yellow")
        lb.place(x=1080,y=700)
        lb1=tk.Label(self.root,text="Timings:09:00AM-09:00PM",font=("bold"),bg="yellow")
        lb1.place(x=50,y=700)

    def register_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Welcome to Prathima Hospital", font=("Times New Roman",50)).pack(pady=10)
        tk.Label(self.root,text="REGISTER HERE",font=("Times New Roman",20,"bold")).pack(pady=5)
        tk.Label(self.root, text="Enter Your Name:",font=("Times New Roman",25,"bold")).pack(pady=20)
        self.name = tk.Entry(self.root,width=20)
        self.name.pack(pady=5)
        tk.Label(self.root, text="Enter Password:",font=("Times New Roman",25,"bold")).pack(pady=20)
        self.password= tk.Entry(self.root,width=20)
        self.password.pack(pady=5)
        tk.Label(self.root, text="Enter your Phone Number:",font=("Times New Roman",25,"bold")).pack(pady=20)
        self.phone= tk.Entry(self.root,width=20)
        self.phone.pack(pady=5)
        tk.Label(self.root,text="Location:",font=("Times New Roman",25,"bold")).pack(pady=20)
        self.location=tk.Entry(self.root,width=20)
        self.location.pack(pady=5)
        tk.Button(self.root, text="Submit",command=self.verification,width=10).pack(pady=20)
        lb=tk.Label(self.root,text="Phone Number:040-5960 3636",font=("bold"),bg="yellow")
        lb.place(x=1080,y=700)
        lb1=tk.Label(self.root,text="Timings:09:00AM-09:00PM",font=("bold"),bg="yellow")
        lb1.place(x=50,y=700)

    def verification(self):
        name1= self.name.get().strip()
        password = self.password.get().strip()
        phone=self.phone.get().strip()
        details.append({"Name":name1,"Password":password})
        if not(name1 and password and phone):
            messagebox.showerror("Missing Data", "Please fill all the fields.")
            return
        if not (phone.isdigit() and len(phone)==10):
            messagebox.showerror("Invalid number", "Please give a correct phone number.")
            return
        
        messagebox.showinfo("Success","Registration done!!")
        self.first_screen()
    
    def login_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Welcome to Prathima Hospital", font=("Times New Roman",50)).pack(pady=10)
        tk.Label(self.root,text="LOGIN HERE",font=("Times New Roman",20,"bold")).pack(pady=40)
        tk.Label(self.root, text="Enter Your Name:",font=("Times New Roman",25,"bold")).pack(pady=20)
        self.identity = tk.Entry(self.root,width=20)
        self.identity.pack(pady=15)
        tk.Label(self.root, text="Enter Password:",font=("Times New Roman",25,"bold")).pack(pady=20)
        self.pas= tk.Entry(self.root)
        self.pas.pack(pady=15)
        tk.Button(self.root, text="Submit", command=self.verification1,width=10).pack(pady=20)
        lb=tk.Label(self.root,text="Phone Number:040-5960 3636",font=("bold"),bg="yellow")
        lb.place(x=1080,y=700)
        lb1=tk.Label(self.root,text="Timings:09:00AM-09:00PM",font=("bold"),bg="yellow")
        lb1.place(x=50,y=700)

    def verification1(self):
        name2 = self.identity.get().strip()
        pas = self.pas.get().strip()
        for user in details:
            if not(name2 and pas):
                messagebox.showerror("Missing Data", "Please fill all the fields.")
                return
            elif user["Name"] == name2 and user["Password"] == pas:
                messagebox.showinfo("Success", "Login Successful!")
                self.username = name2
                self.appointment_screen()
                return
        messagebox.showerror("Error", "Invalid Name or Password")

    def appointment_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Prathima Hospital", font=("Times New Roman",50)).pack(pady=10)
        tk.Label(self.root, text=f"Hello {self.username}, Book your Appointment", font=("Times New Roman", 20)).pack(pady=20)

        self.photo1=tk.PhotoImage(file=r"C:\Users\hamsa\OneDrive\Desktop\Python\my_venv\Scripts\Prathimahospital1.png")
        tk.Label(self.root,image=self.photo1).place(x=8,y=130)

        self.photo2=tk.PhotoImage(file=r"C:\Users\hamsa\OneDrive\Desktop\Python\my_venv\Scripts\Prathimahospital2.png")
        tk.Label(self.root, image=self.photo2).place(x=980,y=130)

        tk.Label(self.root,text="Enter Patient's Name:").pack(pady=20)
        self.patient=tk.Entry(self.root)
        self.patient.pack(pady=10)
        tk.Label(self.root, text="Select Department:").pack(pady=20)
        departments = ["Cardiology", "General Medicine", "Oncology", "Ophthalmology", "Radiology"]
        self.department = ttk.Combobox(self.root, values=departments)
        self.department.pack(pady=10)
        tk.Label(self.root, text="Your Problem:").pack(pady=20)
        self.problem = tk.Entry(self.root,width=20)
        self.problem.pack(pady=10)
        tk.Label(self.root, text="Select Doctor:").pack(pady=20)
        doctors = ["Dr.Smith - Cardiology", "Dr.Patel - General Medicine", "Dr.Johnson - Oncology", "Dr.Sailaja - Ophthalmology", "Dr.Sarvani - Radiology"]
        self.doctor = ttk.Combobox(self.root, values=doctors)
        self.doctor.pack(pady=10)
        tk.Label(self.root, text="Appointment Time (HH:MM):").pack(pady=20)
        self.time_entry = tk.Entry(self.root)
        self.time_entry.pack(pady=10)
        tk.Button(self.root, text="Pay & Confirm (₹500)", command=self.save_appointment).pack(pady=10)
        lb=tk.Label(self.root,text="Phone Number:040-5960 3636",font=("bold"),bg="yellow")
        lb.place(x=1000,y=700)
        lb1=tk.Label(self.root,text="Timings:09:00AM-09:00PM",font=("bold"),bg="yellow")
        lb1.place(x=150,y=700)

    def save_appointment(self):
        name = self.patient.get()
        problem = self.problem.get()
        department = self.department.get()
        doctor = self.doctor.get()
        time_str = self.time_entry.get()

        if not (name and problem and doctor and time_str and department):
            messagebox.showerror("Missing Data", "Please fill all the fields.")
            return

        original_time = datetime.datetime.strptime(time_str, "%H:%M")
        same_time_count =sum(1 for appt in appointments
                             if appt["doctor"] == doctor and appt["time1"].strftime("%H:%M") == original_time.strftime("%H:%M"))
        adjusted_time = original_time + datetime.timedelta(minutes=15 * same_time_count)
        if same_time_count > 0:
            messagebox.showwarning("Time Slot Adjusted", f"Slot already booked. Your new appointment is at {adjusted_time.strftime('%H:%M')}.")
        appointments.append({"name": name,"time1": original_time,"department": department,"problem": problem,"doctor": doctor,"time": adjusted_time})
        messagebox.showinfo("Success", "Appointment Confirmed. Thank you!")
        self.show_appointments()

    def show_appointments(self):
        self.clear_screen()
        tk.Label(self.root, text="All Appointments", font=("Arial", 14)).pack(pady=10)
        tree = ttk.Treeview(self.root, columns=("S.No","Name", "Appointment Taken","Department", "Doctor", "Problem","Adjusted time"), show="headings")
        for col in ("S.No","Name", "Appointment Taken","Department", "Doctor", "Problem","Adjusted time"):
            tree.heading(col, text=col)
            tree.column(col,width=200)
        tree.pack(pady=10)
        doctor_appointments = {}
        for appt in appointments:
            doctor_appointments.setdefault(appt["doctor"], []).append(appt)
        for doc_appts in doctor_appointments.values():
            doc_appts.sort(key=lambda x: x["time"])
        for doctor, doc_appts in doctor_appointments.items():
            for index, appt in enumerate(doc_appts,start=1):
                tree.insert("", "end",values=(index,appt["name"],appt["time1"].strftime("%H:%M"),appt["department"],appt["doctor"],appt["problem"],appt["time"].strftime("%H:%M")))
        tk.Button(self.root, text="Back to Home", command=self.first_screen).pack(pady=10)
        tk.Button(self.root,text="Back to Appointment Registration",command=self.appointment_screen).pack(pady=10)
        lb=tk.Label(self.root,text="Phone Number:040-5960 3636",font=("bold"),bg="yellow")
        lb.place(x=1080,y=700)
        lb1=tk.Label(self.root,text="Timings:09:00AM-09:00PM",font=("bold"),bg="yellow")
        lb1.place(x=50,y=700)

root = tk.Tk()
app = HospitalApp(root)
root.iconbitmap(r"C:\Users\hamsa\OneDrive\Desktop\Python\my_venv\Scripts\Prathimahospitalicon.ico")
root.config(bg="lavender")
root.mainloop()