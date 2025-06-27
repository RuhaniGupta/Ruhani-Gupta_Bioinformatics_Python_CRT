#Write a python program to print square numbers from 1 to n.
def Square(N):
    if N==0:
        return 
    Square(N-1)
    print(N*N)
Square(5)

#Write a python program to print square numbers from n to 1.
def Square(N):
    if N==0:
        return 
    print(N*N)
    Square(N-1)
Square(5)

#Write a python program to print prime numbers from 1 to n.
def is_prime(num, i=2):
    if num < 2:
        return False
    if i*i > num:
        return True
    if num % i == 0:
        return False
    return is_prime(num, i+1)

def print_primes(n, curr=1):
    if curr > n:
        return
    if is_prime(curr):
        print(curr)
    print_primes(n, curr+1)
print_primes(20)

#Write a python program to print prime numbers from n to 1.
def is_prime(num, i=2):
    if num < 2:
        return False
    if i*i > num:
        return True
    if num % i == 0:
        return False
    return is_prime(num, i+1)

def print_primes_reverse(n):
    if n < 1:
        return
    if is_prime(n):
        print(n)
    print_primes_reverse(n-1)
print_primes_reverse(20)
#Write a python program to print lower case alphabets from a to z.
def print_lowercase(ch=97):
    if ch > 122:
        return
    print(chr(ch), end=' ')
    print_lowercase(ch + 1)

print_lowercase()