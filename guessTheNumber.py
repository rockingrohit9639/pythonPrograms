n = 75
lives = 1
print("____WELCOME TO THE GAME - GUESS THE NUMBER ____ ")
print("You have to guess the number in 3 chances.")
print("----Lets Start the Game ----")
while(True):
    guess = int(input("Enter your guess : "))
    if guess > 75:
        print("Wrong Guess. Your guess number is greater. You lost ", lives, "live")
        print("You have ",3 - lives, "lives remaining.")
        lives += 1
    elif guess < 75:
        print("Wrong Guess. Your guess number is lesser. You lost ", lives, "live")
        print("You have ", 3 - lives, "lives remaining.")
        lives += 1
    elif guess == 75:
        print("Hurrey ! You won the game in", lives, "chances.")
        break
    if lives > 3 :
        print("Sorry you lost the game.")
        break