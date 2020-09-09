
pos=-1
def search(lst,n):
    l=0
    u=len(lst)-1

    while l<=u:
        mid = (l + u) // 2
        if lst[mid] == n:
            globals()['pos']=mid
            return True
        elif lst[mid] < n:
            l = mid+1

        else:
            u = mid-1
    return False

lst=[4,7,8,12,45,99]
n=10
if search(lst,n):
    print("found at index ",pos+1)
else:
    print("not found")