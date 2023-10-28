def has_pair(list1, random_num):
    numbers = {}
    for num in list1:
        dif = random_num - num
        if dif in numbers:
            return True
        numbers[num] = True
    return False
list1 = [1, 2, 3, 4, 5]
random_num = 3
print(has_pair(list1, random_num))

