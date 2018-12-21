# from math import *
from random import *
from tkinter import *
from time import sleep
# ________Variables_____________
number_of_line_variable = 1
credit_per_line_variable = 1
players_credits = 100  # Test Varible
# End of Variables_____________


# ________Pre-definded functions_____________
def spin():
    # Variables
    # wheel_chance = randint(1, 8)
    global a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3, f1, f2, f3
    # Reel 1
    a1 = randint(1, 128)  # Line 2 (array 0)
    a2 = randint(1, 128)  # Line 1 (array 1) NOTE: CANT HAVE WILD
    a3 = randint(1, 128)  # Line 3 (array 2)
    # Reel 2
    b1 = randint(1, 128)  # Line 2 (array 3)
    b2 = randint(1, 128)  # Line 1 (array 4) NOTE: CANT HAVE WILD
    b3 = randint(1, 128)  # Line 3 (array 5)
    # Reel 3
    c1 = randint(1, 128)  # Line 2 (array 6)
    c2 = randint(1, 128)  # Line 1 (array 7) NOTE: CANT HAVE WILD
    c3 = randint(1, 128)  # Line 3 (array 8)
    # Reel 4
    d1 = randint(1, 128)  # Line 2 (array 9)
    d2 = randint(1, 128)  # Line 1 (array 10) NOTE: CANT HAVE WILD
    d3 = randint(1, 128)  # Line 3 (array 11)
    # Reel 5
    f1 = randint(1, 128)  # Line 2 (array 12)
    f2 = randint(1, 128)  # Line 1 (array 13) NOTE: CANT HAVE WILD
    f3 = randint(1, 128)  # Line 3 (array 14)

    # # Change the lable text
# ==============================================================

    # reel_text = [[a1, a1_text], [a2, a2_text], [a3, a3_text],
    #              [b1, b1_text], [b2, b2_text], [b3, b3_text],
    #              [c1, c1_text], [c2, c2_text], [c3, c3_text],
    #              [d1, d1_text], [d2, d2_text], [d3, d3_text],
    #              [f1, f1_text], [f2, f2_text], [f3, f3_text]]

    # for reel_postion in reel_text:
    #     reel_postion[1].config(text=reel_postion[0])

    # ^ The stuff bellow is the same as the for loop above. The for loop use the Multi-array. SEE LINE 807 in IFB104/Assessment 1/assessment
    # a1_text.config(text=a1) # Reel 1
    # a2_text.config(text=a2) # Reel 1
    # a3_text.config(text=a3) # Reel 1

    # b1_text.config(text=b1) # Reel 2
    # b2_text.config(text=b2) # Reel 2
    # b3_text.config(text=b3) # Reel 2

    # c1_text.config(text=c1) # Reel 3
    # c2_text.config(text=c2) # Reel 3
    # c3_text.config(text=c3) # Reel 3

    # d1_text.config(text=d1) # Reel 4
    # d2_text.config(text=d2) # Reel 4
    # d3_text.config(text=d3) # Reel 4

    # f1_text.config(text=f1) # Reel 5
    # f2_text.config(text=f2) # Reel 5
    # f3_text.config(text=f3) # Reel 5

    # NOTE:: THIS WILL BE MOVED TO CHECK WHEEL
    # ==============================================================

    print(str(a1) + ' ' + str(b1) + ' ' +
          str(c1) + ' ' + str(d1) + ' ' + str(f1))
    print(str(a2) + ' ' + str(b2) + ' ' +
          str(c2) + ' ' + str(d2) + ' ' + str(f2))
    print(str(a3) + ' ' + str(b3) + ' ' +
          str(c3) + ' ' + str(d3) + ' ' + str(f3))
    print('\n \n')
    check_wheel()

# Select how many lines are played
def change_how_many_line(line):
    global number_of_line_variable, credit_per_line_variable
    number_of_line_variable = line
    calculate_the_cost_of_spin(
        number_of_line_variable, credit_per_line_variable)
    # return number_of_line_variable


def change_bet_ammount(bet):
    global credit_per_line_variable, number_of_line_variable
    credit_per_line_variable = bet
    calculate_the_cost_of_spin(
        number_of_line_variable, credit_per_line_variable)
    # return credit_per_line_variable


def calculate_the_cost_of_spin(lines_variable, credit_variable):
    cost_of_the_spin = lines_variable * credit_variable
    player_bet_per_line.config(text=cost_of_the_spin)
    return cost_of_the_spin

# This will be collected from a database, or a files
def get_players_credits():
    pass

# Checks if the player can spin, if the player has enough credits the slots will spin.
def check_if_user_can_spin():
    global players_credits
    print('\n \n')
    if calculate_the_cost_of_spin(number_of_line_variable, credit_per_line_variable) > players_credits:
        print("Error")
    else:
        players_credits = players_credits - \
            calculate_the_cost_of_spin(
                number_of_line_variable, credit_per_line_variable)
        spin()
    print("players credits: ", players_credits)


def check_wheel():
    global reel_text
    reel_text = [[a1, a1_text], [a2, a2_text], [a3, a3_text],  # Reel 1
                 [b1, b1_text], [b2, b2_text], [b3, b3_text],  # Reel 2
                 [c1, c1_text], [c2, c2_text], [c3, c3_text],  # Reel 3
                 [d1, d1_text], [d2, d2_text], [d3, d3_text],  # Reel 4
                 [f1, f1_text], [f2, f2_text], [f3, f3_text]]  # Reel 5

    # reel_letter = [[a1], [a2], [a3], [b1], [b2], [b3], [c1], [c2], [c3], [d1], [d2], [d3], [f1], [f2], [f3]]
    for reel_section in reel_text:
        if reel_section[0] == 1:
            reel_section[1].config(text='Queen')
        elif reel_section[0] == 2:
            reel_section[1].config(text='Nine')
        elif reel_section[0] == 3:
            reel_section[1].config(text='Jack')
        elif reel_section[0] == 4:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 5:
            reel_section[1].config(text='Ace')
        elif reel_section[0] == 6:
            reel_section[1].config(text='Nine')
        elif reel_section[0] == 7:
            reel_section[1].config(text='King')
        elif reel_section[0] == 8:
            reel_section[1].config(text='Ten')
        elif reel_section[0] == 9:
            reel_section[1].config(text='King')
        elif reel_section[0] == 10:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 11:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 12:
            reel_section[1].config(text='Nine')
        elif reel_section[0] == 13:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 14:
            reel_section[1].config(text='Nine')
        elif reel_section[0] == 15:
            reel_section[1].config(text='King')
        elif reel_section[0] == 16:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 17:
            reel_section[1].config(text='Ten')
        elif reel_section[0] == 18:
            reel_section[1].config(text='Jack')
        elif reel_section[0] == 19:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 20:
            reel_section[1].config(text='Feature')
        elif reel_section[0] == 21:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 22:
            reel_section[1].config(text='Ace')
        elif reel_section[0] == 23:
            reel_section[1].config(text='Queen')
        elif reel_section[0] == 24:
            reel_section[1].config(text='Ten')
        elif reel_section[0] == 25:
            reel_section[1].config(text='Ten')
        elif reel_section[0] == 26:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 27:
            reel_section[1].config(text='Nine')
        elif reel_section[0] == 28:
            reel_section[1].config(text='King')
        elif reel_section[0] == 29:
            reel_section[1].config(text='Ten')
        elif reel_section[0] == 30:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 31:
            reel_section[1].config(text='Ace')
        elif reel_section[0] == 32:
            reel_section[1].config(text='Ace')
        elif reel_section[0] == 33:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 34:
            reel_section[1].config(text='Jack')
        elif reel_section[0] == 35:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 36:
            reel_section[1].config(text='Nine')
        elif reel_section[0] == 37:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 38:
            reel_section[1].config(text='King')
        elif reel_section[0] == 39:
            reel_section[1].config(text='Ten')
        elif reel_section[0] == 40:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 41:
            reel_section[1].config(text='Feature')
        elif reel_section[0] == 42:
            reel_section[1].config(text='King')
        elif reel_section[0] == 43:
            reel_section[1].config(text='King')
        elif reel_section[0] == 44:
            reel_section[1].config(text='Ten')
        elif reel_section[0] == 45:
            reel_section[1].config(text='Nine')
        elif reel_section[0] == 46:
            reel_section[1].config(text='Jack')
        elif reel_section[0] == 47:
            reel_section[1].config(text='Queen')
        elif reel_section[0] == 48:
            reel_section[1].config(text='Jack')
        elif reel_section[0] == 49:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 50:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 51:
            reel_section[1].config(text='King')
        elif reel_section[0] == 52:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 53:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 54:
            reel_section[1].config(text='Ten')
        elif reel_section[0] == 55:
            reel_section[1].config(text='Queen')
        elif reel_section[0] == 56:
            reel_section[1].config(text='Nine')
        elif reel_section[0] == 57:
            reel_section[1].config(text='Queen')
        elif reel_section[0] == 58:
            reel_section[1].config(text='King')
        elif reel_section[0] == 59:
            reel_section[1].config(text='King')
        elif reel_section[0] == 60:
            reel_section[1].config(text='Jack')
        elif reel_section[0] == 61:
            reel_section[1].config(text='Jack')
        elif reel_section[0] == 62:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 63:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 64:
            reel_section[1].config(text='King')
        elif reel_section[0] == 65:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 66:
            reel_section[1].config(text='Jack')
        elif reel_section[0] == 67:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 68:
            reel_section[1].config(text='Nine')
        elif reel_section[0] == 69:
            reel_section[1].config(text='Ace')
        elif reel_section[0] == 70:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 71:
            reel_section[1].config(text='Ten')
        elif reel_section[0] == 72:
            reel_section[1].config(text='Ace')
        elif reel_section[0] == 73:
            reel_section[1].config(text='Queen')
        elif reel_section[0] == 74:
            reel_section[1].config(text='Queen')
        elif reel_section[0] == 75:
            reel_section[1].config(text='Nine')
        elif reel_section[0] == 76:
            reel_section[1].config(text='Queen')
        elif reel_section[0] == 77:
            reel_section[1].config(text='Jack')
        elif reel_section[0] == 78:
            reel_section[1].config(text='Queen')
        elif reel_section[0] == 79:
            reel_section[1].config(text='Ten')
        elif reel_section[0] == 80:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 81:
            reel_section[1].config(text='Ten')
        elif reel_section[0] == 82:
            reel_section[1].config(text='Jack')
        elif reel_section[0] == 83:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 84:
            reel_section[1].config(text='Ten')
        elif reel_section[0] == 85:
            reel_section[1].config(text='Queen')
        elif reel_section[0] == 86:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 87:
            reel_section[1].config(text='Nine')
        elif reel_section[0] == 88:
            reel_section[1].config(text='Queen')
        elif reel_section[0] == 89:
            reel_section[1].config(text='Jack')
        elif reel_section[0] == 90:
            reel_section[1].config(text='Jack')
        elif reel_section[0] == 91:
            reel_section[1].config(text='King')
        elif reel_section[0] == 92:
            reel_section[1].config(text='Nine')
        elif reel_section[0] == 93:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 94:
            reel_section[1].config(text='King')
        elif reel_section[0] == 95:
            reel_section[1].config(text='Jack')
        elif reel_section[0] == 96:
            reel_section[1].config(text='King')
        elif reel_section[0] == 97:
            reel_section[1].config(text='Ace')
        elif reel_section[0] == 98:
            reel_section[1].config(text='Nine')
        elif reel_section[0] == 99:
            reel_section[1].config(text='Queen')
        elif reel_section[0] == 100:
            reel_section[1].config(text='Ten')
        elif reel_section[0] == 101:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 102:
            reel_section[1].config(text='Queen')
        elif reel_section[0] == 103:
            reel_section[1].config(text='Jack')
        elif reel_section[0] == 104:
            reel_section[1].config(text='Nine')
        elif reel_section[0] == 105:
            reel_section[1].config(text='Queen')
        elif reel_section[0] == 106:
            reel_section[1].config(text='Ten')
        elif reel_section[0] == 107:
            reel_section[1].config(text='Queen')
        elif reel_section[0] == 108:
            reel_section[1].config(text='Ace')
        elif reel_section[0] == 109:
            reel_section[1].config(text='Nine')
        elif reel_section[0] == 110:
            reel_section[1].config(text='Ace')
        elif reel_section[0] == 111:
            reel_section[1].config(text='Feature')
        elif reel_section[0] == 112:
            reel_section[1].config(text='Ten')
        elif reel_section[0] == 113:
            reel_section[1].config(text='Ace')
        elif reel_section[0] == 114:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 115:
            reel_section[1].config(text='Ace')
        elif reel_section[0] == 116:
            reel_section[1].config(text='Nine')
        elif reel_section[0] == 117:
            reel_section[1].config(text='Ten')
        elif reel_section[0] == 118:
            reel_section[1].config(text='Jack')
        elif reel_section[0] == 119:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 120:
            reel_section[1].config(text='Ace')
        elif reel_section[0] == 121:
            reel_section[1].config(text='Ten')
        elif reel_section[0] == 122:
            reel_section[1].config(text='Ace')
        elif reel_section[0] == 123:
            reel_section[1].config(text='Feature')
        elif reel_section[0] == 124:
            reel_section[1].config(text='Jack')
        elif reel_section[0] == 125:
            reel_section[1].config(text='Wild')
        elif reel_section[0] == 126:
            reel_section[1].config(text='Nine')
        elif reel_section[0] == 127:
            reel_section[1].config(text='Feature')
        elif reel_section[0] == 128:
            reel_section[1].config(text='Nine')
        else:
            print('Please Spin')
    # check_for_feature()
    line1()

# Checking line 1 for matching items
def line1():
    queens = 0

    if reel_text[1][1]["text"] == "Queen":
        queens = queens + 1
        if reel_text[4][1]["text"] == "Queen":
            queens = queens + 1
            if reel_text[7][1]["text"] == "Queen":
                queens = queens + 1
                if reel_text[10][1]["text"] == "Queen":
                    queens = queens + 1
                    if reel_text[13][1]["text"] == "Queen":
                        queens = queens + 1
                        print(queens)
                        # print("Add 7 Credits")
                        calculate_credit(7)
                    else:
                        # print("Add 6 Credits")
                        calculate_credit(6)
                else:
                    # print("Add 5 Credits")
                    calculate_credit(5)
            else:
                print("No Win")
                print(queens)
        else:
            print("No Win")
            print(queens)
    else:
        print("NO Win")
        print(queens)

# Adds x amount of credits to the users credits
def calculate_credit(How_many_credit_to_add):
    global players_credits
    players_credits = players_credits + How_many_credit_to_add
    print("credits add: ", How_many_credit_to_add)

# Pressing the cashout button saves the creidts to a file or a database.
def cashout(): 
    pass


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

spin_button = Button(master, text="spin", command=check_if_user_can_spin)

# How much credit has the player got in text
text_credit = Label(master, text="Credit: ")
player_ammout_of_cash = Label(master, text="0")
# Bet ammount
text_bet_ammount = Label(master, text="Bet Amount: ")
player_bet_per_line = Label(master, text="1")
# Ammount won text
text_winnings = Label(master, text="Payout: ")
player_payout = Label(master, text="0")
# Choose how many lines the player wants to play.
bet_how_much_per_line_1_button = Button(
    master, text="1 Line", command=lambda: change_how_many_line(1))
bet_how_much_per_line_2_button = Button(
    master, text="2 Line", command=lambda: change_how_many_line(2))
bet_how_much_per_line_3_button = Button(
    master, text="3 Line", command=lambda: change_how_many_line(3))
bet_how_much_per_line_4_button = Button(
    master, text="4 Line", command=lambda: change_how_many_line(4))
bet_how_much_per_line_5_button = Button(
    master, text="5 Line", command=lambda: change_how_many_line(5))
# Bet how many credits to use per line
bet_number_of_lines_1_button = Button(
    master, text="1 Credit", command=lambda: change_bet_ammount(1))
bet_number_of_lines_2_button = Button(
    master, text="2 Credit", command=lambda: change_bet_ammount(2))
bet_number_of_lines_3_button = Button(
    master, text="3 Credit", command=lambda: change_bet_ammount(3))
bet_number_of_lines_4_button = Button(
    master, text="4 Credit", command=lambda: change_bet_ammount(4))
bet_number_of_lines_5_button = Button(
    master, text="5 Credit", command=lambda: change_bet_ammount(5))

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
