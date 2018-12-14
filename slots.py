# from math import *
from random import *
from tkinter import *
# ________Variables_____________
# number = []
# End of Variables_____________


# ________Pre-definded functions_____________
def checkNumber(var):
    pass

def spin():
    # Variables
    # Reel 1
    a1 =  randint(0, 128)
    a2 =  randint(0, 128)
    a3 =  randint(0, 128)
    # Reel 2
    b1 =  randint(0, 128)
    b2 =  randint(0, 128)
    b3 =  randint(0, 128)
    # Reel 3
    c1 =  randint(0, 128)
    c2 =  randint(0, 128)
    c3 =  randint(0, 128)
    # Reel 4
    d1 =  randint(0, 128)
    d2 =  randint(0, 128)
    d3 =  randint(0, 128)
    # Reel 5
    f1 =  randint(0, 128)
    f2 =  randint(0, 128)
    f3 =  randint(0, 128)

    # Change the lable text
    a1_text.config(text=a1) # Reel 1
    a2_text.config(text=a2) # Reel 1
    a3_text.config(text=a3) # Reel 1

    b1_text.config(text=b1) # Reel 2
    b2_text.config(text=b2) # Reel 2
    b3_text.config(text=b3) # Reel 2

    c1_text.config(text=c1) # Reel 3
    c2_text.config(text=c2) # Reel 3
    c3_text.config(text=c3) # Reel 3

    d1_text.config(text=d1) # Reel 4
    d2_text.config(text=d2) # Reel 4
    d3_text.config(text=d3) # Reel 4

    f1_text.config(text=f1) # Reel 5
    f2_text.config(text=f2) # Reel 5
    f3_text.config(text=f3) # Reel 5

    print(str(a1) + ' ' + str(b1) + ' ' + str(c1) + ' ' + str(d1) + ' ' + str(f1) )
    print(str(a2) + ' ' + str(b2) + ' ' + str(c2) + ' ' + str(d2) + ' ' + str(f2) )
    print(str(a3) + ' ' + str(b3) + ' ' + str(c3) + ' ' + str(d3) + ' ' + str(f3) )
    print('\n \n')

# Tkinter window setings
master = Tk()
master.title("Spin 4 Cash")

a1_text = Label(master, text="spin")
a2_text = Label(master, text="spin")
a3_text = Label(master, text="spin")
b1_text = Label(master, text="spin")
b2_text = Label(master, text="spin")
b3_text = Label(master, text="spin")
c1_text = Label(master, text="spin")
c2_text = Label(master, text="spin")
c3_text = Label(master, text="spin")
d1_text = Label(master, text="spin")
d2_text = Label(master, text="spin")
d3_text = Label(master, text="spin")
f1_text = Label(master, text="spin")
f2_text = Label(master, text="spin")
f3_text = Label(master, text="spin")

spin_button = Button(master, text="spin", command=spin)
# Placement of items
a1_text.grid(row=1, column=1)
b1_text.grid(row=1, column=2)
c1_text.grid(row=1, column=3)
d1_text.grid(row=1, column=4)
f1_text.grid(row=1, column=5)

a2_text.grid(row=2, column=1)
b2_text.grid(row=2, column=2)
c2_text.grid(row=2, column=3)
d2_text.grid(row=2, column=4)
f2_text.grid(row=2, column=5)

a3_text.grid(row=3, column=1)
b3_text.grid(row=3, column=2)
c3_text.grid(row=3, column=3)
d3_text.grid(row=3, column=4)
f3_text.grid(row=3, column=5)

spin_button.grid(row=4, column=3)

master.mainloop()
