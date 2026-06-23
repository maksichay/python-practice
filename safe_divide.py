def safe_divide(numbers, divisor):
    if divisor == 0:
        return "Деление на 0 невозможно!"
    else:
        result = []
        for num in numbers:
            result.append(num / divisor)
        return(result)
print(safe_divide([10, 20, 30], 2))