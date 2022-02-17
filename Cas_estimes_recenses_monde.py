import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from scipy import integrate, optimize, stats
from scipy.integrate import odeint

'''
But: afficher les données (4 méthodes + cas confirmés) pour le monde
    in: tableau des données pour le monde
    out:graphe
'''

df3 = pd.read_csv (r'my_tab_world.csv') #créé dans Procedure_3_monde.r

arr_T=pd.date_range(start=df3.loc[df3.index[0],'dates'], end = df3.loc[df3.index[-1],'dates'])

fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111,  axisbelow=True)
ax.plot(arr_T, df3['ICL'], 'b', alpha=0.5, lw=2, label='ICL')
ax.plot(arr_T, df3['IHME'], 'gray', alpha=0.5, lw=2, label='IHME')
ax.plot(arr_T, df3['YGG'], 'r', alpha=0.5, lw=2, label='YGG')
ax.plot(arr_T, df3['LSHTM'], 'g', alpha=0.5, lw=2, label='LSHTM')
ax.plot(arr_T, df3['conf_cases'], 'orange', alpha=0.5, lw=2, label='confirmés')
ax.set_xlabel('temps')
ax.set_ylabel('Infectés')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
plt.title('Nombre d\'infections dans le monde')
plt.gcf().autofmt_xdate(rotation=50)
plt.savefig('nb_infectes_monde.png')
plt.show()
#1e+6