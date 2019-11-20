from collections import Counter


a = Counter()
x = 'ajhdgahsgdjahsgjdhagv'
for i in x:
    a[i] += 1
b = Counter()
for q in 'ajhdgahsgdjahsgj':
    b[q] += 1
print(a)
print(b)

