ratings = {}

num = input('Enter player 1\'s jersey number: ')
print(num)
rating = input('Enter player 1\'s rating: ')
print(rating)
ratings[num] = rating

num2 = input('Enter player 2\'s jersey number: ')
print(num2)
rating2 = input('Enter player 2\'s rating: ')
print(rating2)
ratings[num2] = rating2

num3 = input('Enter player 3\'s jersey number: ')
print(num3)
rating3 = input('Enter player 3\'s rating: ')
print(rating3)
ratings[num3] = rating3

num4 = input('Enter player 4\'s jersey number: ')
print(num4)
rating4 = input('Enter player 4\'s rating: ')
print(rating)
ratings[num4] = rating4

def roster():
    print('           ROSTER')
    print('Jersey number: %3d, Rating: %3d' % \
          [i for i in ratings], [i for i[i] in ratings])
    return
          
menu_prompt =  """ 
                a - Add player
                d - Remove player
                u - Update player rating
                r - Output players above a rating
                o - Output roster
                q - Quit
            
                Choose an option:\n
        
               """
def menu():
    ans = input(menu_prompt)
    while ans != 'Q':
        if ans.lower() == 'a':
            new_player = input('Enter new player\'s jersey number:\n')
            new_rating = input('Enter new player\'s rating:\n')
            ratings[new_player] = new_rating
            print('New player added.')
            menu()
        elif ans.lower() == 'd':
            delete_player = input('Enter jersey number of player to delete:\n')
            del ratings[delete_player]
            print('Player deleted.')
            menu()
        elif ans.lower() == 'u':
            update_player = input('Enter jersey number of player to update:\n')
            update_rating = input('Enter new rating:\n')
            ratings[update_player] = update_rating
            print('Player updated.')
            menu()
        elif ans.lower() == 'o':
            roster()
            menu()
        elif ans.lower() == 'q':
            print('Exiting.')
            break
        else:
            print('Invalid entry. Try again')
        return

menu()
