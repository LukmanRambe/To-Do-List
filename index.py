import tkinter as tk
from tkinter import font
import tkinter.messagebox
import pickle
import os

# ==== PARENT (WINDOW) ====
parent = tk.Tk()
parent.geometry('1000x345')
parent.resizable(0, 0)


# ==== FUNCTIONS ====

# ==== LEFT CONTAINER ====
# addTask
def addTask():
    task = entry.get()
    if task.strip() != "":
        leftTasksList.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        tk.messagebox.showwarning(title="Warning!", message="You have to enter a task!")

# deleteSelectedTask
def deleteSelectedTask():
    try:
        selectedTask = leftTasksList.curselection()
        leftTasksList.delete(selectedTask)
    except:
        tk.messagebox.showwarning(title="Warning!", message="You have to select a task!")

# deleteAllTask
def deleteAllTask():
    leftTasksList.delete(0, tk.END)
    taskTitle.delete(0, tk.END)
    entry.delete(0, tk.END)

# saveTask
def saveList():
    tasks = leftTasksList.get(0, leftTasksList.size())
    title = taskTitle.get()
    if len(title) != 0:
        if len(tasks) != 0:
            pickle.dump(tasks, open("database/" + title + ".txt", "wb"))
            rightTasksList.insert(tk.END, title)
        else:
            tk.messagebox.showwarning(title="Warning!", message="You have to add a task!")
    else:
        tk.messagebox.showwarning(title="Warning!", message="You have to insert the title!")


# ==== RIGHT CONTAINER ====
def loadSelectedList():
    try:
        title = rightTasksList.get(rightTasksList.curselection())
        tasks = pickle.load(open("database/" + title + ".txt", "rb"))
        leftTasksList.delete(0, tk.END)
        taskTitle.delete(0, tk.END)
        taskTitle.insert(tk.END, title)

        for task in tasks:
            leftTasksList.insert(tk.END, task)
    except:
        tk.messagebox.showwarning(title="Warning!", message="You have to select a list!")

def loadFromDatabase():
    lists = os.listdir("database")
    rightTasksList.delete(0, tk.END)
    if len(lists) > 0:
        for item in lists:
            rightTasksList.insert(tk.END, os.path.splitext(item)[0]) # Remove file extension
    else:
        tk.messagebox.showwarning(title="Warning!", message="You haven't saved anything yet!")

def deleteSelectedList():
    try:
        selectedTask = rightTasksList.curselection()
        title = rightTasksList.get(selectedTask)
        os.remove("database/" + title + ".txt")
        rightTasksList.delete(selectedTask)
    except:
        tk.messagebox.showwarning(title="Warning!", message="You have to select a list!")



# ==== GUI ====

# Title
appTitle = parent.title("To Do List")

# ==== RIGHT CONTAINER ====
# Container2
rightContainer = tk.Frame(parent)
rightContainer.pack(side=tk.RIGHT)

# Label
rightLabel = tk.Label(rightContainer, text="Saved Lists", font=("MS Sans Serif", 9, "bold"), background="#494949", foreground="#fffdf6")
rightLabel.pack()

# Scrollbar
rightScrollbar = tk.Scrollbar(rightContainer)
rightScrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# ListBox
rightTasksList = tk.Listbox(rightContainer, height=15, width=75, foreground="#494949", background="#fffdf6", font=("Sans Serif", 9))
rightTasksList.pack()

rightTasksList.config(yscrollcommand=rightScrollbar.set)
rightScrollbar.config(command=rightTasksList.yview)

# loadSelectedList
loadSelectedList = tk.Button(rightContainer, text="Load List", width=74, command=loadSelectedList, background="#faf6e9", foreground="#494949", font=("Sans Serif", 9))
loadSelectedList.pack()

# loadFromDatabase
loadFromDatabase = tk.Button(rightContainer, text="Load Lists From Database", width=74, command=loadFromDatabase, background="#faf6e9", foreground="#494949", font=("Sans Serif", 9))
loadFromDatabase.pack()

# deleteSelectedList
deleteSelectedList = tk.Button(rightContainer, text="Delete List", width=74, command=deleteSelectedList, background="#faf6e9", foreground="#494949", font=("Sans Serif", 9))
deleteSelectedList.pack()


# ==== LEFT CONTAINER ====
leftContainer = tk.Frame(parent)
leftContainer.pack(side=tk.LEFT)

# taskTitle
enterTitle = tk.Label(leftContainer, text="List Title: ", width=15, height=1, font=("MS Sans Serif", 9, "bold"), foreground="#494949")
enterTitle.pack()

taskTitle = tk.Entry(leftContainer, width=30, background="#fffdf6", foreground="#494949", font=("Sans Serif", 9))
taskTitle.pack()

# Scrollbar
leftScrollbar = tk.Scrollbar(leftContainer)
leftScrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# ListBox
leftTasksList = tk.Listbox(leftContainer, height=11, width=80, foreground="#494949", background="#fffdf6", font=("Sans Serif", 9))
leftTasksList.pack()

leftTasksList.config(yscrollcommand=leftScrollbar.set)
leftScrollbar.config(command=leftTasksList.yview)

# Entry (input)
entry = tk.Entry(leftContainer, width=80, background="#494949", foreground="#fffdf6", font=("Sans Serif", 9))
entry.pack()

# addBtn
addBtn = tk.Button(leftContainer, text="Add Task", width=68, command=addTask, background="#faf6e9", foreground="#494949", font=("Sans Serif", 9))
addBtn.pack()

# deleteBtn
deleteBtn = tk.Button(leftContainer, text="Delete Task", width=68, command=deleteSelectedTask, background="#faf6e9", foreground="#494949", font=("Sans Serif", 9))
deleteBtn.pack()

# deleteAllBtn
deleteAllBtn = tk.Button(leftContainer, text="Delete All", width=68, command=deleteAllTask, background="#faf6e9", foreground="#494949", font=("Sans Serif", 9))
deleteAllBtn.pack()

# saveBtn
saveBtn = tk.Button(leftContainer, text="Save List", width=68, command=saveList, background="#faf6e9", foreground="#494949", font=("Sans Serif", 9))
saveBtn.pack()


# ==== RUN GUI ====
parent.mainloop()