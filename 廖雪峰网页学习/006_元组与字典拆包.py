def return_num():
    return 1, 2


a, b = return_num()
print(f'{a}\t{b}')


dict1 = {'name': 'K', 'age': 20}
c, d = dict1
print(f'{c}\t{d}')
print(f'{dict1[c]}\t{dict1[d]}')