#function to calculate the sum of any 10 numbers 
def total_of_ten(lst):
    return sum(lst)

#initilising a list to store the 10 numbers to be entered from the keyboard
nums_list = []
for i in range(10):
    num = int(input("enter a number: "))
    nums_list.append(num)


print(f'the sum of these 10 numbers is: {total_of_ten(nums_list)}')