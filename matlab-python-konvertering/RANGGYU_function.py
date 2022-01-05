import requests
import wave 
import pyaudio
import os

def RANGGYU_function():
    if "RANGGYU.wav" not in os.listdir():
        url = "https://github.com/jacobllie/RANGGYU/blob/main/RANGGYU.wav?raw=true"
        raw = requests.get(url).content
        
        with open('RANGGYU.wav', mode='bx') as f:
            f.write(raw)
    

    # Set chunk size of 1024 samples per data frame
    chunk = 1024  
    
    # Open the sound file 
    wf = wave.open("RANGGYU.wav", 'rb')
    
    # Create an interface to PortAudio
    p = pyaudio.PyAudio()
    
    # Open a .Stream object to write the WAV file to
    # 'output = True' indicates that the sound will be played rather than recorded
    stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                    channels = wf.getnchannels(),
                    rate = wf.getframerate(),
                    output = True)
    
    # Read data in chunks
    data = wf.readframes(chunk)
    
    # Play the sound by writing the audio data to the stream
    while data != '':
        stream.write(data)
        data = wf.readframes(chunk)

    # Close and terminate the stream
    stream.close()
    p.terminate()
    
    os.remove("RANGGYU.wav")
    
    pass