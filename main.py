# Global constant variable
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

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

# Call the function
#deposit()
def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, you´re current balance is: ${balance}")
        else: 
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

main()

