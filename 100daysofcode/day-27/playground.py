def add(*args):     # unlimited arguments
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(2,3,4,5,6,12))

def calculate(n, **kwargs):        # unlimited keyword arguments
    # print(kwargs)
    # for key, val in kwargs.items():
    #     print(key)
    #     print(val)
    n += kwargs['add']
    n *= kwargs['multiply']
    return n

print(calculate(2, add=3, multiply=5))