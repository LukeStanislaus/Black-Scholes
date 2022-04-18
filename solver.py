import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import kde
r=1.004
sigma = 1.007310782
K=19.5
S=20
normn= 100
tau = 1
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

plt.plot(x, y)
plt.title("Density Plot of the data")
plt.show()