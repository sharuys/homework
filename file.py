#task1
with open('output.txt', 'w') as file:
    while True:
        inputus = input("Введіть ярдок")
        if not inputus:
            break
        file.write(inputus + '\n')

