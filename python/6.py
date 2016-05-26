def myArray(*array):
    def f(method, i = 0):
        if method == "take":
            return array[i]
        elif method == "len":
            return len(array)
        elif "range":
            if (len(array) > 1):
                return list(range(array[0], array[-1] + 1))
            else:
                return list(range(1, array[0] + 1))
        else:
            print("Ошибка")
    return f

def Take(pair, i = 0):
    return pair("take", i)

def Len(pair):
    return pair("len")

def myRange(pair):
    return pair("range")

a = myArray(1,2,3,4,5,6,7)
# print(a)
print(Len(a))

print(Take(a, 3))


w = myArray(1, 10)
q = myArray(10)

print(myRange(w))
print(myRange(q))
