import pyaudio
import wave
import numpy as np

def pyaudio_acquisition(RECORD_SECONDS,RATE):
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    CHUNK = 1024
    audio = pyaudio.PyAudio()
     
    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    print ("recording...")
    #frames = []
     
    
    buffer = stream.read(RATE * RECORD_SECONDS)
    mydata = np.frombuffer(buffer,dtype = "int16")
    
    
    #for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
     #   data = stream.read(CHUNK)
      #  frames.append(np.fromstring(data, dtype=float))
        #frames.extend(np.frombuffer(data, dtype = float))
    print ("finished recording")
    
    
    #mydata = np.hstack(frames)
    #mydata = np.hstack(frames)
    
     
    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
    save = input("Vil du lagre dataene som en .wav fil [Y/n]?  ")
    if save == "Y" or save == "y":
       WAVE_OUTPUT_FILENAME = input("Skriv filnavn på formen filename.wav ")   
       waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
       waveFile.setnchannels(CHANNELS)
       waveFile.setsampwidth(audio.get_sample_size(FORMAT))
       waveFile.setframerate(RATE)
       waveFile.writeframes(b''.join(mydata))
       waveFile.close()

    return mydata


#pyaudio_acquisition(5, 44100)