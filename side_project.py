import random

MAX_LINES = 3 # similar to slot machine [[1] [2] [3]] <--- 1 line 
MAX_BET = 1000
MIN_BET = 1

ROWS = 3 
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winnings(columns,lines,bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:  
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)
            
    return winnings, winnings_lines
            
    

#collecting user input 
#getting deposit 

def get_slot_machine(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():  # captures symbol_count dict inside a list
        for _ in range(symbol_count):       # appends symbol(key) for every value of value(symbol_count)
            all_symbols.append(symbol)    
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:  
                print(column[row], end="")

        print()


def deposit():
    while True:
        actual_deposit = int(input('How many do you wanna deposit? $'))
        if actual_deposit > 0:
            actual_deposit = actual_deposit
            break
        else:
            print("Enter a valid number")
    return actual_deposit

#collect the bet

def get_number_of_lines():
    while True:
        lines = input(f"How many lines do you want to be on (1-{str(MAX_LINES)}) ")
        if int(lines) > 0:
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number")
        else:
            print("Please input a number")
    return lines


# ask how many bet per line
def get_bet():
    while True:
        bet_amount = input(f"How many do you want to bet? ")
        if int(bet_amount) > 0:
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} and {MAX_BET}")
        else:
            print("Please input a number")
    return bet_amount
    

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines    
        if total_bet > balance:           
            print(f"Your bet should be within your balance, your current balance is ${balance}")
            get_bet()
        else:
            break
    print(f"Bet: ${bet} Lines:{lines} Total Bet: ${total_bet} ")

    slots = get_slot_machine(ROWS,COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main_game():
    balance = deposit()
    while True:
        print(f"Current balance is: ${balance}")
        answer = input("Press enter to play (q to quit)")
        if answer =="q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main_game()
