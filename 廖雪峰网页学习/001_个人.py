h = 1
while h < 10:
    l = 1
    while l <= h:
        print(f'{l}*{h}={h*l}',end='\t')
        l += 1
    print()
    h += 1
