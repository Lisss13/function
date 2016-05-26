# к 4.pu
def func (array, f , ff):
    array1 = list(filter(f, array))
    return list(filter(ff, array1))

a = lambda x: x > 0
b = lambda y: y % 2 == 0

print(func(array, a, b))
