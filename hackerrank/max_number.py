def max_score(numbers, num_highest=1):
    numbers = sorted(list(set(numbers)), reverse=True)
    if(len(numbers) > 0):
        try:
            return(numbers[num_highest-1])
        except:
            return(numbers[-1])
    else:
        return None
    

nums = [2, 5, 7, 3, 7]
print(max_score(nums, num_highest=3))