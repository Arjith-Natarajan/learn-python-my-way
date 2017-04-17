# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/magical-word/

# from sys import argv

def prime_number_before (x):
    while(x):
        count =0
        for i in range(2,x/2+1):
            if(x%i==0):
                count+=1
        if(count==0 and (x>=64 and x<=118 )):
            return x
        x-=1

def prime_number_after (x):
    while(x):
        count =0
        for i in range(2,x/2+1):
            if(x%i==0):
                count+=1
        if(count==0 and x>=64):
            return x
        x+=1

# number of test cases
t =  int(raw_input())
output = []
for i in range(0,t):
    n = int(raw_input())
    s = raw_input()
    lol = []
    lol = list(s)

    for key, value in enumerate(lol):
        v = ord(value)
        a = prime_number_after(v)
        b = prime_number_before(v)


        letter = b
        if  b < 64:
            letter = a
        elif a > 118:
            letter = b
        elif a-v < v-b:
            letter = a
        lol[key]= chr(letter)
        # print chr(a), chr(b)

    M = "".join(lol)

    output.append(M)

for name in output :
    print name
