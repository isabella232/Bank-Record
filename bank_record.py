
def delete(records):
    ''' removes an entry from records '''
    entryToDel = input("Enter a name: ")

    # check if entry exists
    if (entryToDel not in records):
        print(entryToDel + " does not exist")
        return

    # delete the entry
    del records[entryToDel]
    

def insert(records):
    ''' inserts a new entry '''
    name = input("Owner: ")
    money = input("$")
    if (not money.isdigit()):
        print("Invalid amount: $" + money)
        return
    
    memo = input("Memo: ")

    # create the entry and assign it to using appropriate key
    records[name] = [money, memo]


def merge(records):
    ''' merges two entries into one
        the amounts are added together
    '''
    entry1 = input("First entry to merge: ")
    if (entry1 not in records):
        print(entry1 + " not found")
        return
    
    entry2 = input("Second entry to merge: ")
    if (entry2 not in records):
        print(entry2 + " not found")
        return
    mergedEntry = input("Owner of merged entry: ")
    if (mergedEntry in records):
        print(mergedEntry + " already exists")
        return
    
    memos = input("Memo: ")

    # get the total money and remove individual entries
    total = records[entry1][0] + records[entry2][0]
    del records[entry1]
    del records[entry2]
    
    # create new merged entry
    records[mergedEntry] = [total, memos]


def print_all(records):

    ''' print all entries by a given topic '''
    for entry in records:
        print("Name: " + str(entry))
        print("Amount: " + str(records[entry][0]))
        print("memo: " + records[entry][1])
        print("\n")


def print_menu():
    ''' prints available options using a list '''
    options = [
        'Exit',
        'Print all entries',
        'Add a new entry',
        'Delete an entry',
        'Merge entries'
    ]

    print("Please pick 1-" + str(len(options)))

    # print the options
    i = 0
    for option in options:
        print(str(i) + ". ", end="")
        print(option, end="\n")
        i += 1

def main():
    ''' Keeps track of a dictionary with key values as:
        {"Name" : [money(int), memos joined (string)]}
        User can choose to print entries, add or remove some, or merge them
    '''
    records = {}

    while (True):
        print_menu()
    
        choice = input("Your choice: ")
        if (choice.isdigit() and int(choice) >= 0 and int(choice) <= 4):
            choice = int(choice)
        else:
            print("Invalid choice")
            continue

        if (choice == 0):
            return

        switch = {
            1: print_all,
            2: insert,
            3: delete,
            4: merge
        }

        switch[choice](records)
