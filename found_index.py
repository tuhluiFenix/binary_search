def main(num_array, value):
    # Проверка на случай, если все элементы в массиве одинаковые
    if all(x == num_array[0] for x in num_array) and num_array[0] == value:
        return 0
    left, right = 0, len(num_array)-1
    while left <= right:
        mid = (left + right) // 2
        # Проверяем, равно ли среднее значение целевому
        if num_array[mid] == value:
            return mid
        # Если целевое значение меньше среднего, ищем в левой части
        elif num_array[mid] > value:
            right = mid - 1
        # Если целевое значение больше среднего, ищем в правой части
        else:
            left = mid + 1

    # Если значение не найдено, возвращаем индекс, где оно могло бы находиться
    return left


if __name__ == '__main__':
    num_array = [int(_) for _ in input().split()]
    value = int(input())
    result = main(num_array, value)
    print(result)
# Это бинарный поиск