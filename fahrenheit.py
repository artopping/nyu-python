#!/usr/bin/env python3

def to_celsius (degrees_fahrenheit):
    degrees_celsius= 5/9*(degrees_fahrenheit-32)
    return degrees_celsius

def main():
    print(to_celsius(32))

if __name__=='__main__':
    main()


