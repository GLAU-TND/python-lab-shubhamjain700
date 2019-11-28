class Myexception(Exception):
    pass
def xyz(a,b):
        c=a+b
        if(c<150):
            raise Myexception("Custom ExceptionOccur")
        else:
            print("Sum is " + str(c))


a=int(input())
b=int(input())
xyz(a,b)


