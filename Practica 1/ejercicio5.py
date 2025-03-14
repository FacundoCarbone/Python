numeros= []

while True:
    num=float(input('INTRODUCE UN NUMERO: '))

    if(num < 0):
        break

    numeros.append(num)
print('Lista',numeros)

