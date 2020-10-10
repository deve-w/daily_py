##Using For loop
n= int(input())
ans = {}
for i in range(1,n+1):
    ans[i] = i*i
print(ans)

##using dictionart comprehension
k = int(input())
ans1 = {i:i*i for i in range(1,n+1)}
print(ans1)