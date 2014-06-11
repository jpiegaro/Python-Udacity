Python 2.7.6 (default, Nov 10 2013, 19:24:24) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def stfind(s):
	if s.find('s') != -1
	
SyntaxError: invalid syntax
>>> 
>>> def stfind(s):
	if s.find('s') != -1:
		return s.find('s')
	else:
		print 'Target string not found.'

>>> stfind('super')
0
>>> stfind('hello')
Target string not found.
>>> def find_last(s1,s2):
    if s1.find(s2) != -1:
        fnd=s1.find(s2)   
        while True:
            fnd=fnd+1
            result = s1.find(s2,fnd)
            if result == -1:
                break
        return fnd-1
    
    else:
        return s1.find(s2)

>>> for i in range (1,10)
SyntaxError: invalid syntax
>>> for i in range(1,10):
	print i

	
1
2
3
4
5
6
7
8
9
>>> def print_multiplication_table(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print i, "*", j, "=", i*j

            
>>> print_multiplication_table(4)
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
4 * 4 = 16
>>> def print_multiplication_table(n):
    i=1
    while i<=n:
        print i,'*',n,'=',i*n
        i=i+1
    i=1
    while n>=i:
        print n,'*',i,'=',n*i
        n=n-1

        
>>> def print_multiplication_table(n):
    i=1
    while i<=n:
        j=1
        while j<=n:
            print str(i) + '*' + str(j) + '=' + str(i*j)
            j=j+1
        i=i+1
