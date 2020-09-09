#compiletime error
#logical error
#Runtime error

a=5
b=2
#b=0

try:
    print("resource open")
    print(a/b) #critical statemnt
    k=int(input("Enter a number"))
    print(k)
except ZeroDivisionError as e:
    print("can not divide by 0 ",e)
except ValueError as e:
    print("Invalid input ", e)
except Exception:
    print("General")
finally:
    print("resource closed")
    print("bye")