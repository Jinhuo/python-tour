list = [1,2,3,4]
tt = iter(list)
import sys
for x in tt:
    print(x,end = ",")
while True:
    try:
        print(next(tt))
    except StopIteration:
        sys.exit()
