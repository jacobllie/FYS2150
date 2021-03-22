
import sounddevice as sd
import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np
import time
import sys

samplerate = 96000  # Hertz
duration = 5  # seconds
fmin = 12300 #Hz
#mydata, _ = sf.read("purest_sound_ever.wav")
t = np.linspace(0, duration, samplerate*duration)

sd.default.latency = 'low'
start = time.time()
mydata = sd.Stream(samplerate, blocksize = 1024, channels = 1)
mydata = sd.rec(int(samplerate * duration), samplerate=samplerate,
                channels=1, blocking=True)
print(time.time()-start)
sd.wait()

plt.style.use("seaborn")
plt.subplot(1,3,1)
plt.plot(t,mydata)

#sf.write(filename, mydata, samplerate)


def stykkevisFFT(t,fs,data,fmin):
    """
    Algoritmen som numpy bruker for FFT foretrekker arrays med log_2 lengde.
    For enkelthetens skyld, fortsetter vi med det.
    Grunnen til at vi ofte bruker FFT_length//2 er fordi vi ønsker bare å plotte den reelle delen av signalet,
    og halvparten av arrayet som FFT returnerer er den komplekskonjugerte.
    """
    wp2 = 14
    FFT_length = 2**wp2
    #hvert tidsintervall vil få disse punktene å utføre FFT på.
    n = int(len(t)/FFT_length)
    print(t[2]-t[1])
    #making t an array with log_2 length
    t = t[:n*FFT_length].reshape(n,FFT_length)
    y = data[:n*FFT_length].reshape(n,FFT_length)
    tw = t[:,FFT_length//2]    #tw er tiden midt i alle intervallene
    fw = np.zeros(n)
    FFT_freq = fs/2*np.linspace(0,1,FFT_length//2)  #frekvenser til plotting av FFT
    power = np.zeros((n,FFT_length//2,))            # til plotting av absoluttverdien av signalet.
    fmin_index = np.min(np.where(FFT_freq>fmin))
    #Fourier transformerer hvert intervall med datapunkter
    for i in range(n):
        FFT = np.fft.fft(y[i,:],FFT_length)
        #tar bare med FFT'en til frekvenser som er større enn fmin
        #og tar ikke med siste halvdel, siden vi ikke er interessert i komplekskonjugerte
        power[i,:] = np.abs(FFT[:FFT_length//2])**2
        #Vi ønsker å hente ut indeksen til den maksimale amplituden per intervall
        max_amp_indx = np.argmax(np.abs(FFT[fmin_index:FFT_length//2])**2)
        print(max_amp_indx)
        fw[i] = FFT_freq[max_amp_indx+fmin_index-1]

    return tw, fw, n, FFT_freq, power

tw, fw, n, FFT_freq, power = stykkevisFFT(t,samplerate,mydata,fmin)

plt.subplot(1,3,2)
plt.plot(tw,fw,"o-")


i = 0
plt.subplot(1,3,3)
plt.plot(FFT_freq,power[i])
plt.show()

"""
fourier = np.fft.fft(mydata)
fft_freq = np.fft.fftfreq(mydata.size)

plt.plot(fft_freq,fourier)
plt.show()

plt.specgram(mydata)
plt.show()
"""
#sf.write('purest_sound_ever.wav', mydata, samplerate)
