numbers = [1, 2, 2, 3, 3, 3]
def count_numbers(numbers):
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] = counts[num] + 1
        else:
            counts[num] = 1
    return(counts)
print(count_numbers([1, 2, 2, 3, 3, 3]))