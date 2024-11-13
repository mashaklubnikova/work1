numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Исходный список
list = [2, -93, -2, 8, -15.65, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Находим сумму всех элементов списка, кроме пропущенного элемента
total_sum = sum(num for num in list if num is not None)

# Находим количество всех элементов списка, включая пропущенный элемент
total_count = len([num for num in list if num is not None])

# Находим среднее арифметическое
average = total_sum / total_count

# Заменяем пропущенный элемент средним арифметическим
for i in range(len(list)):
 if list[i] is None:
        list[i] = average

print("Измененный список:", list)



