import sys
from config import install, reinstall, delete, connect, check_database
from passcode import passcode


def start_menu():
    # Menu for terminal
    print('-' * 30)
    print(('-' * 13) + 'Menu' + ('-' * 13))
    print('1: Star PassCode')
    print('2: Install PassCode database')
    print('3: Reinstall PassCode database')
    print('4: Delete PassCode database')
    print('X: Exit')
    print('-' * 30)
    return input(f'Type here:\n> ')


# Loop for terminal menu
while True:
    run = start_menu()
    if run == '1':
        if connect() != 'error':
            if check_database() is not None:
                passcode()
                sys.exit()
            else:
                print(f"No 'passcode' database. You need to install it first")
    if run == '2':
        if connect() != 'error':
            install()
            type('Press Enter to continue...')
            continue
    if run in ['3', '4']:
        if connect() != 'error':
            print('Are you sure? You will lose all your saved passwords.')
            while True:
                answer = input("Type 'Y' to continue or type 'N' to cancel.\n> ")
                if answer in ['Y', 'y']:
                    if run == '3':
                        reinstall()
                        break
                    if run == '4':
                        delete()
                        break
                if answer in ['N', 'n']:
                    print('Canceled')
                    break
                else:
                    continue
            continue
    if run in ['X', 'x']:
        sys.exit()
    else:
        continue
