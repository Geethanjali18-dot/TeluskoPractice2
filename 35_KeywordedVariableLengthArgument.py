def person(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)




person('Geetha',age=30,city="blr",phno=9728990)