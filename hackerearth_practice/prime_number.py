# You are given an integer N.
# You need to print the
# series of all prime numbers till N.
# SAMPLE INPUT
# 9
# SAMPLE OUTPUT
# 2 3 5 7

n = int(raw_input())
for i in range(2,n):
    count =0
    for j in range(2,i/2+1):
        if(i%j==0):
            count+=1
    if count==0 :
        print i,
