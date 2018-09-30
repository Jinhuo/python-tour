import re
str1 = 'jy is a smart student'
text1 = re.match('jy',str1)
print(text1.group())
text2 = re.search('mar',str1).span() #span()返回元组（开始，结束）位置
print(text2)
text3 = re.compile(r'\w*s\w')
print(re.findall(r'\w*s\w',str1))
print(text3.findall(str1))
str2 = 'one1two2three3four4five'
print(re.split(r'\d+',str2))  # 按数字分割字符串返回列表
text4 = re.compile(r'\d{3}-\d{6}')
print(text4.findall('010-628888'))