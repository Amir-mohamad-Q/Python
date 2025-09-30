import random

def validation_inpot(user_guess):
    
    if not user_guess.isdigit():
        print(f'invalid inpot. try a number between 1-6.{user_guess}')
        return False
    if 7 < int(user_guess) or 0 > int(user_guess):
        print('please enter a number between 1-6')
        return False
    return True


def main():
    score = 100
while True:
    guess = random.randint(1,6)
    user_guess = input('Guess a number between 1-6')
    if user_guess == 'q':
        print('thank ypu for playing.')
        break

        print(user_guess.type())
    if not validation_inpot(user_guess):
        continue

    if int(user_guess) == guess:
        print(f"you win! with {user_guess} number :)\nscore: {score}\n--------------------") 
    else : 
        score -= 5
        print(f"you faile :(\nscore: {score}\n--------------------")
print(score)


if __name__ == '__main__':
    main()