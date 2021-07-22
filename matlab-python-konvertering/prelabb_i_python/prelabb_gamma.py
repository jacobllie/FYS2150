import numpy as np
import matplotlib.pyplot as plt
from prelabb_tid_og_frekvens import mean, std
from prelabb_masse_og_kraft import regression, linear
import scipy.io

mat = scipy.io.loadmat('poisson.mat')
poisson_data =  mat["data"]

print("Gjennomsnitt = {:.4}".format(mean(poisson_data)))

print("Standardavvik = {:.4}".format(std(poisson_data)))

z = np.array([0, 4, 8, 12, 16, 20, 24])*1e-3 #meter
n = np.log(np.array([13.7, 12.4, 11.0, 9.7, 8.9, 7.9, 7.1])) #counts / second


m, dm, c, dc = regression(z,n)

print("Dempningskoeffisienten mu = {:.4f} m^-1".format(-m))

print("dmu = {:.4}".format(dm))

z_extra = np.linspace(np.min(z),np.max(z),100)
line = linear(m, c, z_extra)

plt.style.use("seaborn")
plt.plot(z,n,"o",label= "Intensity Data")
plt.plot(z_extra,line,label= "Fit")
plt.xlabel("z[mm]")
plt.ylabel(r"Counting Rate [$s^{-1}$]")
plt.title("Intensity vs Depth")
plt.legend()
plt.show()


#11
#Anntar lineær dempning i bakgrunnsstrålingen for Fullenergitoppen.

mat = scipy.io.loadmat('spektrum.mat')
spectrum = np.array(mat["spektrum"])
I = np.arange(0,1024,1)


#Lager en lineær tilpasning mellom starten på Fullenergitoppen og slutten på Fullenergitoppen.
I_FWHM = np.array([I[662],I[1000]])
spectrum_FWHM = np.array([spectrum[662],spectrum[1000]])
background_fit = np.polyfit(I_FWHM,spectrum_FWHM,1)

#Finner bakgrunnsverdiene for hver kanal mellom index 662 og 1000.
#Må reshape bakgrunnsstrålingen fra (x,) til (x,1), for at np.subtract skal funke

background_radiation = np.polyval(background_fit,I[662:1000]).reshape(-1,1)
peak_adjusted = np.subtract(spectrum[662:1000],background_radiation)

#Finner alle punkter som ligger over midten av Fullenergitoppen.
c = np.argwhere(peak_adjusted >= 1/2*np.max(spectrum))


"""
Oppløsningen er bestemt av FWHM, som er bredden halvveis opp på fullenergitoppen.
For å konvertere fra kanalnummer til energi, bruker vi formel 6 i labteksten:
E = dE * I + E0
E1 og E2 er første og andre punkt i FWHM, og differansen er:
dE(I2-I1)
"""
print(" Estimert energioppløsning er dE(I2 - I1)  = {} keV".format(2*(c[-1,0]-c[0,0])))



plt.subplot(121)
plt.title("Gammaspekter med bakgrunnsstråling")
plt.xlabel("Kanal")
plt.ylabel("Tellinger")
plt.plot(I,spectrum,label="Spekter fra ukjent kilde")
plt.plot(I[662:1000],background_radiation)
plt.legend()
plt.subplot(122)
plt.title("Fullenergi topp justert for bakgrunnsstråling")
plt.xlabel("Kanal")
plt.plot(I[662:1000],peak_adjusted,label="Fullenergitopp")
plt.legend(loc="upper left")
plt.show()



from math import factorial

def poisson(k,m):
    P = [factorial(i) for i in k]
    return m**k/P*np.exp(-m)
