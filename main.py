a = input('Podaj wartość a funkcji')
b = input('Podaj wartość b funkcji')
c = input('Podaj wartość c funkcji')
print('Twoja funkcja ma postać: ' + a + "x^2" + " + " + b + "x" + " + " + c)
if int(a) > 0:
    print("Funkcja jest rosnąca")
elif int(a) == 0:
    print("Funkcja jest stała")
elif int(a) < 0:
    print("Funkcja jest malejąca")
delta = int(b)**2 - 4 * int(a) * int(c)
print("Delta funkcji wynosi:" + str(delta))
x1 = (-int(b) - delta) / (2 * int(a))
x2 = (-int(b) + delta) / (2 * int(a))
x3 = (-int(b) / (2*int(a)))
if int(delta) > 0:
    print("Funkcja ma dwa miejsca zerowe: " + str(x1) + ", " + str(x2))
elif int(delta) == 0:
    print("Funkcja ma jedno miejsce zerowe: " + x3)
else:
    print("Funkcja nie ma miejsc zerowych")
p = -int(b) / (2 * int(a))
q = -int(delta) / (4*int(a))
kanoniczna = "f(x) = " + str(a) + "(" + "x - " + str(p)  + ")^2 " +  "+ " + str(q) + ")"
print("Postać kanoniczna funkcji wynosi: " + str(kanoniczna))
iloczynowa = "f(x) = " + str(a) + "(x - " + str(x1) + ")(x - " + str(x2) + ")"
print("Postać iloczynowa funkcji wynosi: " + iloczynowa)