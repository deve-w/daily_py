from math import *
C,H = 50,30

def calc(D):
    D = int(D)
    return str(input(sqrt((2*C*D)/H)))

D = input().split(",")
D = list(map(calc,D))  #applying calc function on D and storing as  A LIST
print(",".join(D))