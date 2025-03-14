entrada=input('Ingrese los numeros separados por un espacio')
numeros=list(map(int,entrada.split()))
numeros_filtrados=[str(num)for num in numeros if num % 3 !=0]
resultado='-'.join(numeros_filtrados)
print('Resultado final',resultado)