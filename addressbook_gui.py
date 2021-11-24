'''
This is an address book gui that allows to store informaiton into a sqlite database
The information will contain First and Last name as well as the Address of that person
You can add delete and edit the address book within the gui application 
'''
from tkinter import *
import PIL
import sqlite3


root = Tk()
root.title("Address Book")
root.geometry("480x600")

# Creates a database or you can connect to one
conn = sqlite3.connect('address_book.db')

#Creates cursor
c = conn.cursor()

#Creates Table if one does not already exist
#Edited it out once the table was made successfully 
"""
c.execute('''CREATE TABLE addresses(
    first_name text,
    last_name text,
    address text, 
    city text,
    state text, 
    zipcode integer
    )''')
"""

#Creates function to delete a record
def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    #delete a record
    c.execute("DELETE from addresses WHERE oid= " + delete_box.get())

    # Commi the changes
    conn.commit()
    # Close the connection
    conn.close()



#Creates Submit function
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    #Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get(),
            })

    # Commi tthe changes
    conn.commit()
    # Clsoe the connection
    conn.close()

    #clear text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

#creates query function
def query():
        # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    #query the databse
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall() 
    #print(records)

    #loop through results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[6]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)

    # Commi the changes
    conn.commit()
    # Clsoe the connection
    conn.close()


    
#TODO: Find some way to shorten this repeated mess. Maybe have layout beneth act as a template to import at top of file 
#All the Text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10,0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, pady=(10,0))
address = Entry(root, width=30)
address.grid(row=2, column=1, pady=(10,0))
city = Entry(root, width=30)
city.grid(row=3, column=1, pady=(10,0))
state = Entry(root, width=30)
state.grid(row=4, column=1, pady=(10,0))
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, pady=(10,0))
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

#Creates text box labels
f_name_label= Label(root, text= "First Name")
f_name_label.grid(row=0, column=0)
l_name_label= Label(root, text= "Last Name")
l_name_label.grid(row=1, column=0)
address_label= Label(root, text= "Address")
address_label.grid(row=2, column=0)
city_label= Label(root, text= "City")
city_label.grid(row=3, column=0)
state_label= Label(root, text= "State")
state_label.grid(row=4, column=0)
zipcode_label= Label(root, text= "Zipcode")
zipcode_label.grid(row=5, column=0)
delete_box_label = Label(root, text="Delete ID")
delete_box_label.grid(row=9, column=0, pady=5)

#Submit button
submit_btn = Button(root, text="Add Record To Databse", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=109)

#Create a query button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#create a delete button
delete_btn = Button(root, text="Delete Records", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=134)


# Commi tthe changes
conn.commit()

# Clsoe the connection
conn.close()

root.mainloop()
