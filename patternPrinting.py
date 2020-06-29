rows = int(input("No. of rows daalo bhai : "))
bl = bool(int(input("Bool dalo (0/1) : ")))
if bl == True:
    for i in range(1,rows+1):
        print("* " * i)
else:
    for i in range(rows):
        i = rows - i
        print("* " * i)