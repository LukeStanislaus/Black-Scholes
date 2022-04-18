import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import kde
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

    density = kde.gaussian_kde(data)
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
sigmaplot= 0
for i in range(10,100, 10):
    sigmaVar= maxsigma*i/100
    x = math.log(S/K) + (r - 1/2*math.pow(0,2))
    (x,y) = blackscholes(r, sigmaVar, K, S, normn, tau)
    
    if(i==10 or 100):
        sigmaplot = plt.plot(x, y, str(i/100), label=("sigma = " + str(sigmaVar)))

    else:
        sigmaplot = plt.plot(x, y, str(i/100))
    # increasing sigma = more white
    
    plt.title("Density Plot of C with different values of sigma")
plt.legend(["sigma=0", "sigma= "+str(maxsigma)])
plt.savefig("sigmavalue.png")
plt.show()

for i in range(10,100, 10):
    (x,y) = blackscholes(r, sigma, i, S, normn, tau)
    
    if(i==10 or 100):
        sigmaplot = plt.plot(x, y, str(i/100), label=("k = " + str(i)))

    else:
        sigmaplot = plt.plot(x, y, str(i/100))
    # increasing sigma = more white
    
    plt.title("Density Plot of C with different values of k")
plt.legend(["k=0", "k= "+str(100)])
plt.savefig("kvalue.png")
plt.show()