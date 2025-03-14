numeros = [11, 12, 13, 14, 15]
numpar=[]
numimpar=[]
for numero in numeros:
    if numero % 2 !=0:
        numimpar.append(numero)
    else:
        numpar.append(numero)

print("lista par: ",numpar)
print("lista impar: ",numimpar)
