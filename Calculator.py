import tkinter as tk
calculator = tk.Tk()
calculator.title("Calculator")

frame1 = tk.Frame(calculator)
frame1.pack()
frame2 = tk.Frame(calculator)
frame2.pack()
frame3 = tk.Frame(calculator)
frame3.pack()
frame4 = tk.Frame(calculator)
frame4.pack()


value = tk.DoubleVar()
value2 = tk.DoubleVar()
value3 = tk.DoubleVar()
setNum = tk.BooleanVar()
setNum.set(False)
add = tk.BooleanVar()
add.set(False)
subtract = tk.BooleanVar()
subtract.set(False)
multiply = tk.BooleanVar()
multiply.set(False)
divide = tk.BooleanVar()
divide.set(False)
action = tk.BooleanVar()
action.set(False)

def num0Button():
    if action.get()==False:
        if setNum.get()==True:
            value.set(value2.get()*10)
            value2.set(value.get())
        if setNum.get()==False:
            value.set(0)
            value2.set(0)
            setNum.set(True)     
        
    if action.get()==True:
        if setNum.get()==True:
            value.set(value3.get()*10)
            value3.set(value.get())
        if setNum.get()==False:
            value.set(0)
            value3.set(0)
            setNum.set(True) 

def num1Button():
    if action.get()==False:
        if setNum.get()==True:
            value.set(value2.get()*10 + 1)
            value2.set(value.get())
        if setNum.get()==False:
            value.set(1)
            value2.set(1)
            setNum.set(True)     
        
    if action.get()==True:
        if setNum.get()==True:
            value.set(value3.get()*10 + 1)
            value3.set(value.get())
        if setNum.get()==False:
            value.set(1)
            value3.set(1)
            setNum.set(True) 

def num2Button():
    if action.get()==False:
        if setNum.get()==True:
            value.set(value2.get()*10 + 2)
            value2.set(value.get())
        if setNum.get()==False:
            value.set(2)
            value2.set(2)
            setNum.set(True)     
        
    if action.get()==True:
        if setNum.get()==True:
            value.set(value3.get()*10 + 2)
            value3.set(value.get())
        if setNum.get()==False:
            value.set(2)
            value3.set(2)
            setNum.set(True) 

def num3Button():
    if action.get()==False:
        if setNum.get()==True:
            value.set(value2.get()*10 + 3)
            value2.set(value.get())
        if setNum.get()==False:
            value.set(3)
            value2.set(3)
            setNum.set(True)     
        
    if action.get()==True:
        if setNum.get()==True:
            value.set(value3.get()*10 + 3)
            value3.set(value.get())
        if setNum.get()==False:
            value.set(3)
            value3.set(3)
            setNum.set(True) 

def num4Button():
    if action.get()==False:
        if setNum.get()==True:
            value.set(value2.get()*10 + 4)
            value2.set(value.get())
        if setNum.get()==False:
            value.set(4)
            value2.set(4)
            setNum.set(True)     
        
    if action.get()==True:
        if setNum.get()==True:
            value.set(value3.get()*10 + 4)
            value3.set(value.get())
        if setNum.get()==False:
            value.set(4)
            value3.set(4)
            setNum.set(True) 

def num5Button():
    if action.get()==False:
        if setNum.get()==True:
            value.set(value2.get()*10 + 5)
            value2.set(value.get())
        if setNum.get()==False:
            value.set(5)
            value2.set(5)
            setNum.set(True)     
        
    if action.get()==True:
        if setNum.get()==True:
            value.set(value3.get()*10 + 5)
            value3.set(value.get())
        if setNum.get()==False:
            value.set(5)
            value3.set(5)
            setNum.set(True) 

def num6Button():
    if action.get()==False:
        if setNum.get()==True:
            value.set(value2.get()*10 + 6)
            value2.set(value.get())
        if setNum.get()==False:
            value.set(6)
            value2.set(6)
            setNum.set(True)     
        
    if action.get()==True:
        if setNum.get()==True:
            value.set(value3.get()*10 + 6)
            value3.set(value.get())
        if setNum.get()==False:
            value.set(6)
            value3.set(6)
            setNum.set(True) 

def num7Button():
    if action.get()==False:
        if setNum.get()==True:
            value.set(value2.get()*10 + 7)
            value2.set(value.get())
        if setNum.get()==False:
            value.set(7)
            value2.set(7)
            setNum.set(True)     
        
    if action.get()==True:
        if setNum.get()==True:
            value.set(value3.get()*10 + 7)
            value3.set(value.get())
        if setNum.get()==False:
            value.set(7)
            value3.set(7)
            setNum.set(True) 

def num8Button():
    if action.get()==False:
        if setNum.get()==True:
            value.set(value2.get()*10 + 8)
            value2.set(value.get())
        if setNum.get()==False:
            value.set(8)
            value2.set(8)
            setNum.set(True)     
        
    if action.get()==True:
        if setNum.get()==True:
            value.set(value3.get()*10 + 8)
            value3.set(value.get())
        if setNum.get()==False:
            value.set(8)
            value3.set(8)
            setNum.set(True) 

def num9Button():
    if action.get()==False:
        if setNum.get()==True:
            value.set(value2.get()*10 + 9)
            value2.set(value.get())
        if setNum.get()==False:
            value.set(9)
            value2.set(9)
            setNum.set(True)     
        
    if action.get()==True:
        if setNum.get()==True:
            value.set(value3.get()*10 + 9)
            value3.set(value.get())
        if setNum.get()==False:
            value.set(9)
            value3.set(9)
            setNum.set(True) 

def equalCommand():
    if action.get()==True:
        if add.get()==True:
            value.set(value2.get() + value3.get())
        if subtract.get()==True:
            value.set(value2.get() - value3.get())
        if multiply.get()==True:
            value.set(value2.get() * value3.get())
        if divide.get()==True:
            value.set(value2.get() / value3.get())
    value2.set(value.get())     
    add.set(False)
    subtract.set(False)
    multiply.set(False)
    divide.set(False)
    action.set(True)
    setNum.set(False)

def addButton():
    equalCommand()
    add.set(True)

def subtractButton():
    equalCommand()
    subtract.set(True)

def multiplyButton():
    equalCommand()
    multiply.set(True)

def divideButton():
    equalCommand()
    divide.set(True)

def resetButton():
    value.set(0)
    value2.set(0)
    value3.set(0)
    action.set(False)
    add.set(False)
    subtract.set(False)
    multiply.set(False)
    divide.set(False)
    setNum.set(False)

l= tk.Label(frame1, textvariable=value)
l.pack(side="top")

b7 = tk.Button(frame1, width=10, text="7", activebackground="gray", bd=5, command=num7Button)
b7.pack(side="left")

b8 = tk.Button(frame1, width=10, text="8", activebackground="gray", bd=5, command=num8Button)
b8.pack(side="left")

b9 = tk.Button(frame1, width=10, text="9", activebackground="gray", bd=5, command=num9Button)
b9.pack(side="left")

ba = tk.Button(frame1, width=10, text="+", activebackground="gray", bd=5, command=addButton)
ba.pack(side="left")

b4 = tk.Button(frame2, width=10, text="4", activebackground="gray", bd=5, command=num4Button)
b4.pack(side="left")

b5 = tk.Button(frame2, width=10, text="5", activebackground="gray", bd=5, command=num5Button)
b5.pack(side="left")

b6 = tk.Button(frame2, width=10, text="6", activebackground="gray", bd=5, command=num6Button)
b6.pack(side="left")

bs = tk.Button(frame2, width=10, text="-", activebackground="gray", bd=5, command=subtractButton)
bs.pack(side="left")

b1 = tk.Button(frame3, width=10, text="1", activebackground="gray", bd=5, command=num1Button)
b1.pack(side="left")

b2 = tk.Button(frame3, width=10, text="2", activebackground="gray", bd=5, command=num2Button)
b2.pack(side="left")

b3 = tk.Button(frame3, width=10, text="3", activebackground="gray", bd=5, command=num3Button)
b3.pack(side="left")

bm = tk.Button(frame3, width=10, text="*", activebackground="gray", bd=5, command=multiplyButton)
bm.pack(side="left")

b0 = tk.Button(frame4, width=10, text="0", activebackground="gray", bd=5, command=num0Button)
b0.pack(side="left")

br = tk.Button(frame4, width=10, text="C", activebackground="gray", bd=5, command=resetButton)
br.pack(side="left")

be = tk.Button(frame4, width=10, text="=", activebackground="gray", bd=5, command=equalCommand)
be.pack(side="left")

bd = tk.Button(frame4, width=10, text="/", activebackground="gray", bd=5, command=divideButton)
bd.pack(side="left")



calculator.mainloop()