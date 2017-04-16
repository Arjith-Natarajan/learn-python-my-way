def create_list(numbers,limit):
    i = 0

    while i <= limit:
        numbers.append(i)

        i = i + 3
        # print "Numbers now: ", numbers
        # print "At the bottom i is %d" % i

    print "The numbers: ",

    for num in numbers:
        print num,

elements = []
create_list(elements,4)

another_elements=[]
create_list(another_elements, 20)
