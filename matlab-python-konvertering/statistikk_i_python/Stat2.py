import numpy as np
import matplotlib.pyplot as plt
def histogram(x,normalisering = False):
    """
    Et histogram teller antall hendelser. X aksen er hendelsen f.eks. om du har
    kastet mynt eller krone. Y aksen er hvor mange ganger du har fått enten mynt eller krone.
    """
    bin_count = int(np.ceil(np.log2(len(x)) + 1))  #Sturge's regel
    plt.hist(x, bins=bin_count,density = normalisering, facecolor = '#2ab0ff', edgecolor='#169acf', linewidth=0.5)
    plt.xlabel('Bins')
    plt.ylabel('Values')


X = 10
sigma = 1
n = 50
x = sigma * np.random.randn(int(n)) + X
print(np.mean(x))

"""
Nå har vi funnet ett gjennomsnitt av 50 målinger,
men vi ønsker å finne fordelingen av gjennomsnittene.
Vi gjør det ved å trekke n tilfeldige tall fra normalfordelingen,
finne gjennomsnittet av dem, og lage en array som inneholder mange slike gjennomsnitt.
"""

"""
Hva skjer med denne fordelingen når vi øker antall målinger.
Det finner vi ut i loopen nedenfor.
"""


plt.style.use('seaborn')
num_measurements = np.array([50,1e3,5e4])
reps = 1000
meanSim = np.zeros([3,reps])
for index,n in enumerate(num_measurements):
    for i in range(reps):
        x = sigma * np.random.randn(int(n)) + X
        meanSim[index,i] = np.mean(x)
    plt.subplot(1,3,index+1)
    plt.title("Gjennomsnitts fordeling n = {}".format(num_measurements[index]))
    histogram(meanSim[index])
    plt.xlim(X-0.5,X+0.5)
plt.show()

"""
Det vi ser i plottene er at histogrammet blir spissere og spissere, ettersom antall målinger økes.
Det gir mening, fordi gjennomsnittet nærmer seg det sanne snittet når antall målinger går mot uendelig.
Da gir det også mening at når vi trekker 50 000 tilfeldige tall 1000 ganger, så blir
gjennomsnittet tilnærmet likt hver gang, og spredningen er nesten null.
"""
