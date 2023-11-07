def longest_words(file):
    with open(file, 'r') as f:
        text = f.read()

    words = text.split()
    words = [word.strip('.,!?') for word in words]
    max_length = max(len(word) for word in words)
    longest = [word for word in words if len(word) == max_length]
    return longest

result = longest_words("article.pages")#в мене немає txt
print(result)