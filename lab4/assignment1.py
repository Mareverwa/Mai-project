def even(lst):
    evenslst = []
    for i in lst:
        if i % 2 == 0:
            evenslst.append(i)
    
    return evenslst

#test case
print(even(list(range(100))))