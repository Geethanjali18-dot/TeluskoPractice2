def selectionSort(lst):
    for i in range(len(lst)):
        minpos=i
        for j in range(i,6):
            if lst[j]<lst[minpos]:
                minpos=j
        temp=lst[i]
        lst[i]=lst[minpos]
        lst[minpos]=temp
        print(lst)




lst=[5,3,8,6,7,2]
print(selectionSort(lst))