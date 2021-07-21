import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#data hentet fra Table 4.2 side 34. Squires
T = np.array([570.6, 555.9, 549.4, 544.1, 527.3, 522.2, 513.1, 497.6, 484.9]) #temperatur i K
R = np.array([148.1, 202.6, 227.1, 255.1, 362.0, 406.1, 502.5, 750.1, 1026.7]) #motstand i Ohm

#transformerer data for å få noe lineært
x = 1000/T
y = np.log(R)


"""
Vi ønsker å gjøre en lineærtilpasning på de transformerte dataene.
Til det bruker vi pakken funksjonen linregress fra stats biblioteket stats fra scipy.

"""

Y = stats.linregress(x,y)


"""
Vi ønsker å plotte residualene, m.a.o. differansen mellom predikert data, og faktisk data.
Vi plotter predikerte verdier på x aksen, og residualen på y aksen.
"""

#predicted = np.polyval([Y.slope,Y.intercept],x)

def line(x,m,b):
    return x*m + b

predicted = line(x,Y.slope,Y.intercept)
residual = y - predicted

plt.style.use("ggplot")
plt.subplot(121)
plt.plot(predicted,residual,"o",label = "residual")
plt.plot(y,np.zeros(len(x)),"--",label = "Perfekt prediksjon")
plt.xlabel("Predikerte verdier")
plt.ylabel("Grad av avvik")

plt.legend(edgecolor="black")
#plt.show()

"""
Jo tettere punktene ligger til den striplede linjen, jo bedre modell har vi.
Vi observerer avvik rundt 1%, og kan konkludere med at en lineær modell kan være rett.
"""

"""
La oss se om disse residualene er normalfordelt.
"""
plt.subplot(122)
QQ = stats.probplot(residual,plot = plt)
plt.title("QQ plot med residualer")
plt.show()

"""
Ja det kan se ut til at residualene er nokså normalfordelte.
"""

"""
La oss nå ta en titt på de oprinnelige dataene. Vil den lineære modellen være best
i dette tilfellet ?
"""

Y = stats.linregress(T,R)
x_extra = np.linspace(min(T),max(T),100)
y_extra = np.polyval([Y.slope, Y.intercept],x_extra)
plt.subplot(121)
plt.plot(T,R,"o",label="data")
plt.plot(x_extra,y_extra,label="fit")
plt.xlabel("Temperatur")
plt.ylabel("Motstand")
plt.legend(edgecolor="black")

"""
Rent visuelt kan man tenke seg at en lineær modell ikke er så gal, men la oss
se hva residual plottet sier.
"""

predicted = np.polyval([Y.slope,Y.intercept],T)
residual = R - predicted

plt.subplot(122)
plt.plot(predicted,residual,"o",label = "residual")
plt.plot(R,np.zeros(len(x)),"--",label = "Perfekt prediksjon")
plt.xlabel("Predikerte verdier")
plt.ylabel("Grad av avvik")

plt.legend(edgecolor="black")
plt.show()

"""
Her er forholdet mellom residualene og de predikerte verdiene et polynom, og
skalaen på y aksen er mye større i dette tilfellet sammenlignet med det forrige.
Vi kan derfor konkludere med at vi kan skrote den lineære modellen for de
opprinnelige dataene.
"""
