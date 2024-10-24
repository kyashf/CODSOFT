from tkinter import *

def btn_click(item):
    global expers
    expers = expers + str(item)
    input_text.set(expers)

def btn_clear():
    global expers
    expers = ""
    input_text.set("")

def btn_delete():
    global expers
    expers = expers[:-1]
    input_text.set(expers)

def btn_equal():
    try:
        global expers
        result = str(eval(expers))
        input_text.set(result)
        expers = result
    except:
        input_text.set("Error")
        expers = ""


window = Tk()
window.geometry("300x400")
window.title("Calculator")
window.configure(bg="#505050")

expers = ""
input_text = StringVar()

input_frame = Frame(window, width=300, height=50, bd=0, bg="#000000")
input_frame.pack(side=TOP,pady=10)

input_field = Entry(input_frame, font=("Helvetica", 20), textvariable=input_text, width=18, bg="#202020", fg="white", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=20)


btns_frame = Frame(window, width=300, height=350, bg="#000000")
btns_frame.pack()

clear = Button(btns_frame, text="C", width=18, height=3, bg="#E06C75", fg="white", command=lambda: btn_clear()).grid(row=0, column=0, columnspan=2)
clear = Button(btns_frame, text="D", width=8, height=3, bg="#F06D75", fg="white", command=lambda: btn_delete()).grid(row=0, column=2)
divide = Button(btns_frame, text="/", width=8, height=3, bg="#61AFEF", fg="white", command=lambda: btn_click("/")).grid(row=0, column=3)

seven = Button(btns_frame, text="7", width=8, height=3, bg="#98C379", fg="white", command=lambda: btn_click(7)).grid(row=1, column=0)
eight = Button(btns_frame, text="8", width=8, height=3, bg="#98C379", fg="white", command=lambda: btn_click(8)).grid(row=1, column=1)
nine = Button(btns_frame, text="9", width=8, height=3, bg="#98C379", fg="white", command=lambda: btn_click(9)).grid(row=1, column=2)
multiply = Button(btns_frame, text="*", width=8, height=3, bg="#61AFEF", fg="white", command=lambda: btn_click("*")).grid(row=1, column=3)

four = Button(btns_frame, text="4", width=8, height=3, bg="#98C379", fg="white", command=lambda: btn_click(4)).grid(row=2, column=0)
five = Button(btns_frame, text="5", width=8, height=3, bg="#98C379", fg="white", command=lambda: btn_click(5)).grid(row=2, column=1)
six = Button(btns_frame, text="6", width=8, height=3, bg="#98C379", fg="white", command=lambda: btn_click(6)).grid(row=2, column=2)
minus = Button(btns_frame, text="-", width=8, height=3, bg="#61AFEF", fg="white", command=lambda: btn_click("-")).grid(row=2, column=3)

one = Button(btns_frame, text="1", width=8, height=3, bg="#98C379", fg="white", command=lambda: btn_click(1)).grid(row=3, column=0)
two = Button(btns_frame, text="2", width=8, height=3, bg="#98C379", fg="white", command=lambda: btn_click(2)).grid(row=3, column=1)
three = Button(btns_frame, text="3", width=8, height=3, bg="#98C379", fg="white", command=lambda: btn_click(3)).grid(row=3, column=2)
plus = Button(btns_frame, text="+", width=8, height=3, bg="#61AFEF", fg="white", command=lambda: btn_click("+")).grid(row=3, column=3)

zero = Button(btns_frame, text="0", width=18, height=3, bg="#98C379", fg="white", command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2)
point = Button(btns_frame, text=".", width=8, height=3, bg="#98C379", fg="white", command=lambda: btn_click(".")).grid(row=4, column=2)
equals = Button(btns_frame, text="=", width=8, height=3, bg="#C678DD", fg="white", command=lambda: btn_equal()).grid(row=4, column=3)

sign = Label(window, text="© 2024 Firoziyash", 
             font=("Helvetica", 10), 
             fg="#F0F0F0", 
             bg="#505050")
sign.pack()

window.mainloop()