import matplotlib.pyplot as plt
import numpy as np

def stykkevisFFT(t,fs,data,fmin):
    """
    Algoritmen som numpy bruker for FFT foretrekker arrays med log_2 lengde.
    For enkelthetens skyld, fortsetter vi med det.
    Grunnen til at vi ofte bruker FFT_length//2 er fordi vi ønsker bare å plotte den reelle delen av signalet,
    og halvparten av arrayet som FFT returnerer er den komplekskonjugerte.

    Stykkevis FFT tar Fourier transformasjon på et tidsinterval.
    Vi deler opp total duration inn i intervaller med lengde
    (duration * samplingfreq)/2^x. x er et predefinert heltall.
    Parameters
    ----------
    t :  Array
        Aqcuisition time
    fs : Int
        Sampling frequency.
    data : Array
           Sound data aqcuisition.
    fmin : Int
        Minimal frequency to include.

    Returns
    -------
    tw : Array
        Et array med midten av hvert tidsintervall.
    fw : Frekvensen fra hvert tidsintervall.
    n : Int
        ¨Lengden på hvert tidsintervall.
    FFT_freq : Array
        Frekvens aksen i Fourier transformasjonen.
    power : Array
        Kvadrert frekvensamplitude fra Fourier Transformasjon.

    """
    wp2 = 14
    FFT_length = 2**wp2
    #hvert tidsintervall vil få disse punktene å utføre FFT på.
    n = int(len(t)/FFT_length)
    #gjør om t til lengde 2**wp2, dette vil gjøre at man mister et neglisjerbart
    #antall datapunkter.
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
        fw[i] = FFT_freq[max_amp_indx+fmin_index-1]

    return tw, fw, n, FFT_freq, power
