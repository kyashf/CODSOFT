from tkinter import *
from tkinter import messagebox
from genAI import responce

font_style = "Helvetica"

def add_task_function():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(END, task)
        task_entry.delete(0, END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def remove_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Delete Error", "Please select a task to remove.")

def complete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_task_index)
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(END, task + " (Completed)")  
        tasks_listbox.itemconfig(END, {'fg': 'red'})  
    except:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

def AI_Guide():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_task_index)
        response = responce(task)
        messagebox.showinfo("Response from AI", response)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to ask the AI.")

window = Tk()
window.title("To Do List")
window.geometry("400x550")
window.configure(bg="#303030")

title = Label(window, text="Add your Future Tasks!", 
              font=(font_style, 18, "bold"), 
              fg="#00ff00", 
              bg="#303030")
title.pack(pady=10)

task_entry = Entry(window, width=30, 
                    font=(font_style, 14), 
                    bg="#98C379", 
                    fg="#282C34", 
                    borderwidth=2, 
                    relief="solid")
task_entry.pack(pady=10)

task_btn = Button(window, text="Add Task", 
                  width=36, 
                  font=(font_style, 12), 
                  bg="#E06C75", 
                  fg="white", 
                  command=add_task_function)
task_btn.pack(pady=5)

complete_btn = Button(window, text="Mark as Completed", 
                      width=36, 
                      font=(font_style, 12), 
                      bg="#C678DD", 
                      fg="white", 
                      command=complete_task)
complete_btn.pack(pady=5)

remove_btn = Button(window, text="Delete Task", 
                    width=36, 
                    font=(font_style, 12), 
                    bg="#D19A66", 
                    fg="white", 
                    command=remove_task)
remove_btn.pack(pady=5)

guide_btn = Button(window, text="Ask with AI", 
                   width=36, 
                   font=(font_style, 12), 
                   bg="#A19A9A", 
                   fg="white", 
                   command=AI_Guide)  
guide_btn.pack(pady=5)

tasks_listbox = Listbox(window, width=30, 
                        height=10, 
                        font=(font_style, 14), 
                        bg="#ABB2BF", 
                        fg="#282C34", 
                        borderwidth=2, 
                        relief="solid")
tasks_listbox.pack(pady=5)

sign = Label(window, text="© 2024 Firoziyash", 
             font=(font_style, 10), 
             fg="#61AFEF", 
             bg="#303030")
sign.pack()

window.mainloop()
