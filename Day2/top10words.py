# A program to find top 10 repeatedly found words on the words.txt
fhand = open('words.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0)+1
lst = list()
for key, val in counts.items():
    newTuple = (val, key)
    lst.append(newTuple)
# Sort the list of tuples in lst.
lst = sorted(lst, reverse=True)
print('Top 10 common words are\n')
for val, key in lst[:10]:
    print(key,'\t', val)
