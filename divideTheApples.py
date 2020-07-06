if __name__ == '__main__':
    n = int(input("Enter number of apples you have : "))
    mn = int(input("Enter minimum : "))
    mx = int(input("Enter maximum : "))
    for i in range(mn, mx+1):
        if n%i == 0:
            print(f"{i} is divisor of {n}.")
        else:
            print(f"{i} is not divisor of {n}.")