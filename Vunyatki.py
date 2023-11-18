def processing():
    try:
        value1 = float(input("Введіть перше значення: "))
        value2 = float(input("Введіть друге значення: "))
        result = value1 + value2
    except ValueError:
        value1 = input("Перше значення не є числом. Введіть ще раз: ")
        value2 = input("Друге значення не є числом. Введіть ще раз: ")
        result = value1 + value2

    print("Результат:", result)

processing()