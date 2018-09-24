from sys import argv
#get the scripts name and arguments 
print(argv)
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
number_one = argv[1]
if not is_number(number_one):
    exit('invalid number one')
else:
    number_one = float(number_one)
symbo = argv[2]
number_two = argv[3]
if not is_number(number_two):
    exit('invalid number two')
else:
    number_two = float(number_two)
print(number_two)
if symbo == '+':
    result = number_one + number_two
elif symbo == '-':
    result = number_one - number_two
elif symbo == '*':
    result = number_one * number_two
elif symbo == '/':
    if number_two == 0:
        exit('invalid number two')
    result = number_one / number_two
print(result)