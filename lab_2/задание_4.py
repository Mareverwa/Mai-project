#Программа принимает с клавиатуры 3 числа и выводит на экран количество уникальных чисел.
a = int(input("Введите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))

v=0
if a==b:
    v=v+1
else:
    v=v+2
if a==c or c==b:
    v=v+0
else:
    v=v+1


print("количество уникальных чисел : ", v)