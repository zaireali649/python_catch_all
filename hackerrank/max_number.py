# function to get nth highest number (not including duplicates)
# accepts list and nth number
def max_score(numbers, num_highest=1):
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
    

nums = [2, 5, 7, 3, 7]
print(max_score(nums, num_highest=3))