from tkinter import *
from generatePass import randomGen

def genPass():
    length = int(password_length.get())
    gen_password = randomGen(length)
    password.config(text=gen_password)

def copy():
    window.clipboard_clear()
    window.clipboard_append(password.cget("text"))

window = Tk()
window.geometry("300x400")
window.title("GenPass")
window.configure(bg="#333333")

heading = Label(window, text="Generate your Password", bg="#333333", fg="#ffffff")
heading.config(font=("Helvetica", 12, "bold"), height=1)
heading.pack(pady=10)

choice_frame = Frame(window, width=300, height=30, bg="#000000")
choice_frame.pack(pady=10)

password = Label(choice_frame, text="", fg="#00ff00", bg="#000000")
password.config(width=30, height=2)
password.pack()

Label(window, text="Password Length:", bg="#333333", fg="#ffffff").pack(pady=10)

password_length = Entry(window)
password_length.pack()

generate = Button(window, width=20, height=2, text="Generate", command=genPass)
generate.pack(pady=20)

copy_button = Button(window, width=20, height=2, text="Copy", command=copy)
copy_button.pack(pady=10)

sign = Label(window, text="© 2024 Firoziyash", 
             font=("Helvetica", 10), 
             fg="#F0F0F0", 
             bg="#505050")
sign.pack(pady=10)
window.mainloop()
