x = int(input()) #número na base 10
y = int(input()) #qualquer base abaixo de 10
z = []
resp = ''

while x//y != 0 or x%y != 0:
    z.append(x%y)
    x = x//y

z.reverse() #comando para inverter a lista e ter a verdadeira resposta na conversão

for i in range(len(z)):
    if z[i] > 9: #para casos até hexadecimal
        if z[i] == 10:
            z[i] = 'A'
        elif z[i] == 11:
            z[i] = 'B'
        elif z[i] == 12:
            z[i] = 'C'
        elif z[i] == 13:
            z[i] == 'D'
        elif z[i] == 14:
            z[i] == 'E'
        elif z[i] == 15:
            z[i] == 'F'
    resp += str(z[i]) #transformando lista para str

print(resp)
