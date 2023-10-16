# Write a function checkprime which returns True if the number is prime and False otherwise

def checkprime(n):
    prime = True
    for i in range(2, n):
        if (n % i == 0):
            prime = False
            break
    return prime

print("prime function")

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    if(checkprime(n)):
        print("The number is prime")
    else:
        print("The number is  not prime")