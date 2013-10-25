


n = 15

def mysum(n):
    result = 0
    for i in range (1 , n):
        result = result + i
    return result

def fib(n):
    a, b = 0,1
    while b < n:
        print b,
        a, b = b, a + b

series = "fibonacci"
if (series == "fibonacci"):
    print fib (n)
    
elif (series) == "sum":
    print mysum(n)
else:
    print "not valid"
    
