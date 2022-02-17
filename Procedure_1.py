import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from scipy import integrate, optimize
from scipy.integrate import odeint

'''
But: calculer les paramètres beta sigma gamma S_0 E_0 avec P1 pour un pays donné.

  in: tableau des infections recencées, (pathfile à changer pour exécution du programme)
      pays, intervalle de dates, 
      population du pays, estimation des paramètres beta-sigma-gamma
  out:retourne les paramètres beta sigma gamma pour la procédure 1
'''

# Partie 1: SEIR modèle avec équation différentielles
def deriv(y, t, N, beta,sigma, gamma):
    S, E,I, R = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - sigma*E
    dIdt = sigma*E - gamma * I
    dRdt = gamma * I
    return dSdt,dEdt, dIdt, dRdt

def function_SEIR(N, R0, E0,I0,S0,beta,sigma,gamma,t,date_depart): #fct SEIR et Printing graph
    # conditions initiales
    y0 = S0, E0, I0, R0
    T=len(t)
    arr_T=pd.date_range(start=date_depart, periods=T)
    # intègre les équation SIR sur l'intervalle de temps T.
    ret = odeint(deriv, y0, t, args=(N, beta,sigma, gamma))
    S,E,I,R = ret.T
    global SEIR_val
    SEIR_val=[S[-1],E[-1],I[-1],R[-1]]
    # affichage du graphe pour S,E,I et R
    fig = plt.figure(facecolor='w')
    ax = fig.add_subplot(111,  axisbelow=True)
    ax.plot(arr_T, S, 'b', alpha=0.5, lw=2, label='S')
    ax.plot(arr_T, E, 'gray', alpha=0.5, lw=2, label='E')
    ax.plot(arr_T, I, 'r', alpha=0.5, lw=2, label='I')
    ax.plot(arr_T, R, 'g', alpha=0.5, lw=2, label='R')
    ax.set_xlabel('temps')
    ax.set_ylabel('population')
    ax.set_ylim(-0.01,1.01)
    legend = ax.legend()
    legend.get_frame().set_alpha(0.5)
    plt.title('SEIR correspondant pour un interval de {} jours'.format(T))
    plt.gcf().autofmt_xdate(rotation=50)
    plt.show()

#Partie 2: pour un pays donné
df0 = pd.read_csv (r'owid-covid-data.csv')
cols = [2,3,4,5,6]
df2 = df0[df0.columns[cols]]
df3=df2.loc[df2['location'] == 'Switzerland']
df3.date = pd.to_datetime(df3['date'], format='%Y-%m-%d')
df=df3
depart=47 # date de départ
df=df.iloc[depart:60] 

#modèle SEIR
pop_ch=8600000
taille_T=100
date_depart=df['date'].iloc[0]

ydata = df['new_cases_smoothed'].div(pop_ch)
vx=[]
[vx.append(str(i)) for i in range(1,len(df['total_cases'])+1)]
xdata = vx

ydata = np.array(ydata, dtype=float)  #new cases I_t
xdata = np.array(xdata, dtype=float)  #les jours allant de 1 à la fin de l'interval temps

def seir_model(y, x, beta, sigma, gamma):
    S = -beta * y[0] * y[2] / N
    E = beta * y[0] * y[2] / N - sigma*y[1]
    I = sigma*y[1] - (gamma*y[2])
    R = gamma * y[2]
    return S, E, I, R

def fit_odeint(x, beta, sigma, gamma):
    return integrate.odeint(seir_model, (S0, E0, I0, R0), x, args=(beta, sigma, gamma))[:,1]
# This scipy.integrate.odeint() integrates the given equation by taking 4 parameters odeint(model,y0,t,args) 
# model- the differential equation function 
# y0-the inital value of y 
# t- the timepoints for which we need to plot the curve 
# args- Extra arguments to pass to function

N = 1.0
I0 = ydata[0]
E0= (ydata[0]+ydata[1])/2 # est une hypothèse
S0 = N - I0 - E0
R0 = 0.0

popt, pcov = optimize.curve_fit(fit_odeint, xdata, ydata)
# curve_fit() function takes the fit_odeint-function, xdata and ydata as argument and returns  
# the coefficients (beta, sigma, gamma) in popt and the estimated covariance of popt in pcov 

fitted = fit_odeint(xdata, popt[0],popt[1],popt[2])

plt.plot(df['date'], ydata, 'o',label='données des infectés (lissées)')
plt.plot(df['date'], fitted, label='estimation des infectés (modèle SIR)')
plt.title('Suisse $1^{ère}$ vague \napproximations: β='+str(np.round(popt[0],2))
          +', σ='+str(np.round(popt[1],2))+', γ='+str(np.round(popt[2],2))+'\ndu '
          +str((df['date'].iloc[0]).strftime('%Y-%m-%d'))+' au '+str((df['date'].iloc[-1]).strftime('%Y-%m-%d')))
plt.gcf().autofmt_xdate(rotation=50)
plt.xlabel('temps')
plt.ylabel('population')
plt.legend()
plt.show()

function_SEIR(N, R0, E0,I0,S0,popt[0],popt[1],popt[2],np.linspace(0, taille_T,taille_T),date_depart)
print(SEIR_val)
#print(df['date'].iloc[0])