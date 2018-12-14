# from math import *
from random import *
from tkinter import *
from time import sleep
# ________Variables_____________
number_of_line_variable = 1
credit_per_line_variable = 1
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

# Select how many lines are played
def change_how_many_line(line):
    global number_of_line_variable, credit_per_line_variable
    number_of_line_variable = line
    calculate_the_cost_of_spin(number_of_line_variable, credit_per_line_variable)
    # return number_of_line_variable

def change_bet_ammount(bet):
    global credit_per_line_variable, number_of_line_variable
    credit_per_line_variable = bet
    calculate_the_cost_of_spin(number_of_line_variable, credit_per_line_variable)
    # return credit_per_line_variable

def calculate_the_cost_of_spin(lines_variable, credit_variable):
    cost_of_the_spin = lines_variable * credit_variable
    player_bet_per_line.config(text = cost_of_the_spin)
    print("COST OF SPIN:", cost_of_the_spin)
    return cost_of_the_spin


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

# How much credit has the player got in text
text_credit = Label(master, text="Credit: ")
player_ammout_of_cash = Label(master, text="0.00")
# Bet ammount
text_bet_ammount = Label(master, text="Bet Ammount: ")
player_bet_per_line = Label(master, text="0.00")
# Ammount won text 
text_winnings = Label(master, text="Payout: ")
player_payout = Label(master, text="0.00")
# Choose how many lines the player wants to play.
bet_how_much_per_line_1_button = Button(master, text="1 Line", command=lambda: change_how_many_line(1))
bet_how_much_per_line_2_button = Button(master, text="2 Line", command=lambda: change_how_many_line(2))
bet_how_much_per_line_3_button = Button(master, text="3 Line", command=lambda: change_how_many_line(3))
bet_how_much_per_line_4_button = Button(master, text="4 Line", command=lambda: change_how_many_line(4))
bet_how_much_per_line_5_button = Button(master, text="5 Line", command=lambda: change_how_many_line(5))
# Bet how many credits to use per line
bet_number_of_lines_1_button = Button(master, text="1 Credit", command=lambda: change_bet_ammount(1))
bet_number_of_lines_2_button = Button(master, text="2 Credit", command=lambda: change_bet_ammount(2))
bet_number_of_lines_3_button = Button(master, text="3 Credit", command=lambda: change_bet_ammount(3))
bet_number_of_lines_4_button = Button(master, text="4 Credit", command=lambda: change_bet_ammount(4))
bet_number_of_lines_5_button = Button(master, text="5 Credit", command=lambda: change_bet_ammount(5))

# Test button
# TEST_button = Button(master, text="TEST BUTTON", command=calculate_the_cost_of_spin)

# Placement of items

# Row 1
a1_text.grid(row=1, column=1)
b1_text.grid(row=1, column=2)
c1_text.grid(row=1, column=3)
d1_text.grid(row=1, column=4)
f1_text.grid(row=1, column=5)
# Row 2
a2_text.grid(row=2, column=1)
b2_text.grid(row=2, column=2)
c2_text.grid(row=2, column=3)
d2_text.grid(row=2, column=4)
f2_text.grid(row=2, column=5)
# Row 3
a3_text.grid(row=3, column=1)
b3_text.grid(row=3, column=2)
c3_text.grid(row=3, column=3)
d3_text.grid(row=3, column=4)
f3_text.grid(row=3, column=5)
# Row 4
text_credit.grid(row=4, column=1)
player_ammout_of_cash.grid(row=4, column=2)
text_bet_ammount.grid(row=4, column=3)
player_bet_per_line.grid(row=4, column=4)
text_winnings.grid(row=4, column=5)
player_payout.grid(row=4, column=6)
# Row 5 Bet Per line
bet_number_of_lines_1_button.grid(row=5, column=1)
bet_number_of_lines_2_button.grid(row=5, column=2)
bet_number_of_lines_3_button.grid(row=5, column=3)
bet_number_of_lines_4_button.grid(row=5, column=4)
bet_number_of_lines_5_button.grid(row=5, column=5)
# Row 6 How many lines
bet_how_much_per_line_1_button.grid(row=6, column=1)
bet_how_much_per_line_2_button.grid(row=6, column=2)
bet_how_much_per_line_3_button.grid(row=6, column=3)
bet_how_much_per_line_4_button.grid(row=6, column=4)
bet_how_much_per_line_5_button.grid(row=6, column=5)


# Last Row
spin_button.grid(row=1000, column=3)

# TEST_button.grid(row=1001, column=3)
master.mainloop()
