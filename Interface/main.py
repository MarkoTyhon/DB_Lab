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
root.geometry("1920x1000")



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