import math

while True:
    long = float(input("long "))
    short = float(input("short "))

    print(round(math.sqrt(long * long - short * short), 1))
    print("")


