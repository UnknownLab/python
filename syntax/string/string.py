words = 'Hello World'
letter = words[1]

print(letter)
print(len(words))

# index = 0
# while index < len(fruit):
#     letter = fruit[index]
#     print(letter)
#     index = index + 1

for letter in words:
    print(letter)

print(words[0:5])
print(words[6:12])

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return - 1

print(find(words, 'l'))
print(words.upper())
print(words.find('l'))
print('Hell' in words)

def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)

in_both('Hello','Hell')