from random import randint
from time import sleep
maxNum = int(input("Enter the max number you want to play!\n"))
if maxNum < 100:
    exit("The number %d is too smaller, please enter a great one for fun!\n"%max)
target  = randint(1, maxNum)
end = maxNum
print("Game Start....")
sleep(1)
print("Ready for play!!!")
sleep(2)
seed = int(input("Number is between 1  and %d\n" %maxNum))
begin = 1
count = 0

while seed != target:
    count += 1
    if seed > 1 and seed < target:
        begin = seed
        seed = int(input("Number is between %d and %d\n"%(begin, end)))
    elif seed > target:
        end = seed
        seed = int(input("Number is between %d and %d\n"%(begin, end)))
print("Count %d times, You win!!!"%count)