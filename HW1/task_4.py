#Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
#должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
#числа используйте код:
#from random import randint
#num = randint(LOWER_LIMIT, UPPER_LIMIT) 

from random import randint
print("попробуйте угадать число от 0 до 1000 за 10 попыток ")
number_rnd = randint(0, 1000)
my_number = 0
attempts = 10
while True:
    if attempts == 0:
        print(f"К сожалению попытки закончились!рандомным числом являлось число: {number_rnd}")
        break
    my_number = int(input("введите число: "))
    attempts -=1
    print(f"попыток осталось: {attempts}")
    if my_number < number_rnd:
        print("Ваше число меньше рандомного ")
    elif my_number > number_rnd:
        print("Ваше число больше рандомного")
    elif my_number == number_rnd:
        print("вы угадали ранломное число!")
        break
   

    

