import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

'''
But: afficher un modèle SEIR
    in: N, R0, E0, I0, S0, beta, gamma: paramètres du modèle SIR
        T: l'intervalle de temps souhaité
    out: les valeurs des fonctions S, E, I et R ainsi que le graphe SEIR correspondant
'''

# Définition de l'équation différentielle pour le modèle SEIR
def deriv(y, t, N, beta,sigma, gamma):
    S, E,I, R = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - sigma*E
    dIdt = sigma*E - gamma * I
    dRdt = gamma * I
    return dSdt,dEdt, dIdt, dRdt

def function_SEIR(N, R0, E0,I0,S0,beta,sigma,gamma,t):
    # Conditions initiales
    y0 = S0, E0, I0, R0

    # Résoud l'équation différentielle en utilisant LSODA de la libraire Fortran
    ret = odeint(deriv, y0, t, args=(N, beta,sigma, gamma))
    S, E,I, R = ret.T

    # Afficher le graphe
    fig = plt.figure(facecolor='w')
    ax = fig.add_subplot(111,  axisbelow=True)
    ax.plot(t, S/100, 'b', alpha=0.5, lw=2, label='S')
    ax.plot(t, E/100, 'gray', alpha=0.5, lw=2, label='E')
    ax.plot(t, I/100, 'r', alpha=0.5, lw=2, label='I')
    ax.plot(t, R/100, 'g', alpha=0.5, lw=2, label='R')
    ax.set_xlabel('temps')
    ax.set_ylabel('population')
    ax.set_ylim(-0.01,1.01)
    legend = ax.legend()
    legend.get_frame().set_alpha(0.5)
    plt.title('SEIR, \u03B2=0.2, \u03C3=0.2 et \u03B3=0.07 ')
    plt.show()

#Le array du temps
T=np.linspace(0, 220, 220)

#Execution de la fonction
function_SEIR(100,0,.01,0,99.95,0.2,0.2,0.07,T)