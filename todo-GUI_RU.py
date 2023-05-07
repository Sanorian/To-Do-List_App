from tkinter import *
from tkinter import ttk
import os.path
if os.path.isfile('todo.txt')==True:
    data = open('todo.txt').readlines()
else:
    data = open('todo.txt', "w+").readlines()
while '\n' in data:
    data.pop(data.index('\n'))
def add():
    new_task = tasks_entry.get()
    data.append(new_task)
    data_var.set(data)
    todo_file = open('todo.txt', 'w')
    for i in range(0, len(data)):
        todo_file.write(data[i]+'\n')
def delete():
    selection = data_listbox.curselection()
    select_task = data_listbox.get(selection[0])
    data_listbox.delete(selection[0])
    data.pop(selection[0])
    todo_file = open('todo.txt', 'w')
    for i in range(0, len(data)):
        todo_file.write(data[i])
 
root = Tk()
root.title("ToDo-Planner")
root.geometry("300x250")
root.columnconfigure(index=0, weight=4)
root.columnconfigure(index=1, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=3)
 
data_var = StringVar(value=data)
 
tasks_entry = ttk.Entry()
tasks_entry.grid(column=0, row=0, padx=6, pady=6, sticky=EW)
ttk.Button(text="Добавить", command=add).grid(column=1, row=0, padx=6, pady=6)
 
data_listbox = Listbox(listvariable=data_var)
data_listbox.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=5, pady=5)

ttk.Button(text="Удалить", command=delete).grid(row=2, column=1, padx=5, pady=5)
 
root.mainloop()