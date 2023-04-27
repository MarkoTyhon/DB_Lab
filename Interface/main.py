"""import mysql.connector
from tkinter import *
from tkinter import messagebox


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="qwertz123",
    database="computer_components"
    )
mycursor = mydb.cursor()

   # Create the main Tkinter window
root = Tk()
root.title("Computer Components Database")
root.geometry("400x600")


def insert_component():
    # Get the input values from the Entry fields
    name = name_entry.get()
    description = description_entry.get()
    brand = brand_entry.get()
    model = model_entry.get()
    price = price_entry.get()
    quantity = quantity_entry.get()
    category = category_entry.get()

    # Insert the component into the database
    sql = "INSERT INTO components (name, description, brand, model, price, quantity, category) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (name, description, brand, model, price, quantity, category)

    mycursor.execute(sql, val)
    mydb.commit()

    messagebox.showinfo("Success", "Component inserted successfully!")


# Create and place labels and entry fields for input
name_label = Label(root, text="Name:")
name_label.pack()
name_entry = Entry(root)
name_entry.pack()

description_label = Label(root, text="Description:")
description_label.pack()
description_entry = Entry(root)
description_entry.pack()

brand_label = Label(root, text="Brand:")
brand_label.pack()
brand_entry = Entry(root)
brand_entry.pack()

model_label = Label(root, text="Model:")
model_label.pack()
model_entry = Entry(root)
model_entry.pack()

price_label = Label(root, text="Price:")
price_label.pack()
price_entry = Entry(root)
price_entry.pack()

quantity_label = Label(root, text="Quantity:")
quantity_label.pack()
quantity_entry = Entry(root)
quantity_entry.pack()

category_label = Label(root, text="Category:")
category_label.pack()
category_entry = Entry(root)
category_entry.pack()

# Create and place the insert button
insert_button = Button(root, text="Insert Component", command=insert_component)
insert_button.pack()


# Start the Tkinter event loop
root.mainloop()"""
""" 
import mysql.connector
from tkinter import *
from tkinter import messagebox

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="qwertz123",
    database="computer_components"
    )

# Create a cursor object
mycursor = mydb.cursor()

# Create the main Tkinter window
root = Tk()
root.title("Computer Components Database")
root.geometry("800x600")

# Create a Frame for the components display
components_frame = Frame(root)
components_frame.pack(pady=20)

# Create a scrollbar for the components display
scrollbar = Scrollbar(components_frame)
scrollbar.pack(side=RIGHT, fill=Y)

# Create a Listbox to display the components
components_listbox = Listbox(components_frame, width=100, yscrollcommand=scrollbar.set)
components_listbox.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=components_listbox.yview)


def show_components():
    # Clear the components listbox
    components_listbox.delete(0, END)

    # Retrieve all components from the database
    mycursor.execute("SELECT * FROM components")

    # Fetch all the rows
    components = mycursor.fetchall()

    # Insert the components into the listbox
    for component in components:
        components_listbox.insert(END, f"{component[1]} - {component[3]} - {component[6]}")


# Create and place the Show Components button
show_button = Button(root, text="Show Components", command=show_components)
show_button.pack()


# Start the Tkinter event loop
root.mainloop()
"""

import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# Connect to the database
# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="qwertz123",
    database="computer_components"
    )

# Create a cursor object
mycursor = mydb.cursor()

# Create the main Tkinter window
root = Tk()
root.title("Computer Components Database")
root.geometry("1920x600")



def show_table(table_name):
    # Clear the components treeview
    components_treeview.delete(*components_treeview.get_children())

    # Retrieve column names from the specified table
    mycursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}'")
    columns = mycursor.fetchall()
    column_names = [column[0] for column in columns]

    # Retrieve data from the specified table
    mycursor.execute(f"SELECT * FROM {table_name}")
    data = mycursor.fetchall()

    # Insert the column names into the treeview
    components_treeview['columns'] = column_names
    for col in column_names:
        components_treeview.heading(col, text=col)

    # Insert the data into the treeview
    for row in data:
        components_treeview.insert('', END, values=row)


def insert_data():
    table_name = table_combobox.get()
    values = []
    for entry in entry_list:
        values.append(entry.get())

    # Insert data into the selected table
    try:
        query = f"INSERT INTO {table_name} VALUES {tuple(values)}"
        mycursor.execute(query)
        mydb.commit()
        messagebox.showinfo("Insert Successful", "Data inserted successfully!")
    except Exception as e:
        messagebox.showerror("Insert Error", str(e))

    # Refresh the displayed table
    show_table(table_name)


# Create a Frame for the components display
components_frame = Frame(root)
components_frame.pack(pady=20)

# Create a Treeview to display the components
components_treeview = ttk.Treeview(components_frame)
components_treeview.pack()

# Create a Frame for the insert form
insert_frame = Frame(root)
insert_frame.pack(pady=10)

# Create a Combobox for table selection
table_combobox = ttk.Combobox(insert_frame, values=("components", "manufacturers", "reviews", "orders", "order_items", "component_manufacturer"))
table_combobox.grid(row=0, column=0, padx=5)

# Create an empty list to store the Entry widgets
entry_list = []

# Retrieve column names from the first table (components) for the insert form
mycursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'components'")
columns = mycursor.fetchall()
column_names = [column[0] for column in columns]

# Create Entry widgets for each column in the insert form
for i, col in enumerate(column_names):
    label = Label(insert_frame, text=col)
    label.grid(row=i+1, column=0, padx=5, pady=5)
    entry = Entry(insert_frame)
    entry.grid(row=i+1, column=1, padx=5, pady=5)
    entry_list.append(entry)

# Create a Button to insert data into the selected table
insert_button = Button(insert_frame, text="Insert", command=insert_data)
insert_button.grid(row=len(column_names)+1, columnspan=2, padx=5, pady=10)


def button_click(table_name):
    messagebox.showinfo("Button Clicked", f"Displaying {table_name}")
    show_table(table_name)


# Create buttons for each table
tables = ["components", "manufacturers", "reviews", "orders", "order_items", "component_manufacturer"]

for i, table_name in enumerate(tables):
    button = ttk.Button(root, text=table_name.capitalize(), command=lambda name=table_name: button_click(name))
    button.pack(pady=5)


# Start the Tkinter event loop
root.mainloop()