#Программа принимает с клавиатуры 3 числа, сравнивает между собой и выводит на экран наибольшее.

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите тритье число: "))

print(max(c, max(a,b)), "наибольшее")
