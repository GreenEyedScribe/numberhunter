import random

print('\nWelcome to Number Hunter!')
print('\nI will pick a number between 1 and 1000. You have ten guesses to guess it.')
print('Sounds easy, right? But there\'s a catch...')
print('\nEach time you miss, I\'m going to move the number away from your guess.')
print('The target number may shift by up to half the difference (rounded down).')
print('(And yes, it can end up as a negative number.)')
print('\nThat\'s it for the rules, so let\'s begin!')

replay = True

##### GAME START #####

while replay == True:

    winner = False
    # Choose a number to guess
    target = random.randint(1,1000)

    for round_num in range(10):

        guess = 'loop'
        while guess == 'loop':
            print('\nTake your best guess!')
            guess = input('> ')
            try:
                guess = int(guess)
            except:
                print('\nA guess needs to be an integer, my friend.')
                guess = 'loop'

        if guess == target:
            print('\nYou guessed it! You win!')
            print(f'You took {round_num + 1} guesses to find the number.')
            winner = True
            break

        else:
            direction = target - guess

            if direction > 0 and round_num < 9:
                print('\nYou need to guess a higher number.')
                shuffler = random.randint(0, direction // 2)
                if shuffler > 0:
                    target += shuffler
                    print(f'I am adding {shuffler} to the target number.')

            elif round_num < 9:
                print('\nYou need to guess a lower number.')
                shuffler = random.randint(direction // 2, 0)
                if shuffler < 0:
                    target += shuffler
                    print(f'I am subtracting {-shuffler} to the target number.')

    if winner == False:
        print('\nSorry, you lose!')
        print(f'The final number was {target}.')

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
