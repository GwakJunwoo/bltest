# how to make a excel add-in by python

import tkinter as tk
from tkinter import *
import sqlite3
 
root=tk.Tk()
root.title("Database GUI Program")
 
#Connecting to the database file
conn = sqlite3.connect('database.db')
c = conn.cursor()
 
#Creating table in the database file if not exists 
def create_table():  #Function to create table in the database file if not exists 
    c.execute('CREATE TABLE IF NOT EXISTS student (name TEXT, address TEXT, phone INTEGER)')   #Creating table with 3 columns name, address and phone number 

    c.execute("INSERT INTO student VALUES ('John', 'Highway 21', 123456789)") #Inserting values into the table

    conn.commit()   #Commiting changes to the database file

    c.close()       #Closing connection to the database file

    conn.close()    #Closing connection to the database file

    
#Function for adding records to the table in the database file    
def add_records():     #Function for adding records to the table in the database file  

    conn = sqlite3.connect('database.db')   #Connecting to the database file

    c = conn.cursor()   #Creating cursor object for executing SQL commands

    record_name=name_entry1.get()     #Getting data from entry boxes and storing it into variables 

    record_address=address_entry1.get()

    record_phone=phone_entry1.get()

    c.execute("INSERT INTO student (name, address, phone) VALUES (?, ?, ?)",(record_name, record_address, record_phone))   #Inserting data into table using SQL command with placeholders for data values 

    conn.commit()   #Commiting changes to the database file

    c.close()       #Closing connection to the database file

    conn.close()    #Closing connection to the database file

    
#Function for displaying records from table in the databse file    
def show_records():      #Function for displaying records from table in the databse file  

	conn = sqlite3.