#  lambda

# квадрат

# foo = lambda x: x * x
#
# print(foo(4))



#################################################################

# замыкание


# def spam( x, y ):
#     print( 'param1 = {0}, param2 = {1}'.format( x, y ) )
#
# spam1 = lambda x : lambda y : spam( x, y )
#
#
# spam = spam1(10)
# spam(20)
#
# # или
#
# spam1(4)(5)




#############################################################################

# вариант 1

# def main (a, f):
#     return f(a)
#
# foo = lambda x: x * x
#
# print(main(3, foo))


# вариант 2


def main (a, f):
    return f(a)

print(main(4, lambda x: x * x))
