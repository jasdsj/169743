a = 'napis'
print(a)
b = 5
c = 5.5
print(b, c)
d = 5+3j
print(d)
e = c+b
print(e)
f = c//b
print(f)
g = c % b
print(g)
h = b**2
print(h)
i = b**1/2
j = pow(b, 1/2)
print(i)
print(j)

print(b)
b += 2
print(b)

listy = ['a', 4 ,5, 6, [1, 2, 3], 5.6]
print(listy)
listy.append(4)
print(listy)
print(listy[5])

lista = [1, 4, 6, 2, 5, 7]
print(lista)

#dodać element o danej pozycji
lista.insert(2, 9)
print(lista)
#dodać kilka elementów
yep = (3, 8)
lista.extend(yep)
print(lista)
#usunąć element o danej pozycji
lista.pop(1)
print(lista)
#usunąć element z listy o danej wartości
lista.remove(1);
print(lista)
#odwrócic elementy listy
lista.reverse()
print(lista)
#zrobić sortwonie
lista.sort()
print(lista)