import numpy as np
import time



def multiplication(A,sol):
    x=np.zeros(len(A))
    for i in range(len(A)):
        for j in range(len(A[0])):
            x[i]+=A[i][j]*sol[j]

    return x

def distance(x,B):
    d=[]
    for i in range(len(x)):
        d.append(abs(x[i]-B[i])/abs(B[i]))
    print(np.array(d))



def GaussReduction(Aaug):
    n = len(Aaug)
    L = []
    for j in range(n):
        for i in range(j + 1, n):
            c = Aaug[i][j] / Aaug[j][j]
            Aaug[i] = Aaug[i] - c * Aaug[j]
    return Aaug


def SolveUppTriSyst(Taug):

    n=len(Taug)
    x=np.zeros(n)
    for i in range(1,n+1):
        x[n-i]=Taug[n-i][n]/Taug[n-i][n-i]
        for j in range(1,i):
            x[n-i]-=Taug[n-i][n-j]/Taug[n-i][n-i]*x[n-j]
    return x

def Gauss(A,B):
    l=[]
    for i in range(len(A)):

        l.append(np.append(A[i],B[i]))

    Aprime=np.array(l)

    Taug=GaussReduction(Aprime)
    sol=SolveUppTriSyst(Taug)
    x=multiplication(A,sol)
    distance(x,B)




#A=np.array([[1,2,3],[-4,-9,9],[8,0,1]])
#B=np.array([[-3],[-1],[2]])
times=[]
list=[10,100,500]
for i in list:
    A=np.random.rand(i,i)
    B=np.random.rand(i,1)
    start_time=time.time()
    Gauss(A,B)
    times.append(time.time() - start_time)




import matplotlib.pyplot as plt

x = np.array(['10x10', '100x100', '500x500'])
y=np.array(times)
plt.bar(x,y)
plt.show()