from StykkevisFFT import stykkevisFFT
import numpy as np
from sound_aqcuisition import sound_data_aqcuisition
import soundfile as sf
import matplotlib.pyplot as plt
%matplotlib auto
#Ta opp lyd-data for å finne egenfrekvensen til messingsstaven
#Jacob Lie 22.4.21, basert på matlab kode fra Alex Read 1.3.18

duration = 5
samplerate = 96000
fmin = 0.8e3

print("{} samples skal registreres".format(samplerate*duration))

"""
Hvis du allerede har data, kan du lese det inn i linjen under.
Men da er det viktig at du vet samplerate og varighet på lydklippet.
"""

#mydata, samplerate = sf.read("purest_sound_ever.wav")
#t = np.linspace(0,len(mydata)//samplerate,len(mydata))
"""
    Hvis du ikke har data, kan du kjøre linjen
    mydata = sound_data_aqcuisition(duration, samplerate)
"""

t = np.linspace(0, duration, samplerate*duration)
mydata = sound_data_aqcuisition(duration, samplerate)

plt.subplot(121)
plt.xlabel("Tid [s]")
plt.ylabel("Amplitude [a.u]")
plt.plot(t,mydata)


n = len(mydata)
Y = np.fft.fft(mydata)
power = np.abs(Y[:len(Y)//2])**2




FFT_freq = samplerate//40*np.linspace(0,1,len(power))

fmin_index = np.where(FFT_freq >= fmin)
print(fmin_index)

FFT_freq = FFT_freq[np.min(fmin_index):]
power = power[np.min(fmin_index):]

print(len(power))
print(len(FFT_freq)) 

#FFT_freq = samplerate*np.linspace(0,1,len(Y)//2)

plt.subplot(122)
plt.xlabel("Frekvens [Hz]")
plt.ylabel("Amplitude [a.u.]")
plt.plot(FFT_freq,power)
plt.show()

#Finner egenfrekvensen til staven

print("Grunntonen er {:.4} Hz".format(FFT_freq[np.argmax(power)]))
