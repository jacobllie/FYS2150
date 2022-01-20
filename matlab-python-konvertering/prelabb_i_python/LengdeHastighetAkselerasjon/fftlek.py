import numpy as np
import matplotlib.pyplot as plt

"""
Dette er et lite script for å se hvor små frekvenser man kan skille
med en diskret fouriertransformasjon, og får å få en følelse av
hvordan energispekteret fra en diskret fouriertransormasjon ser ut.

scriptet lager et signal med to sinusbølger med frekvenser f og fm der
frekvensforskjellen er liten, dvs fm/f~1.

Signalet fouriertransformeres med fft() og energispekteret plottes

Simuler dopplershift for hastighet v og lyd i tørr luft ved 20 grader C
"""
v = -10.333 #hastighet [m/s]
temp = 20 #temprature [C]
c = 331.1 + 0.606*temp #lydhastighet i tørr luft [m/s]

T = 0.25 #totaltid [s]
fs = 2500 #samplingsfrekvens [Hz]
f = 1000 #lydkildefrekvens [Hz]
Ar = 0.5 #relativ amplitude, burde gi faktor Ar^2 i energispekteret
As = 1.0 #støyamplitude

fm_f = c/(c-v) #relativt doppler-dopplershift
#fm_f = 0.99 #mulig å bestemme denne konstanten selv
print(f'Relativt doppler shift fm/f = {fm_f}')


t = np.arange(0,T,1/fs) #s
n = len(t)

#lager sinus signal med random støy
omega_t = 2*np.pi *f*t
y1 = np.sin(omega_t)
y2 = Ar*np.sin(fm_f*omega_t) + As *np.random.randn(n)
y = y1+y2


plt.style.use("seaborn")
plt.plot(t,y)
plt.xlabel("tid [s]")
plt.ylabel("Amplitude [A.U]")
plt.show()


#henter ut fourier transformasjonen
FFT = np.fft.fft(y)
#vi trenger et spenn med frekvenser vi kan plotte, det fikser numpy
freq = np.fft.fftfreq(len(FFT),1/fs)


#Vi ønsker bare halve FFT arrayet, best forklart på denne måten:
#It's inherent to FFT algorithm. The second half of FFT array is the conjugate of the first half, so don't contain any new information.
#To visualize the spectrum, just use the first half. 
#Eller sagt på en annen måte: den andre halvdelen er bare en speiling.
plt.style.use("seaborn")
plt.title("Fourier transform of signal")
plt.plot(freq[:n//2],np.abs(FFT[:n//2]))
plt.xlabel("Frequency [s^-1]")
plt.ylabel("Amplitude [A.U.]")
plt.show()
