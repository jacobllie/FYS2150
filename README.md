# FYS-2150 programmer for datainnsamling og behandling i Python

Her finner du nødvendig informasjon for nedlastning av programmer og pakker, for å kjøre enkelte programmer i **FYS-2150**.
Det inkluderer ikke pakker som numpy, matplotlib, os og sys ettersom de er bygget inn i python må ikke lastes ned.
Vi har heller ikke inkludert detaljerte beskrivelser av samtlige programmer, ettersom de ikke inneholder pakker som må lastes ned, og det er tilstrekkelig med å **kommentere** direkte i programmet.

## Nødvendige programmer
### Anaconda

Det kreves at PC'en kan kjøre og redigere Python 3 programmer.
Derfor anbefaler vi å laste ned [Anaconda](https://www.anaconda.com/products/individual).
 <br />
Anaconda gir tilgang til **Spyder**, som kan både skrive og kjøre Python programmer. I Spyder er det integrert et ipython vindu. Det gjør det mulig å bruke [pip](https://pypi.org/project/pip/), som er pythons package installer.

### NI-DAQmx

NI (national instruments) er et selskap som produserer instrumenter til bl.a. datainnsamling. For at PC'en skal kommunisere med hardware krever det at man laster ned en driver kalt [NI-DAQmx](https://www.ni.com/en-no/support/downloads/drivers/download.ni-daqmx.html#382067).

## Nødvendige pakker

Her finner du både en beskrivelse av pakkene, samt hvordan du laster dem ned.

### **Pendelperiode.py**

Dette programmet samler inn og behandler data fra en **NI USB-6211**. For å gi kommandoer til driveren **NI-DAQmx** kreves det en API (Application Programming Interface) som er kompatibel med Python. Til dette trenger vi å laste ned [nidaqmx](https://nidaqmx-python.readthedocs.io/en/latest/).
<br />

I et ipython vindu kan du skrive:


`
pip install nidaqmx
`

Dersom det ikke fungerer kan du prøve kommandoen:

`
conda install -c conda-forge nidaqmx-python
`


### **sound_acquisition_sounddevice.py**

Dette programmet tar opp lyd fra en mikrofon, til dette trenger man pakkene [sounddevice](https://python-sounddevice.readthedocs.io/en/0.4.1/usage.html) og [soundfile](https://pypi.org/project/SoundFile/).
Sounddevice beskrives best av en bruker på [reddit](https://www.reddit.com/r/Python/comments/3k11g5/whats_a_good_sound_recording_library/):
 "Sounddevice is a wrapper that tries to make portaudio pythonic. It provides a proper Stream class with play and record methods and callbacks for long-running interactive recordings. Additionally, there are some high level play and record standalone functions if all you need is play or record one short sample."


 SoundFile gjør det mulig å skrive lydopptaket til en wav fil.

I et ipython vindu kan du skrive:


`pip install sounddevice`

`pip install soundfile`


### **sound_acquisition_pyaudio.py**

På lab datamaskinene har jeg fått en error, ved bruk av **sounddevice**

**"PortAudioError: Error querying device -1"**

Denne får jeg ikke på min personlige datamaskin, og jeg må finne ut hva det kommer av. 
Men som en **backup** bruker jeg pakken [Pyaudio](https://people.csail.mit.edu/hubert/pyaudio/docs/), for å ta opp lyd. 

For å laste ned **Pyaudio** skriver du dette i et ipython vindu i f.eks. Spyder:

`pip install PyAudio`

Dersom det ikke funker, kan det være at du den pyaudioen som pip prøver å laste ned ikke passer med din versjon av python. 
Prøv å gjør dette i steden:

1. Sjekk din versjon av python. 
   Det kan gjøres i Spyder sitt iPython vindu: <br>
   `import sys` <br>
   `print(sys.version)`
  Output:   
  ![pyaudio_install](https://user-images.githubusercontent.com/72126694/148218621-df278c6d-33c5-4688-8f84-a83d5bead3c8.png)

Her ser vi at vi har python 3.8 64 bit (AMD). 

Gå deretter inn på [denne nettsiden](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) for å finne den pyaudio som stemmer med din python versjon. 
I vårt tilfelle ønsker vi **PyAudio‑0.2.11‑cp38‑cp38‑win_amd64.whl**.
Etter du har lastet ned riktig fil. Gå til et iPython vindu. og skriv:

![pyaudio_install2](https://user-images.githubusercontent.com/72126694/148220150-5c1fc690-0eba-460d-b299-46324539b5e2.png)


### **videoframes.py**

Dette programmet leser en videofil og spiller den av frame by frame. Ved hjelp av tastene l, j og q kan man manøvrere seg frem, tilbake og avslutte en avspilling.
Det er nødvendig å laste ned [opencv-python](https://pypi.org/project/opencv-python/), for å få tilgang til **cv2**.
Det gjør man igjen via pip:

`pip install opencv-python`


## Annet

### **plotting i spyder**

Ved flere anledninger ønsker vi å analysere plottene vi lager derfor er det ønskelig at plottene kommer opp som et pop up. Slik at vi f.eks. zoome inn og se på x og y verdier. For å få til det, må du:

1. Trykk på tools
   
![spyder_plot1](https://user-images.githubusercontent.com/72126694/148220286-0bfa5f29-1d98-4bb3-a760-d018c852e70c.png)

2. Preferences 

 ![sspyder_plot2](https://user-images.githubusercontent.com/72126694/148220610-087bcc96-63b2-4221-abd1-46727cc3e7b5.jpg)


3. iPython console - Graphics - Graphics backend 
   Endre fra Inline til Automatic
![spyder_plot3](https://user-images.githubusercontent.com/72126694/148220953-dc50abfd-3596-4432-bdc7-0083c87e40ae.png)

