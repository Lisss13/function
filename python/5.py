# ускорение

# a = 0
#
# for i in range(1,100):
#     a += i
#
# print(a)

##################################################################################3

# def ffor (start, stop):
#     if start >= stop:
#         return start
#     else:
#         return ffor(start + 1, stop)
#
# print(ffor(1,100))


######################################################################################

def myfor (start, stop, acc = 0):
    if start >= stop:
        return acc
    else:
        acc += start
        return myfor(start + 1, stop, acc)

print(myfor(1, 100))


# def myfor(start, stop, func, step = 1, rung = 0)
# 	if start >= stop
# 		puts func.call(start, rung)
# 	else
# 		puts func.call(start, rung)
# 		myfor(start + step, stop, func)
# 	end
# end
#
# fun = -> (a, b) { a ** b }
#
# func = -> (x, y = 0) {
# 	if y == 50
# 		puts fun.call(x, y)
# 	else
# 		puts fun.call(x, y)
# 		func.call(x, y + 1)
# 	end
# }



###################################################################################

# практика


###################################################################################


def sumGenerator(fun):
    return lambda a, b: sum(a, b, fun)

def sum(a, b, fun):
    if a > b:
        return 0
    else:
        return fun(a) + sum(a + 1, b, fun)

sunInter = sumGenerator(lambda x: x + x)

print(sunInter(1,100))
