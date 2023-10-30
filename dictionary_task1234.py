import random
#task1
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
result = {**dictionary_1, **dictionary_2}
print(result)
#task2
ran_dict = {f'key{i}': random.randint(1,10)
         for i in range(20)}
result = 1
for value in ran_dict.values():
    result*=value

print(ran_dict)
print(result)
#task3
dict3 = {x: x**3 for x in range(1,11)}
print(dict3)
#task4
a = ['a', 'b', 'c']
b = [1, 2, 3]
res4 = dict(zip(a,b))
print(res4)