#bubble sort
'''n = len(lst) - 1
for i in range(0, n):
    for d in range(n, i, -1):
        if lst[d] < lst[d-1]:
            lst[d], lst[d - 1] = lst[d - 1], lst[d]
print(lst)'''

lst = [12,11,1,2,2,4,56,44,23,22,11,2,3,5]
for i in range (1, len(lst)):
    temp = lst[i]
    j = i-1
    while j >= 0 and lst[j] > temp:
        lst[j+1] = [j]
        j = j-1
        lst[j+1] = temp
    print(lst)
