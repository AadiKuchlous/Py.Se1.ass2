start = int(input("Enter the starting number \n"))
end = int(input("Enter the ending number \n"))

def is_prime(y):
        for i in range(2, int(round(y/2))+1):
            if (int(y) % i == 0):
                return False
        return True

for y in range(start, end):
    if (is_prime(y)):
        print (y)
