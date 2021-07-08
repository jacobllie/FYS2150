import sounddevice as sd
import soundfile as sf

def sound_data_aqcuisition(duration,samplerate):
    """
    Bruker sounddevice for å ta opp lyd fra mikrofon, og soundfile
    for å skrive dataen til fil. 
    Parametere
    ----------
    duration : int
        Varighet på opptak.
    samplerate : int
        Hvor mange samples som tas opp per sekund.

    Returns
    -------
    mydata : array
        data fra lydopptak.

    """

    sd.default.latency = 'low' #var dette som fungerte best
    print("Data aqcuisition started...")
    #setter opp en stream med kontinuerlig input output
    #dette kan tas opp av sd.rec for data behandling. 
    mydata = sd.Stream(samplerate, blocksize = 1024, channels = 1) 
    mydata = sd.rec(int(samplerate * duration), samplerate=samplerate,
                    channels=1, blocking=True) 
    #blocking = True, gjør at outputen til sd.rec ikke kommer før opptaket er
    #fullført.

    save = input("Vil du lagre dataene som en .wav fil [Y/n]?  ")
    if save == "Y" or save == "y":
        filename = input("Skriv filnavn på formen filename.wav ")
        sf.write(filename, mydata, samplerate)

    return mydata
