import random

int_elements = [random.randint(1, 500) for _ in range(25)]
print(int_elements)

squared_elements = [x ** 2 for x in int_elements]
print(squared_elements)

remainder_11_elements = [x % 11 for x in int_elements]
print(remainder_11_elements)

par_elements = [x for x in int_elements if x % 2 == 0]
print(par_elements)

nepar_elements = [x for x in int_elements if len(str(x)) % 2 != 0]
print(nepar_elements)

non_multiple_3_elements = [int_elements[i] for i in range(len(int_elements)) if i % 3 != 0]
print(non_multiple_3_elements)