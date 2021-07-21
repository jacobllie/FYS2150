import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#data hentet fra Table 4.2 side 34. Squires
T = np.array([570.6, 555.9, 549.4, 544.1, 527.3, 522.2, 513.1, 497.6, 484.9])/1000 #temperatur i K
R = np.array([148.1, 202.6, 227.1, 255.1, 362.0, 406.1, 502.5, 750.1, 1026.7]) #motstand i Ohm

#transformerer data for å få noe lineært
x = 1/T
y = np.log(R)


"""
Vi ønsker å gjøre en lineærtilpasning på de transformerte dataene.
Til det bruker vi pakken funksjonen linregress fra stats biblioteket stats fra scipy.

"""

Y = stats.linregress(x,y)

"""
Linregress returnerer:

LinregressResult(slope=6.22827923445122, intercept=-5.910297159240161,
rvalue=0.9998679481548884, pvalue=8.71137976427864e-14, stderr=0.03826038230685759,
intercept_stderr=0.0725401430250171)

De viktigste variablene er slope, intercept, stderr og intercept_stderr.

Den bruker minste kvadraters metode på å tilpasse stigningstall og konstantledd
til ligningen:

y = slope * x + intercept.

Den finner også standarderror (stderr) i stigningstallet og konstantleddet (intercept_stderr).
"""


"""
For å ekstrapolere lineærtilpasningen lager vi en forlengelse av x, og en forlengelse av y

Polyval returnerer verdier y = slope * x + intercept.
"""
x_extra = np.linspace(min(x),max(x),100)
#y_extra = np.polyval([Y.slope, Y.intercept],x_extra)

def line(x,m,b):
    return x*m + b

y_extra = line(x_extra,Y.slope,Y.intercept)


plt.style.use("seaborn")
plt.subplot(1,2,1)
plt.plot(T,R,"o",label="ubehandlede data")
plt.legend()
plt.subplot(1,2,2)
plt.plot(x,y,"*",label="transformerte variabler")
plt.plot(x_extra,y_extra,label="fit")




"""
Nå har vi gjort en lineærtilpasning, men vi ønser å si noe kvantitativt om hvor
selvsikre vi er på estimeringen av stigningstall og konstantledd.
Vi vil bruke 68-95-99,7 regelen (se kompendiet om konfidensintervaller)

vi ønsker 95% sannsynlighet for at verdiene ligger innenfor et gitt intervall.
Derfor velger vi z = 1.96

Da kan vi bare putte den inn i formelen slope +- z * sigma / sqrt(n)
hvor sigma /sqrt(n) er standarderror, som vi har!
"""

z = 1.96
print("Konfidensintervallet til stigningstallet med 95% dekningsgrad blir [{:.4},{:.4}]"\
      .format(Y.slope - 1.96 * Y.stderr , Y.slope + 1.96 * Y.stderr))
print("Konfidensintervallet til konstantleddet med 95% dekningsgrad blir [{:.4},{:.4}]"\
      .format(Y.intercept - 1.96 * Y.intercept_stderr, Y.intercept + 1.96 * Y.intercept_stderr))


"""
Vi kan også legge Konfidensintervallet med i plottet
"""

y = np.polyval([Y.slope, Y.intercept],x_extra)
ci = 1.96* np.std(y)/np.sqrt(len(y))

plt.fill_between(x_extra, y - ci , y + ci,color = "b",alpha = 0.1)
plt.title("Transformerte data med lineærtilpasning og konfidensintervall")
plt.legend()
plt.show()
