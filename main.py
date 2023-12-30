x = int(input("Введіть число:"))
y = int(input("Введіть те саме число ще раз:"))

i = j = 0
while i < y:
    j = 0
    while j < x:
        if i > j:
            print(f'[{i},{j}]', end=' ')
        else:
            print(f'     ', end=' ')
        j += 1
    print()
    i += 1