for n in range(1, 100):
    if n%18 == 0:
       print("Fuzz")
    elif n%6 == 0:
       print("Buzz")
    elif n%3 == 0:
       print("Fuzzy")
    else:
       print(n)
