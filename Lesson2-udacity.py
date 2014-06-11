# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a,b,c):
    if biggest(a,b,c) == a:
        if bigger(b,c) == b:
            return b
        else:
            return c
    else:
        if bigger(b,c) == b:
            if bigger(a,c) == a:
                return a
            else:
                return c
        else:
            if bigger(b,c) == c:
                if bigger (a,b) == b:
                    return b
                else:
                    return a

    

#Test runs shown below with expected answers

print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7
