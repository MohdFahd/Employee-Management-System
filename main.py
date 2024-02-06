from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import clear
from db import DataBase
db = DataBase("employee.db")

root = Tk()
root.title("Employee Management System")

id = StringVar()
name = StringVar()
age = StringVar()
job = StringVar()
email = StringVar()
gender = StringVar()
mobile = StringVar()
# address = StringVar()

# textvariable = [name,age,job,email,gender,mobile]


# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x = (screen_width - 1310) // 2
y = (screen_height - 515) // 2

root.geometry("1110x510+{}+{}".format(x, y))
root.resizable(False, False)
root.configure(bg='blue')


# Dvide the screen into two parts

entries_frame = Frame(root, bg='white')
entries_frame.place(x=1, y=1, width=360, height=510)
title = Label(entries_frame, text="Employee Company", font=("times new roman", 20, "bold"), bg="white")
title.place(x=10,y=1)


# Define function
def hide():
    root.geometry("360x515")
def show():
    x = (screen_width - 1310) // 2
    y = (screen_height - 515) // 2

    root.geometry("1110x510+{}+{}".format(x, y))
    root.resizable(False, False)
    root.configure(bg='blue')

btnHide = Button(entries_frame, text="Hide" , cursor='hand2', command=hide).place(x=260, y=10)
btnHide = Button(entries_frame, text="Show" , cursor='hand2', command=show).place(x=300, y=10)



lblName = Label(entries_frame, text="Name:", font=("times new roman", 15), bg="white")
lblName.place(x=10,y=60)
txtName = Entry(entries_frame,textvariable=name, font=("times new roman", 15), bg="lightyellow")
txtName.place(x=80,y=62)

lblJob = Label(entries_frame, text="Job:", font=("times new roman", 15), bg="white")
lblJob.place(x=10,y=95)
txtJob = Entry(entries_frame,textvariable=job, font=("times new roman", 15), bg="lightyellow")
txtJob.place(x=80,y=95)

lblGender = Label(entries_frame, text="Gender:", font=("times new roman", 15), bg="white")
lblGender.place(x=10,y=130)
ComboGender = ttk.Combobox(entries_frame,textvariable=gender, font=("times new roman", 15), state="readonly")
ComboGender['values']= ("Male", "Female")
ComboGender.set("Select Gender")
ComboGender.place(x=80,y=130)

lblAge = Label(entries_frame, text="Age:", font=("times new roman", 15), bg="white")
lblAge.place(x=10,y=170)
txtAge = Entry(entries_frame, textvariable=age,font=("times new roman", 15), bg="lightyellow")
txtAge.place(x=80,y=170)

lblEmail = Label(entries_frame, text="Email:", font=("times new roman", 15), bg="white")
lblEmail.place(x=10,y=210)
txtEmail = Entry(entries_frame,textvariable=email, font=("times new roman", 15), bg="lightyellow")
txtEmail.place(x=80,y=210)

lblContact = Label(entries_frame, text="Contact:", font=("times new roman", 15), bg="white")
lblContact.place(x=10,y=250)
txtmobile = Entry(entries_frame, textvariable=mobile,font=("times new roman", 15), bg="lightyellow")
txtmobile.place(x=80,y=250)

lblAddress = Label(entries_frame, text="Address:", font=("times new roman", 15), bg="white")
lblAddress.place(x=10,y=290)
txtAddress = Text(entries_frame,width=30,height=2, font=("times new roman", 15), bg="lightyellow")
txtAddress.place(x=15,y=320)



# Define Table Frame and Scrollbar for table display

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    
    name.set(row[1])
    age.set(row[2])
    job.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    mobile.set(row[6])
    txtAddress.delete('1.0', END)
    txtAddress.insert(END,row[7])
    # address.set(row[7])

    con = sqlite3.connect(database="db.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    return rows

def clear():
    name.set("")
    job.set("")
    gender.set("")
    age.set("")
    email.set("")
    mobile.set("")
    txtAddress.delete('1.0', END)

def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)

def delete():
    db.remove(row[0])
    clear()
    displayAll()
    
def update():
    if name.get() == "" or job.get() == "" or gender.get() == "" or age.get() == "" or email.get() == "" or mobile.get() == "" or txtAddress.get('1.0', END) == "":
        messagebox.showerror("Error", "All fields are required", parent=root)
    else:
        db.update(row[0], name.get(), age.get(), job.get(), email.get(), gender.get(), mobile.get(), txtAddress.get('1.0', END))
        clear()
        displayAll()     
        messagebox.showinfo("Success", "Record has been updated", parent=root)

def add_employee():
    if name.get() == "" or job.get() == "" or gender.get() == "" or age.get() == "" or email.get() == "" or mobile.get() == "" or txtAddress.get('1.0', END) == "":
        messagebox.showerror("Error", "All fields are required", parent=root)
    else:
        db.insert(name.get(), age.get(), job.get(), email.get(), gender.get(), mobile.get(), txtAddress.get('1.0', END))
        messagebox.showinfo("Success", "Record has been inserted", parent=root)
        clear()
        displayAll()

# Buttons Frame
btnFrame = Frame(entries_frame, bg="white",bd=1, relief=SOLID)
btnFrame.place(x=10,y=400,width=320,height=100)

btnAdd = Button(btnFrame, text="Add", font=("times new roman", 15),command=add_employee, width=10,fg="white",bg='#16a085').place(x=10,y=10 )
btnEdit = Button(btnFrame, text="Edit", font=("times new roman", 15),command=update, width=10,fg="white",bg='#2990b9').place(x=10,y=55 )
btnDelete = Button(btnFrame, text="Delete", font=("times new roman", 15),command=delete, width=10,fg="white",bg='#c0392b').place(x=170,y=10 )
btnClear = Button(btnFrame, text="Clear", font=("times new roman", 15),command=clear, width=10,fg="white",bg='#f39c12').place(x=170 ,y=55 )

# Table Frame
table_frame = Frame(root, bg='#242b4f')
table_frame.place(x=360, y=1, width=760, height=510)

style = ttk.Style()
style.configure("mystyle.Treeview", font=("times new roman", 15), rowheight=50)
style.configure("mystyle.Treeview.Heading", font=("times new roman", 13))

tv = ttk.Treeview(table_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings", style="mystyle.Treeview")
tv.heading(1, text="ID")
tv.column(1, width=40)
tv.heading(2, text="Name")
tv.column(2, width=100)
tv.heading(3, text="Age")
tv.column(3, width=100)
tv.heading(4, text="Job")
tv.column(4, width=100)
tv.heading(5, text="Email")
tv.column(5, width=100)
tv.heading(6, text="Gender")
tv.column(6, width=100)
tv.heading(7, text="mobile")
tv.column(7, width=100)
tv.heading(8, text="Address")
tv.column(8, width=100)
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData )

displayAll()
#Same place but with hrizontal view
tv.pack()

# keep window showing
root.mainloop()
