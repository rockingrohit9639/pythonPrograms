import random

def guess(pl, num):
    if pl == num:
        return True
    elif pl > num:
        return f"Your number is greater. Try another guess."
    elif pl < num:
        return f"Your number is less. Try another guess."

if __name__ == '__main__':
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    number1 = random.randrange(a, b)
    # print(number)
    pl1_chances = 0
    pl2_chances = 0
    print("Player 1 chance first --- ")
    while True:
        pl_num = int(input("Enter your choice : "))
        if guess(pl_num, number1) == True:
            print("Your guess is right.")
            break
        else:
            print(guess(pl_num, number1))
            pl1_chances += 1
    number2 = random.randrange(a, b)
    print("Player 2 chance Now --- ")
    while True:
        pl_num = int(input("Enter your choice : "))
        if guess(pl_num, number2) == True:
            print("Your guess is right.")
            break
        else:
            print(guess(pl_num, number2))
            pl2_chances += 1

print(f"Player 1 took {pl1_chances} chances.")
print(f"Player 2 took {pl2_chances} chances.")
if pl1_chances < pl2_chances:
    print("Hence Player 1 wins.")
else:
    print("Hence Player 2 wins.")

