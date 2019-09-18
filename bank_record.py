
def delete(records):
    ''' removes an entry from records '''
    entryToDel = input("Enter a name: ")

    if (entryToDel not in records):
        print(entryToDel + " does not exist")
        return

    del records[entryToDel]
    

def insert(records):
    ''' inserts a new entry '''
    name = input("Owner: ")
    money = int(input("$"))
    comments = input("Comments: ")
    records[name] = [money, comments]


def merge(records):
    ''' merges two entries into one
        the amounts are added together
    '''
    entry1 = input("First entry to merge: ")
    entry2 = input("Second entry to merge: ")
    mergedEntry = input("Owner: ")
    comments = input("Comments: ")

    # get the total money and remove individual entries
    total = 0
    del records[entry1]
    del records[entry2]

    # create new merged entry
    records[mergedEntry] = [total, comments]


def print_all(records):

    ''' print all entries by a given topic '''
    for entry in records:
        print(entry)

    return


def print_menu():
    ''' prints available options '''
    options = [
        'Exit',
        'Print all entries',
        'Add a new entry',
        'Delete an entry',
        'Merge entries'
    ]

    print("Please pick 1-" + str(len(options)))
    i = 0
    for option in options:
        print(str(i) + ". ", end="")
        print(option, end="\n")
        i += 1

def main():
    ''' Keeps track of a dictionary with key values as:
        {"Name" : [money(int), comments joined (string)]}
        User can choose to print entries, add or remove some, or merge them
    '''
    records = {}

    while (True):
        print_menu()
    
        choice = int(input("Your choice: "))

        if (choice == 0):
            return
        # TODO note switch stmts in cards
        switch = {
            1: print_all,
            2: insert,
            3: delete,
            4: merge
        }

        switch[choice](records)
