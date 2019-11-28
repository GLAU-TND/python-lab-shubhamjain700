try:
    n=int(input())  # ValueError if we pass any other value except integer
    b=int(input())
    a=input()
    c=n+b
    l=a+b   # TypeEror
    n.append(3)   #AttributeError
except ValueError:
    raise ValueError("Value Error Occured")
except TypeError:
    raise TypeError("Type Error Occured")
except AttributeError:
    raise AttributeError("Attribute Error Occured")
