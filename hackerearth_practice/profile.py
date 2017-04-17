# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/roy-and-profile-picture/

l = int(raw_input())
n = int(raw_input())
output =[]
for i in range(0,n):
    in_str = raw_input()
    in_list = in_str.split()
    w = int(in_list[0])
    h = int(in_list[1])

    if (w < l or h < l):
        output.append("UPLOAD ANOTHER")
    elif (w>=l and h>=l and w==h):
        output.append("ACCEPTED")
    else:
        output.append("CROP IT")

for s in output:
    print s
