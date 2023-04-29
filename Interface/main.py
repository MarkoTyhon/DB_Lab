import tkinter as tk
from tkinter import ttk
import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="<host>", #your_host
    user="<user>", #your_user
    password="<password>", #your_password
    database="computer_components"
    )

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create the main application window
root = tk.Tk()
root.title("Computer Components Database")

# Function to handle button clicks for each table
def show_table(table_name):
    # Execute a SELECT query to retrieve data from the table
    cursor.execute(f"SELECT * FROM {table_name}")
    data = cursor.fetchall()

    # Create a new window to display the table data
    table_window = tk.Toplevel(root)
    table_window.title(table_name)

    # Create a treeview widget to display the data
    tree = ttk.Treeview(table_window)

    # Define the table columns
    tree["columns"] = tuple(cursor.column_names)

    # Configure column headings
    for column in cursor.column_names:
        tree.heading(column, text=column)

    # Insert data into the treeview
    for row in data:
        tree.insert("", tk.END, values=row)

    # Pack the treeview into the window
    tree.pack()

# Create buttons for each table
tables = ["components", "manufacturers", "reviews", "orders", "order_items", "component_manufacturer"]
for table in tables:
    btn = tk.Button(root, text=table.capitalize(), command=lambda t=table: show_table(t))
    btn.pack(pady=5)

# Run the main event loop
root.mainloop()

# Close the cursor and the database connection
cursor.close()
conn.close()