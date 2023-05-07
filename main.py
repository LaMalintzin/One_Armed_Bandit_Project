# Global variable
MAX_LINES = 3

# Function which asks how much the player wants to deposit 
def deposit():
    while True:
        amount = input("How much do like to deposit ? ")
        #Check if its a valid number 
        if amount.isdigit():
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

# Call the function
#deposit()
def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)

main()
