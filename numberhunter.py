import random

# Range and rounds are included here to tweak difficulty more easily
max_rng = 1000
max_rounds = 10

# Intro text
print('\nWelcome to Number Hunter!')
print(f'\nI will pick a number between 1 and {max_rng}. You have ten guesses to guess it.')
print('Sounds easy, right? But there\'s a catch...')
print('\nEach time you miss, I\'m going to move the number away from your guess.')
print('The target number may shift by up to twice the difference.')
print('(And yes, it can end up as a negative number.)')
print('\nThat\'s it for the rules, so let\'s begin!')

replay = True

##### GAME START #####

while replay == True:

    # You lose unless proven otherwise
    winner = False
    # Choose a number to guess
    target = random.randint(1,max_rng)

    # Loop for specified number of rounds
    for round_num in range(max_rounds):

        # Setting guess = False doesn't allow you to guess 0
        guess = 'loop'

        # The guess must be an integer
        while guess == 'loop':
            print('\nTake your best guess!')
            guess = input('> ')
            try:
                guess = int(guess)
            except:
                print('\nA guess needs to be an integer, my friend.')
                guess = 'loop'

        # Did you win? If so, set winner = True and break out of the for loop
        if guess == target:
            print('\nYou guessed it! You win!')
            print(f'You took {round_num + 1} guesses to find the number.')
            winner = True
            break

        # Otherwise, determine if you need to go higher or lower, and make the adjustment
        else:
            direction = target - guess

            # No need to do this part if on the last guess (index = max_rounds - 1)
            if direction > 0 and round_num < max_rounds - 1:
                print('\nYou need to guess a higher number.')
                shuffler = random.randint(0, direction * 2)
                if shuffler > 0:
                    target += shuffler
                    print(f'I am adding {shuffler} to the target number.')

            # This is already an else condition if the guess was off so the guess must be too high
            elif round_num < max_rounds - 1:
                print('\nYou need to guess a lower number.')
                shuffler = random.randint(direction * 2, 0)
                if shuffler < 0:
                    target += shuffler
                    print(f'I am subtracting {-shuffler} from the target number.')

    # Once the for loop is done, did you win?
    if winner == False:
        print('\nSorry, you lose!')
        print(f'The final number was {target}.')

    # Making sure the input is accurate because people suck
    yes_no = False
    while yes_no == False:
        print('\nPlay again? (Y/N)')
        yes_no = input('> ').upper()
        if yes_no == 'N':
            replay = False
        elif yes_no != 'Y':
            print('\nPlease choose "Y" or "N". Thanks!')
            yes_no = False

print('\nThanks for playing Number Hunter! Please come back soon!\n')
