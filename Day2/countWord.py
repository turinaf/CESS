counts = dict()
line = input("Enter a line of text: ")
words = line.split()
print(words)
print('COUNTING...')
      
for word in words:
    counts[word] = counts.get(word,0)+1
print(counts)
