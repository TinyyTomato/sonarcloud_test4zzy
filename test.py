import numpy as np
import pandas as pd

def sonarcloud_test4zzy(t):  
    dd = 5
    e = 5
    c = 5 if dd == e else 0
    d = 20

    if dd != e:
        print("True")
    if e == c:
        print("True")
    if (dd + e + c) == d:
        print("True")
    else:
        print("What the fuck!")

    t = d
    print(t)


t = 100
sonarcloud_test4zzy(t)


