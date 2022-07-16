from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math

window = Tk()
window.title("Калькулятор")
window.geometry("525x125")
window["bg"] = "#ffff00"

def calc(key):
    global memory
    if key == "=":
        strl = "-+01234567890,*/"
        if calc_entryspace.get()[0] not in strl:
            calc_entryspace.insert(END, "Please enter a number.")
            messagebox.showerror("Error!")   
        try:
            result = eval(calc_entryspace.get())
            calc_entryspace.insert(END, "=" + str(result))
        except:
            messagebox.showerror("Error!")
    
    elif key == "DEL":
        calc_entryspace.delete(0, END)
        
    elif key == "xⁿ":
        calc_entryspace.insert(END, "**")
        
    elif key == "π":
        calc_entryspace.insert(END, math.pi)
        
    elif key == "1/x":
        calc_entryspace.insert(END, "=" + 1 / calc_entryspace)
        #except: calc_entryspace.get() == 0
            #calc_entryspace.insert(END, "Cannot divide by zero!")  
                                   
    else:
        if "=" in calc_entryspace.get():
            calc_entryspace.delete(0, END)
        calc_entryspace.insert(END, key)
        
bl = [
    "7", "8", "9", "+", "-",
    "4", "5", "6", "1/x", "*",
    "1", "2", "3", "xⁿ", "/",
    "DEL", "0", ".", "π", "="
 ]
r = 1
c = 0

for i in bl:
    bg = "#007bff"
    rel = ""
    cmd=lambda x=i:calc(x)
    ttk.Button(window, text=i, command=cmd, width=8).grid(row=r, column=c)
    c += 1
    if c>4:
        c=0
        r += 1
        
calc_entryspace = Entry(window, width=35, bg="#ffff00")
calc_entryspace.grid(row=0, column=0, columnspan=15)

window.mainloop()