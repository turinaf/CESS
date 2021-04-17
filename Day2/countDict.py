counts = dict()
names = ['Turi', 'Turi',  'Turi', 'Turi', 'Bona', 'Magarsa', 'Magartu', 'Magartu', 'Magarsa', 'Magarsa']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name]+1
print(counts)
