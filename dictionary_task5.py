text = ('Python is good language to learn and in same time we '
        'like to tell that it is cool expereance for us')
count = {}

for letter in text:
    if letter.isalpha():
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

print(count)