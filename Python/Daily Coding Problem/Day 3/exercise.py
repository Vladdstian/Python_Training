#solution not made by me- I was intrigued by this and had to search for it. If someone coud explain in more details please do so

def cons(a,b):
    def pair(f):
        return f(a,b)
    return pair

def car(cons):
    return cons(lambda a,b: a)

def cdr(cons):
    return cons(lambda a,b: b)

print(car(cons(3,4)))
print(cdr(cons(3,4)))

# ============================================== explaining each line of code with apple analogy ==========================
# define the cons function that takes two arguments and returns a pair
def cons(a,b):
    # define the pair function that takes a single argument (a function f)
    # and returns the result of calling f with the arguments a and b
    def pair(f):
        return f(a,b)
    return pair

# define the car function that takes a pair and returns the first value
def car(cons):
    # call the cons function with a lambda function that takes two arguments
    # and returns the first argument (a)
    return cons(lambda a,b: a)

# define the cdr function that takes a pair and returns the second value
def cdr(cons):
    # call the cons function with a lambda function that takes two arguments
    # and returns the second argument (b)
    return cons(lambda a,b: b)

# example usage
# create a pair that contains two apples
my_pair = cons('apple', 'apple')

# get the first value from the pair, which is 'apple'
print(car(my_pair))

# get the second value from the pair, which is 'apple'
print(cdr(my_pair))



Explanation:

Lines 2-5: The cons function is used to create a pair of two values. The pair function is defined to take a single argument f, which is a function that is then called with the arguments a and b. The result of calling f with a and b is returned by the pair function.
Lines 7-9: The car function is used to get the first value of a pair. It calls the cons function with a lambda function that takes two arguments and returns the first argument a.
Lines 11-13: The cdr function is used to get the second value of a pair. It calls the cons function with a lambda function that takes two arguments and returns the second argument b.
Lines 16-19: An example usage of the cons, car, and cdr functions is shown by creating a pair that contains two apples. The car and cdr functions are then called on the pair to retrieve the first and second values, respectively.
