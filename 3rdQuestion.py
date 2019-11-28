try:
    n=int(input())

except ValueError:
    raise ValueError("Value Error Occured")
except EOFError:
    raise  EOFError("End of file Error")
except KeyboardInterrupt:
    raise KeyboardInterrupt("Keyboard interupt occured")