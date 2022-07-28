def max_score(numbers, num_highest=1):
    return(sorted(list(set(numbers)), reverse=True)[num_highest-1])
    

nums = [2, 5, 7, 3, 7]
print(max_score(nums, num_highest=2))