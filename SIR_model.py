import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

'''
But: afficher un modèle SIR
    in: N, R0, I0, S0, beta, gamma: paramètres du modèle SIR
        T: l'intervalle de temps souhaité
    out: les valeurs des fonctions S, I et R ainsi que le graphe SIR correspondant
'''

# Définition de l'équation différentielle pour le modèle SIR
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

def f(N, R0, I0,S0,beta,gamma,t):
    # Conditions initiales
    y0 = S0, I0, R0

    # Résoud l'équation différentielle en utilisant LSODA de la libraire Fortran
    ret = odeint(deriv, y0, t, args=(N, beta, gamma))
    S, I, R = ret.T

    # Afficher le graphe
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
    plt.title('\u03B2={}, \u03B3={}'.format(beta,gamma) )
    plt.show()
    #fig.savefig('SIR_ex_beta{}_gamma{}.png'.format(beta,gamma))

#Le array du temps
T=np.linspace(0, 250, 250)

#Execution de la fonction
f(100,0,.01,99.99,0.3,0.2,T)