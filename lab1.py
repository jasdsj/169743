"""
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

slownik = {'a': 2, 1: 2, 4: 'ab', 1: 3}
print(slownik)
print(slownik[4])
slownik['klucz'] = 'wartosc'
print(slownik)
slownik.pop('klucz')
print(slownik)
print(slownik.keys())
print(slownik.values())

print('a=%(zm)d' % {'zm': 12})
print('a={}, b={}'.format(12, 12))

napis = 'a={}, b={}'
print(napis.format(12, 12))

#if warunek1:
    # instrukcja1
    # instrukcja2
#elif warunek2:
    # instrukcja1
    # instrukcja2
#else:
    # instrukcja1

a = input('podaj a: ')
b = input('podaj b: ')
print(a)
print(b)
print(type(a))
print(type(b))
a = int(a)
b = int(b)
print(type(a))
print(type(b))

if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print('a = b')

a = input('podaj a: ')
b = input('podaj b: ')

if a==b:
    print('liczby są równe')
else:
    print('liczby są różne')

a = input('podaj a: ')
b = input('podaj b: ')
c = input('podaj c: ')
d = input('podaj d: ')
a = int(a)
b = int(b)
c = int(c)
d = int(d)

if (a > b) & (c > d):
    print('a większe od b i c większe od d')
else:
    print('a mniejsze od b lub c mniejsze od d')


#for element in sekwecja:
 #instrukcja1
 #instrukcja2
#else:
 #instrukcja1
 #instrukcja2

for x in range (1, 6, 1):
     print(x)
else:
    print('koniec pętli for')


for x in listy:
    print(x)
"""
listy = ['a', 4, 5, 6, [1, 2, 3], 5.6, 1]

for x in range(0, len(listy)):
    print(listy[x])
