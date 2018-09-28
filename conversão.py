base10 = int(input()) #número na base 10
newbase = int(input()) #qualquer base até 16
lista = []
resp = ''

while base10//newbase != 0 or base10%newbase != 0:
    lista.append(base10%newbase)
    base10 = base10//newbase

lista.reverse() #comando para inverter a lista e ter a verdadeira resposta na conversão

for i in range(len(lista)):
    if lista[i] > 9: #para casos até hexadecimal
        if lista[i] == 10:
            lista[i] = 'A'
        elif lista[i] == 11:
            lista[i] = 'B'
        elif lista[i] == 12:
            lista[i] = 'C'
        elif lista[i] == 13:
            lista[i] == 'D'
        elif lista[i] == 14:
            lista[i] == 'E'
        elif lista[i] == 15:
            lista[i] == 'F'
    resp += str(lista[i]) #transformando lista para str

print(resp)
