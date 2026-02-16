y = 1

def hello() -> str:
    global y
    y = 2
    print(y)
    return 'Hello World'

x = hello()
print(y)
print(x)