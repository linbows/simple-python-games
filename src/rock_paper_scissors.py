import random as r
import time as t

def rps():
    user_action = input('[R]ock [p]aper or [s]cissors?')
    user_action = user_action.lower()
    t.sleep(0.5)
    comp_actions = ['rock','paper','scissors']
    comp_action = r.choice(comp_actions)
    print(f'{name} chose {user_action}!')

    if user_action == comp_action:
        print(f'You both selected {user_action}, it\'s a tie!')
    elif user_action == 'r' or user_action == 'rock':
        if comp_action == 'scissors':
            print('Rock smashes scissors, you win!')
        else:
            print('Papers covers rock, you lose. :(')
    elif user_action == 'p' or user_action == 'paper':
            if comp_action == 'rock':
                print('Paper covers rock, you win!')
            else:
                print('Scissors cut paper, you lose. :(')
    elif user_action == 's' or user_action == 'scissors':
        if comp_action == 'paper':
            print('Scissors cut paper, you win!')
        else:
            print('Rock smashes scissors, you lose!')

print('Welcome!')
t.sleep(0.5)
name = input('What\'s your name? ')
name = name.capitalize()
rps()
print('Thanks for playing!')
play_again = input('Play again? ')
play_again = play_again.lower()

if play_again == 'y' or play_again == 'yes':
    rps()
else:
    print('exiting..')
    t.sleep(0.5)
    exit()