
nums = raw_input()
num = nums.split()
count = 0

for i in range(int(num[0]), int(num[1])+1):
    if(i % int(num[2]) == 0):
        count += 1
    # print i

print count
