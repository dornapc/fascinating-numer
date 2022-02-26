num = 192
a = 0
if len(str(num)) >=3:
    n2 = num * 2
    n3 = num * 3
    fs = str(num) + str(n2) + str(n3)
    for j in range(1,10):
        if str(j) in fs:
            a += 1
        else:
            print("not a fascinating number")
            break
    else:
        print("yes its a fascinating number")
#its working coding tested
