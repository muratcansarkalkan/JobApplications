l = 0
r = 0
def oddNumbers(l, r):
    oddities = []
    for i in range(l, r+1):
        if i % 2 == 1:
            oddities.append(i)
        else:
            continue
    return oddities

oddNumbers(3,32)