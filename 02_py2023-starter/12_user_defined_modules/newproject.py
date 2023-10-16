# Copy the prime_function.py to the current folder and rename it to primes.py 
# Reuse the checkprime function in this example

# Get several numbers from the user
# Extract the maximum, minimum and all the prime numbers
# from the input

#import primes
from primes import checkprime

# input

N = []
print("Enter your numbers: ")
while True:
    n = input("--> ")
    if(n == "!"):
        break
    else:
        if(n.isdigit()):
            N.append(int(n))

# process

# ---------------------------------- start of task

primenumbers = []
for n in N:
    if(checkprime(n)):
        primenumbers.append(n)

# ---------------------------------- end of task

# output
print("-" * 50)
print(N)
print("MAXIMUM  : ", max(N))
print("MINIMUM  : ", min(N))
print("PRIMES   : ", primenumbers)