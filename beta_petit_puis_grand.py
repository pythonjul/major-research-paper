import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
#from ipywidgets import interact, fixed

'''
But: créer un graphe avec une valeur beta qui change au cours du temps.
    in: valeur de beta, gamma, et conditions initiales
    out:deux graphes concaténés ensembles
'''

Z=[0,0,0,0,0]
beta1=0.3
beta2=0.5

def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

T1=np.linspace(0, 50)
T2=np.linspace(50, 100)

N, R0, I0,S0,beta,gamma,t=100,0,.01,99.99,beta1,0.035,T1
# cond. init.
y0 = S0, I0, R0
# integre sir sur t
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T
# affiche S,I et R
Z=[S[-1],I[-1],R[-1],beta,gamma]

N, R0, I0,S0,beta,gamma,t=100,Z[2],Z[1],Z[0],beta2,0.035,T2
# cond. init.
y0 = S0, I0, R0
# integre sir sur t
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S2, I2, R2 = ret.T

S=np.concatenate((S,S2))
I=np.concatenate((I,I2))
R=np.concatenate((R,R2))
t=np.concatenate((T1,T2))


fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111,  axisbelow=True)
ax.plot(t, S/100, 'b', alpha=0.5, lw=2, label='S')
ax.plot(t, I/100, 'r', alpha=0.5, lw=2, label='I')
ax.plot(t, R/100, 'g', alpha=0.5, lw=2, label='R')
ax.set_xlabel('temps')
ax.set_ylabel('population')
ax.set_ylim(-0.01,1.01)

legend = ax.legend()
legend.get_frame().set_alpha(0.5)
plt.title('\u03B2={}, \u03B3={} puis \u03B2={}, \u03B3={}'.format(beta1,gamma,beta2,gamma) )
plt.show()
#fig.savefig('SIR_2_differents_beta_1.png'.format(beta,gamma))

print([S2[-1],I2[-1],R2[-1]])
