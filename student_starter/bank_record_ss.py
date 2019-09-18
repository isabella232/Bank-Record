
def delete(records):
    ''' removes an entry from records '''
    # ask the user for which entry to delete

    # check if entry exists

    # delete the entry
    

def insert(records):
    ''' inserts a new entry '''
    # ask the user for which entry to insert

    # insert the new entry


def merge(records):
    ''' merges two entries into one
        the amounts are added together
    '''
    # ask the user for which entries to merge and the new entry's data

    # merge the two entries into here


def print_all(records):

    ''' print all entries by a given topic '''


def print_menu():
    ''' prints available options using a list '''
    # create a list here

    # print the message and options (numbered)
   

def main():
    ''' Keeps track of a dictionary with key values as:
        {"Name" : [money(int), memos joined (string)]}
        User can choose to print entries, add or remove some, or merge them
    '''
    records = {}

    while (True):
        print_menu()
    
        choice = int(input("Your choice: "))

        if (choice == 0):
            return

        switch = {
            1: print_all, # TODO fill-in
            2: insert, # TODO fill-in
            3: delete, # TODO fill-in
            4: merge # TODO fill-in
        }

        switch[choice](records)
