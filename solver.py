import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import stats
def blackscholes(r,sigma,K,S,normn,tau):
    x = math.log(S/K) + (r - 1/2*math.pow(sigma,2))*tau
    d1 = np.random.normal(0, (1/(sigma * math.sqrt(tau)))*
        ((x + 1/2 * math.pow(sigma,2) * tau ) + 1/2 * math.pow(sigma,2) + tau), normn)
    d2 = np.random.normal(0, (1/(sigma * math.sqrt(tau)))*
        ((x + 1/2 * math.pow(sigma,2) * tau ) - 1/2 * math.pow(sigma,2) + tau),normn)

    def u(x,tau, d1, d2):
        return K*math.pow(math.e,x + 1/2 * math.pow(sigma,2)*tau)*d1 - K*d2
    data = [0]*normn
    for i in range(normn):
        data[i] =u(x, tau, d1[i], d2[i])/math.pow(math.e, r*tau)

    density = stats.gaussian_kde(data)
    x = np.linspace(-100,100,300)
    y=density(x)
    return (x,y)




r=1.004
sigma = 1.007310782
K=19.5
S=20
normn= 10000
tau = 1
maxsigma = math.sqrt(((2/tau)*math.log(S/K) + 2*r))
handles= [0]*10
for i in range(10,110, 10):
    sigmaVar= maxsigma*i/100
    x = math.log(S/K) + (r - 1/2*math.pow(0,2))
    (x,y) = blackscholes(r, sigmaVar, K, S, normn, tau)
    handles[int(i/10 -1)], = plt.plot(x, y, str((i+10)/110), label=str(round(sigmaVar,2)))
    # increasing sigma = more white
    
    plt.title("Density Plot of C with different values of σ")
plt.legend(handles = handles, title="Value of σ")
plt.savefig("sigmavalue.png")
maxK = S * math.pow(math.e, (1/2)* math.pow(sigma, 2) - r)
for i in range(10,110, 10):
    kVar=maxK * i/100
    (x,y) = blackscholes(r, sigma, kVar, S, normn, tau)

    handles[int(i/10 -1)], = plt.plot(x, y, str((i+10)/110), label=str(round(kVar,2)))


    plt.title("Density Plot of C with different values of k")
plt.legend(handles = handles, title = "Values of strike K")
plt.savefig("kvalue.png")
maxTau = (math.log(K/S,math.e))/(r-1/2*math.pow(sigma,2))
print(maxTau)
for i in range(10,110, 10):
    tauVar=abs(maxTau * i)
    (x,y) = blackscholes(r, sigma, K, S, normn, tauVar)

    handles[int(i/10 -1)], = plt.plot(x, y, str((i+10)/110), label= str(round(tauVar,2)))


    plt.title("Density Plot of C with different values of τ")
plt.legend(handles = handles, title= "Values of τ")
plt.savefig("tauvalue.png")