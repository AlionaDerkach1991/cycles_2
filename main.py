x = int(input("Введіть непарне число:"))
y = int(input("Введіть те саме число ще раз:"))
#Щоб вийшла рівнобічна фігура спочатку має бути квадрат

i = j = 0
while i < y:
    j = 0
    while j < x:
        if j <= int(x/2):
            if i <= j:
                print(f'[{i},{j}]', end=' ')
            else:
                print(f'     ', end=' ')
        else:
            if i + j <= y - 1:
                print(f'[{i},{j}]', end=' ')
            else:
                print(f'     ', end=' ')
        j += 1
    print()
    i += 1