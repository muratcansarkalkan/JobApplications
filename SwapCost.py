arr = [1,2,3,5,4]

# define arranged lists for ascending and descending
ara = sorted(arr)
ard = ara[::-1]

def swapcost(arr):
# define costs for ascend and descend
    costa = 0
    costd = 0

    for i in range(0,len(arr)):
        # does for ascend
        k = abs(ara[i]-arr[i])
        costa += k
    
    for i in range(0,len(arr)):
        # does for descend
        k = abs(ard[i]-arr[i])
        costd += k 
    # returns the lower one
    return min(costa,costd)
swapcost(arr)