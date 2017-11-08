"""Crazy Cat-Lady Cat Tracker 2000"""

cats_owned = {'siamese': 2, 'bengals': 1, 'tabbys': 3,
              'ragdoll': 2, 'persian': 3, 'sphynx': 4}

def cat_tracker():
    print('1 - Remove Cat')
    print('2 - Add Cat')
    print('3 - Calculate total of cats')
    print('4 - Calculate total cats by breed')
    print('5 - Quit')
    usr_input = str(input('Choose a menu item\n'))
    if usr_input == '1':
        removed_cat = str(input('What breed of cat would you like to delete?\n')).lower()
        amnt_cat = int(input('How many?\n'))
        if removed_cat in cats_owned.keys():            #Determines if cat requested is already in dict
            del cats_owned[removed_cat]
        elif removed_cat not in cats_owned:
            print('There are no', removed_cat)          #If you delete all of one breed then try to delete more it asks
        print('Deleted\n')                              #how many...
        cat_tracker()
    elif usr_input == '2':
        add_cat = str(input('What type of cat would you like to add?\n'))
        amnt_cat = int(input('How many?\n'))
        cats_owned[add_cat] += amnt_cat
        print('Updated')
        cat_tracker()
    elif usr_input == '3':
        print('Total cats:', sum(cats_owned.values()))
        print()
        cat_tracker()
    elif usr_input == '4':
        for i in cats_owned:
            print(f'{i}: {cats_owned[i]}')
            print()
        cat_tracker()
    elif usr_input == '5':
        exit()
    return

cat_tracker()