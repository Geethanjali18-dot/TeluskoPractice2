data={1:'Geetha',2:'Seetha',4:'Harshita'}
print(data)
print(data[1])
print(data.get(1))
print(data.keys())
print(data.get(1,'Not found'))
print(data.get(3,'Not found'))
keys=['Geetha','Seetha','Neetha']
values=['Python','Java','C']
data=dict(zip(keys,values))
print(data)
print(data['Geetha'])
data['Kiran']='C#'
print(data)
prog={'JS':'Atom','CS':'VS','Python':['Pycharm','Sublime'],'Java':{'JEE':'Eclipse','JAVA SE':'Netbeans'}}
print(prog['JS'])
print(prog['Python'][1])
print(prog['Java'])
print(prog['Java']['JAVA SE'])
