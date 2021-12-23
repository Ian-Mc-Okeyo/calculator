from tkinter import *
from math import *

root = Tk()
root.title('N@ikr@m Calculator')
root.geometry('530x260')
root.resizable(False, False)
entry = Entry(root, width=34, font=('Helvetica', 15))
entry.grid(column=0, row=0, pady=5, columnspan=7)
ans_entry = Entry(root, width=34, font=('Helvetica', 15))
ans_entry.grid(column=0, row=1, pady=5, columnspan=7)

value = ''
def numbers(num):
    global value
    value+=str(num)
    entry.insert(INSERT, num)
    eqls('')

def ans():
    answer = ans_entry.get()
    clear()
    entry.insert(END, answer)

def eqls(event):
    ans_entry.delete(0, END)
    answer = eval(entry.get())
    ans_entry.insert(END, answer)
    print(value)

root.bind('<Key>', eqls)

def clear():
    entry.delete(0, END)
    ans_entry.delete(0, END)
def Cos(x):
    return cos(radians(x))
def Tan(x):
    return tan(radians(x))
def Sin(x):
    return sin(radians(x))
def ln(x):
    return log(x)
def Log(x):
    return log10(x)
def fact(x):
    return factorial(x)
w, h = 5, 1

button1 = Button(root, text='1', command=lambda:numbers(1), width=w, height=h)
button1.grid(column=0, row=2, padx=5, pady=5)
button2 = Button(root, text='2', command=lambda:numbers(2), width=w, height=h)
button2.grid(column=1, row=2, padx=5, pady=5)
button3 = Button(root, text='3', command=lambda:numbers(3), width=w, height=h)
button3.grid(column=2, row=2, padx=5, pady=5)
button4 = Button(root, text='4', command=lambda:numbers(4), width=w, height=h)
button4.grid(column=0, row=3, padx=5, pady=5)
button5 = Button(root, text='5', command=lambda:numbers(5), width=w, height=h)
button5.grid(column=1, row=3, padx=5, pady=5)
button6 = Button(root, text='6', command=lambda:numbers(6), width=w, height=h)
button6.grid(column=2, row=3, padx=5, pady=5)
button7 = Button(root, text='7', command=lambda:numbers(7), width=w, height=h)
button7.grid(column=0, row=4, padx=5, pady=5)
button8 = Button(root, text='8', command=lambda:numbers(8), width=w, height=h)
button8.grid(column=1, row=4, padx=5, pady=5)
button9 = Button(root, text='9', command=lambda:numbers(9), width=w, height=h)
button9.grid(column=2, row=4, padx=5, pady=5)
button0 = Button(root, text='0', command=lambda:numbers(0), width=w, height=h)
button0.grid(column=0, row=5, padx=5, pady=5)

btn_multiply = Button(root, text = 'X', command=lambda:numbers('*'), width=w, height=h)
btn_multiply.grid(column=3, row=2, padx=5, pady=5)

btn_div = Button(root, text = '/', command=lambda:numbers('/'), width=w, height=h)
btn_div.grid(column=3, row=3, padx=5, pady=5)

btn_add = Button(root, text = '+', command=lambda:numbers('+'), width=w, height=h)
btn_add.grid(column=3, row=4, padx=5, pady=5)

btn_sub = Button(root, text = '-', command=lambda:numbers('-'), width=w, height=h)
btn_sub.grid(column=3, row=5, padx=5, pady=5)

button_ans = Button(root, text='ANS', command=ans, width=w, height=h)
button_ans.grid(column=1, row=5, padx=5, pady=5)

button_eqls = Button(root, text='=', command=lambda:eqls(''), width=w, height=h)
button_eqls.grid(column=2, row=5)

btn_cos = Button(root, text = 'Cos', command=lambda:numbers('Cos()'), width=w, height=h)
btn_cos.grid(row=2, column=4)
btn_tan = Button(root, text = 'Tan', command=lambda:numbers('Tan()'), width=w, height=h)
btn_tan.grid(row=3, column=4)
btn_sin = Button(root, text = 'Sin', command=lambda:numbers('Sin()'), width=w, height=h)
btn_sin.grid(row=4, column=4)

btn_clear = Button(root, text='Clear', width=w, height=h, command=clear)
btn_clear.grid(row=5, column=4)

btn_log = Button(root, text='Log', command=lambda:numbers('Log()'), width=w, height=h)
btn_log.grid(row=2, column=5)
btn_ln = Button(root, text='ln', command=lambda:numbers('ln()'), width=w, height=h)
btn_ln.grid(row=3, column=5)

btn_lft_brack = Button(root, text='(', command=lambda:numbers('('), width=w, height=h)
btn_lft_brack.grid(row=4, column=5)
btn_right_brack = Button(root, text=')', command=lambda:numbers(')'), width=w, height=h)
btn_right_brack.grid(row=4, column=6)

btn_abs = Button(root, text='lxl', command=lambda:numbers('abs()'), width=w, height=h)
btn_abs.grid(row=2, column=6)
btn_fact = Button(root, text='!', command=lambda:numbers('fact()'), width=w, height=h)
btn_fact.grid(row=3, column=6)
btn_dot = Button(root, text='.', command=lambda:numbers('.'), width=w, height=h)
btn_dot.grid(row=5, column=5)
btn_inverse = Button(root, text='1/x', command=lambda:numbers('1/'), width=w, height=h)
btn_inverse.grid(row=5, column=6)

root.config(background='#696969')

root.mainloop()