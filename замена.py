numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

list = [2, -93, -2, 8, -15.65, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

total_sum = sum(num for num in list if num is not None)

total_count = len([num for num in list if num is not None])

average = total_sum / total_count

for i in range(len(list)):
    if list[i] is None:
        list[i] = average

print("Измененный список:", list)
