numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

none_index = numbers.index(None)

valid_numbers = [num for num in numbers if num is not None]

total = sum(valid_numbers)
average = total / len(numbers)

numbers[none_index] = average

print("Измененный список:", numbers)
