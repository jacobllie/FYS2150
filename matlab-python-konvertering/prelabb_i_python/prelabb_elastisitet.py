import numpy as np
import matplotlib.pyplot as plt
from prelabb_masse_og_kraft import regression, linear

#spørsmål 4 og 5
data = np.loadtxt("maalinger_h.dat")  #kg, mm

m = data[:,0] #masse
h = data[:,1] #utslag


a, da, c, dc = regression(m,h)


print("A = {:.4e} m/kg".format(a/1000))
print("dA = {:.4e} m/kg".format(da/1000))


#spørsmål 8
#importerer soundfile for å lese av wav filer.
#pip install soundfile
import soundfile as sf

f_hat = 1.107e3 #Hz
filename = "messing_lyd.wav"
mydata, samplerate = sf.read(filename)

duration = int(len(mydata)/samplerate)
#må sørge for at amplituden ikke overskrider 1 total
mydata*0.5


t = np.linspace(0,duration,len(mydata))
def sinus(f,t):
    return 0.5*np.sin(2*np.pi*f*t)

sum_signal = mydata + sinus(f_hat,t)

sf.write("svevninger.wav", sum_signal, samplerate)

#importerer playsound for å spille av det summerte signalet.
#pip install playsound
from playsound import playsound

playsound('svevninger.wav')
