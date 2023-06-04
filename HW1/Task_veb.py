# Нарисовать ёлочку, спросив у пользователя, 
# сколько рядов должно быть у ёлочки 

count_row = int(input("Введите число рядов в треугольнике: "))
count_star = 1
counter = count_row 

while count_star <= count_row*2:
    spase = " "
    star = "*"
    print(spase*counter, star*count_star,end="")
    print("")
    count_star +=2
    counter -= 1

print("=====================================================================")

# Написать порграмму, 
# которая выодит в консоль таблицу умножения 
# "как на тетрадках"

for i in range(2,10):
    for j in range(2,6):
        print(j, "*", i, "=", j*i, end="\t")
    print("")
    
print("")

for i in range(2,10):
    for j in range(6,10):
        print(j, "*", i, "=", j*i, end="\t")
    print("")