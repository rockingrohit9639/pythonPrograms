import random

l = ["snake", "water", "gun"]
pc_win = 0
pl_win = 0
winner = ""
i=0
while i < 5:
    pc_choice = random.choice(l)
    pl_choice = input("Enter snake, water or gun : ")

    if pl_choice == pc_choice:
        print("This is tie b/w both.")
    elif pl_choice == "snake" and pc_choice == "gun":
        pc_win += 1
    elif pl_choice == "snake" and pc_choice == "water":
        pl_win += 1
    elif pl_choice == "water" and pc_choice == "snake":
        pc_win += 1
    elif pl_choice == "water" and pc_choice == "gun":
        pl_win += 1
    elif pl_choice == "gun" and pc_choice == "snake":
        pl_win += 1
    elif pl_choice == "gun" and pc_choice == "water":
        pc_win += 1
    elif pl_choice == "gun" and pc_choice == "water":
        pc_win += 1
    else:
        print("Wrong Input")
    i += 1
if pc_win > pl_win:
    print("You Loss PC Wins")
    print(f"PC points {pc_win} \nYour Points {pl_win}")
else:
    print("You Wins PC Loss")
    print(f"Your points {pl_win} \nPC Points {pc_win}")

