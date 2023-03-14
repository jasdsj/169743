import math
#Zadanie 1
print((math.e)**10)

a = (math.log(5+math.sin(8)**2))

print(pow(a, 1/6))

print(math.floor(3.55))

print(math.ceil(4.80))

#Zadanie 2

imie='JAN'
nazwisko="SWINIARSKI"

imie=imie.lower()
nazwisko=nazwisko.lower()

print(imie.capitalize()+" "+nazwisko.capitalize())

#Zadanie 3

fragment = 'la la la la cos tam tam la na la'
print(fragment.count('la'))


#Zadanie 4

print(imie[1],imie[-1])

#Zadanie 5

string='Yos Yas'
print(string.split())

#Zadanie 6

print("string: {0}, float: {1}, hex: {2:x}".format("string", 0.3, 0x4E8))

#Zadanie 7

ulub = ['siatkowka', 'pilka nozna', 'golf']
print(ulub)

ulub.reverse()
print(ulub)

ulub.append('snooker')
print(ulub)

#zadanie 8

skrt = {'np.': 'na przykład', 'm.in.' : 'między innymi', 'cyt.' : 'cytując'}
print(skrt['np.'])

#zadanie 9

gry = {'lol' : 2700, 'cs:go' : 1000, 'paladins' : 200}
print(len(gry))

#zadanie 10

zdanie=input("Podaj zdanie")

print(zdanie.count('a'))

#zadanie 11

a=input("Podaj a: ")
b=input("Podaj b: ")
c=input("Podaj c: ")

if a>b:
    if a>c:
        print('a Jest największe')
    else:
        print('c jest największe')
elif b>c:
    print('b jest największe')
else:
    print('c jest największe')

#zadanie 12

lis = [1, 1.5, 2, 2.5]

for x in range(len(lis)):
    lis[x] = lis[x]**2

print(lis)

#zadanie 13

dodanie = []
i = 0

while i < 10:
    l = int(input("Podaj liczbe: "))
    if l % 2 == 0:
        dodanie.append(l)
    i += 1
print(dodanie)
