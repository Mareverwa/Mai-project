# Функцию, которая принимает массив чисел и возвращает количество чисел равных нулю.

def number_of_zeros():
    lst = []
    for i in range(10):
        num = eval(input("введите число: "))
        lst.append(num)
    return len([i for i in lst if i == 0])

print('количество чисел равных нулю - ', number_of_zeros())