def insert(name, amount, joinDate):
    return

def join():
    return

def print_all():
    return

def print_menu():
    options = [
        'Print all entries',
        'Add a new entry',
        'Remove an entry',
        'Join entries'
    ]

    print("Please pick 1-" + str(len(options)))
    i = 1
    for option in options:
        print(str(i) + ". ", end="")
        print(option, end="\n")
        i += 1

def remove():
    return

def main():
    records = {}
    print_menu()
    
    choice = input("Your choice: ")

    # TODO note switch stmts in cards
    switcher = {
        1: print_all,
        2: insert,
        3: remove,
        4: join
    }

    switcher[int(choice)]
