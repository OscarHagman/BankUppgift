#FUNCTIONS
def try_input_to_int():
    while True:
        try:
            return int(input())
        except:
            print("You can only enter numbers, try again")

def check_valid_pin(input):
    str_input = str(input)
    if len(str_input) == 4 or len(str_input) == 6 and type(input) is int:
        return True
    else:
        return False

def get_intresst(years, balance):
    if balance >= 1 and balance <= 1000:
        balance = balance * 2 * years
        
    elif balance >= 1001 and balance <= 5000:
        balance = balance * 3 * years

    elif balance >= 5001 and balance <= 10000:
        balance = balance * 4 * years

    elif balance > 10001:
        balance = balance * 5 * years
    else:
        print("Can't get intresst when you're in debt...")
    return balance

#CODE STARTS HERE
print("Welcome to the bank of Zeros and Ones!\n")
login_screen = True
while login_screen:
    balance_history = []
    balance = 0
    print("Enter your 4 or 6 digit pin")
    if check_valid_pin(try_input_to_int()):       
        is_run = True
        while is_run:
            print("\n[1] Deposit money\n[2] Withdraw money\n[3] Check Balance\n[4] Collect intresst\n[5] Exit")

            menu_choise = input()
            if menu_choise == "1":
                print("How much do you want to deposit?")
                balance += try_input_to_int()
                balance_history.append(balance)
                print("Current balance is " + str(balance))

            elif menu_choise == "2":
                print("How much do you want to withdraw?")
                balance -= try_input_to_int()
                balance_history.append(balance)
                print("Current balance is " + str(balance))
            
            elif menu_choise == "3":
                print("Your balance is " + str(balance))
            
            elif menu_choise == "4":
                print("How many years do you wanna skip")
                years = try_input_to_int()
                balance = get_intresst(years, balance)
                balance_history.append(balance)
                print("You have now skipped " + str(years) + " and your current balance is " + str(balance))

            elif menu_choise == "5":
                print("\nExiting\nBalance history:")
                print('\n'.join(map(str, balance_history)))
                print("\nGood bye...\n")
                is_run = False
            
            else:
                print("\nYou can only choose between 1 and 5 in this menu")
    else:
        print("Invalid pin\n")