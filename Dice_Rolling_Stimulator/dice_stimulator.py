from random import randint
from ascii_art import dice_faces


print('**********Dice Stimulator**********')

new = True
while True:
    message = 'Do you want to roll a Die '
    if not new:
        message += 'again '
    play = input(message + '[y/n]: ').lower()
    new = False


    if play != 'y':
        print('Bye...')
        break

    random_number = randint(1, 6)

    print(dice_faces[random_number])