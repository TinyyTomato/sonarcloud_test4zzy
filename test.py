import numpy as np
import panadas as pd

def sonarcloud_test4zzy(t):  
    a = 10 if t % 2 == 0 else 5
    b = 5
    c = 0 if a == b else 1
    d = 20

    if a != b:
        print("True")
    if b == c:
        print("True")
    if (a + b + c) == d:
        print("True")
    else:
        print("What the fuck!")

    t = d


t = 100
sonarcloud_test4zzy(t)


