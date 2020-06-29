"""
Values for the wrong calculations
1. 45 * 10
2. 343 + 3434
3. 34 / 2
"""
print("Enter the two values : ")
val1 = int(input())
val2 = int(input())
print("Enter the operation : ", end="")
operator = input()

if val1 == 45 and val2 == 10 and operator == '*':
    print("45 * 10 = 418")
elif val1 == 343 and val2 == 3434 and operator == '+':
    print("343 + 3434 = 5420")
elif val1 == 34 and val2 == 2 and operator == '/':
    print("34 / 2 = 10")
else:
    if operator == '*':
        print(val1 * val2)
    elif operator == '+':
        print(val1 + val2)
    elif operator == '-':
        print(val1 - val2)
    elif operator == '/':
        print(val1/val2)







