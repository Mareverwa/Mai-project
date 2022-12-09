n=int(input("Ввыдите лубое число, n: "))
for i in range (1, n + 1):
    spaces = '' * (n - i)
    for j in range(1,i+1):
        spaces += str(j)  
   
    print(spaces)