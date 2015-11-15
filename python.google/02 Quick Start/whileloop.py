#!/usr/bin/python3

# simple fibonacci series
# the sum of two elements defines the next set

a = 0
b = 1
while b < 100:
    print(b)
    a = b
    b = a + b

a, b = 0, 1
while b < 50:
   print(b)
   a, b = b, a + b
