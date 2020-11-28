import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import numpy as np
from tkinter import *
import tkinter.font


now = datetime.now()
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('accounts_conexsent.json' , scope )
client = gspread.authorize(creds)
sheet = client.open('Conexsent_Accounts').sheet1
######################all the imports are finished#################




def start_new() :
  window = Tk()
  window.geometry('320x320')
  window.title("Accounts")
  def close_all() : 
    window.destroy()
    
  welcome = Label(window ,  text = "Welcome Please let Me know What I can do for You").pack(pady=10)
  new_entry_button = Button(window , text = "Create New Entry" , command = lambda:[new_entry(),close_all()]).pack(pady=10)

  show_totals = Button(window , text = "Show Total Expense and Earning" , command = lambda:[close_all(), show_everything()]).pack(pady=10)

  close = Button(window , text = "Close the Window" , command = close_all).pack(pady=10)
  window.mainloop()
  
  

def new_entry() :
  window = Tk()
  window.geometry('320x320')
  window.title("New Entry")
  def close_all() : 
    window.destroy()
    
  welcome1 = Label(window ,  text = "Please click Your choice").pack(pady=10)
  expense_entry1 = Button(window , text = "Expense Entry" , command = lambda:[expense_window() , close_all()]).pack(pady=10)
  expense_entry2 = Button(window , text = "Income Entry" , command = lambda:[income_window() , close_all()]).pack(pady=10)
  go_back = Button(window , text = "Go to Main menu" , command = lambda:[close_all() , start_new()]).pack(pady=10)

  
def expense_window() : 
  window = Tk()
  window.geometry('320x320')
  window.title("New Expense Entry")
  def close_all() : 
    window.destroy()
  welcome2 = Label(window ,  text = "Your Expense Value").pack(pady=10)
  expense = Entry(window)
  expense.pack(pady=10)
  welcome2 = Label(window ,  text = "Your Expense Path").pack(pady=10)
  expense_type = Entry(window)
  expense_type.pack(pady=10)
  def submit_expense():
    now = datetime.now()
    now = str(now)
    income = 0
    income_type = 'NA'
    expense1 = expense.get()
    expense_type1 = expense_type.get()
    entry_insert = [now , income , income_type , expense1 , expense_type1]
    sheet.insert_row(entry_insert , 2)
  submit = Button(window , text = "Submit" , command = submit_expense ).pack(pady=10)
  go_back = Button(window , text = "Go to Main menu" , command = lambda:[close_all() , start_new()]).pack(pady=10)

def income_window() : 
  window = Tk()
  window.geometry('320x320')
  window.title("New Income Entry")
  def close_all() : 
    window.destroy()
  welcome2 = Label(window ,  text = "Your income Value").pack(pady=10)
  income = Entry(window)
  income.pack(pady=10)
  welcome2 = Label(window ,  text = "Your income Source").pack(pady=10)
  income_type = Entry(window)
  income_type.pack(pady=10)

  def submit_income():
    now = datetime.now()
    expense = 0
    expense_type = 'NA'
    now = str(now)
    income1 = income.get()
    income_type1 = income_type.get()
    entry_insert = [now , income1 , income_type1 , expense , expense_type]
    sheet.insert_row(entry_insert , 2) 
    
  submit = Button(window , text = "Submit" , command = lambda:[submit_income() , button_enabled() ] ).pack(pady=10)
  go_back = Button(window , text = "Go to Main menu" , command = lambda:[close_all() , start_new()]).pack(pady=10)
  remove = Button(window , text = "Undo the last Entry" , command = lambda:[rmv_last_entry()])
  remove.pack(pady=10)
  remove.config(state = "disabled" )
  
  def rmv_last_entry():
    sheet.delete_rows(2)
    remove.config(state= 'disabled')
  def button_enabled():
    remove.config(state = "active")


def show_everything():     ##this shows all the monthly expenses
  window = Tk()
  window.geometry('320x320')
  window.title("Total Monthly expenses")
  def close_all() : 
    window.destroy()
  total_expense = (sheet.col_values(4))
  total_expense = total_expense[ 1 : ]
  total_expense = np.array(total_expense)
  total_expense = total_expense.astype(int)
  total_income = (sheet.col_values(2))
  total_income = total_income[ 1 : ]
  total_income = np.array(total_income)
  total_income = total_income.astype(int)
  in_bank = sum(total_income)-sum(total_expense)
  income1 = ("Total Income : " + str(sum(total_income)) + " Rs")
  expense1 = ("Total Expense : " + str(sum(total_expense)) + " Rs")
  in_bank = ("Savings : " + str(in_bank) + ' Rs')
  welcome1 = Label(window ,  text =  expense1)
  welcome1.pack(pady= 5)
  welcome1.config(font=("Courier", 10 , 'bold'))
  welcome1 = Label(window ,  text =  income1)
  welcome1.pack(pady= 5)
  welcome1.config(font=("Courier", 10 , 'bold'))
  welcome1 = Label(window ,  text =  in_bank)
  welcome1.pack(pady= 5)
  welcome1.config(font=("Courier", 10 , 'bold'))
  add_new = Button(window , text = "Add new entry" , command = lambda:[close_all() , new_entry()]).pack(pady=10)
  go_back = Button(window , text = "Go to Main menu" , command = lambda:[close_all() , start_new()]).pack(pady=10)
  

start_new()