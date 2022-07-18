t1 = 0
t2 = 1
t3 = t1 + t2
cont = 3
v = False

n = int(input('Qual o seu número? '))

if n >= t3:
    print(f'{t1} - {t2}', end='')

if n == t1:
    print(f'{t1}')
    v = True

while t3 <= n:
    print(f' - {t3}', end='')
    t1 = t2
    t2 = t3
    if n == t3:
        v = True
    t3 = t2 + t1
    cont += 1

if v == True:
    print(f'\nO número {n} está na sequência de Fibonacci!')
else:
    print(f'\nO número {n} não está na sequência de Fibonacci!')





