numbers = [1,3,3,5,3,3,5,6,7,8,2,1,3,5,6]

# define func
def countDuplicate(numbers):
    # define list
    dupl = []
    
    for i in numbers:
        # if i is a duplicate
        if numbers.count(i) > 1:
            # and not in dupl
            if i not in dupl:
                # append then
                dupl.append(i)
            
    print (dupl)

countDuplicate(numbers)