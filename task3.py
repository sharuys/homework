import random

mnozhina = set(random.sample(range(1, 101), 15))

par = {num for num in mnozhina if num % 2 == 0}
nepar = {num for num in mnozhina if num % 2 != 0}

sum_par = sum(par)
sum_nepar = sum(nepar)

result = "Так" if sum_nepar > sum_par else "Hi"
print(result)