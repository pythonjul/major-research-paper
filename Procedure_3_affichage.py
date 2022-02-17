import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from scipy import integrate, optimize, stats
from scipy.integrate import odeint
'''
But: afficher les 4 méthodes ansi que les cas confirmés pour un pays donné.

  in: tableau des infections recencées, tableau des infections simulées (pathfile à changer pour exécution du programme)
      pays, intervalle de dates
  out:retourne le graphe complet ainsi qu'un graphe zoomé sur une période donnée.
'''

pays_sel='Switzerland'
df0 = pd.read_csv (r'daily-new-estimated-infections-of-covid-19.csv')
cols = [0,2,3,4,5,6,7]
df2 = df0[df0.columns[cols]]
df3=df2.loc[df2['Entity'] == pays_sel]

arr_T=pd.date_range(start=df3.loc[df3.index[0],'Date'], end = df3.loc[df3.index[-1],'Date'])

fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111,  axisbelow=True)
ax.plot(arr_T, df3['Daily new estimated infections of COVID-19 (ICL, mean)'], 'b', alpha=0.5, lw=2, label='ICL')
ax.plot(arr_T, df3['Daily new estimated infections of COVID-19 (IHME, mean)'], 'gray', alpha=0.5, lw=2, label='IHME')
ax.plot(arr_T, df3['Daily new estimated infections of COVID-19 (YYG, mean)'], 'r', alpha=0.5, lw=2, label='YGG')
ax.plot(arr_T, df3['Daily new estimated infections of COVID-19 (LSHTM, median)'], 'g', alpha=0.5, lw=2, label='LSHTM')
ax.plot(arr_T, df3['Daily new confirmed cases due to COVID-19 (rolling 7-day average, right-aligned)'], 'orange', alpha=0.5, lw=2, label='Confirmed')
ax.set_xlabel('temps')
ax.set_ylabel('Infectés')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
plt.yscale('log')
plt.title('Nombre d\'infections pour la Suisse')
plt.gcf().autofmt_xdate(rotation=50)
plt.show()

mask = (df3['Date'] >= '2020-10-01') & (df3['Date'] <= '2020-10-30') # Intervalle de dates
df3=df3.loc[mask]
arr_T=pd.date_range(start=df3.loc[df3.index[0],'Date'], end = df3.loc[df3.index[-1],'Date'])
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111,  axisbelow=True)
ax.plot(arr_T, df3['Daily new estimated infections of COVID-19 (ICL, mean)'], 'b', alpha=0.5, lw=2, label='ICL')
ax.plot(arr_T, df3['Daily new estimated infections of COVID-19 (IHME, mean)'], 'gray', alpha=0.5, lw=2, label='IHME')
ax.plot(arr_T, df3['Daily new estimated infections of COVID-19 (YYG, mean)'], 'r', alpha=0.5, lw=2, label='YGG')
ax.plot(arr_T, df3['Daily new estimated infections of COVID-19 (LSHTM, median)'], 'g', alpha=0.5, lw=2, label='LSHTM')
ax.plot(arr_T, df3['Daily new confirmed cases due to COVID-19 (rolling 7-day average, right-aligned)'], 'orange', alpha=0.5, lw=2, label='Confirmed')
ax.set_xlabel('temps')
ax.set_ylabel('Infectés')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
plt.yscale('log')
plt.title('Nombre d\'infections pour la Suisse zoomé')
plt.gcf().autofmt_xdate(rotation=50)
plt.show()