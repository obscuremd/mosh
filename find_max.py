def find_max(numbers):
    max = numbers[0]
    for i in numbers:
        if i > max:
            max = i
    return(max)