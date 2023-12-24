import numpy as np
import pandas as pd

def sonarcloud_test4zzy(t):  
    a = 10 if t % 2 == 0 else 5
    e = 5
    c = 0 if a == e else 5
    d = 20

    if a != e:
        print("True")
    if e == c:
        print("True")
    if (a + e + c) == d:
        print("True")
    else:
        print("What the fuck!")

    t = d
    print(t)


t = 100
sonarcloud_test4zzy(t)


