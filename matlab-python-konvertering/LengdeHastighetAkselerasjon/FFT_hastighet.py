import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np
from sound_acquisition_pyaudio import pyaudio_acquisition
from StykkevisFFT import stykkevisFFT

inputs = input("Har du en lydfil fra før? [Y/n] ")

if inputs == "Y" or inputs == "y":
    filename = input("Skriv inn filnavn på formen filnavn.wav ")
    fmin = int(input("Hva er minimumsfrekvensen? "))
    mydata, samplerate = sf.read(filename)
    duration = int(len(mydata)/samplerate)

if inputs == "N" or inputs == "n":
    temp = input("Skriv inn samplerate [Hz] varighet [s] og fmin [Hz] ").split()
    samplerate = int(temp[0])
    duration = int(temp[1])
    fmin = int(temp[2])

    """For pyaudio unhash linjen under."""
    mydata = pyaudio_acquisition(duration, samplerate)
    """For sounddevice unhash linjen under."""
    #mydata = sound_data_acquisition(duration, samplerate).transpose().reshape(-1)
    """
    Dersom du bruker sounddevice så vil mydata har shapen (1,n),
    for at fourier transformasjonen skal gå riktig for seg,
    er vi nødt til å først transponere den til (n,1), deretter reshape
    den slik at den får formen (n,).
    """

t = np.linspace(0, duration, samplerate*duration)

try:
    print("{} antall samples er registrert." .format(len(mydata)))
except:
    print("\n Har du husket å unhashe mydata linjen?")


tw, fw, n, FFT_freq, power = stykkevisFFT(t,samplerate,mydata,fmin)


fmin_idx = np.argwhere(FFT_freq > fmin)

power = power[:,np.min(fmin_idx):]
FFT_freq = FFT_freq[np.min(fmin_idx):]



plt.style.use("seaborn")
plt.subplot(1,3,1)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [A.U]")
plt.plot(t,mydata)


plt.subplot(1,3,2)
plt.plot(tw,fw,"o-")
plt.xlabel("Time [s]")
plt.ylabel("Frequency [Hz]")


#plotter bare Fourier for første tidsintervall.
i = 0
plt.subplot(1,3,3)
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude  [A.U]")
plt.plot(FFT_freq,power[i])
plt.savefig("FFT_test.png")
plt.show()
