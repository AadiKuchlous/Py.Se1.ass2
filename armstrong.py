num = input("Enter a number")

def armstrong(n):
    digit1 = int(n[0])
    digit2 = int(n[1])
    digit3 = int(n[2])
    cube = digit1**3 + digit2**3 + digit3**3
    if (cube == int(n)):
        print(n, "is an armstrong number")
    else:
        print(n, "is not an armstrong number")

armstrong(num)
