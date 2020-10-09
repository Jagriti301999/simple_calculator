from tkinter import *
root=Tk()
root.configure(background="black")
root.title("Simple Calculator")
e=Entry(root,width=30,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=20)
def button_click(num):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(num))
    return

def button_clear():
     e.delete(0,END)
     
def button_add():
    num1=e.get()
    global f_num
    global math
    math="add"
    f_num=int(num1)
    e.delete(0,END)
    
def button_equal():
    num2=e.get()
    e.delete(0,END)
    if  math=="add":
     e.insert(0,f_num+int(num2))
    if  math=="sub":
     e.insert(0,f_num-int(num2))
    if  math=="mul":
     e.insert(0,f_num*int(num2))
    if  math=="div":
     e.insert(0,f_num/int(num2))

    
def button_sub():
    num1=e.get()
    global f_num
    global math
    math="sub"
    f_num=int(num1)
    e.delete(0,END)
    return

def button_mul():
    num1=e.get()
    global f_num
    global math
    math="mul"
    f_num=int(num1)
    e.delete(0,END)
    return

def button_div():
    num1=e.get()
    global f_num
    global math
    math="div"
    f_num=int(num1)
    e.delete(0,END)

button1=Button(root,text="1",padx=40,pady=20,fg='black',bg='orange',command=lambda: button_click(1),height=1,width=1)
button1.grid(row=3,column=0)
button2=Button(root,text="2",padx=40,pady=20,fg='black',bg='orange',command=lambda: button_click(2),height=1,width=1)
button2.grid(row=3,column=1)
button3=Button(root,text="3",padx=40,pady=20,fg='black',bg='orange',command=lambda: button_click(3),height=1,width=1)
button3.grid(row=3,column=2)
button4=Button(root,text="4",padx=40,pady=20,fg='black',bg='orange',command=lambda: button_click(4),height=1,width=1)
button4.grid(row=2,column=0)
button5=Button(root,text="5",padx=40,pady=20,fg='black',bg='orange',command=lambda: button_click(5),height=1,width=1)
button5.grid(row=2,column=1)
button6=Button(root,text="6",padx=40,pady=20,fg='black',bg='orange',command=lambda: button_click(6),height=1,width=1)
button6.grid(row=2,column=2)
button7=Button(root,text="7",padx=40,pady=20,fg='black',bg='orange',command=lambda: button_click(7),height=1,width=1)
button7.grid(row=1,column=0)
button8=Button(root,text="8",padx=40,pady=20,fg='black',bg='orange',command=lambda: button_click(8),height=1,width=1)
button8.grid(row=1,column=1)
button9=Button(root,text="9",padx=40,pady=20,fg='black',bg='orange',command=lambda: button_click(9),height=1,width=1)
button9.grid(row=1,column=2)
button0=Button(root,text="0",padx=40,pady=20,fg='black',bg='orange',command=lambda: button_click(0),height=1,width=1)
button0.grid(row=4,column=0)
#button_dot=Button(root,text=".",padx=40,pady=20,fg='black',bg='orange',command=lambda: button_dot,height=1,width=1)
#button_dot.grid(row=4,column=1)
button_equal=Button(root,text="=",padx=40,pady=20,fg='black',bg='orange',command=button_equal,height=1,width=1)
button_equal.grid(row=4,column=2)
button_add=Button(root,text="+",padx=40,pady=20,fg='black',bg='orange',command=button_add,height=1,width=1)
button_add.grid(row=1,column=4)
button_sub=Button(root,text="-",padx=40,pady=20,fg='black',bg='orange',command=button_sub,height=1,width=1)
button_sub.grid(row=2,column=4)
button_mul=Button(root,text="x",padx=40,pady=20,fg='black',bg='orange',command=button_mul,height=1,width=1)
button_mul.grid(row=3,column=4)
button_div=Button(root,text="/",padx=40,pady=20,fg='black',bg='orange',command=button_div,height=1,width=1)
button_div.grid(row=4,column=4)
button_clear=Button(root,text="C",padx=40,pady=20,fg='black',bg='orange',command=button_clear,height=1,width=1)
button_clear.grid(row=4,column=1)
root.mainloop()
