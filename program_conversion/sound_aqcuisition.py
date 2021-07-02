import sounddevice as sd
import soundfile as sf

def sound_data_aqcuisition(duration,samplerate):
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

    return mydata
