def sudoku(a):
	#***this procedure will not differentiate values from the input list (integer vs. non-integer).
	n=len(a)
	b=1
	main=[]
	while b<=n:
		main.append(b)
		b+=1
	return main

def transpose(a):
	n=len(a)
	trans=a
	for i in range(n):
		for j in range(n):
			trans[i][j] = trans[j][i]
	return trans
	
def check_sudoku(a):
	test = sudoku(a)
	for e in a:
		if set(e)==set(test):
			return True
	for f in transpose(a):
		if set(f)==set(test):
			return True
	return False
		
case1=[[0,1,2],[1,2,3],[2,3,1]]
case2=[[0,1,2],[0,1,2],[0,1,2]]

def intTest(a):  #this procedure needs to be reworked
	test=sudoku(a) #problem with sudoku procedure not recognizing non-integer values.
	for e in test:
		if e not in [1,2,3,4,5,6,7,8,9]:
			return False
	return True