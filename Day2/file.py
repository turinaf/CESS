file = open('sample.txt', 'r')
fileContent = file.read()
# print(fileContent)
fruits = fileContent.splitlines()
# print(fruits)
output = open('output.txt', 'a')
fruits.append('Grapes')
print(fruits)
for fruit in fruits:
    output.write(fruit+'\n')
# output.write(str(fruits))
output.close()