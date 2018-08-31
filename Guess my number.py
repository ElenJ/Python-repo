import random

print('Hello, my new friend')
print('What is your name?')
name=input()
print('Well, nice to meet you, '+name)
print('Let us play a game. Do you want to play a game?')
decide = input()
negate = ['no','nope','nee','ne'] #change to answer starts with "n"
while decide not in negate:

    print('Im thinking of a number which is...')
    secretNumber = random.randint(0, 20)
   # print(secretNumber)
    for i in range(5):

        while True:
            try:
                usersinput = input()
                usersinput=int(usersinput)
                break
            except ValueError:
                print('Please enter a number')
        if usersinput < secretNumber:
            print('Too low')
        elif usersinput > secretNumber:
            print('Too high')
        else:
            break

    if usersinput == secretNumber:
        print('You guessed it!!!')
    print('You needed ' + str(i + 1) + ' guesses')
    if usersinput != secretNumber:
        print('You need greater parapsychological powers!')


    print('Play again?')
    decide = input()
print('OK, bye then')

