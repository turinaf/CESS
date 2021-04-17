fname = input("Enter file name: ")
try:
    fhand = open(fname, 'r')
except:
    print('Cannot open the file: ', fname)
    quit()
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
      counts[word] = counts.get(word, 0)+1
bigcount = 0
bigword =  None
for jecha, count in counts.items():
    if bigcount < count or bigword is None:
        bigcount = count
        bigword = jecha
    print(jecha, count)

print("The most frequent word is:\n", bigword, bigcount)
