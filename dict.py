cities={
    '湖北':{
        '武汉':['武昌','汉口','汉阳'],
        '荆州':['监利','公安','仙桃']
    },
    '江苏':{
        '无锡':['滨湖','崇安','北塘'],
        '南京':['南京1区','南京2区','南京3区']
    }
  }
for i in cities['湖北']:
    print(i)
dict1 = {'a':1,'b':2,'c':3}
dicvalues = dict1.values()
rever = {v : k for k, v in dict1.items()}
print(dict1)
#获取值需要将相应的键放入方括号中
print(dict1['a'])
#获取值需要转换为列表
print(list(dicvalues))
print(rever)