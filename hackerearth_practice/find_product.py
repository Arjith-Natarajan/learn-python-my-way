# Find Product
p=1
m=1000000007
raw_input()
input = raw_input().split()
for _ in range(0,len(input)):
    p= ((p%m)*(int(input[_])%m))% m
print p
