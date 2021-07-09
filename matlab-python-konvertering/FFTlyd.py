import numpy as np
from sound_acquisition import sound_data_acquisition
import soundfile as sf
import matplotlib.pyplot as plt
from sound_acquisition_pyaudio import pyaudio_acquisition

#Ta opp lyd-data for å finne egenfrekvensen til messingsstaven
#Jacob Lie 22.4.21, basert på matlab kode fra Alex Read 1.3.18


fmin = 5e2 #minimumsfrekvens for å fjerne støy
fmax = 2e3


fmin = 500  #definerer en minimumsfrekvens for å fjerne støy
fmax = 2000

inputs = input("Har du en lydfil fra før? [Y/n] ")

if inputs == "Y" or inputs == "y":
    filename = input("Skriv inn filnavn på formen filnavn.wav ")
    mydata, samplerate = sf.read(filename)

if inputs == "N" or inputs == "n":
    temp = input("Skriv inn samplerate og duration ").split()
    samplerate = int(temp[0])
    duration = int(temp[1])
    
    """For pyaudio unhash linjen under."""
    #mydata = pyaudio_acquisition(duration, samplerate)
    """For sounddevice unhash linjen under."""
    #mydata = sound_data_acquisition(duration, samplerate).transpose().reshape(-1)
    """
    Dersom du bruker sounddevice så vil mydata har shapen (1,n),
    for at fourier transformasjonen skal gå riktig for seg,
    er vi nødt til å først transponere den til (n,1), deretter reshape 
    den slik at den får formen (n,).
    """

try: 
    print("{} antall samples er registrert." .format(len(mydata)))
except:
    print("\n Har du husket å unhashe mydata linjen?")
    
 
t = np.linspace(0,len(mydata)//samplerate,len(mydata))


plt.subplot(121)
plt.xlabel("Tid [s]")
plt.ylabel("Amplitude [a.u]")
plt.plot(t,mydata)

Y = np.fft.fft(mydata)
power = np.abs(Y[:len(Y)//2]) #ønsker bare de reelle verdiene, og vil ikke
#inkludere speilingen, derfor har vi len(Y)//2
 

FFT_freq = samplerate//2*np.linspace(0,1,len(power))  #Deler på to pga. Nyquistfrekvensen


fmin_index = np.where(FFT_freq >= fmin)  
fmax_index = np.where(FFT_freq <= fmax)
FFT_freq = FFT_freq[np.min(fmin_index):np.max(fmax_index)] #fjerner støy og justerer x-aksen

power = power[np.min(fmin_index):np.max(fmax_index)]



plt.subplot(122)
plt.xlabel("Frekvens [Hz]")
plt.ylabel("Amplitude [a.u.]")
plt.plot(FFT_freq,power)
plt.show()

#Finner egenfrekvensen til staven.

print("Grunntonen er {:.4} Hz".format(FFT_freq[np.argmax(power)]))
