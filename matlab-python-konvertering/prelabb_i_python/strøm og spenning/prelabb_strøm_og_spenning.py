import numpy as np
import scipy.io
import matplotlib.pyplot as plt
import pandas as pd

"""
Fasit til siste oppgave i strøm og spenning prelabb.
I dette eksempelet, har jeg brukt algoritmen til squires, men man kan fint erstatte
den med
import scipy
Y = scipy.stats.linregress(x,y)
"""

def regression(x,y):

    """
    Side 39 i Squires. for minste kvadraters metode
    """
    n = len(x)
    D = np.sum(x**2)-1/n*np.sum(x)**2
    E = np.sum(x*y)-1/n*np.sum(x)*np.sum(y)
    F = np.sum(y**2)-1/n*np.sum(y)**2

    x_bar = 1/n*np.sum(x)
    y_bar = 1/n*np.sum(y)

    m = E/D
    c = y_bar - m*x_bar
    d = y - m*x -c

    dm = np.sqrt(1/(n-2) *(D*F - E**2)/D**2)
    dc = np.sqrt(1/(n-2)*(D/n+x_bar**2)*(D*F - E**2)/D**2)
    return m, dm, c, dc

def linear(slope,intercept,x):
    """
    Funksjon for å lage ekstrapoleringspunkter fra lineærtilpasningen
    """
    print("{:.4f} + {:.4f}x".format(intercept,slope))
    return intercept + slope*x


mat = pd.read_csv('RC_data.csv')

#print(mat[])

vu_over_vi = np.log10(mat["Vu_over_Vi"])
frekvens = np.log10(mat["frekvens"])

"""
Etter å ha plottet dataene, vi har identifisert hvor plottet er lineært og kan
lage en tilpasning her.
"""

m, dm, c, dc = regression(frekvens[-9:],vu_over_vi[-9:])
linear_fit = np.polyfit(frekvens[-9:],vu_over_vi[-9:],1)

print(m,c)
plt.style.use("ggplot")
plt.title("vu over vi as a function of frequency")
plt.xlabel("frequency [s^-1]")
plt.ylabel("vu_over_vi")
plt.plot(frekvens,vu_over_vi,"o",label="vu_over_vi data")

lin_frekvens = np.linspace(np.min(frekvens[-9:]),np.max(frekvens[-9:]),100)


plt.plot(lin_frekvens,linear(m,c,lin_frekvens))
plt.legend(edgecolor="black")
plt.show()
