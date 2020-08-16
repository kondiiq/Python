secret_num = 9
chance = 0
max_chance = 3
while chance < max_chance:
    guess = int(input('Guess:'))
    chance += 1
    if guess == secret_num :
        print('You won!')
        break
else:
    print('You lose friend :(')
    