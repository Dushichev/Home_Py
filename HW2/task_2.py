#Напишите программу, которая принимает две строки вида “a/b” -
#дробь с числителем и знаменателем. Программа должна возвращать
#сумму и произведение* дробей. 
#Для проверки своего кода используйте модуль fraction

import fractions

line1 = input("Введите числитель первой дроби ")
line2 = input("Введите знаменатель первой дроби ")
number1 = int(line1)
number2 = int(line2)

line3 =input("Введите числитель второй дроби ")
line4 = input("Введите знаменатель второй дроби ")
number3 = int(line3)
number4 = int(line4)


res1 = (number1 / number2 ) + (number3 / number4)
res2 = (number1 / number2 ) * (number3 / number4)
print(res1)
print(res2)
fraction1 = fractions.Fraction(number1, number2)
fraction2 = fractions.Fraction(number3, number4)
res3 = fraction1 + fraction2
res4 = fraction1 * fraction2
print(res3)
print(res4)