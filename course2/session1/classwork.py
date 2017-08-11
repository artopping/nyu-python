#!/usr/bin/env python3

def fact(n):
    """return the factorial of the given number."""
    r=1
    while n>0:
        r=r*n
        n=n-1
    return r

if __name__ == '__main__':
    n=5
    r=fact(n)
    print("Factorial of {} = {}".format(n, r))


