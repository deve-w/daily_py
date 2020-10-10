n = int(input()) #input() function takes input as a string type
#int() converts it to integer type
fact = 1
i = 1
while i<=n:
    fact = fact*i
    i = i+1
print(fact)