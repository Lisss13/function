# замыкание

# def foo (x):
#     def doo(y):
#         return x + y
#     return doo
#
# a = foo(5)
#
# print(a(2), a(10))

# ################################################################


# def f (x = 0):
#     def ff(*array):
#         array = [c * x for c in array]
#         return array
#     return ff
#
#
# plus = f(10)
#
# print(plus(1,2,3,4,5,6,7))

##########################################################################

# # второй вариант замыкания

# n = 3
# def foo( k, mul = n ):
#     return mul * k
#
# n = 7
# print( foo( 3 ) )
# n = 13
# print( foo( 5 ) )


##############################################



# псевдо случайные числа




# реализовать






##########################################################################

# карринг

def spam( x, y ):
    print( 'param1 = {0}, param2 = {1}'.format( x, y ) )


def spam2( x ) :
    def new_spam( y ) :
        return spam( x, y )
    return new_spam

spam2( 2 )( 3 )
