import sounddevice as sd
import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np
from StykkevisFFT import stykkevisFFT

samplerate = 96000  # Hertz
duration = 5  # seconds
fmin = 12300 #Hz

"""
Hvis du allerede har data, kan du lese det inn i linjen under.
"""
#mydata, _ = sf.read("filename.wav")
t = np.linspace(0, duration, samplerate*duration)

sd.default.latency = 'low'

print("Data aqcuisition started...")    
mydata = sd.Stream(samplerate, blocksize = 1024, channels = 1)
mydata = sd.rec(int(samplerate * duration), samplerate=samplerate,
                channels=1, blocking=True)
sd.wait()

save = input("Vil du lagre dataene som en .wav fil [Y/n]?  ")
if save == "Y" or save == "y":
    filename = input("Skriv filnavn på formen filename.wav ")
    sf.write(filename, mydata, samplerate)


tw, fw, n, FFT_freq, power = stykkevisFFT(t,samplerate,mydata,fmin)


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

