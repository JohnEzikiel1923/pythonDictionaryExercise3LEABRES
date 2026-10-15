word = open('mbox-short.txt')
words_list = dict()

for line in word:
    if line.startswith('From '):
        email = line.split()[1]
        words_list[email] = words_list.get(email, 0) + 1

print(words_list)
