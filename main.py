import random

while True:
    try:
        question = int(input('Guess a number between 1 and 10: '))
        number = random.randint(1, 10)
        if 0 < number < 10:
            if question == number:
                print('You are right')
                break
            else:
                print('Please pick a number between 1 and 10')
    except ValueError:
        print('Please enter a number between 1 and 10')