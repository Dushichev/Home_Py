#2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
#Дано a, b, c - стороны предполагаемого треугольника.
#Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
#Если хотя бы в одном случае отрезок окажется больше суммы двух других, 
#то треугольника с такими сторонами не существует. 
#Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a = int(input("Введите длинну стороны треугольника - a: "))
b = int(input("Введите длинну стороны треугольника - b: "))
c = int(input("Введите длинну стороны треугольника - c: ")) 

if a < b+c and b < a+c and c < a+b:
    print("Такой треугольник существует", end=" ")
    if a==b and a==c:
        print("и он явояется равносторонним!")
    elif a == b or a == c or a == c:
        print("и он является равнобедренным!")
    else:
        print("и он является разносторонним")
else:
    print("такого треугольника не существует") 