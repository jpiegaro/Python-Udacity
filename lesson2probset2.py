Python 2.7.6 (default, Nov 10 2013, 19:24:24) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 29/5
5
>>> 30/5
6
>>> print 29/5
5
>>> 8/5
1
>>> 8.0/5
1.6
>>> ================================ RESTART ================================
>>> # Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required 
# to make up that value. The return value should be a tuple of three numbers 
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as 
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as 
# needed to make up the total.
#
# (No fair for USians to just say use a "Forever" stamp and be done with it!)
#

def stamps(n):
    a=5
    b=2
    c=1
    t1=n/a
    t1a=n-(t1*a)
    t2=t1a/b
    t2a=t1a-(t2*b)
    t3=t2a/c
    
    return t1,t2,t3


print stamps(8)
#>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
print stamps(5)
#>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
print stamps(29)
#>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and no 1p stamps
print stamps(0)
#>>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps
