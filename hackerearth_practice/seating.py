n = int(raw_input())
output = []
for i in range(0, n):
    seat_no = int(raw_input())
    # n_seat =
    # print "Normalized seat :", n_seat
    index = seat_no / 12
    if (seat_no % 12 != 0):
        index += 1

    # print "block :", index
    # end = index*12
    # print "End seat_no: ", end
    # start = (index-1)*12 +1
    # print "Start seat_no", start
    # tot_sum = start+ end
    # print "Sum to be satisfied: ",tot_sum
    # opp_seat_no = tot_sum - seat_no
    # print "Opp seat: ", opp_seat_no
    output.append(((index-1)*12 +1)+index*12 - seat_no)
    # block = 3
    # if n_seat==0 or n_seat>9:
    #     output.append(12*(index-1) + n_seat+1)
    # elif n_seat <= 3 :
    #     output.append((12*(index+1)) - n_seat+1)
    # elif n_seat <= 6:
    #     output.append((12 * (index + 1)) - n_seat + 1)
    # elif n_seat <= 9:
    #     output.append((6 * ((seat_no / 6))) - (n_seat % 6) + 1)
    # else

    # if n_seat <= 3:
    #     print (12*(index+1)) - n_seat+1
    # if n_seat <= 3:
    #     print (12*(index+1)) - n_seat+1

    if seat_no % 6 == 0 or (seat_no - 1) % 6 == 0:
        output.append("WS")
    elif seat_no % 3 == 0 or (seat_no - 1) % 3 == 0:
        output.append("AS")
    else:
        output.append("MS")

for i in range(0, len(output) - 1):
    if i % 2 == 0:
        print output[i], output[i + 1]
