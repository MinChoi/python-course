# banking exercise

def show_balance(balance):
    print('--------------')
    print(f'Your balance is ${balance:.2f}')

def deposit():
    amount = float(input('Enter deposit amount: '))
    if amount < 0:
        print('Error! Amount input is less than 0')
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input('Enter withdrawn amount: '))
    if amount > balance:
        print('Insufficient funds!')
        return 0
    elif amount < 0:
        print('Amount should be bigger than 0')
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:

        print('--------------')
        print('ABC bank')
        print('--------------')
        print('1. Show Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')

        choice = input('Enter the number:')

        match choice:
            case '1':
                show_balance(balance)
            case '2':
                balance += deposit()
            case '3':
                balance -=  withdraw(balance)
            case '4':
                is_running = False
            case _:
                print('Please try again')

    print('--------------')
    print('Goodbye!')

if __name__ == '__main__':
    main()