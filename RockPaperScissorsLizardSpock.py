    # Rock Paper Scissors Lizard Spock
import random
import os
v = ''
while v == '':
    userscore = 0
    computerscore = 0
    title = '\t\t\tRock Paper Scissors Lizard Spock'
    tie = 0
    s = ''
    while s == '':
        os.system('cls')
        comppick = random.randint(1,5)
        print(title)
        if userscore == 2 or computerscore == 2:
            if userscore > computerscore:
                print('\nUSER IS THE WINNER')
                input('\nPress Enter To Restart')
                break
            if computerscore > userscore:
                print('\nSorry, Computer Wins')
                input('\nPress Enter To Restart')
                break
        print('\nComputer\'s Score: ', computerscore)
        print('\nUser\'s Score: ',userscore)
        print('\nties :', tie)
        userpick = input('\nType R for Rock, P for Paper, S for Scissors, L for Lizard, or SP for Spock: ').lower().strip()
        if userpick:
            os.system('cls')
            if userpick == 'r':
                user = 'rock'
            elif userpick == 'p':
                user = 'paper'
            elif userpick == 's':
                user = 'scissors'
            elif userpick == 'l':
                user = 'lizard'
            elif userpick == 'sp':
                user = 'spock'
            else:
                print('Fault, Press Enter to restart')
                input()
                continue
            if comppick == 1:
                computer = 'rock'
            elif comppick == 2:
                computer = 'paper'
            elif comppick == 3:
                computer = 'scissors'
            elif comppick == 4:
                computer = 'lizard'
            elif comppick == 5:
                computer = 'spock'
        else:
            print('\nNo Guess?')
            input('\nPress Enter to continue')
            continue
        print("\nComputer: ", computer.upper())
        print("\nUser: ", user.upper())
        if user == computer:
            print('\nIts a tie')
            tie = tie + 1
            input('\nPress enter to continue')
            continue
        elif user == 'rock':
            if computer == 'scissors':
                print('\n\t\t\t\tRock Smashes Scissors')
                userscore = userscore + 1
            elif computer == 'paper':
                print('\n\t\t\t\tPaper Covers Rock')
                computerscore = computerscore + 1
            elif computer == 'lizard':
                print ('\n\t\t\t\tRock Smashes Lizard')
                userscore = userscore + 1
            elif computer == 'spock':
                print('\n\t\t\t\tSpock Vaporizes Rock')
                computerscore = computerscore + 1
        elif user == 'paper':
            if computer == 'rock':
                print('\n\t\t\t\tPaper Covers Rock')
                userscore = userscore + 1
            elif computer == 'scissors':
                print('\n\t\t\t\tScissors Cut Paper')
                computerscore = computerscore + 1
            elif computer == 'lizard':
                print('\n\t\t\t\tLizard Eats Paper')
                computerscore = computerscore + 1
            elif computer == 'spock':
                print('\n\t\t\t\tPaper Disproves Spock')
                userscore = userscore + 1
        elif user == 'scissors':
            if computer == 'paper':
                print('\n\t\t\t\tScissors Cut Paper')
                userscore = userscore + 1
            elif computer == 'rock':
                print('\n\t\t\t\tRock Smashes Scissors')
                computerscore = computerscore + 1
            elif computer == 'lizard':
                print('\n\t\t\t\tScissors Decapitates Lizard')
                userscore = userscore + 1
            elif computer == 'spock':
                print('\n\t\t\t\tSpock Smashes Scissors')
                computerscore = computerscore + 1
        elif user == 'lizard':
            if computer == 'paper':
                print('\n\t\t\t\tLizard Eats Paper')
                userscore = userscore + 1
            elif computer == 'rock':
                print('\n\t\t\t\tRock Crushes Lizard')
                computerscore = computerscore + 1
            elif computer == 'scissors':
                print('\n\t\t\t\tScissors Decapitates Lizard')
                computerscore = computerscore + 1
            elif computer == 'spock':
                print('\n\t\t\t\tLizard Poisons Spock')
                userscore = userscore + 1
        elif user == 'spock':
            if computer == 'paper':
                print('\n\t\t\t\tPaper Disproves Spock')
                computerscore = computerscore +1
            elif computer == 'scissors':
                print('\n\t\t\t\tSpock Smashes Scissors')
                userscore == userscore +1
            elif computer == 'rock':
                print('\n\t\t\t\tSpock Vaporizes Rock')
                userscore = userscore + 1
            elif computer == 'lizard':
                print('\n\t\t\t\tLizard Poisons Spock')
                computerscore = computerscore + 1
    
        print('\nComputer\'s Score: ', computerscore)
        print('\nUser\'s Score: ', userscore)
        r = input('\n\nPress enter to continue.')
                
