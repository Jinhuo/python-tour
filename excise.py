for n in range(2,20):
    for x in range(2,n):
        if n % x == 0:
            print(n,'equals',x,'*',n//x)
            break
    else:
        print(n,'is a prime number')
def fib(k):
    a , b = 0, 1
    while a < k :
        print(a, end = ",")
        a, b = b, a + b
print(fib(100))
def fib2(k):
    result = []
    a, b = 0, 1
    while a < k:
        result.append(a)
        a, b = b, a + b
    return result
print(fib2(100))
