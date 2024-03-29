# Python doesn’t support the do-while loop statement.
# Use a while loop and the break statements to emulate a do...while loop in Python


from random import randint

# determine the range
MIN = 0
MAX = 10

# generate a secret number
secret_number = randint(MIN, MAX)

# initialize the attempt
attempt = 0

while True:
    attempt += 1

    input_number = int(input(f'Enter a number between {MIN} and {MAX}:'))

    if input_number > secret_number:
        print('It should be smaller.')
    elif input_number < secret_number:
        print('It should be bigger.')
    else:
        print(f'Bingo! {attempt} attempt(s)')
        break
