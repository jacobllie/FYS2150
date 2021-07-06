from StykkevisFFT import stykkevisFFT
import numpy as np
from sound_aqcuisition import sound_data_aqcuisition
import soundfile as sf
import matplotlib.pyplot as plt
#%matplotlib auto
#Ta opp lyd-data for å finne egenfrekvensen til messingsstaven
#Jacob Lie 22.4.21, basert på matlab kode fra Alex Read 1.3.18

fmin = 500


inputs = input("Har du en lydfil fra før? [Y/n] ")

if inputs == "Y" or inputs == "y":
    filename = input("Skriv inn filnavn på formen filnavn.wav ")
    mydata, samplerate = sf.read(filename)
    t = np.linspace(0,len(mydata)//samplerate,len(mydata))

if inputs == "N" or inputs == "n":
    #samplerate, duration = input("Skriv inn samplerate og duration på opptaket ")
    temp = input("Skriv inn samplerate og duration ").split()
    samplerate = int(temp[0])
    duration = int(temp[1])
    mydata = sound_data_aqcuisition(duration, samplerate)


#duration = 5
#samplerate = 96000
#t = np.linspace(0, duration, samplerate*duration)
#mydata = sound_data_aqcuisition(duration, samplerate)

plt.subplot(121)
plt.xlabel("Tid [s]")
plt.ylabel("Amplitude [a.u]")
plt.plot(t,mydata)


n = len(mydata)
Y = np.fft.fft(mydata)
power = np.abs(Y[:len(Y)//2])**2

FFT_freq = samplerate//2*np.linspace(0,1,len(power))  #Deler på to pga. Nyquist

fmin_index = np.where(FFT_freq >= fmin)
FFT_freq = FFT_freq[np.min(fmin_index):]
power = power[np.min(fmin_index):]



plt.subplot(122)
plt.xlabel("Frekvens [Hz]")
plt.ylabel("Amplitude [a.u.]")
plt.plot(FFT_freq,power)
plt.show()

#Finner egenfrekvensen til staven.

print("Grunntonen er {:.4} Hz".format(FFT_freq[np.argmax(power)]))
