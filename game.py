import random
import math

# compare user & computer input for each round 
def result(user, computer):
    if user == computer:
        return "TIE"
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return "VICTORY"
    return "DEFECT"

# Start the game
def run_game():
    player_wins = 0
    computer_wins = 0
    name = str(input('Enter Your Name : '))

    # Error check for integer input
    try:
        best_of = int(input('Enter Play Best of : '))
    except ValueError:
        print('\nInvalid Input for Best_Of pls Enter Integer....')
        return

    # if best_of is even then devide-by 2 and add +1
    # if it's odd then devide-by 2
    if best_of%2 == 0:
        wins_necessary = math.ceil(best_of/2) + 1
    else:
        wins_necessary = math.ceil(best_of/2)

    # loop until player_wins or computer_wins < required_to_win (wins_necessary)
    while player_wins < wins_necessary and computer_wins < wins_necessary :
        user_choice = str(input('\nEnter your Choice (r, p, s) : '))
        if user_choice in ['r', 'R', 'rock', 'Rock', 'ROCK']:
            user_choice = 'r'
        elif user_choice in ['p', 'P', 'paper', 'Paper', 'PAPER']:
            user_choice = 'p'
        elif user_choice in ['s', 'S', 'scissor', 'Scissor', 'SCISSOR']:
            user_choice = 's'
        else:
            print("\nIvalid Choice...")
            return

        # choose random from r, p, s for computer
        comp_choice = random.choice(['r', 'p', 's'])

        # calling result function for compare
        game_result = result(user_choice, comp_choice)

        # increasing winners count
        if game_result == "VICTORY":
            player_wins = player_wins + 1
        elif game_result == "DEFECT":
            computer_wins = computer_wins + 1

        # printing result for each round
        print('\n\n\n###  {}  ###\n'.format(game_result))
        print('{0} entered :- "{1}"'.format(name, "Rock" if user_choice=='r' else "Paper" if user_choice=='p' else "Scissor"))
        print('Computer entered :- "{}"'.format("Rock" if comp_choice=='r' else "Paper" if comp_choice=='p' else "Scissor"))
        
        print('\n{} Wins : {}'.format(name, player_wins))
        print('Computer Wins : {}'.format(computer_wins))

    # printing final result
    if player_wins > computer_wins:
        print('\n\nVictory *** Victory *** Victory')
        print('You "WON" this Game')
    else:
        print('\n\nDefect *** Defect *** Defect')
        print('Sorry!! You "Lost" this Game')

    # ask to play again
    again = str(input('\nTry once more (y/n) ? '))
    if again in ['y', 'Y', 'yes', 'Yes', 'YES']:
        run_game()
    elif again in ['n', 'N', 'no', 'No', 'NO']:
        pass
    else:
        print('\nInvalid Input...')
        pass
        
# Starting the app
if __name__ == '__main__':
    run_game()
