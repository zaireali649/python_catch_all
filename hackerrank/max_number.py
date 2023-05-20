

# function to get nth highest number (not including duplicates)
# accepts list and nth number
def max_score(numbers, num_highest=1):
    # consider bad num_highest
    if(num_highest <= 0):
        num_highest = 1
    # remove duplicates and sort list
    numbers = sorted(list(set(numbers)), reverse=True)
    # check if the list has elements
    if(len(numbers) > 0):
        # try to get nth highest number
        try:
            return(numbers[num_highest-1])
        # default to lowest number if out of index
        except:
            return(numbers[-1])
    # there are no elements in list
    else:
        return None
    
if __name__=='__main__':
    # some tests to validate function works as expected
    print(max_score([2, 3, 6, 6, 5], num_highest=2) == 5)
    print(max_score([57, 57, -57, 57], num_highest=2) == -57)
    print(max_score([5, 5, 5, 5, 5, 5, 5, 5, 5, 6], num_highest=2) == 5)
    print(max_score([2, 3, 6, 6, 5]) == 6)
    print(max_score([]) == None)
    print(max_score([2, 3, 6, 6, 5], num_highest=5) == 2)
    print(max_score([2, 3, 6, 6, 5], num_highest=50) == 2)
    print(max_score([2, 3, 6, 6, 5], num_highest=-1) == 6)
