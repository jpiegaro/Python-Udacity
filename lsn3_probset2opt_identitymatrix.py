def pretest(a):
    for i in a:
        if len(a)!=len(i):
            return False
    return True
  
def pretest2(a):
    if pretest(a)==True:
        n=len(a)
        count=0
        for i in range(n):
            for j in range(n):
				if a[i][j]<0:
                    return False
                count=count+a[i][j]
        if count==n:
            return True
    return False