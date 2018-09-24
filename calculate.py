
date = input("请输入一个日期(yyyy-mm-dd)：")
s = date.split('-')
if len(s) != 3:
    exit('日期有误')
for i in s:
    if not is_number(i):
        exit('非法输入')
print(s)
year = int(s[0])
month = int(s[1])
day = int(s[2])
if year > 9999 or year <= 0:
    exit('年份有误')
if month > 12 or month <= 0:
    exit('月份有误')
elif month in [1,3,5,7,8,10,12]:
    if day > 31 or day <= 0:
        exit('天数有误')
elif month in [4,6,9,11]:
    if day > 30 or day <= 0:
        exit('天数有误')
elif month in [2]:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        if day > 29 or day <= 0:
            exit('天数有误')
    else:
        if day > 28 or day <= 0:
            exit('天数有误')
print(year)
print(month)
print(day)
daylist = [31,29,31,30,31,30,31,31,30,31,30,31]
n = 0
sum = 0
if is_leep(year):
    #print('%04d是闰年，2月份有29天。'%year)
    for n in range(month - 1):
        sum += daylist[n]
    #print(sum + day)
else:
    #print('%04d不是闰年，2月份有28天。'%year)
    daylist[1] = 28
    for n in range(month - 1):
        sum += daylist[n]
    #print(sum + day)


def is_leep(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False