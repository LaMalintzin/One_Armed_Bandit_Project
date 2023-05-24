import random
# Global constant variable
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# Dictionary which represent the symbols of the reels 
# and how big are the chances that they will come up, where D will be the most common symbol. 
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
 
# Value which multiplies the bet. 
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# Function that will check which rows the user bet on and multiply by the symbol_values if the values are the same  
def check_winnings(columns, lines, bet, values):
    #Start with checking the lines we bet on
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            # If a symbol is not the same as the on before, break out of the loop
            if symbol != symbol_to_check:
                break
            else:
                winnings += values[symbol] * bet
                winning_lines.append(line + 1)

    return winnings, winning_lines

# Function which randomly picks rows and columns, the function generates which symbols that will be in each column 
# based on the frequency of symbols in the symbol_count dictinary! 
# By creating a list with all the possible values we could select from and then randomly chosse 3 of those values. 
# Each value chosen is removed from the list.

def get_slot_machine_spin(rows, cols, symbols):
    # List with the symbols
    all_symbols = []
    #for-loop adding the symbols to the List
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    # columns = [[], [], []]
    # Here we choose which values should go in every single column. 
    columns = []
    for _ in range(cols):
        column = []
        # Making a copy of the symbols list. This sign [:] called the slice-operator is used so the copy does affect the original. 
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            # Adding the value to the column
            column.append(value)
        
        columns.append(column)
    
    return columns

# Function to write the columns in a verticle line instead of rows, by flipping the rows around. 
# This operation is called Transposing. 
def print_slot_machine(columns):
    # Creating a for loop based on the number of rows based on our columns, 
    # the number of rows is based on the number of elements in our columns.  
    for row in range(len(columns[0])):
        # Enumerate gives an index and the item eg 0, 1 , 2 etc
        for i, column in enumerate(columns):
            # len columns -1 is checking the maximum index
            if i != len(columns) -1:
                print(column[row], end = " | ")
            else:
                print(column[row], end = "")
        
        print()

# Function which asks how much the player wants to deposit 
def deposit():
    while True:
        amount = input("How much do like to deposit ? ")
        #Check if its a valid number 
        if amount.isdigit():
            #Converts amount to an int
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0!!")
        else:
            print("Please enter a number.")

    return amount

# Function for how many lines you are betting
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you are bettingon (1-" + str(MAX_LINES) + ")? " )
        #Check if digits are entered
        if lines.isdigit():
            lines = int(lines)
            # Python special
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines!")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    while True:
        amount = input ("How much do you like to bet on each line ? $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET: 
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}. ")
        else:
            print("Please enter a number. ")

    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, you´re current balance is: ${balance}")
        else: 
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines: ", *winning_lines)
    return winnings - total_bet 


def main():
    balance = deposit()
    while True:
        print(f"Current balance is $ {balance}")
        playerChoice = input("Press enter to play (q is equal to quit).")
        if playerChoice == "q":
            break
        balance += spin(balance) 

    print(f"You left with ${balance}!!")
        
main()

